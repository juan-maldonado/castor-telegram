#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup, ReplyKeyboardRemove
from commands.emotions.keyboards import emotions_keyboard

def emotions(update, context):
    keyboard = emotions_keyboard()
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (
        "Selecciona una emoción!"
    )
    update.message.reply_text(
        message,
        reply_markup = reply_markup,
        parse_mode = 'markdown'
    )
    return
