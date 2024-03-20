'''
Отобразить список перелетов
 - ​с номером
 - с названием от куда куда, 
 - время вылета
 - и цена за перелет
'''
avia_raises = [
{'code': 100, 'destination': 'Бишкек-Ош', 'start_time': '13:00', 'price': 4500},
{'code': 101, 'destination': 'Бишкек-Москва', 'start_time': '23:00', 'price': 12500},
{'code': 102, 'destination': 'Бишкек-Стамбул', 'start_time': '04:00', 'price': 24500},
{'code': 103, 'destination': 'Бишкек-Париж', 'start_time': '01:00', 'price': 34500},
{'code': 104, 'destination': 'Бишкек-Турция', 'start_time': '12:00', 'price': 54500},
{'code': 105, 'destination': 'Бишкек-Дубаи', 'start_time': '17:00', 'price': 34500}
]

def print_avia():
    print("Авиа рейсы:")
    for avia in avia_raises:
        print('==========================')
        print(f'CODE: {avia["code"]}')
        print(f'Маршрут: {avia["destination"]}')
        print(f'Время вылета: {avia["start_time"]}')
        print(f'Цена: {avia["price"]} сом')
        print('==========================')


# Пользователю требуется выбрать по номеру перелет

def choice_destination_by_code():
    while True:
        try:
            code = int(input('Введите код авиа рейса: '))
        except Exception:
            print('Не верный формат кода, введите обратно!')
            continue
    
        result = None
        for avia in avia_raises:
            if code == avia['code']:
                result = avia

        if result is None:
            print('С таким кодом авиа рейса не существует, введите обратно!')
            continue    

        break

    return result

# Стартуем функции
print_avia()
my_fly = choice_destination_by_code()
print('==========================')
print(f'\t Ваш Маршрут: {my_fly["destination"]}')
print(f'\t Вылет в {my_fly["start_time"]}')
print(f'\t Стоимость билета: {my_fly["price"]} сом')
print('==========================')

'''
Заплатить сколько требуется
​​​​​ - ​если введные денежные средства совпадает с ценой то успешно
 - если больше отдать сдачу
 - если меньше то отказать и отобразить сообщение
'''

def avia_bill():
    while True:
        try:
            bill = int(input('Оплатите: '))
            if bill == my_fly['price']:
                # После успешного прохождения, вывести сообщение
                # ​​​​​​​​​​​​​​номер билета
                # с названием от куда куда
                # время вылета
                print('==========================')
                print('=========ОПЛАЧЕНО=========')
                print('==========================')
                print(f'Ваш код: {my_fly['code']}, \nРейс: {my_fly['destination']}, \nвремя: {my_fly['start_time']}')
                break
            elif bill > my_fly['price']:
                cashback = bill - my_fly['price']
                print('==========================')
                print('=========ОПЛАЧЕНО=========')
                print('==========================')
                print(f'Ваш код: {my_fly['code']}, \nрейс: {my_fly['destination']}, \nвремя: {my_fly['start_time']}')
                print(f'Ваша сдача: {cashback}')
                break
            else:
                print('У вас недостаточно средств на балансе!')
        finally:            
            break

avia_bill()