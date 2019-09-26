#!/usr/bin/python
# -*- coding: utf-8 -*-

def greetings(update, context, pub):
    message = "Saludando ... 👋"
    msg = "greet"
    pub.publish(msg)
    update.message.reply_text(
        message,
        parse_mode = "markdown"
    )
    return
