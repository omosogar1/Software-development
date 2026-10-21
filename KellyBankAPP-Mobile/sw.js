const CACHE_NAME = "kellybank-v8-autolock";
const FILES_TO_CACHE = [
  "./",
  "./index.html",
  "./manifest.json",
  "./logo.png"
];

// Install - Cache files
self.addEventListener("install", (event) => {
  console.log("KellyBank SW: Installing v8");
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(FILES_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// Activate - Clean old cache
self.addEventListener("activate", (event) => {
  console.log("KellyBank SW: Activating v8");
  event.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(
        keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log("Deleting old cache:", key);
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch - Offline support + BVN/PIN data stays in localStorage
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      // Return cached or fetch from network
      return response || fetch(event.request).then((fetchRes) => {
        // Cache new files
        return caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, fetchRes.clone());
          return fetchRes;
        });
      });
    }).catch(() => {
      // If offline and not in cache, return index
      if (event.request.destination === 'document') {
        return caches.match('./index.html');
      }
    })
  );
});
