(() => {
  const button = document.querySelector('.theme-toggle');
  if (!button) return;
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  let manuallySelected = false;
  try { manuallySelected = ['light', 'dark'].includes(localStorage.getItem('notebook-theme')); } catch (_) { /* Optional storage. */ }
  const update = () => {
    const dark = document.documentElement.dataset.theme === 'dark';
    button.setAttribute('aria-pressed', String(dark));
    button.setAttribute('aria-label', `Switch to ${dark ? 'light' : 'dark'} theme`);
    button.title = `Switch to ${dark ? 'light' : 'dark'} theme`;
  };
  button.hidden = false;
  update();
  button.addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    manuallySelected = true;
    try { localStorage.setItem('notebook-theme', next); } catch (_) { /* Theme still works without storage. */ }
    update();
  });
  systemTheme.addEventListener('change', event => {
    if (!manuallySelected) {
      document.documentElement.dataset.theme = event.matches ? 'dark' : 'light';
      update();
    }
  });
})();
