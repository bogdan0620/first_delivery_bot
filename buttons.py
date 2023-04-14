from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# knopka dlya otpravki nomera telefona
def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Поделиться контактом 📞', request_contact=True)
    kb.add(button)
    return kb

# knopka dlya otpravki lokacii
def location_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Поделиться локацией 📍', request_location=True)
    kb.add(button)
    return kb

# knopka dlya vibora pola
def gender_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Мужчина ')
    button2 = KeyboardButton('Женщина ')
    kb.add(button, button2)
    return kb

# knopki dlya vibora kolichestva
def product_count():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [KeyboardButton(str(i)) for i in range(1, 10)]
    back = KeyboardButton('◀️ Назад')
    kb.add(*buttons, back)
    return kb

# knopki dlya korzini
def cart_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Очистить')
    button2 = KeyboardButton('Оформить заказ')
    button3 = KeyboardButton('Редактировать')
    button4 = KeyboardButton('◀️ Назад')
    kb.add(button, button2, button3, button4)
    return kb

# knopki pri vibore sposoba oplati
def pay_type_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Наличные')
    button2 = KeyboardButton('Карта')
    button3 = KeyboardButton('◀️ Назад')
    kb.add(button, button2, button3)
    return kb

# knopki dlya potverjdeniya zakaza
def confirmation_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Подтвердить')
    button2 = KeyboardButton('Отменить')
    button3 = KeyboardButton('◀️ Назад')
    kb.add(button, button2, button3)
    return kb









# knopki s nazvaniyami tovarov
def products_kb():
    pass
