#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram import KeyboardButton as Button
from telegram import InlineKeyboardButton as InButton

def createKeyboard(strKeys, mode="keyboard", callbacks = None):
    keyboard = []
    if mode == "keyboard":
        ButtonAux = Button
    else:
        ButtonAux = InButton
    if callbacks == None:
        ButtonType = ButtonAux
        for row in strKeys:
            newRow = map(ButtonType, row)
            keyboard.append(newRow)
    else:
        ButtonType = lambda text, callback: ButtonAux(text, callback_data = callback)
        for row, callback in zip(strKeys, callbacks):
            newRow = map(ButtonType, row, callback)
            keyboard.append(newRow)
    return keyboard
