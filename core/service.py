from loguru import logger

from core.settings.config import settings

messages_to_delete = {}


async def chat_spam(bot):

    chat_list, spam_text = settings.CHATS, settings.SPAM_TEXT

    for chat_id in chat_list:
        message_to_delete = messages_to_delete.get(str(chat_id), None)

        if message_to_delete:

            try:

                await bot.delete_message(
                    chat_id=chat_id,
                    message_id=message_to_delete
                )
                logger.info(f'{chat_id} message deleted successfully.')

            except Exception as e:

                logger.error(f'{chat_id} delete message failed: {e}')

        try:

            msg = await bot.send_message(
                chat_id=chat_id,
                text=spam_text,
                parse_mode="HTML"
            )
            logger.info(f'{chat_id} spammed successfully.')

            messages_to_delete[str(chat_id)] = msg.message_id

        except Exception as e:

            logger.error(f'{chat_id} spam failed: {e}')