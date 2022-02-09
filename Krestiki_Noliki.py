print('Игра "Крестики-Нолики"')
print('Кординаты X Y вводить по очереди')


pole = [[' ' for j in range(3)]for i in range(3)]
a = list(range(1, 9))
b = [((0, 0), (0, 1), (0,2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
     ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
     ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))]

pobeditel = dict(zip(a, b))

def igrovoe_pole():
  print('  0|1|2 -- X')
  print('--------')
  for i in range(3):
      print(i, ('|'.join(pole[i])))
      print('--------')
  print('|')
  print('Y')

def vvod_coordinat():
  while True:
     y = (input('Введите координату Х:\n'))[0]
     x = (input('Введите координату Y:\n'))[0]

     if (x.isdigit() and y.isdigit()) != True:
        print('Введены не числа')
        continue
     x, y = int(x), int(y)

     if not (0 <= x <= 2 or 0 <= y <= 2):
         print ('Значения за пределами диапазона!')
         continue

     if pole[x][y] != ' ':
         print('Поле занято!')
         continue

     return x, y


def proverka_pobeditelia():
   for n in range(1, 9):
      a = pobeditel[n]
      s = ''
      for f in range(3):
         s += pole[a[f][0]][a[f][1]]
      if s == 'XXX':
          igrovoe_pole()
          print('Победили "Крестики"')
          return True
          break
      if s == 'OOO':
          igrovoe_pole()
          print('Победили "Нолики"')
          return True
          break


for i in range(1, 10):
    igrovoe_pole()
    if i%2 == 0:
        print('Ходят "Нолики"')
        x, y = vvod_coordinat()
        pole[x][y] = 'O'
    else:
        print('Ходят "Крестики"')
        x, y = vvod_coordinat()
        pole[x][y] = 'X'
    if i >= 5:
       if proverka_pobeditelia() == True:
          break
    if i == 9:
        igrovoe_pole()
        print('Ничья')
print('Игра окончена')



