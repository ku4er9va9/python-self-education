def read_and_print_strings(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str1 = contents[0]
        str2 = contents[1]
        print(str1, end="")
        print(str2)
        return str1, str2


str1, str2 = read_and_print_strings("input.txt")


def check_number_range(str2):
    if 0 <= int(str2) <= 100:
        print('Число попало в промежуток от 0-100')
        x = 'Число попало в промежуток от 0-100'
    elif 200 <= int(str2) <= 300:
        print('Число попало в промежуток от 200-300')
        x = 'Число попало в промежуток от 200-300'
    else:
        print('Не попало ни в один из промежутков')
        x = 'Не попало ни в один из промежутков'
    return x


result = check_number_range(str2)
print(result)


def write_to_file(str1, x, filename="output.txt"):
    with open(filename, "w") as file:
        file.write(str1)
    with open(filename, "a") as file:
        file.write(str(x) + '\n')
    print(' ')


write_to_file(str1, result)

######################################

def read_and_print_strings_2(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str3 = contents[2]
        str4 = contents[3]
        print(str3, end="")
        print(str4)
        return str3, str4


str3, str4 = read_and_print_strings_2("input.txt")


def calculate_time_remaining(timeBoil):
    t = (100 - int(timeBoil)) * 2
    xx = str(t) + ' минут'
    return xx


time_remaining = calculate_time_remaining(str4)
print(time_remaining)


def write_output_to_file(str3, str4, xx, filename="output.txt"):
    with open(filename, "a") as file:
        file.write('\n' + str3)
        file.write(str4)
        file.write(xx + '\n')


write_output_to_file(str3, str4, time_remaining)


print('')
########################################

def read_and_print_strings_3(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str5 = contents[4]
        str6 = contents[5]
        print(str5, end="")
        print(str6)
        return str5, str6


str5, str6 = read_and_print_strings_3("input.txt")

def write_task_to_file(str5, str6, filename="output.txt"):
    with open(filename, 'a') as f:
        f.write('\n' + str5)
        for i in range(int(str6)):
            f.write(f"{i+1}: 000\n")
            print(f"{i+1}: 000")

write_task_to_file(str5, str6)


#######################################

print("        ")


def read_and_print_strings_4(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str7 = contents[6]
        str8 = contents[7]
        print(str7, end="")
        print(str8)
        return str7, str8


str7, str8 = read_and_print_strings_4("input.txt")

height = int(str8)


def write_triangle_to_file(str7, height, filename="output.txt"):
    with open(filename, 'a') as f:
        f.write('\n' + str7)
        for i in range(1, height + 1):
            line = "**" * i
            print(line)
            f.write(line + '\n')
        f.write('\n')


write_triangle_to_file(str7, height)
#############################################

print("    ")

def read_input_file_5(filename="input.txt"):
    with open(filename, "r") as file:
        contents = file.readlines()
        str9 = contents[8].strip()
        A = int(contents[9])
        B = int(contents[10])
        C = int(contents[11])
        M = int(contents[12])
        K = int(contents[13])

    return str9, A, B, C, M, K


str9, A, B, C, M, K = read_input_file_5()
print(str9)
print(A, B, C, M, K)


def check_fits_in_door(A, B, C, M, K):
    if A <= M and B <= K:
        y = "Коробка войдет в дверь"
    elif B <= M and A <= K:
        y = "Коробка войдет в дверь"
    elif A <= M and C <= K:
        y = "Коробка войдет в дверь"
    elif C <= M and A <= K:
        y = "Коробка войдет в дверь"
    elif B <= M and C <= K:
        y = "Коробка войдет в дверь"
    elif C <= M and B <= K:
        y = "Коробка войдет в дверь"
    else:
        y = "Коробка не войдет в дверь"

    print(y)
    return y


result_1 = check_fits_in_door(A, B, C, M, K)

def write_to_file(str9, y):
    with open("output.txt", "a") as file:
        file.write(str9)
        file.write('\n')
    with open("output.txt", "a") as file:
        file.write(str(y) + '\n')
    print(' ')


write_to_file(str9, result_1)

##################################


print("       ")

def read_and_print_strings_6(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str15 = contents[14]
        h = contents[7]
        return str15, h


str15, h = read_and_print_strings_6('input.txt')

height = int(h)


def create_triangle(height):
    triangle = ''
    for i in range(1, height + 1):
        triangle += ' ' * (height - i)  # добавление отступов слева
        triangle += '*' * (2 * i - 1)  # добавление символов "*"
        triangle += '\n'  # добавление переноса строки
    return triangle


triangle = create_triangle(height)

# Запись треугольника в файл


def write_triangle_to_file(str15, triangle):
    with open('output.txt', 'a') as f:
        f.write('\n'+str15)
        f.write(triangle)
    print(str15)
    print(triangle)

write_triangle_to_file(str15, triangle)



################################
print(" ")

def read_and_print_strings_7(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str17 = contents[16]
        str18 = contents[17]
        N = int(str18)
        print(str17, end="")
        print(N)
    return str17, N


str17, N = read_and_print_strings_7('input.txt')


def generate_squares_below_N(N):
    squares = [i**2 for i in range(1, int(N**0.5)+1)]
    result = [str(i) for i in squares if i < N]
    output = "\n".join(result)
    return output


output = generate_squares_below_N(25)
print(output)

def write_squares_to_file(str17, output):
    with open("output.txt", "a") as file:
        file.write('\n'+str17)
        file.write(output)
        file.write('\n')


write_squares_to_file(str17, output)


##########################


def read_and_print_strings_8(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str19 = contents[18]
        str20 = contents[19]
        k = int(str20)
        print('\n'+str19, end="")
        print(k)
        return str19, k


str19, k = read_and_print_strings_8('input.txt')

def can_buy_exactly_k_scoops(k):
    # ищем сумму подмножеств среди чисел 3 и 5
    dp = [False] * (k+1)
    dp[0] = True
    for x in [3, 5]:
        for i in range(k, x-1, -1):
            dp[i] |= dp[i-x]
    # возвращаем результат для k
    return dp[k]


result = "да" if can_buy_exactly_k_scoops(k) else "нет" # проверяем, можно ли купить ровно k шариков мороженого
output = f"Можно ли купить ровно {k} шариков мороженого? {result}" # формируем строку с результатом

def write_and_return_output(output, filename):
    with open(filename, "a") as file:
        file.write("\n" + str19)
        file.write(output)
    print(output)
    return output


write_and_return_output(output, 'input.txt')
print('')

##################

def read_input_values_9(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str21 = contents[20]
        str22 = contents[21]
        str23 = contents[22]
        str24 = contents[23]
        P = int(str22)
        r = int(str23)
        Z = int(str24)
        return str21, P, r, Z


str21, P, r, Z = read_input_values_9('input.txt')


def calculate_deposit(P, r, Z):
    A = P
    n = 0
    while A < Z:
        n += 1
        A *= (1 + r / 100)
    result = f"Сумма вклада превысит {Z} тыс. грн через {n} лет"
    return result


result = calculate_deposit(P, r, Z)
print(str21)
print(result)

# with open("output.txt", "a") as file:
#     file.write('\n')
#     file.write('\n'+str21)
#     file.write(result)


def write_result_to_file(result, output_file, info_string):
    with open(output_file, "a") as file:
        file.write('\n')
        file.write('\n' + info_string)
        file.write(result)


write_result_to_file(result,'output.txt', str21)

#################

def read_input_values_10(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
        str25 = contents[24]
        str26 = contents[25]
        NN = int(str26)
        return str25, NN


str25, NN = read_input_values_10('input.txt')
print('\n'+str25, end="")
print(NN)


def show_sum_of_digits(NN):
    digits = [int(d) for d in str(NN)]
    result = sum(digits)
    output = f"Сумма цифр числа {NN}: {result}"
    with open("output.txt", "a") as file:
        file.write('\n')
        file.write('\n'+str25)
        file.write(output)
    print(output)# выводим результат в консоль


show_sum_of_digits(NN)

