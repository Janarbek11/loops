
# Допустим у нас есть список языков программирования. lang1 = 'Rust'
#  languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#  Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'.
#  Если этого языка нет в списке, ничего не нужно выводить
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for i in languages:
    if i == lang1:
        print('this languages is in list')
    else:
        pass

# . Будем работать с тем же списком: languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# С помощью цикла нужно “перебрать” все языки в списке, и когда код доходит до “php”, цикл должен быть прерван.
for i in languages:
    if i == "php":
        print("Succes!")
        break

# Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз.
counter = 0
seven = 7
res = 7
while counter != 5:
    res *= seven
    print(res)
    counter += 1


# Напишите код, который выведет на экран список языков с нумерацией.
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
shet = 0
num = 0
while shet != len(languages):
    print(num, languages[shet])
    shet += 1
    num += 1

# Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
# Усиление:
# Получите такой же результат но с ОДНИМ циклом

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# d = x[1:10]
for n in x:
    print(n)

