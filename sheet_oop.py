class sheet:

    def __init__(self, thickness):
        self.thickness = thickness


    def counter(self):
        stek_sq = []
        stek_masa = []
        while True:
            th = float(input('Введите толщину листа, мм:'))
            quontity = int(input('Введите колличество деталей:'))
            sq = quontity *  / 1000000
            stek_sq.append(sq)
            masa = sq * th * 7.850
            stek_masa.append(masa)
            again = str(input('Добавить еще лист?(Да (Д), Yes(Y)/No, Нет):'))
            if again == 'Y'.lower() or again == 'Д'.lower() or again == 'Yes'.lower() or again == 'Да'.lower():
                continue
            break




