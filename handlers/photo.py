
from aiogram import Router, types
from services.ai_service import generate_infographic
from utils.file_manager import save_photo, generate_output_path
from keyboards.inline import get_result_keyboard
import logging

router = Router()

@router.message(lambda message: message.photo)
async def photo_handler(message: types.Message, bot):
    await message.answer("🎨 Обрабатываю изображение...")

    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_bytes = await bot.download_file(file.file_path)

    input_path = save_photo(file_bytes.read())
    output_path = generate_output_path()

    try:
        await generate_infographic(input_path, output_path)

        await message.answer_photo(
            photo=types.FSInputFile(output_path),
            caption="✅ Инфографика готова",
            reply_markup=get_result_keyboard()
        )
    except Exception as e:
        logging.error(f"AI generation error: {e}")
        await message.answer("❌ Ошибка генерации. Попробуйте позже.")
