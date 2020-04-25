#line-bot

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('xsPykhTayjqn7NbtiLxFA2InK3PgicVDKngj7PNNnQErUH7UdpL5PfRVx0VNFTOcpX28XXHgfI/IJAuy18eSEg5FOmrEZFpMsPvIKIor8pxe6XTUHMFO7CSOgRe7XA2xd6UWzyXWKLDklojY6LbYlgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('96de5fbcbe77c47d4790aa28b4218433')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text
	r = 'what dii you say?'
	if msg == 'hi' :		
		r = 'hi'
	elif msg == '早安'：
		r = 'moring'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()