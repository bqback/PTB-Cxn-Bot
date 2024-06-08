from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import DiceEmoji

# from components.constants import constants

async def goal(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_dice(emoji=DiceEmoji.FOOTBALL)