import configparser

from telegram import Update, LinkPreviewOptions, ChatMemberOwner
from telegram.ext import Defaults, ApplicationBuilder, Application, ChatMemberHandler, CommandHandler
from telegram.constants import ParseMode

from components.callbacks import monitoring, fun

async def post_init(application: Application):
    admins = await application.bot.get_chat_administrators(application.bot_data["chat"])
    actual_admins = list(filter(lambda admin: isinstance(admin, ChatMemberOwner) or admin.can_invite_users, admins))
    application.bot_data["admins"] = [admin.user.id for admin in actual_admins]


def main():
    config = configparser.ConfigParser()
    config.read("bot.ini")

    link_preview_options = LinkPreviewOptions(is_disabled=True)
    defaults = Defaults(
        parse_mode=ParseMode.HTML, link_preview_options=link_preview_options
    )
    application = (
        ApplicationBuilder()
        .token(config["KEYS"]["bot_api"])
        .defaults(defaults)
        .post_init(post_init)
        .build()
    )

    application.bot_data["owner"] = config["ID"]["owner"]
    application.bot_data["chat"] = config["ID"]["chat"]

    # application.add_handler(TypeHandler(Update, debug.show_update), group=-1)
    application.add_handler(ChatMemberHandler(monitoring.admin_promoted, chat_member_types=ChatMemberHandler.CHAT_MEMBER), group=-1)
    application.add_handler(ChatMemberHandler(monitoring.admin_gone, chat_member_types=ChatMemberHandler.CHAT_MEMBER), group=-1)

    application.add_handler(CommandHandler('GOOOOOOOL', fun.goal))

    application.run_polling(allowed_updates=Update.ALL_TYPES, close_loop=False, drop_pending_updates=True)


if __name__ == "__main__":
    main()
