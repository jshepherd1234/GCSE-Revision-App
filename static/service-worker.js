const CACHE_NAME = "gcse-version-v1";

const FILES_TO_CACHE = [

    "/",

    "/static/style.css"

];

self.addEventListener("Install", event => {

    event.waitUntil(

        caches.open(CACHE_NAME)

        .then(cache => {

            return cache.addAll(FILES_TO_CACHE);
        
        })
    );

});

self.addEventListener("fetch", event => {

    event.respondWith(

        caches.match(event.request)

        .then(response => {

            return response || fetch(event.request);

        })
    );

});