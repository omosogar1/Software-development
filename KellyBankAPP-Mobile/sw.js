const CACHE_NAME = "kelly-bank-v6";
const urlsToCache = [
  "/Software-development/KellyBankAPP-Mobile/",
  "/Software-development/KellyBankAPP-Mobile/index.html",
  "/Software-development/KellyBankAPP-Mobile/manifest.json",
  "/Software-development/KellyBankAPP-Mobile/icon-192.png",
  "/Software-development/KellyBankAPP-Mobile/icon-512.png"
];
self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE_NAME).then(c => c.addAll(urlsToCache)));
});
self.addEventListener("fetch", e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
