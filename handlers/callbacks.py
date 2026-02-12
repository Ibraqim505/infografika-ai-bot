
from aiogram import Router, types

router = Router()

@router.callback_query(lambda c: c.data == "redo")
async def redo_handler(callback: types.CallbackQuery):
    await callback.message.answer("🔄 Переделываю...")

@router.callback_query(lambda c: c.data == "new")
async def new_handler(callback: types.CallbackQuery):
    await callback.message.answer("🎨 Создаю новую версию...")
