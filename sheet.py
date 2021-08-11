def counter():
    lenght = float(input("Введите длину, мм:"))
    weght = float(input("Введите ширину, мм:"))
    squear = lenght * weght
    return squear



stek_sq = []
stek_masa = []
while True:
    th = float(input('Введите толщину листа, мм:'))
    quontity = int(input('Введите колличество деталей:'))
    sq = quontity * counter() / 1000000
    stek_sq.append(sq)
    masa = sq * th * 7.850
    stek_masa.append(masa)
    again = str(input('Добавить еще лист?(Да (Д), Yes(Y)/No, Нет):'))
    if again == 'Y'.lower() or again == 'Д'.lower() or again == 'Yes'.lower() or again == 'Да'.lower():
        continue
    break

print('Общая площадь, метров квадратных:', sum(stek_sq))
print('Общая масса, кг:', sum(stek_masa))