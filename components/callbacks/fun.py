from telegram import Update
from telegram.ext import ContextTypes

from components.constants import constants

async def goal(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(constants.SOCCER_BALL)