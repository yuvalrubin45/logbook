"""Post a Telegram channel message whose buttons give private (ephemeral) replies.

Each viewer who taps a button sees a popup only they can see.

Usage:
  export BOT_TOKEN=123:abc          # from @BotFather
  export CHANNEL=@yourchannel       # or -100... id. Bot must be a channel admin
  python3 ephemeral_bot.py post     # send the message
  python3 ephemeral_bot.py run      # keep running to answer button taps
"""
import json
import os
import sys
import urllib.request

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ.get("CHANNEL", "")
API = f"https://api.telegram.org/bot{TOKEN}/"

# Edit the post and the private replies here (each reply max 200 chars).
MESSAGE = "Tap a button below. Only you will see the answer 👇"
BUTTONS = [
    ("🎁 Reveal secret", "secret", "The secret code is LOGBOOK2026. Only you can see this."),
    ("ℹ️ More info", "info", "This reply is private to you. Nobody else in the channel sees it."),
]
REPLIES = {key: text for _, key, text in BUTTONS}


def call(method, **params):
    req = urllib.request.Request(
        API + method,
        data=json.dumps(params).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["result"]


def post():
    keyboard = [[{"text": label, "callback_data": key}] for label, key, _ in BUTTONS]
    msg = call("sendMessage", chat_id=CHANNEL, text=MESSAGE,
               reply_markup={"inline_keyboard": keyboard})
    print("Posted message", msg["message_id"])


def run():
    print("Listening for button taps. Ctrl+C to stop.")
    offset = 0
    while True:
        for update in call("getUpdates", offset=offset, timeout=50,
                           allowed_updates=["callback_query"]):
            offset = update["update_id"] + 1
            q = update.get("callback_query")
            if q:
                call("answerCallbackQuery", callback_query_id=q["id"],
                     text=REPLIES.get(q.get("data"), "Unknown button"),
                     show_alert=True)


if __name__ == "__main__":
    {"post": post, "run": run}.get(sys.argv[1] if len(sys.argv) > 1 else "", lambda: print(__doc__))()
