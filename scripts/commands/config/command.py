#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def config(update, context):
    message = "Lanzando ROS 🚀"
    command = "roslaunch castor_motors_orchestrator orchestrator.launch"
    try:
        p = subprocess.Popen(command, shell = True)
        state = p.poll()
    except:
        message = "Error lanzando ROS ❌"
    update.message.reply_text(
        message,
        parse_mode = "markdown"
    )
