from telegram import Update, ChatMemberAdministrator
from telegram.ext import ContextTypes


async def admin_promoted(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member.new_chat_member
    if isinstance(member, ChatMemberAdministrator) and member.can_invite_users:
        context.bot_data["admins"].append(member.user.id)


async def admin_gone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_member = update.chat_member.new_chat_member
    old_member = update.chat_member.old_chat_member
    if (
        isinstance(old_member, ChatMemberAdministrator)
        and old_member.can_invite_users
        and (
            not isinstance(new_member, ChatMemberAdministrator)
            or not new_member.can_invite_users
        )
    ):
        context.bot_data["admins"].pop(new_member.user.id)
