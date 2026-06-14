# UPI Payment Page

A static payment page that generates UPI deep links for quick mobile payments. Pass an amount via URL and the page handles the rest.

## Usage

Link to `pay.html` with an `amount` query parameter:

```
/pay.html?amount=250
```

Or use the clean redirect route:

```
/pay/250
```

## Behaviour

- **Android / other browsers** — shows four app buttons (Google Pay, PhonePe, Paytm, BHIM) that open the respective UPI app directly.
- **Safari (iOS / macOS)** — UPI deep links are not supported in Safari, so the page shows a scannable QR code and a tap-to-copy UPI ID instead.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Google Pay direct deep link (legacy) |
| `pay.html` | Main payment page with app detection |
| `static/` | SVG icons for each UPI app |
| `server.py` | Simple Python server with `/pay/:amount` redirect |

## Run Locally

```bash
python server.py
```

Runs on `http://localhost:5000`. The UPI deep links only activate on a mobile device with a UPI app installed.
