/* Catnap Theatre information page 1.0.0. Layout previews and muted cover loops. */
(() => {
  'use strict';
  const SCRIPT_VERSION = '1.0.0';
  const layoutPreviews = {
    playlist: ['Playlist, artwork and lyrics sit side by side.', 'Catnap Theatre with playlist, artwork and lyrics'],
    lyrics: ['Give the lyrics more room beside the cover.', 'Catnap Theatre with artwork and large lyrics'],
    artwork: ['Let the cover fill the stage.', 'Catnap Theatre with the cover art as the focus'],
  };
  const buttons = [...document.querySelectorAll('[data-layout-preview]')];
  for (const button of buttons) {
    button.addEventListener('click', () => {
      const key = button.dataset.layoutPreview;
      const [caption, alt] = layoutPreviews[key];
      const image = document.getElementById('layout-image');
      image.src = './media/layout-' + key + '.webp';
      image.alt = alt;
      document.getElementById('layout-caption').textContent = caption;
      for (const peer of buttons) peer.setAttribute('aria-pressed', String(peer === button));
    });
  }
  const hostPreviews = {
    'both-visual-stages': ['Both visual stages in Suno playlist mode', 'Theatre with both visual panes and music bars'],
    'playlist-visual-stage': ['A visual underneath the playlist, with full-height lyrics', 'Theatre with one visual under the playlist, full-height lyrics, and music bars'],
  };
  const hostButtons = [...document.querySelectorAll('[data-visual-preview]')];
  for (const button of hostButtons) {
    button.addEventListener('click', () => {
      const key = button.dataset.visualPreview;
      const [caption, alt] = hostPreviews[key];
      const image = document.getElementById('host-layout-image');
      image.src = './media/' + key + '.webp';
      image.alt = alt;
      document.getElementById('host-layout-caption').textContent = caption;
      for (const peer of hostButtons) peer.setAttribute('aria-pressed', String(peer === button));
    });
  }
  // Leave the poster visible for visitors who prefer to reduce motion.
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  if (motion.matches || !('IntersectionObserver' in window)) return;
  const observer = new IntersectionObserver(entries => {
    for (const {target, isIntersecting} of entries) {
      if (isIntersecting && !motion.matches) target.play().catch(() => {});
      else target.pause();
    }
  }, {threshold: 0.32});
  for (const video of document.querySelectorAll('[data-loop]')) observer.observe(video);
  document.documentElement.dataset.theatrePage = SCRIPT_VERSION;
})();
