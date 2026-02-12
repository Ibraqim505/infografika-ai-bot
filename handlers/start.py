
from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "🚀 <b>AI Инфографика Бот</b>\n\n"
        "Загрузи фото товара — получи готовую продающую инфографику."
    )
