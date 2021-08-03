def counter():
    lenght = float(input("Введите дину, мм:"))
    weght = float(input("Введите ширину, мм:"))
    squear = lenght * weght
    return squear

th = float(input('Введите толщину листа:'))
stek_sq = []
stek_masa = []
while True:
    sq = counter() / 1000000
    stek_sq.append(sq)
    masa = sq * 7850
    stek_masa.append(masa)
    again = str(input('Добавить еще лист?'))
    if again == 'Y' or again == 'Д' or again == 'Yes' or again == 'Да':
        continue
    break

print('Оющая площадь, метров квадратных:', round(sum(stek_sq)), 2)
print('Общая масса, кг:', round(sum(stek_masa)), 2)