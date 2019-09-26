#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def movements_keyboard():
    keyboardStr = [
        ['Saludo', 'Me alegro', 'Como estás'],
        ['Muy bien', 'Jugar', 'Adivina'],
        ['Sigue intentando', 'Felicitar', 'Despedida', 'Brazo'],
        ['◀️ Atrás']
    ]
    callbackStr = [
        ['greet', 'nicetomeet', 'howru'],
        ['fine', 'play', 'guess'],
        ['tryagain', 'nice', 'Lbye', 'greet_bye'],
        ['back']
    ]
    return createKeyboard(keyboardStr, "inline", callbackStr)
