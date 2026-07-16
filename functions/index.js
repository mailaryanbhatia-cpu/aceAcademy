const functions = require("firebase-functions");
const admin     = require("firebase-admin");

admin.initializeApp();

// ── Gemini API Proxy ──────────────────────────────────────────────────────────
// Keeps the Gemini API key server-side; students never see it.
// Call from client: POST /aiChat  { messages, system, maxTokens }
// Returns: { content: "..." }  or  { error: "..." }
// (Previously called Claude/Anthropic — switched to Gemini's free tier.)

const GEMINI_MODEL    = "gemini-3.5-flash";
const GEMINI_ENDPOINT = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent`;
const MAX_TOKENS_CAP  = 1500; // prevent runaway costs

exports.aiChat = functions
  .runWith({ secrets: ["GEMINI_API_KEY"], timeoutSeconds: 60 })
  .https.onCall(async (data, context) => {
    // Rate-limit: require auth (signed-in students only)
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

    const key = process.env.GEMINI_API_KEY;
    if (!key) {
      throw new functions.https.HttpsError("internal", "API key not configured.");
    }

    // Gemini's REST shape differs from Anthropic's: each message becomes a
    // { role, parts:[{text}] } entry ("assistant" -> "model"), and the system
    // prompt goes in its own top-level "systemInstruction" field instead of
    // living alongside the messages array.
    const contents = messages.map(m => ({
      role: m.role === "assistant" ? "model" : "user",
      parts: [{ text: m.content }]
    }));

    const body = {
      contents,
      ...(system ? { systemInstruction: { parts: [{ text: system }] } } : {}),
      generationConfig: {
        maxOutputTokens: Math.min(maxTokens || 800, MAX_TOKENS_CAP)
      }
    };

    const resp = await fetch(GEMINI_ENDPOINT, {
      method:  "POST",
      headers: {
        "Content-Type":   "application/json",
        "x-goog-api-key": key
      },
      body: JSON.stringify(body)
    });

    if (!resp.ok) {
      const err = await resp.text();
      functions.logger.error("Gemini API error", err);
      throw new functions.https.HttpsError("internal", "Gemini API error: " + resp.status);
    }

    const json = await resp.json();
    const text = json.candidates?.[0]?.content?.parts?.map(p => p.text).join("") ?? "";
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
