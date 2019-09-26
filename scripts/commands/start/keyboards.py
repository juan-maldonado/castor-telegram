#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def start_keyboard():
    keyboardStr = [
        ['/emociones 😃', '/acciones 🎭'],
        ['/saludos 👋', '/hablar 🗣️'],
        ['/cabeza 🎮', '/brazos 🎮'],
        ['/ping 🏓', '/config ⚙️']
    ]
    return createKeyboard(keyboardStr)
