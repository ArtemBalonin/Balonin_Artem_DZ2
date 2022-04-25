# Дан список
def get_sign(x):
    if x[0] in '+-':
        return x[0]
given = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать - обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
# и кавычку после элемента списка, являющегося числом) и дополнить нулем до двух целочисленных разрядов
i = 0
while i < len(given):
    sign = get_sign(given[i])
    if given[i].isdigit() or (sign and given[i][1:].isdigit()):
        if sign:
            given[i] = sign = given[i][1:].zfill(2)
        else:
            given[i] = given[i].zfill(2)
        given.insert(i, '"')
        given.insert(i+2, '"')
        i += 2
    i += 1
print(given)
print(" ".join(given))