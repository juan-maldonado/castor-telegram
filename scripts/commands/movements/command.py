#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup, ReplyKeyboardRemove
from commands.movements.keyboards import movements_keyboard

def movements(update, context):
    keyboard = movements_keyboard()
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (
        "Selecciona una opción en el teclado:"
    )
    update.message.reply_text(
        message,
        reply_markup = reply_markup,
        parse_mode = 'markdown'
    )
    return
