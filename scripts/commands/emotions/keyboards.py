#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def emotions_keyboard():
    keyboardStr = [
        ['Feliz 😃', 'Sorprendido 😲', 'Neutro 🙂'],
        ['Triste 🙁', 'Furioso 😠️'],
        ['◀️ Atrás']
    ]
    callbackStr = [
        ['happy', 'surprise', 'neutral'],
        ['sad', 'angry'],
        ['back']
    ]
    return createKeyboard(keyboardStr, "inline", callbackStr)
