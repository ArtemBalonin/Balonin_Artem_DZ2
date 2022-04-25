
arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
       'директор аэлита']
answer = {}
for string in arr:
       name = string.split()[-1].capitalize()
       print(f'Привет, {name}!')