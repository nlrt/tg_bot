#functions.py

import xlrd

def get_products_from_file():
    # Открываем файл
    with open("Шаблон номенклатуры.xlsx", "r") as f:
        data = f.readlines()

    # Удаляем пустые строки из файла
    products = [
        line.strip()
        for line in data
        if line.strip() != ""
    ]

    # Разделяем строки на массивы
    products = [
        line.split(";")
        for line in products
    ]

    return products

def check_password(update: Update, context: CallbackContext):
    if update.message.text != "515746":
        context.bot.send_message(
            update.effective_chat.id,
            "Неверный пароль. Пожалуйста, введите правильный пароль.",
        )
        return

    context.user_data["is_authenticated"] = True
    context.bot.send_message(
        update.effective_chat.id, "Вы успешно прошли аутентификацию."
    )

def search_product(update: Update, context: CallbackContext):
    if not context.user_data["is_authenticated"]:
        context.bot.send_message(
            update.effective_chat.id, "Пожалуйста, пройдите аутентификацию."
        )
        return

    # Получаем от пользователя данные для поиска

    search_data = update.message.text
