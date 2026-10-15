// Apply the preference before paint. Storage may be unavailable in private contexts.
(() => {
  let theme;
  try { theme = localStorage.getItem('notebook-theme'); } catch (_) { /* Use system preference. */ }
  if (theme !== 'light' && theme !== 'dark') {
    theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  document.documentElement.dataset.theme = theme;
})();
