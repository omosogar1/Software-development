const CACHE_NAME = "kellybank-v26-9-original";
const FILES_TO_CACHE = [
  "./",
  "./index.html?v=26.9-original",
  "./manifest.json?v=26.9-original",
  "./logo.png"
];

self.addEventListener("install", (event) => {
  console.log("Kelly Bank V26.9 Original Installing");
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(FILES_TO_CACHE))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => 
      Promise.all(keyList.map((key) => {
        if (key !== CACHE_NAME) return caches.delete(key);
      }))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request).catch(() => caches.match("./index.html?v=26.9-original"));
    })
  );
});
