buhlo = {'viskar': 0, 'vodochka': 0, 'roman': 0}

print("Сколько вас?")
per = float(input())

print("Какой у вас бюджет?")
money = float(input())
a = None

while a != 'vse':

    print("введите наименование алкоголя" + '\n' + "v - виски" + '\n' + "l - водочка" + '\n' + "r - ром" + '\n'+"vse - если больше ничего не надо")
    a = input()

    if a == 'v':
        print("введите объем вискаря")
        b = input()
        b = b.replace(',', '.')
        b = float(b)
        print("введите цену вискаря")
        val = input()
        val = val.replace(',', '.')
        val = float(val)
        print("сколько бутылок?")
        k = int(input())
        buhlo['viskar'] += b*k
        money -= val * k
        print("Дороговато, конечно... Советую взять водочки! У вас остается еще ", money)

    if a == 'l':
        print("введите объем водочки")
        b = input()
        b = b.replace(',', '.')
        b = float(b)
        print("введите цену водочки")
        val = input()
        val = val.replace(',', '.')
        val = float(val)
        print("сколько бутылок?")
        k = int(input())
        buhlo['vodochka'] += b*k
        money -= val * k
        print("Отличный выбор! У вас остается еще ", money)

    if a == 'r':
        print("введите объем, Рома")
        b = input()
        b = b.replace(',', '.')
        b = float(b)
        print("введите цену, Рома")
        val = input()
        val = val.replace(',', '.')
        val = float(val)
        print("сколько бутылок?")
        k = int(input())
        buhlo['roman'] += b*k
        money -= val * k
        print("Дороговато, конечно... Советую взять водочки! У вас остается еще ", money)

print(buhlo)
if buhlo['vodochka'] == 0:
    print("а как без водочки? :(")
else:
    print("водочки маловато")
if money < 0:
    print("на такой закуп не хватает", money)
else:
    print("хватает и остается еще", money)
print("по моим расчетам у вас ", (buhlo['vodochka'] + buhlo['roman'] + buhlo['viskar']) / per, " литра на человека")
