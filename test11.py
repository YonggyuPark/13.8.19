Ticket_num = int(input())
Ticket = None  # Счетчик/индекс билетов
Sum = 0  # Итоговая сумма
Age = []  # Список возрастов посетителей

print('Кол-во билетов: ', Ticket_num)
Age = [int(input(f'{Ticket}-й посетитель(возраст): ')) for Ticket in range(1, Ticket_num+1)]
# List comp/список билетов


for Ticket in range(Ticket_num):
    if 18 <= Age[Ticket] <= 25:
        Sum += 990
    elif Age[Ticket] > 25:
        Sum += 1390

if Ticket_num >= 3:
    Sum *= 0.9
    print('Ваша скидка - 10%')

print('Итого к оплате: ', Sum)

# Подскажите, стоило ли включать сюда доп.условия (Что если человек введет отрицательное число) ??
# Или нам необязательно этим заниматься, так как учимся писать тесты, а не программы ??
