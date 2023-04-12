from aiogram.dispatcher.filters.state import State, StatesGroup

# processi dlya registracii
class Registration(StatesGroup):
    getting_name_state = State()
    getting_phone_number_state = State()
    getting_location = State()
    getting_gender = State()

# processi dlya vibora opredelennogo tovara
class GetProduct(StatesGroup):
    getting_pr_name = State()
    getting_pr_count = State()

# processi pri rabote s korzinoy
class Cart(StatesGroup):
    waiting_for_product = State()
    waitinf_new_count = State()

# processi pri oformlenii zakaza
class Order(StatesGroup):
    waiting_location = State()
    waiting_pay_type = State()
    waiting_accept = State()
