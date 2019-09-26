#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram import ReplyKeyboardMarkup
from commands.start.keyboards import start_keyboard

def start(update, context):
    keyboard = start_keyboard()
    reply_markup = ReplyKeyboardMarkup(keyboard)
    message = (
        "🇨🇴 Hola! Yo soy CastorBot! \n"
        "Si quieres conocer mis funcionalides envía \n /help: \n\n"
        "También puedes utilizar mi teclado especial ⌨️!\n\n"
        "Intenta ahora!"
    )
    update.message.reply_text(
        message,
        reply_markup = reply_markup,
        parse_mode = 'markdown'
    )
    return
