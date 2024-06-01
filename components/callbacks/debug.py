from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes   
import pprint
import json

async def show_update(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    pprint.pprint(update_str)
    await context.bot.send_message(
        chat_id = context.bot_data["owner"],
        text = f"```json\n{json.dumps(update_str, indent=2, ensure_ascii=False)}\n```",
        parse_mode = ParseMode.MARKDOWN_V2
    )