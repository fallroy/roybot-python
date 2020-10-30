import logging

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    TextSendMessage,
)

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
line_bot_api = LineBotApi(access_token)
handler = WebhookHandler("3181bcb492171200e04e398f513610b3")


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
    line_bot_api.reply_message(reply_token, TextSendMessage(text=message))


def sticker_type(reply_token, message):
    line_bot_api.reply_message(reply_token, TextSendMessage(text="我看不懂貼圖啦"))
