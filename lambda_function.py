import logging
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    TextSendMessage,
)
from service.finance import rp

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
line_bot_api = LineBotApi(os.getenv('ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('SECRET'))


def lambda_handler(event, content):
    print("event:", event)
    body = event['body']

    try:
        events = body['events']
        reply_token = events[0]['replyToken']
        message_type = events[0]['message']['type']
        message = events[0]['message']['text'] if "text" in events[0]['message'] else ""

        execute_type(message_type, reply_token, message)

    except InvalidSignatureError:
        print("ex: InvalidSignature")
        return {'statusCode': 400, 'body': 'InvalidSignature'}
    except Exception as e:
        print("ex: ", e)
        return {'statusCode': 400, 'body': e}
    return {'statusCode': 200, 'body': 'OK'}


def execute_type(message_type, reply_token, message):
    switcher = {
        "text": text_type,
        "sticker": sticker_type
    }
    func = switcher.get(message_type, lambda: "Invalid type")
    func(reply_token, message)


def text_type(reply_token, message):
    if message == 'rp':
        message = rp()
    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))


def sticker_type(reply_token, message):
    line_bot_api.reply_message(reply_token, TextSendMessage(text="我看不懂貼圖啦"))
