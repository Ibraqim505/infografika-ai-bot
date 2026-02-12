
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_result_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Переделать", callback_data="redo")],
        [InlineKeyboardButton(text="🎨 Сделать новую", callback_data="new")],
        [InlineKeyboardButton(text="🚀 Перейти к инфографике", url="https://aidentika.com")],
        [InlineKeyboardButton(text="🎬 Создать видео (Kling AI)", url="https://kling.ai")]
    ])
