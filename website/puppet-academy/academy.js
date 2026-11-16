'use strict';

const checkboxes = [...document.querySelectorAll('.checklist input')];
const progress = document.getElementById('check-progress');
checkboxes.forEach(box => box.addEventListener('change', () => {
  const checked = checkboxes.filter(item => item.checked).length;
  progress.textContent = checked === checkboxes.length
    ? '5 of 5 checked · splendid. Open the uploader!'
    : `${checked} of 5 checked · the crayons can wait.`;
}));

document.getElementById('copy-brief').addEventListener('click', async () => {
  const brief = document.getElementById('song-brief');
  const status = document.getElementById('copy-status');
  try {
    await navigator.clipboard.writeText(brief.value);
    status.textContent = 'Copied! Paste it into your message or submission notes.';
  } catch {
    brief.focus();
    brief.select();
    status.textContent = 'Your brief is selected. Press Ctrl+C (or ⌘C) to copy.';
  }
});

const eventStart = new Date('2026-11-19T16:00:00-08:00');
const localTime = document.getElementById('local-time');
try {
  localTime.textContent = `In your device’s time zone: ${new Intl.DateTimeFormat(undefined, {
    weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', timeZoneName: 'short'
  }).format(eventStart)}`;
} catch {
  localTime.textContent = 'Pacific time · UTC−8';
}
