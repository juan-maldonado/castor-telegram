#!/usr/bin/python
# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardRemove

from commands.emotions.keyboards import emotions_keyboard
from commands.start.keyboards  import start_keyboard

def emotions_callback(update, context, pubEmotions):
    #Get update data
    query = update.callback_query
    #Check callback callback_data
    if query['data'] != "back":
        print "publica"
        #Publish emotion in ROS
        pubEmotions.publish(query["data"])
        #Notify Telegram that we have answered
        query.answer(text="")
        #Update answer
        keyboard = emotions_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = (
            "Selecciona una emoción!"
        )
        query.edit_message_text(
            text=message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
    else:
        #Notify Telegram that we have answered
        query.answer(text="")
        query.edit_message_text(text="Selecciona una opción en el teclado:")

    return
