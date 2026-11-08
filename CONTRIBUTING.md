# Contributing and maintenance

Create a branch for a focused change, make it reviewable, run the relevant checks, then open a pull request. An issue describes desired behavior; a milestone groups a release's work. Neither means a feature exists.

Keep scripts portable Bash with a `SCRIPT_VERSION` variable and a short change summary. Quote paths, especially `Catnap Streaming`. Do not hardcode the maintainer's home directory into distributable tools. Use relative repository roots and explicit configurable runtime data roots.

Record imported source paths and versions, never replace manifest versions with folder labels. Keep shared contracts versioned; avoid copying a changing display core into every product. Capture meaningful adapter and recovery tests; use manual checklists for real browser/media behavior.

Never commit credentials, pairing files, personal IDs/messages, event CSVs, full lyrics, third-party private code, browser profiles or server data. Add only intended source files; review `git diff --cached` before committing. Run `scripts/check-repository.sh REPO_PATH` for a basic publication check; it is a guard, not a proof that every file is safe.

Private repository access is not a substitute for permissions to redistribute artwork or third-party source. All rights are reserved pending an explicit first-party licensing decision and asset review.
