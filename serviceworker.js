// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/app/css/estilos.css',


];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

self.addEventListener("fetch", function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(result) {
            return caches.open(staticCacheName)
            .then(function(c) {
                c.put(event.request.url, result.clone())
                return result              
            })
        })
        .catch(function(e) {
            return caches.match(event.request)
        })
    )
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
    apiKey: "AIzaSyD1Wmiof8b3ayM0-NU7QtNMHb-ksN0uCIM",
    authDomain: "autolavado-e9dbf.firebaseapp.com",
    projectId: "autolavado-e9dbf",
    storageBucket: "autolavado-e9dbf.appspot.com",
    messagingSenderId: "39337215113",
    appId: "1:39337215113:web:b649a14413644f1d75f258"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

let messaging  = firebase.messaging();


messaging.setBackgroundMessageHandler(function(payload) {

    let title = payload.notification.title;
    let options = {
        body: payload.notification.body,
        icon: payload.notification.icon
    }

    self.registration.showNotification(title, options);
});