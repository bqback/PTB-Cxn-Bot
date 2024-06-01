import configparser

from telegram import Update, LinkPreviewOptions
from telegram.ext import Defaults, ApplicationBuilder, TypeHandler, Application
from telegram.constants import ParseMode

from components.callbacks import debug


async def post_init(_: Application):
    return


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

    application.add_handler(TypeHandler(Update, debug.show_update), group=-1)

    application.run_polling(allowed_updates=Update.ALL_TYPES, close_loop=False)


if __name__ == "__main__":
    main()
