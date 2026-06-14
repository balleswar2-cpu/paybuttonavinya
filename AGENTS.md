# Agent Notes

## Architecture

Static site served by `server.py` (Python `http.server` on port 5000). No framework, no build tooling, no dependencies.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Google Pay direct deep link (legacy) |
| `pay.html` | Main payment page — Safari-aware |
| `static/` | SVG icons: `gpay.svg`, `phonepe.svg`, `paytm.svg`, `bhim.svg` |
| `server.py` | Static file server with `/pay/:amount` → `/pay.html?amount=:amount` redirect |

## Key Decisions

- `pay.html` detects Safari using `navigator.vendor` (Apple) plus Chrome-on-iOS / Firefox-on-iOS exclusions (CriOS / FxiOS). Source: https://stackoverflow.com/a/31732310, CC BY-SA 4.0.
- Safari users see a "Use QR code below" note and a tap-to-copy UPI ID — no generated QR image (the QR lives on the main website).
- All other browsers get four UPI app buttons (Google Pay, PhonePe, Paytm, BHIM) with native deep links.
- If no `amount` param is passed, the amount label is hidden and `&am=` is omitted from every UPI deep link.
- App buttons use `<a href>` elements so deep links work natively without extra JS.
- The `upi://` scheme is the standard Android deep link for UPI apps; iOS/Safari does not support UPI deep links natively.
