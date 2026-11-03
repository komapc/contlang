/* Google Analytics 4, loaded only after the visitor allows it.
   Choice is kept in localStorage ("lipu-consent"). Until then nothing is sent to Google.
   Same pattern as vortaro.lipu.dev and tradukilo.lipu.dev, but the key is per origin. */
(function () {
  var GA = document.currentScript && document.currentScript.dataset.ga;
  var KEY = 'lipu-consent';
  var get = function () { try { return localStorage.getItem(KEY); } catch (e) { return null; } };
  var set = function (v) { try { localStorage.setItem(KEY, v); } catch (e) {} };
  function load() {
    if (!GA || window.__gaLoaded) return;
    window.__gaLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA, { anonymize_ip: true });
  }
  var T = {
    en: ['We use Google Analytics (cookies) to count visits.', 'Allow', 'Decline'],
    ru: ['Мы используем Google Analytics (cookie), чтобы считать посещения.', 'Разрешить', 'Отказаться']
  };
  function banner() {
    var l = (document.documentElement.lang || 'en').slice(0, 2);
    var t = T[l] || T.en;
    var st = document.createElement('style');
    st.textContent = '#lipu-consent{position:fixed;left:12px;right:12px;bottom:12px;max-width:560px;margin:0 auto;padding:12px 14px;' +
      'background:var(--card,#fff);color:var(--fg,#1d1d1b);border:1px solid var(--line,#dcd9cf);border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.18);' +
      'font:14px/1.4 system-ui,sans-serif;z-index:2147483000;display:flex;flex-wrap:wrap;gap:8px;align-items:center}' +
      '#lipu-consent span{flex:1 1 220px}#lipu-consent button{font:inherit;padding:6px 12px;border-radius:8px;cursor:pointer;' +
      'border:1px solid var(--acc,#2f5d50);background:none;color:inherit}#lipu-consent button.y{background:var(--acc,#2f5d50);color:var(--bg,#fff)}';
    var d = document.createElement('div');
    d.id = 'lipu-consent'; d.setAttribute('role', 'dialog');
    var sp = document.createElement('span'); sp.textContent = t[0];
    var y = document.createElement('button'); y.type = 'button'; y.className = 'y'; y.textContent = t[1];
    var n = document.createElement('button'); n.type = 'button'; n.textContent = t[2];
    var done = function (v) { set(v); d.remove(); st.remove(); if (v === 'yes') load(); };
    y.onclick = function () { done('yes'); };
    n.onclick = function () { done('no'); };
    d.append(sp, y, n);
    document.head.appendChild(st);
    document.body.appendChild(d);
  }
  var c = get();
  if (c === 'yes') load();
  else if (c !== 'no') {
    if (document.body) banner(); else document.addEventListener('DOMContentLoaded', banner);
  }
})();
