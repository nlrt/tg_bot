# bot.py
import os
import json
import asyncio
import logging
import config
import gspread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CallbackContext, CallbackQueryHandler, CommandHandler, ConversationHandler, MessageHandler, filters


# Установка базового уровня логирования
logging.basicConfig(level=logging.INFO)

# Google Sheets
gc = gspread.service_account(filename=config.CREDENTIALS_FILE)
sh = gc.open_by_key(config.SPREADSHфEET_ID)
wks = sh.worksheet("3В")

# States
WAITING_FOR_ACTION = 0
WAITING_FOR_PASSWORD = 1
WAITING_FOR_AVAILABILITY_INPUT = 2
WAITING_FOR_MARKA_AVTO_RESPONSE = 3
WAITING_FOR_GROUP_RESPONSE = 4

async def start(update: Update, context: CallbackContext) -> None:
    context.user_data.clear()
    await update.message.reply_text("Введите пароль:")
    return WAITING_FOR_PASSWORD

async def check_password(update: Update, context: CallbackContext) -> int:
    if update.message.text == config.PASSWORD:
        await update.message.reply_text("Выберите действие:", reply_markup=create_availability_keyboard())
        return WAITING_FOR_ACTION
    else:
        await update.message.reply_text("Неверный пароль")
        return WAITING_FOR_PASSWORD

async def check_availability(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Введите артикул или название товара:")
    return WAITING_FOR_AVAILABILITY_INPUT

async def availability_input(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    search_value = update.message.text.strip().lower()
    results = wks.findall(search_value, in_column=4)

    if results:
        response = ""
        for res in results:
            row = res.row
            response += f"{wks.cell(row, 1).value} - {wks.cell(row, 4).value}\n"
            response += f"{wks.cell(row, 2).value} {wks.cell(row, 3).value}\n"
            response += f"{wks.cell(row, 6).value} {wks.cell(row, 7).value}\n"
            response += f"{wks.cell(row, 9).value}\n"
            response += f"------------------------------\n"
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("Товар не найден")

    await update.message.reply_text("Выберите действие:", reply_markup=create_availability_keyboard())
    return WAITING_FOR_ACTION

async def create_new_position(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    await query.message.edit_text("Введите артикул:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_MARKA

async def marka(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    marka = query.data.strip()
    context.user_data["marka"] = marka

    await query.message.edit_text("Введите Бренд:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_BREND

async def brend(update: Update, context: CallbackContext) -> None:
    brend = update.message.text.strip()
    context.user_data["brend"] = brend

    await update.message.chat.send_message("Введите Страну производителя:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_COUNTRY

async def country(update: Update, context: CallbackContext) -> None:
    country = update.message.text.strip()
    context.user_data["country"] = country

    await update.message.chat.send_message("Введите Наименование:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_NAME

async def name(update: Update, context: CallbackContext) -> None:
    name = update.message.text.strip()
    context.user_data["name"] = name

    await update.message.chat.send_message("Введите Количество:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_QUANTITY

async def quantity(update: Update, context: CallbackContext) -> None:
    quantity = update.message.text.strip()
    context.user_data["quantity"] = quantity

    await update.message.chat.send_message("Введите Цену:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_PRICE

async def price(update: Update, context: CallbackContext) -> None:
    price = update.message.text.strip()
    context.user_data["price"] = price

    await update.message.chat.send_message("Введите Номер партии:", reply_markup=ReplyKeyboardRemove())
    return WAITING_FOR_PART_NUMBER

async def part_number(update: Update, context: CallbackContext) -> None:
    part_number = update.message.text.strip()
    context.user_data["part_number"] = part_number

    await update.message.chat.send_message("Выберите Марку авто:", reply_markup=create_marka_avto_keyboard())
    return WAITING_FOR_MARKA_AVTO_RESPONSE

async def marka_avto_response(update: Update, context: CallbackContext) -> None:
    marka_avto = update.message.text.strip()
    context.user_data["marka_avto"] = marka_avto

    await update.message.chat.send_message("Выберите Группу:", reply_markup=create_group_keyboard())
    return WAITING_FOR_GROUP_RESPONSE

async def group_response(update: Update, context: CallbackContext) -> None:
    group = update.message.text.strip()
    context.user_data["group"] = group

    # Get the current row number based on the previous input
    row_number = int(context.user_data.get("row_number", 0))

    # Add the new row with the user's input
    wks.update_cell(row_number, 1, context.user_data["marka"])
    wks.update_cell(row_number, 2, context.user_data["brend"])
    wks.update_cell(row_number, 3, context.user_data["country"])
    wks.update_cell(row_number, 4, context.user_data["name"])
    wks.update_cell(row_number, 5, context.user_data["quantity"])
    wks.update_cell(row_number, 6, context.user_data["price"])
    wks.update_cell(row_number, 7, context.user_data["part_number"])
    wks.update_cell(row_number, 8, context.user_data["marka_avto"])
    wks.update_cell(row_number, 9, context.user_data["group"])

    # Clear the user data and reset the state
    context.user_data.clear()
    return WAITING_FOR_ACTION

def create_availability_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Проверить наличие", callback_data="check_availability")],
        [InlineKeyboardButton("Добавить товар", callback_data="create_new_position")]
    ])

def create_marka_avto_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Audi", callback_data="audi"),
         InlineKeyboardButton("BMW", callback_data="bmw")],
        [InlineKeyboardButton("Mercedes-Benz", callback_data="mercedes_benz"),
         InlineKeyboardButton("Volkswagen", callback_data="volkswagen")],
        [InlineKeyboardButton("Ford", callback_data="ford"),
         InlineKeyboardButton("Opel", callback_data="opel")],
        [InlineKeyboardButton("Toyota", callback_data="toyota"),
         InlineKeyboardButton("Honda", callback_data="honda")]
    ])

def create_group_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Группа 1", callback_data="group_1"),
         InlineKeyboardButton("Группа 2", callback_data="group_2")],
        [InlineKeyboardButton("Группа 3", callback_data="group_3"),
         InlineKeyboardButton("Группа 4", callback_data="group_4")]
    ])

async def check_password(update: Update, context: CallbackContext) -> int:
    try:
        if update.message.text == config.PASSWORD:
            await update.message.reply_text("Выберите действие:", reply_markup=create_availability_keyboard())
            return WAITING_FOR_ACTION
        else:
            await update.message.reply_text("Неверный пароль")
            return WAITING_FOR_PASSWORD
    except Exception as e:
        logging.error(f"Error in check_password: {e}")
        return WAITING_FOR_PASSWORD



# Создание объекта приложения
application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()

# Использована проверка filters.TEXT, чтобы избежать конфликта с командами
application.add_handler(MessageHandler(filters.TEXT, check_password))

# Add handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_password))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_availability))
application.add_handler(CallbackQueryHandler(availability_input, pattern="availability_input"))
application.add_handler(CallbackQueryHandler(create_new_position, pattern="create_new_position"))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, marka))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, brend))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, country))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, name))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, quantity))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, price))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, part_number))
application.add_handler(CallbackQueryHandler(marka_avto_response, pattern="marka_avto_response"))
application.add_handler(CallbackQueryHandler(group_response, pattern="group_response"))

async def main() -> None:
    try:
        # Запуск бота
        await application.run_polling()
    except (KeyboardInterrupt, SystemExit):
        logging.info("\nExiting...")
    finally:
        await application.shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(application.run_polling())
    except KeyboardInterrupt:
        logging.info("\nExiting...")
    finally:
        application.shutdown()