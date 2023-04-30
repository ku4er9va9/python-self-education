def interval_check(value: int) -> str:
    if 0 <= value <= 100:
        result = 'Число попало в промежуток от 0-100'
    elif 200 <= value <= 300:
        result = 'Число попало в промежуток от 200-300'
    else:
        result = 'Не попало ни в один из промежутков'
    return result


try:
    with open("input.txt", "r") as file:
        contents = file.readlines()
        str1 = contents[0].strip()
        value = int(contents[1].strip())
        result = interval_check(value)
        print('Задача 1.1')
        print(result+'\n')

    with open("output.txt", "w") as file:
        file.write(f"{str1}\n{result}\n")

except FileNotFoundError:
    print("Input file not found!")
    exit()

except IndexError:
    print("Input file is empty or doesn't contain two lines!")
    exit()

except ValueError:
    print("Invalid input value!")
    exit()

except Exception as e:
    print("Error:", e)
    exit()



######################################

def calculate_time(str4: str) -> str:
    t = (100 - int(str4)) * 2
    return f"{t} минут"

with open("input.txt", "r") as file:
    contents = file.readlines()
    str3 = contents[2]
    str4 = contents[3]
    print(str3, end="")
    print(str4)

xx = calculate_time(str4)

with open("output.txt", "a") as file:
    file.write(f"{str3}{str4}{xx}\n")

print('')

########################################
with open("input.txt", "r") as file:
    contents = file.readlines()
    str5 = contents[4]
    str6 = int(contents[5])

print(str5, end="")

with open('output.txt', 'a') as f:
    f.write('\n' + str5)
    for i in range(1, str6+1):
        line = f"{i}: 000\n"
        f.write(line)
        print(line, end='')



#######################################

print()

with open("input.txt", "r") as file:
    contents = file.readlines()
    str7 = contents[6]
    str8 = contents[7]
    print(str7, end="")
    print(str8)

height = int(str8)

with open('output.txt', 'a') as f:
    f.write('\n' + str7)
    for i in range(1, height + 1):
        line = "*" * i
        print(line)
        f.write(line)
    f.write('\n')

#############################################

with open("input.txt", "r") as file:
    contents = file.readlines()
    str9 = contents[8]
    A, B, C, M, K = map(int, contents[9:14])
    print(str9, A, B, C, M, K)


if (A <= M and B <= K) or (B <= M and A <= K) or (A <= M and C <= K) or (C <= M and A <= K) or (B <= M and C <= K) or (C <= M and B <= K):
    y = "Коробка войдет в дверь"
else:
    y = "Коробка не войдет в дверь"
print(y)


with open("output.txt", "a") as file:
    file.write(f"{str9}{y}\n")


##################################

print("       ")

with open("input.txt", "r") as file:
    contents = file.readlines()
    str15 = contents[14]
    h = int(contents[15])

triangle = '\n'.join([' ' * (h - i) + '*' * (2 * i - 1) for i in range(1, h + 1)])

# Запись треугольника в файл
with open('output.txt', 'a') as f:
    f.write('\n' + str15 + '\n' + triangle)

print(str15)
print(triangle)


################################
# импортируем модуль itertools для использования функции takewhile
import itertools

# читаем данные из файла input.txt
with open("input.txt", "r") as input_file:
    input_data = input_file.readlines()
    output_label = input_data[16].strip() # метка для результата
    n = int(input_data[17].strip()) # верхняя граница для поиска квадратов

# генерируем квадраты чисел до корня из n
squares = map(str, itertools.takewhile(lambda x: x < n, (i**2 for i in itertools.count(1))))

# соединяем квадраты в одну строку, разделяя их символом переноса строки
output_data = "\n".join(squares)

# записываем результат в файл output.txt и выводим его на экран
with open("output.txt", "a") as output_file:
    output_file.write(output_label + "\n" + output_data + "\n")
print(output_label + "\n" + output_data)


##########################

def can_buy_exactly_k_scoops(k):
    # Find the sum of subsets among numbers 3 and 5
    dp = [False] * (k+1)
    dp[0] = True
    for x in [3, 5]:
        for i in range(k, x-1, -1):
            dp[i] |= dp[i-x]
    # Return the result for k
    return dp[k]

# Read input from file
with open("input.txt", "r") as file:
    contents = file.readlines()
    question = contents[18].strip()
    k = int(contents[19].strip())

# Check if it's possible to buy exactly k scoops
can_buy_k_scoops = can_buy_exactly_k_scoops(k)
result = "да" if can_buy_k_scoops else "нет"

# Format output
output = f"Можно ли купить ровно {k} шариков мороженого? {result}"
print(question)
print(k)

# Write output to file
with open("output.txt", "a") as file:
    file.write(f"\n{question}\n")
    file.write(f"{output}\n")

print(output)

##################

def calculate_years_to_reach_amount(P, r, Z):
    A = P
    years = 0
    while A < Z:
        years += 1
        A *= (1 + r / 100)
    if years == 0:
        return "Сумма вклада уже превышает или равна заданной сумме"
    else:
        return f"Сумма вклада превысит {Z} тыс. грн через {years} лет"

with open("input.txt", "r") as file:
    contents = file.readlines()
    try:
        str21 = contents[20]
        str22 = contents[21]
        str23 = contents[22]
        str24 = contents[23]
        P = int(str22)
        r = int(str23)
        Z = int(str24)
        print('\n' + str21)
        print(f"Сумма вклада: {P} тыс. грн")
        print(f"Процентная ставка: {r}%")
        print(f"Целевая сумма: {Z} тыс. грн")
        result = calculate_years_to_reach_amount(P, r, Z)
        with open("output.txt", "a") as file:
            file.write('\n' + str21)
            file.write(result)
            file.write('\n')
        print(result)
    except (ValueError, IndexError):
        print("Ошибка: некорректный формат входных данных")

file.close()

#################

def digit_sum(n):
    return sum(map(int, str(n)))

with open("input.txt", "r") as file:
    contents = file.readlines()
    str25 = contents[24]
    str26 = contents[25]
    NN = int(str26)
    print('\n'+str25, end="")
    print(NN)

result = digit_sum(NN) # находим сумму цифр
output = f"Сумма цифр числа {NN}: {result}" # формируем строку с результатом
with open("output.txt", "a") as file: # открываем файл для записи результата
    file.write('\n')
    file.write('\n'+str25)
    file.write(output)
print(output) # выводим результат в консоль
