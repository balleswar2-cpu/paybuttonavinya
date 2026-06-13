# Agent Notes

## Architecture

Single static file: `index.html`. No framework, no build tooling, no dependencies.

## Key Decisions

- Used a plain `<a>` element (not `<button>`) so the UPI deep link works natively as an `href` — no JavaScript needed.
- The `upi://` scheme is the standard Android deep link for UPI apps; iOS does not support UPI natively.
- No `netlify.toml` is required; Netlify auto-detects `index.html` as a static site.
