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

The `amount` parameter is optional. If omitted, the amount label is hidden and `&am=` is not included in the UPI deep link.

## Behaviour

| Browser | What the user sees |
|---------|-------------------|
| Android / other | Four app buttons — Google Pay, PhonePe, Paytm, BHIM — that open the respective UPI app directly |
| Safari (iOS / macOS) | "Use QR code below." note, plus a tap-to-copy UPI ID |

Safari is detected via `navigator.vendor` (Apple) with Chrome-on-iOS (CriOS) and Firefox-on-iOS (FxiOS) exclusions. Source: [stackoverflow.com/a/31732310](https://stackoverflow.com/a/31732310), CC BY-SA 4.0.

## Files

| File | Purpose |
|------|---------|
| `index.html` | Google Pay direct deep link (legacy) |
| `pay.html` | Main payment page with browser detection |
| `static/` | SVG icons for each UPI app |
| `server.py` | Python static file server with `/pay/:amount` redirect |

## Run Locally

```bash
python server.py
```

Runs on `http://0.0.0.0:5000`.
