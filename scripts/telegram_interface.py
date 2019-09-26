#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
import random

#ROS Libraries
import rospy
from std_msgs.msg import String

#Telegram Libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton as Button

from commands.start.command import start
from commands.start.keyboards import start_keyboard
from commands.emotions.command import emotions
from commands.emotions.callback import emotions_callback
from commands.ping.command import ping
from commands.movements.command import movements
from commands.movements.callback import movements_callback
from commands.config.command import config

#Telegram logging
import logging

logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)8s [%(funcName)s] %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class CastorECIBot():
    def __init__(self, name):
        self.name = name
        #Call of Initializer Functions
        self.initNode()
        self.initParameters()
        self.initSubscribers()
        self.initPublishers()
        self.initVariables()
        #self.main_ros()
        #self.rospy.spin()

    def initNode(self):
        self.rospy = rospy
        self.rospy.init_node(self.name, anonymous = False)
        self.rospy.loginfo("[%s] Starting", self.name)
        self.rate = self.rospy.Rate(20)
        return

    def initParameters(self):
        ## TODO: Hide the Token, it can be used by anyone to control the bot!
        self.token = self.rospy.get_param('/token', '913726881:AAH7kvp95qMlS4fD9hwFfSySl1vBVO_jDXc')
        if self.token is None:
            self.rospy.logerr("[%s] No token found in /telegram/token param server.", self.name)
            exit(0)
        else:
            self.rospy.loginfo("[%s] Got telegram bot token from param server.", self.name)
        self.emotionsTopic = self.rospy.get_param('/emotions_topic', '/emotions')
        self.movementsTopic = self.rospy.get_param('/movements_topic', '/movements')
        return

    def initSubscribers(self):
        return

    def initPublishers(self):
        self.pubEmotions = self.rospy.Publisher(self.emotionsTopic, String, queue_size = 5)
        self.pubMovements = self.rospy.Publisher(self.movementsTopic, String, queue_size = 5)
        return

    def initVariables(self):
        self.selected_function = False
        # TODO: Add more phrases
        self.random_phrases = [
            "Por el momento, no sé como responder a eso 🤔",
            "Yo soy el robot Castor!",
        ]
        return

    def textCallback(self, update, context):
        keyboard = start_keyboard()
        reply_markup = ReplyKeyboardMarkup(keyboard)
        message = (
            random.choice(self.random_phrases)
        )
        update.message.reply_text(
            message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
        return

    def error(self):
        logger.warn('Update "%s" caused error "%s"' % (update, error))
        self.rospy.warn('[%s] Error in telegram bot!', self.name)
        return

    def main_ros(self):
        self.rospy.loginfo("[%s] ROS interfacer for Telegram bot OK", self.name)
        while not self.rospy.is_shutdown():
            self.rate.sleep()
        print("**")

    def main_bot(self):
        updater = Updater(self.token, use_context = True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("emociones", emotions, pass_chat_data = True))
        dp.add_handler(CommandHandler("hablar", movements, pass_chat_data = True))
        dp.add_handler(CommandHandler("config", config))
        dp.add_handler(CallbackQueryHandler(lambda update, context: emotions_callback(update, context, self.pubEmotions)))
        dp.add_handler(CallbackQueryHandler(lambda update, context: movements_callback(update, context, self.pubMovements)))
        dp.add_handler(CommandHandler("ping", ping))
        #dp.add_handler(CommandHandler("prueba", lambda update, context: prueba(update, context, self.pubEmotions)))
        dp.add_handler(MessageHandler(Filters.text, self.textCallback))

        dp.add_error_handler(self.error)

        updater.start_polling()
        logger.info('Listening humans as %s..' % updater.bot.username)
        self.rospy.loginfo('[%s] Telegram Updater for %s OK', updater.bot.username, self.name)
        updater.idle()

        return

if __name__ == '__main__':
    #try:
        Bot = CastorECIBot('CastorProjectBot')
        thread1 = Thread(target = Bot.main_ros)
        thread1.start()
        Bot.main_bot()
    #Bot.main_bot()
    #except:
    #    print("Something's gone wrong. Exiting")
