const functions = require("firebase-functions");
const admin     = require("firebase-admin");

admin.initializeApp();

// ── Claude API Proxy ──────────────────────────────────────────────────────────
// Keeps the Anthropic API key server-side; students never see it.
// Call from client: POST /claudeChat  { messages, system, maxTokens }
// Returns: { content: "..." }  or  { error: "..." }

const CLAUDE_MODEL    = "claude-haiku-4-5-20251001";
const CLAUDE_ENDPOINT = "https://api.anthropic.com/v1/messages";
const MAX_TOKENS_CAP  = 1500; // prevent runaway costs

exports.claudeChat = functions
  .runWith({ secrets: ["ANTHROPIC_KEY"], timeoutSeconds: 60 })
  .https.onCall(async (data, context) => {
    // Rate-limit: require auth (anonymous auth is fine)
    if (!context.auth) {
      throw new functions.https.HttpsError(
        "unauthenticated",
        "Must be signed in to use AI features."
      );
    }

    const { messages, system, maxTokens } = data;
    if (!messages || !Array.isArray(messages)) {
      throw new functions.https.HttpsError("invalid-argument", "messages required");
    }

    const key = process.env.ANTHROPIC_KEY;
    if (!key) {
      throw new functions.https.HttpsError("internal", "API key not configured.");
    }

    const body = {
      model:      CLAUDE_MODEL,
      max_tokens: Math.min(maxTokens || 800, MAX_TOKENS_CAP),
      messages,
      ...(system ? { system } : {})
    };

    const resp = await fetch(CLAUDE_ENDPOINT, {
      method:  "POST",
      headers: {
        "Content-Type":     "application/json",
        "x-api-key":        key,
        "anthropic-version":"2023-06-01"
      },
      body: JSON.stringify(body)
    });

    if (!resp.ok) {
      const err = await resp.text();
      functions.logger.error("Claude API error", err);
      throw new functions.https.HttpsError("internal", "Claude API error: " + resp.status);
    }

    const json = await resp.json();
    const text = json.content?.[0]?.text ?? "";
    return { content: text };
  });

// ── Optional: log tool usage to Firestore for analytics ──────────────────────
exports.logToolVisit = functions.https.onCall(async (data, context) => {
  if (!context.auth) return { ok: false };
  const { tool } = data;
  if (!tool) return { ok: false };
  const uid = context.auth.uid;
  const ref = admin.firestore()
    .collection("analytics")
    .doc(uid)
    .collection("tools")
    .doc(tool);
  await ref.set({
    visits:    admin.firestore.FieldValue.increment(1),
    lastVisit: admin.firestore.FieldValue.serverTimestamp()
  }, { merge: true });
  return { ok: true };
});
