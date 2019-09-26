#!/usr/bin/python
# -*- coding: utf-8 -*-

from commands.start.keyboards import start_keyboard
import rosgraph

def ping(update, context):
    '''
    keyboard = start_keyboard()
    reply_markup = ReplyKeyboardMarkup(keyboard)
    message = (
        "🇨🇴 Hola! Yo soy CastorBot! \n"
        "Si quieres conocer mis funcionalides envía \n /help: \n\n"
        "También puedes utilizar mi teclado especial ⌨️!\n\n"
        "Intenta ahora!"
    )
    '''
    message = "Pong! 🏓 "
    if rosgraph.is_master_online():
        message += "\nROS is running! ✅"
    else:
        message += "\nROS is not running ❌"
    update.message.reply_text(
        message,
        parse_mode = 'markdown'
    )
    return
