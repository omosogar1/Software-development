const CACHE_NAME = "kellybank-v26-tier-final";
const FILES_TO_CACHE = [
  "./",
  "./index.html?v=26",
  "./manifest.json?v=26",
  "./logo.png"
];

self.addEventListener("install", (event) => {
  console.log("KellyBank V26 Installing Tier Final");
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(FILES_TO_CACHE))
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keyList) => 
      Promise.all(keyList.map((key) => {
        if (key !== CACHE_NAME) {
          console.log("Deleting old cache", key);
          return caches.delete(key);
        }
      }))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request).catch(() => caches.match("./index.html?v=26"));
    })
  );
});
