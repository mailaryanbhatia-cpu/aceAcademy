const CACHE = 'ace-v2';
const CORE = [
  '/aceAcademy/',
  '/aceAcademy/index.html',
  '/aceAcademy/ace-theme.css',
  '/aceAcademy/theme.js',
  '/aceAcademy/streak.js',
  '/aceAcademy/manifest.json'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys =>
    Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
  ));
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then(cached => {
      const net = fetch(e.request).then(res => {
        if (res && res.ok) {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
        }
        return res;
      }).catch(() => cached);
      return cached || net;
    })
  );
});

// ── Periodic background sync → streak reminder notification ────
self.addEventListener('periodicsync', e => {
  if (e.tag === 'streak-reminder') {
    e.waitUntil(checkAndNotify());
  }
});

async function checkAndNotify() {
  // Get all clients to check if user already visited today
  const clients = await self.clients.matchAll();
  if (clients.length > 0) return; // app is open, no need to notify

  const now = new Date();
  const hour = now.getHours();
  // Only send reminder in the evening (6pm–10pm)
  if (hour < 18 || hour >= 22) return;

  self.registration.showNotification('🔥 Don\'t break your streak!', {
    body: 'Open aceAcademy to keep your study streak alive.',
    icon: '/aceAcademy/icons/icon-192.png',
    badge: '/aceAcademy/icons/icon-72.png',
    tag: 'streak-reminder',
    renotify: false,
    data: { url: '/aceAcademy/' }
  });
}

// ── Notification click → open app ─────────────────────────────
self.addEventListener('notificationclick', e => {
  e.notification.close();
  const url = (e.notification.data && e.notification.data.url) || '/aceAcademy/';
  e.waitUntil(
    self.clients.matchAll({ type: 'window' }).then(clients => {
      for (const c of clients) {
        if (c.url.includes('/aceAcademy/') && 'focus' in c) return c.focus();
      }
      return self.clients.openWindow(url);
    })
  );
});
