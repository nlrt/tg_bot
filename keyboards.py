# keyboards.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def build_menu(buttons, n_cols):
    menu = []
    for row in range(0, len(buttons), n_cols):
        menu.append(buttons[row:row + n_cols])
    return InlineKeyboardMarkup(menu)

def create_availability_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Проверить наличие номенклатуры", callback_data="check_availability")],
        [InlineKeyboardButton("Создать новую позицию", callback_data="create_new_position")]
    ])

def create_marka_avto_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("AUDI/VW", callback_data="marka_avto_AUDI_VW")],
        [InlineKeyboardButton("BMW", callback_data="marka_avto_BMW")],
        [InlineKeyboardButton("FIAT", callback_data="marka_avto_FIAT")],
        [InlineKeyboardButton("FORD", callback_data="marka_avto_FORD")],
        [InlineKeyboardButton("Hyundai", callback_data="marka_avto_Hyundai")],
        [InlineKeyboardButton("IVECO", callback_data="marka_avto_IVECO")],
        [InlineKeyboardButton("ROVER", callback_data="marka_avto_ROVER")],
        [InlineKeyboardButton("MERCEDES-BENZ", callback_data="marka_avto_MERCEDES_BENZ")],
        [InlineKeyboardButton("OPEL", callback_data="marka_avto_OPEL")],
        [InlineKeyboardButton("Другое авто", callback_data="marka_avto_other")]
    ])

def create_group_keyboard():
    # ... (existing code for creating group keyboard)
    return [
        [InlineKeyboardButton("Плунжерные пары/распылители/расходники", callback_data="group_plunger")],
        [InlineKeyboardButton("Ступицы и подшипники", callback_data="group_hub_bearing")],
        [InlineKeyboardButton("Гофра", callback_data="group_goffra")],
        [InlineKeyboardButton("Масла и жидкости", callback_data="group_oils")],
        [InlineKeyboardButton("Выхлопная/воздушная система", callback_data="group_exhaust")],
        [InlineKeyboardButton("Топливная система", callback_data="group_fuel")],
        [InlineKeyboardButton("Система охлаждения/отопления", callback_data="group_cooling")],
        [InlineKeyboardButton("Тормозная система", callback_data="group_brakes")],
        [InlineKeyboardButton("Система зажигания", callback_data="group_ignition")],
        [InlineKeyboardButton("Ременный привод", callback_data="group_belt_drive")],
        [InlineKeyboardButton("Цепной привод", callback_data="group_chain_drive")],
        [InlineKeyboardButton("Сцепление", callback_data="group_clutch")],
        [InlineKeyboardButton("Подвеска/рулевое управление", callback_data="group_suspension")],
        [InlineKeyboardButton("Амортизация", callback_data="group_amortization")],
        [InlineKeyboardButton("Прокладки", callback_data="group_gaskets")],
        [InlineKeyboardButton("Поршни", callback_data="group_pistons")],
        [InlineKeyboardButton("Клапана", callback_data="group_valves")],
        [InlineKeyboardButton("Гильзы", callback_data="group_cylinders")],
        [InlineKeyboardButton("Поршневые кольца", callback_data="group_piston_rings")],
        [InlineKeyboardButton("Седла", callback_data="group_seats")],
        [InlineKeyboardButton("Напра-е втулки клапана", callback_data="group_valve_guides")],
        [InlineKeyboardButton("Вкладыши", callback_data="group_bearings")],
        [InlineKeyboardButton("Ремкомплекты/сальники", callback_data="group_kits")],
        [InlineKeyboardButton("Распредвал", callback_data="group_camshaft")],
        [InlineKeyboardButton("Коленвал", callback_data="group_crankshaft")],
        [InlineKeyboardButton("Коромысло", callback_data="group_rocker_arm")],
        [InlineKeyboardButton("Компенсатор", callback_data="group_compensator")],
        [InlineKeyboardButton("Рокера", callback_data="group_rocker")],
        [InlineKeyboardButton("Шатун", callback_data="group_connecting_rod")],
        [InlineKeyboardButton("Масляный насос/радиатор/датчики/крышки", callback_data="group_oil_parts")],
        [InlineKeyboardButton("Фильтры", callback_data="group_filters")],
        [InlineKeyboardButton("Прочее", callback_data="group_other")]
    ]