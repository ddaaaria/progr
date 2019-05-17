import random
import os
import time

prnames = ["Алёна", "Василиса", "Эльвира", "Даздраперма", "Рапунцель", "Креветка", "Маня"]
pradjectives = ["Несмеяна", "Датская", "Самодостаточная", "Ивановна", "Нептуновна"]
names = ["нож", "улыбка", "кулак", "копьё", "батон", "зонт", "прищепка", "колбаса", "морковка", "зубная щетка", "пушка"]
adjectives = ["свободы", "смерти", "силы", "удали", "всевластия", "добра", "безнадежности", "хитрости"]
ranks = ["Святополк", "Зевс", "Александр", "Георг", "Наполеон", "Карл", "Валерка", "Максим"]
rangs = ["Лучезарный", "Беспринципный", "Игривый", "Сонный", "Второй", "Купчинский", "Зеленобородый", "Яковлевич"]


class Princess(object):
    def __init__(self):
        self.will = random.randint(-10, 10)
        self.prname = random.choice(prnames)
        self.pradjective = random.choice(pradjectives)


class Fighter(object):
    def __init__(self):
        self.power = random.randint(0, 10)
        self.hp = random.randint(0, 10)

    def fight(self, other):
        other.hp -= self.power


class Monster(Fighter):
    def __init__(self):
        super(Monster, self).__init__()
        self.hunger = random.randint(0, 10)


class Warrior(Fighter):
    def __init__(self):
        super(Warrior, self).__init__()
        self.persuasion = random.randint(-10, 10)
        self.supply = random.randint(-10, 10)


prin = 0
res = 1
player = Warrior()
beast = Monster()
queen = Princess()

print("ВАШЕ РЫЦАРСКОЕ ИМЯ: " + str(random.choice(ranks)) + " " + str(random.choice(rangs)) + "\n" + "\n" \
      + "Сила              : " + str(player.power) + "\n" \
      + "HP                : " + str(player.hp) + "\n" \
      + "Сила убеждения    : " + str(player.persuasion) + "\n" \
      + "Припас еды        : " + str(player.supply) + "\n")

time.sleep(3)
print("ВЫБИРАЙТЕ ОРУЖИЕ:  ", '\n')


class Item(object):
    def __init__(self, id):
        self.id = id
        self.name = random.choice(names)
        self.adjective = random.choice(adjectives)
        self.power = int(random.normalvariate(0, 4))
        self.hp = int(random.normalvariate(0, 4))
        self.persuasion = int(random.normalvariate(0, 4))
        self.hunger = int(random.normalvariate(0, 4))

    def item_create(self):
        return "#" + str(self.id) + " " + self.name + " " + self.adjective + "\n" \
               + "Сила атаки     : " + str(self.power) + "\n" \
               + "HP             : " + str(self.hp) + "\n" \
               + "Сила убеждения : " + str(self.persuasion) + "\n" \
               + "Уталение голода: " + str(self.hunger) + "\n"


ar = []
for i in range(7):
    ar.append(Item(i))
for i in ar:
    print(i.item_create())

c = input("ВВЕДИТЕ  НОМЕРА ВЫБРАННОГО ОРУЖИЯ : ")
b = int(c[0])
d = int(c[2])

player.hp += ar[b].hp + ar[d].hp
player.power += ar[b].power + ar[d].power
player.supply += ar[b].hunger + ar[d].hunger
player.persuasion += ar[b].persuasion + ar[d].persuasion

os.system("cls")

print("Теперь все выглядит так : ", "\n",
      "Ваша сила атаки : ", str(player.power), "\n",
      "HP              : " + str(player.hp), "\n",
      "Сила убеждения  : " + str(player.persuasion), "\n",
      "Припас еды      : " + str(player.supply), "\n")

time.sleep(3)

print("А вот и  монстр!!!", "\n",
      "Сила           : ", str(beast.power), "\n",
      "HP             : " + str(beast.hp), "\n",
      "Голод          : " + str(beast.hunger), "\n")

if player.supply > 0:
    beast.hunger -= player.supply
    print("ВЫ ПОКОРМИЛИ МОНСТРА. ТЕПЕРЬ ЕГО : ", "\n",
          "Сила           : ", str(beast.power), "\n",
          "HP             : " + str(beast.hp), "\n",
          "Голод          : " + str(beast.hunger), "\n")

h = int(input("Сбежать? ДА = 1,НЕТ = 2  "))
if h == 1:
    print(
        "ВЫ СПАСЛИСЬ, НО НЕ СПАСЛИ ЛЮБИМУЮ. ПРИНЦЕССА УМРЁТ В МУКАХ.НАДЕЮСЬ, ВЫ СМОЖЕТЕ ДОГОВОРИТЬСЯ С СОВЕСТЬЮ И БУДЕТЕ СПОКОЙНО СПАТЬ ПО НОЧАМ.",
        "\n")
else:
    h = int(input("Попобовать договориться? ДА = 1,НЕТ = 2  "))
    if h == 1:
        if int(player.persuasion) >= int(beast.hunger):
            print("ВЫ - ПРИРОЖДЕННЫЙ ДИПЛОМАТ! ДРАКОН С РАДОСТЬЮ ПРОПУСКАЕТ ВАС В ПОКОИ ПРИНЦЕССЫ. ", "\n")
            prin = 1
        else:
            print("О-ОУ! ДОГОВОРИТЬСЯ НЕ ПОЛУЧИЛОСЬ, И ВАС СЪЕЛИ,КАК ПУДДИНГ. ВРЕДНЫЙ, НАДОЕДЛИВЫЙ, ГОВОРЯЩИЙ ПУДИНГ. ",
                  "\n")
    else:
        q = int(input("Будете сражаться? ДА = 1,НЕТ = 2  "))
        if q == 1:
            while int(beast.hp) >= 0 and int(player.hp) >= 0:
                if int(player.hp) > 0:
                    res = 1
                    beast.fight(player)
                    print("удар! вы бьете монстра на ", player.power, "\n", "HP монстра : ", beast.hp, "\n")
                if int(beast.hp) > 0:
                    res = 0
                    player.fight(beast)
                    print("контратака! вам наносят удар в ", beast.power, "\n", "Ваше HP : ", player.hp, "\n")

            if res == 1:
                print("УРА, ВЫ ПОБЕДИЛИ ЧУДОВИЩЕ! МОЖЕТЕ С ГОРДОСТЬЮ ПРОЙТИ В ПОКОИ ПРИНЦЕССЫ. ", "\n")
                prin = 1
            else:
                print("ДРАКОН РАССЕРДИЛСЯ И СЪЕЛ ВАС, НЕ ОСТАВИВ НИ КРСТОЧКИ. ", "\n")
        else:
            print("ДРАКОН ПРИНЯЛ ВАС ЗА МЕБЕЛЬ, СЕЛ НА ВАС И РАЗДАВИЛ. А ВЫ НЕ ОЧЕНЬ ХОРОШЕЕ КРЕСЛО. ", "\n")
time.sleep(5)

if prin == 1:
    print("ПРЕКРАСНУЮ ПРИНЦЕССУ ЗОВУТ : " + random.choice(prnames) + " " + random.choice(pradjectives) + "\n" \
          "Её желание сбежать         : " + str(queen.will) + "\n")
    if int(player.persuasion) > 0:
        queen.will += player.persuasion
        print("ВЫ ПРИМЕНИЛИ НАВЫК ОЧАРОВАНИЯ, ТЕПЕРЬ ЕЁ ЖЕЛАНИЕ СБЕЖАТЬ : ", queen.will)
    if int(queen.will) <= 0:
        print(
            "ПРИНЦЕССА НИ ЗА ЧТО НЕ ХОЧЕТ ИДТИ С ВАМИ. ПОХОЖЕ, ОНА ТАК И ОСТАНЕТСЯ В ЭТОМ ЗАМКЕ, А ВЫ КУПИТЕ 30 КОШЕК И УМРЕТЕ В ОДИНОЧЕСТВЕ. ",
            "\n")
    else:
        print(
            "И ОНА СКАЗАЛА ДА! ВЫ БЕРЕТЕ ЕЁ НА РУКИ И КРАСИВО УДАЛЯЕТЕСЬ В ЗАКАТ. ВЫ БУДЕТЕ ВМЕСТЕ, ПОКА НЕ РАЗЛУЧИТ ВАС СМЕРТЬ. НУ, ИЛИ РАЗВОД. ",
            "\n")

print(" К О Н Е Ц")

time.sleep(8)
os.system("cls")
