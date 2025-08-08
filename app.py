import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re

load_dotenv()

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def handle_app_mention_event(body,say):
    say("Yes? How can I help you today?")

@app.message(re.compile("(fuck)"))
def fuckhandler(say,context):
    greeting = context['matches'][0]
    say(f"{greeting} you motherfucker")

if __name__ == "__main__":
    handler = SocketModeHandler(app,os.environ.get("SLACK_APP_TOKEN"))
    handler.start()