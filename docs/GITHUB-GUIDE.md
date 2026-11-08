# Finding and updating the projects

Your projects belong to the GitHub account **inaratalamasca**. Each repository has a different job; the table on the home page links them together.

## The useful parts of each repository

- **Code / README:** what the project does, its current state and where to start. Open `docs` for guides. A folder of source is not automatically an installable product.
- **Issues:** unfinished work, bug reports and feature requests. Use the supplied forms. Include what you expected and what happened, with private information removed.
- **Milestones:** groups of issues for a stage, such as the first standalone pilot. Dates are left open until testing makes a release estimate reasonable.
- **Pull requests:** review a proposed change before it is merged into the main source history. A draft can be discussed before it is ready.
- **Releases:** versioned packages after acceptance. This setup does not label an untested preview as a stable release.

## What private means here

The repositories are private. A person must be granted access before they can read them. Do not make a repo public just to send a package to a tester. Private Chrome Web Store distribution is a separate system with its own Google-account tester access and review.

Event submissions, identity masters, credentials and live server data are not stored here. Keep them in the local event/reference or private server folders. The workspace has a compatibility path for the current installation, so development does not require moving a live extension.

## Asking for a change

Say which product and describe the result you want. For example: “In standalone Theatre, use the three-column view and make lyrics larger; it should still work with Armin disconnected.” A bug report can say “After the third song changed, the previous lyrics stayed visible; Reload lyrics fixed it.”

For an installation or release, use the project's guide and acceptance checklist. New source changes should be tested between shows before replacing the loaded extension. Review the actual version in the manifest rather than relying on an old zip/folder name.
