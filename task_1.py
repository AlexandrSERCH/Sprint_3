import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def get_items_names(self):
        return self.__item_price.keys()

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = 0

        for item in self.__name_items:
            total += self.__item_price[item]

        if len(self.__name_items) > 10:
            total = total * 0.9

        return total

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        discount = 0.9 if len(self.__name_items) > 10 else 1

        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item] * discount)

        return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        discount = 0.9 if len(self.__name_items) > 10 else 1

        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item] * discount)

        return sum(total) * 0.1

    def total_tax(self):
        twenty_percent = self.twenty_percent_tax_calculation()
        ten_percent = self.ten_percent_tax_calculation()

        return twenty_percent + ten_percent

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        if  len(str(telephone_number)) != 10: # Странно, что в условии не указали ещё "меньше 10 символов"
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f"+7{telephone_number}"

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]

        for name, func in date:
            date_and_time.append(f'{name}: {func(now)}')

        return date_and_time


basket = OnlineSalesRegisterCollector()
items_names = basket.get_items_names()
[basket.add_item_to_cheque(item) for item in items_names]
print("Список товаров в корзине:", basket.name_items)
print("Количество товаров в корзине:", basket.number_items)
basket.delete_item_from_check("чипсы")
print("----- После удаления -----")
print("Список товаров в корзине:",basket.name_items)
print("Количество товаров в корзине:", basket.number_items)
print("Стоимость корзины:", basket.check_amount())

amount_twenty_percent_tax = basket.twenty_percent_tax_calculation()
print("Общая сумма НДС со ставкой 20%:", amount_twenty_percent_tax)

amount_ten_percent_tax = basket.ten_percent_tax_calculation()
print("Общая сумма НДС со ставкой 10%:", amount_ten_percent_tax)

print("Общая сумма НДС:", basket.total_tax())

print("Номер телефона:", OnlineSalesRegisterCollector().get_telephone_number(1234567891))

print("Дата и время покупки:", OnlineSalesRegisterCollector().get_date_and_time())
