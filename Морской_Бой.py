from random import randint

class Tochka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы поля!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку."

class BoardWrongShipException(BoardException):
    pass


class Koryto:
    def __init__(self, nos, l, o):
        self.nos = nos
        self.l = l
        self.o = o
        self.lives = l

    @property
    def paluby(self):
        paluby_koryta = []
        for i in range(self.l):
            _x = self.nos.x
            _y = self.nos.y

            if self.o == 0:
                _x += i

            elif self.o == 1:
                _y += i

            paluby_koryta.append(Tochka(_x, _y))

        return paluby_koryta

    def strelba(self, vystrel):
        return vystrel in self.paluby


class Pole:
    def __init__(self, tuman=False, razmer=6):
        self.razmer = razmer
        self.tuman = tuman

        self.schet = 0

        self.razmetka = [["O"] * razmer for _ in range(razmer)]

        self.busy = []
        self.koryta = []

    def __str__(self):
        res = ""
        res += "  | А | Б | В | Г | Д | Е |"
        res += '\n'+'-'*27
        for i, row in enumerate(self.razmetka):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.tuman:
            res = res.replace("█", "O")
        return res

    def out(self, d):
        return not ((0 <= d.x < self.razmer) and (0 <= d.y < self.razmer))

    def contur(self, koryto, verb=False):
        zona_otchujdenia = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in koryto.paluby:
            for dx, dy in zona_otchujdenia:
                cur = Tochka(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.razmetka[cur.x][cur.y] = "T"
                    self.busy.append(cur)


    def dobavit_koryto(self, koryto):

        for d in koryto.paluby:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in koryto.paluby:
            self.razmetka[d.x][d.y] = "█"
            self.busy.append(d)

        self.koryta.append(koryto)
        self.contur(koryto)

    def vystrel(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for koryto in self.koryta:
            if koryto.strelba(d):
                koryto.lives -= 1
                self.razmetka[d.x][d.y] = "X"
                if koryto.lives == 0:
                    self.schet += 1
                    print("Попал!")
                    return True
                else:
                   print("Попал!")
                   return True

        self.razmetka[d.x][d.y] = "T"
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []


class Igrok:
    def __init__(self, svoe_pole, pole_pricel):
        self.svoe_pole = svoe_pole
        self.pole_pricel = pole_pricel

    def ask(self):
        raise NotImplementedError()

    def hod(self):
        while True:
            try:
                pricel = self.ask()
                povtor = self.pole_pricel.vystrel(pricel)
                return povtor
            except BoardException as e:
                print(e)


class AI(Igrok):
    def ask(self):
        d = Tochka(randint(0, 5), randint(0, 5))
        b = 'АБВГДЕ'
        print(f"Ход компьютера: {b[d.y]}{d.x + 1}")
        return d


class User(Igrok):
    def ask(self):
        while True:
            y_ = (input('Введите координату Х:\n'))[0]
            if y_.isalpha() != True:
                print('Введите букву русского алфавита!')
                continue
            a = 'абвгде'
            b = 'АБВГДЕ'
            if (y_ not in a) and (y_ not in b):
                print('Введите букву русского алфавита в диапазоне от А до Е ')
                continue
            if y_ not in a:
                y = b.find(y_)
            else:
                y = a.find(y_)
            x = (input('Введите координату Y:\n'))[0]

            if x.isdigit() != True:
                print('Введено не число')
                continue
            x = int(x)

            if not (1 <= x <= 6):
                print('Значение за пределами диапазона от 1 до 6!')
                continue

            return Tochka(x-1, y)


class Igra:
    def __init__(self, razmer = 6):
        self.razmer = razmer
        pl = self.random_board()
        co = self.random_board()
        co.tuman = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Pole(razmer=self.razmer)
        popytki = 0
        for l in lens:
            while True:
                popytki += 1
                if popytki > 2000:
                    return None
                koryto = Koryto(Tochka(randint(0, self.razmer), randint(0, self.razmer)), l, randint(0, 1))
                try:
                    board.dobavit_koryto(koryto)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board




    def greet(self):
        print('         Игра "Морской Бой"')
        print('              Поле 6х6')
        print('Кордината X - буква русского алфавита.')
        print('Кордината Y - цифра.')
        print('Кординаты X Y вводить по очереди.')

    def risovalka(self):
        print("=" * 27)
        print("Доска пользователя:")
        print(self.us.svoe_pole)
        print("=" * 27)
        print("Доска компьютера:")
        print(self.ai.svoe_pole)


    def loop(self):
        num = 0
        while True:
            self.risovalka()
            if num % 2 == 0:
                print("=" * 27)
                print("Ходит пользователь!")
                repeat = self.us.hod()
            else:
                print("=" * 27)
                print("Ходит компьютер!")
                repeat = self.ai.hod()
            if repeat:
                num -= 1

            if self.ai.svoe_pole.schet == 7:
                self.risovalka()
                print("=" * 27)
                print("Пользователь выиграл!")

                break

            if self.us.svoe_pole.schet == 7:
                self.risovalka()
                print("=" * 27)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


f = Igra()
f.start()


