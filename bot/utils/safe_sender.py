import asyncio
from typing import Any, Awaitable, Callable

from aiogram.types import Message
from aiogram.utils.exceptions import NetworkError, RetryAfter, TelegramAPIError

from bot.logger_mesh import logger


async def _safe_telegram_call(call: Callable[[], Awaitable[Any]], *, context: str) -> Any | None:
    """Execute a Telegram API call with retry on flood-related errors."""
    attempt = 0
    while True:
        try:
            return await call()
        except RetryAfter as exc:
            delay = getattr(exc, "timeout", getattr(exc, "retry_after", 1)) + 0.5
            attempt += 1
            logger.warning("RetryAfter while %s. Sleeping %.1fs (attempt %s)", context, delay, attempt)
            await asyncio.sleep(delay)
        except NetworkError as exc:
            attempt += 1
            delay = min(5, 0.5 * attempt)
            logger.warning("Network error while %s: %s. Retrying in %.1fs", context, exc, delay)
            await asyncio.sleep(delay)
        except TelegramAPIError as exc:
            logger.error("Telegram API error while %s: %s", context, exc)
            return None


def safe_send_message(message: Message, text: str, **kwargs) -> Awaitable[Any | None]:
    """Safely send a new message reusing the bot from a message object."""
    return _safe_telegram_call(
        lambda: message.bot.send_message(chat_id=message.chat.id, text=text, **kwargs),
        context="sending message",
    )


def safe_send_copy(original: Message, chat_id: int, **kwargs) -> Awaitable[Any | None]:
    """Safely copy a message to another chat."""
    return _safe_telegram_call(
        lambda: original.send_copy(chat_id=chat_id, **kwargs),
        context=f"copying message to {chat_id}",
    )
