# user_input.py

def get_text(message):
    return message.text

def get_new_position_info(message):
    position_info = {}
    position_info['article'] = message.text
    bot.send_message(message.chat.id, 'Введите бренд: ')
    position_info['brand'] = message.text
    bot.send_message(message.chat.id, 'Введите страну производителя: ')
    position_info['country'] = message.text
    bot.send_message(message.chat.id, 'Введите наименование: ')
    position_info['name'] = message.text
    bot.send_message(message.chat.id, 'Введите количество: ')
    position_info['quantity'] = message.text
    bot.send_message(message.chat.id, 'Введите цену себестоимости: ')
    position_info['cost'] = message.text
    bot.send_message(message.chat.id, 'Введите номер партии: ')
    position_info['batch_number'] = message.text
    bot.send_message(message.chat.id, 'Выберите марку автомобиля: \nAUDI/VW \nBMW \nFIAT \nFORD \nHyundai \nIVECO \nROVER \nMERCEDES-BENZ \nOPEL \nДругое авто')
    position_info['car_brand'] = message.text
    bot.send_message(message.chat.id, 'Выберите группу: \nПлунжерные пары/распылители/расходники \nСтупицы и подшипники \nГофра \nМасла и жидкости \nВыхлопная/воздушная система \nТопливная система \nСистема охлаждения/отопления \nТормозная система \nСистема зажигания \nРеменный привод \nЦепной привод \nСцепление \nПодвеска/рулевое управление \nАмортизация \nПрокладки \nПоршни \nКлапана \nГильзы \nПоршневые кольца \nСедла \nНапра-е втулки клапана \nВкладыши \nРемкомплекты/сальники \nРаспредвал \nКоленвал \nКоромысло \nКомпенсатор \nРокера \nШатун \nМасляный насос/радиатор/датчики/крышки \nФильтры \nПрочее')
    position_info['group'] = message.text
    return position_info
