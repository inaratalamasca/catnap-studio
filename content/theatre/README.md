# Catnap Theatre brochure source

The public home is https://catnapradio.com/theatre/. The feature page and two install guides live in `website/theatre/`. Keep versions and download details in the install guides. The short poster and PDF describe the experience. They point people back to the site for current information.

## Refresh the share preview

Edit `poster.html` and render at 1600 × 840. Put the new JPEG in `website/theatre/media/` with a fresh dated filename. Update the page’s `og:image` and `twitter:image` to that absolute URL. Keep the canonical page URL stable. Verify the image URL from the public site after publishing. Discord may retain cards it already cached.

`booklet.html` is the optional dark PDF source. Keep it versionless and label plans as plans. The two files use the public site media directory. Recent UI examples use packaged controls populated with demo data.

## Downloads

Community 0.5.0 is the original Lite ZIP. Its verified release asset is hosted under `/theatre/downloads/` without changing the ZIP. The advanced Host kit follows the private AIU pilot distribution. The public Host guide explains where to get it and how to use the bundled optional Suno companion.

Suno MCP access and the companion apply to playlist calls. The Catnap relay serves Radio listeners. The public pages can be deployed as static files.
