with open("input.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)

if 0<= int(str2) and int(str2)<=100:
    print('Число попало в промежуток от 0-100')
    x = 'Число попало в промежуток от 0-100'
elif 200<= int(str2) and int(str2)<=300:
    print('Число попало в промежуток от 200-300')
    x = 'Число попало в промежуток от 200-300'
else:
    print('Не попало ни в один из промежутков')
    x = 'Не попало ни в один из промежутков'

with open("output.txt", "w") as file:
        file.write(str1)

with open("output.txt", "a") as file:
    file.write(str(x)+'\n')
print(' ')

######################################

with open("input.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()
    str3 = contents[2]
    str4 = contents[3]
    print(str3, end="")
    print(str4)

t = (100-int(str4))*2
print(str(t)+' минут')
xx = str(t)+' минут'


with open("output.txt", "a") as file:
    file.write('\n'+str3)
    file.write(str4)
    file.write(xx +'\n')


print('')
########################################
with open("input.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()
    str5 = contents[4]
    str6 = contents[5]
    print(str5, end="")
    print(str6)



with open('output.txt', 'a') as f:
    f.write('\n' + str5)
    for i in range(int(str6)):
        f.write(f"{i+1}: 000\n")
        print(f"{i + 1}: 000")


#######################################

print("        ")


with open("input.txt", "r", encoding='utf-8') as file:
    contents = file.readlines()
    str7 = contents[6]
    str8 = contents[7]
    print(str7, end="")
    print(str8)

height = int(str8)


with open('output.txt', 'a') as f:
    f.write('\n' + str7)
    for i in range(1, height + 1):
        line = "**" * i
        print(line)
        f.write(line + '\n')
    f.write('\n')

#############################################

print("    ")

with open("input.txt", "r") as file:
    contents = file.readlines()
    str9 = contents[8]
    A = contents[9]
    B = contents[10]
    C = contents[11]
    M = contents[12]
    K = contents[13]

    print(str9, end="")
    print(A, end="")
    print(B, end="")
    print(C, end="")
    print(M, end="")
    print(K)


if A <= M and B <= K:
    print("Коробка войдет в дверь")
    y = "Коробка войдет в дверь"
elif B <= M and A <= K:
    print("Коробка войдет в дверь")
    y = "Коробка войдет в дверь"
elif A <= M and C <= K:
    print("Коробка войдет в дверь")
    y = "Коробка войдет в дверь"
elif C <= M and A <= K:
    print("Коробка войдет в дверь")
    y = "Коробка войдет в дверь"
elif B <= M and C <= K:
    print("Коробка войдет в дверь")
    y = "Коробка войдет в дверь"
elif C <= M and B <= K:
    print("Коробка войдет в дверь")
    y = "Коробка войдет в дверь"
else:
    print("Коробка не войдет в дверь")
    y = "Коробка не войдет в дверь"

with open("output.txt", "a") as file:
    file.write(str9)

with open("output.txt", "a") as file:
    file.write(str(y) + '\n')
print(' ')



##################################

print("       ")

with open("input.txt", "r") as file:
    contents = file.readlines()
    str15 = contents[14]
    h = contents[15]

height = int(h)


triangle = ''
for i in range(1, height + 1):
    triangle += ' ' * (height - i)  # добавление отступов слева
    triangle += '*' * (2 * i - 1)  # добавление символов "*"
    triangle += '\n'  # добавление переноса строки

# Запись треугольника в файл
with open('output.txt', 'a') as f:
    f.write('\n'+str15)
    f.write(triangle)
    print(str15)
    print(triangle)


################################
print(" ")

with open("input.txt", "r") as file:
    contents = file.readlines()
    str17 = contents[16]
    str18 = contents[17]
    N = int(str18)
    print(str17, end="")
    print(N)


squares = [i**2 for i in range(1, int(N**0.5)+1)] # создаем последовательность квадратов чисел до корня из N
result = [str(i) for i in squares if i < N] # выбираем числа меньше N и преобразуем их в строки
output = "\n".join(result) # соединяем числа в одну строку, разделяя их символом переноса строки

with open("output.txt", "a") as file: # открываем файл для записи результата
    file.write('\n'+str17)
    file.write(output) # записываем результат в файл
    file.write('\n')
print(output) # выводим результат в консоль


##########################

def can_buy_exactly_k_scoops(k):
    # ищем сумму подмножеств среди чисел 3 и 5
    dp = [False] * (k+1)
    dp[0] = True
    for x in [3, 5]:
        for i in range(k, x-1, -1):
            dp[i] |= dp[i-x]
    # возвращаем результат для k
    return dp[k]

with open("input.txt", "r") as file:
    contents = file.readlines()
    str19 = contents[18]
    str20 = contents[19]
    k = int(str20)
    print('\n'+str19, end="")
    print(k)

result = "да" if can_buy_exactly_k_scoops(k) else "нет" # проверяем, можно ли купить ровно k шариков мороженого
output = f"Можно ли купить ровно {k} шариков мороженого? {result}" # формируем строку с результатом
with open("output.txt", "a") as file: # открываем файл для записи результата
    file.write('\n'+str19)
    file.write(output) # записываем результат в файл
print(output) # выводим результат в консоль

##################

with open("input.txt", "r") as file:
    contents = file.readlines()
    str21 = contents[20]
    str22 = contents[21]
    str23 = contents[22]
    str24 = contents[23]
    P = int(str22)
    r = int(str23)
    Z = int(str24)
    print('\n'+str21, end="")
    print(P)
    print(r)
    print(Z)

A = P
n = 0
while A < Z:
    n += 1
    A *= (1 + r / 100)

result = f"Сумма вклада превысит {Z} тыс. грн через {n} лет"
print(result)

with open("output.txt", "a") as file:
    file.write('\n')
    file.write('\n'+str21)
    file.write(result)

#################

with open("input.txt", "r") as file:
    contents = file.readlines()
    str25 = contents[24]
    str26 = contents[25]
    NN = int(str26)
    print('\n'+str25, end="")
    print(NN)


digits = [int(d) for d in str(NN)] # преобразуем число в список цифр
result = sum(digits) # находим сумму цифр
output = f"Сумма цифр числа {NN}: {result}" # формируем строку с результатом
with open("output.txt", "a") as file: # открываем файл для записи результата
    file.write('\n')
    file.write('\n'+str25)
    file.write(output)
print(output) # выводим результат в консоль
