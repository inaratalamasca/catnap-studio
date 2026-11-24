(() => {
  const covers = document.querySelectorAll(".song-motion-cover");
  const motionToggle = document.getElementById("cover-motion-toggle");
  const preview = document.getElementById("song-cover-preview");
  const previewTitle = document.getElementById("song-cover-preview-title");
  const previewClose = document.getElementById("song-cover-preview-close");
  const previewVideo = preview.querySelector("video");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const visibleCovers = new Set();
  let motionEnabled = !reducedMotion.matches;
  let resumePreview = false;

  function playVideo(video) {
    video.muted = true;
    // The poster also covers browsers that require a direct playback gesture.
    video.play().catch(() => {});
  }

  function updateCovers() {
    const playCovers = motionEnabled && !document.hidden && !preview.open;

    for (const cover of covers) {
      const video = cover.querySelector("video");
      const shouldPlay = playCovers && visibleCovers.has(cover);
      video.hidden = !shouldPlay;

      if (shouldPlay) {
        if (!video.getAttribute("src")) {
          video.src = video.dataset.src;
        }
        if (video.paused) {
          playVideo(video);
        }
      } else if (!video.paused) {
        video.pause();
      }
    }
  }

  function setMotion(enabled) {
    motionEnabled = enabled;
    motionToggle.textContent = enabled ? "Pause cover animations" : "Play cover animations";
    if (!enabled && preview.open) {
      previewVideo.pause();
      resumePreview = false;
    }
    updateCovers();
  }

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      for (const { target, isIntersecting, intersectionRatio } of entries) {
        if (isIntersecting && intersectionRatio >= 0.15) {
          visibleCovers.add(target);
        } else {
          visibleCovers.delete(target);
        }
      }
      updateCovers();
    }, { threshold: 0.15 });

    for (const cover of covers) {
      observer.observe(cover);
    }

    motionToggle.hidden = false;
    setMotion(motionEnabled);
    motionToggle.addEventListener("click", () => setMotion(!motionEnabled));
    reducedMotion.addEventListener("change", event => setMotion(!event.matches));
  }

  if (typeof preview.showModal === "function") {
    for (const cover of covers) {
      cover.setAttribute("aria-haspopup", "dialog");
      cover.addEventListener("click", event => {
        if (event.button !== 0 || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) {
          return;
        }

        event.preventDefault();
        const video = cover.querySelector("video");
        previewTitle.textContent = cover.dataset.title;
        previewVideo.poster = cover.href;
        previewVideo.src = video.dataset.src;
        preview.showModal();
        updateCovers();

        if (motionEnabled) {
          playVideo(previewVideo);
        }
      });
    }

    previewClose.addEventListener("click", () => preview.close());
    preview.addEventListener("click", event => {
      if (event.target === preview) {
        preview.close();
      }
    });
    preview.addEventListener("close", () => {
      previewVideo.pause();
      previewVideo.removeAttribute("src");
      previewVideo.load();
      resumePreview = false;
      updateCovers();
    });
  }

  document.addEventListener("visibilitychange", () => {
    if (preview.open) {
      if (document.hidden) {
        resumePreview = !previewVideo.paused;
        previewVideo.pause();
      } else if (resumePreview) {
        playVideo(previewVideo);
        resumePreview = false;
      }
    }
    updateCovers();
  });
})();
