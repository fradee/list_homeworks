import random
#game_dificult = (('Легко'),('Важко'),('Дуже Важко'))
#game_dificult_choice = int()
min_num_range = 1
max_num_range = 99
game_inProgress = True
magical_digit = random.randint(min_num_range,max_num_range)
range_min = random.randint(min_num_range,magical_digit)
range_max = random.randint(magical_digit,max_num_range)
min_num_range = range_min
max_num_range = range_max
if magical_digit < 100 and magical_digit >= 10:
    num_numbers = 'двох цифр'
elif magical_digit <=999 and magical_digit >=100:
    num_numbers = 'трьох цифр'
elif magical_digit <= 9999 and magical_digit >=1000:
    num_numbers = 'чотирьох цифр'
else:
    num_numbers = 'однієї цифри'
gammer_answer = 99

text_dic = {'main': '''Варіанти для продовження:
    --- 1) відгадати зразу
    --- 2) взяти підказку
    --- 3) задати нижню межу
    --- 4) задати верхню межу
    --- 0) зупинити ігру''',
           'end': 'Ігру завершено і загадане число рівне {0}',
           'win': 'Ви відгадали число!',
           'wrong_number': 'Вказане вами число не збіграється з загаданим числом',
           'init_promt': "Загадано число, яке складається з {2} і знаходиться між {0} і {1}",
           'answer': 'Введіть загадане число або # для попереднього кроку: '
           }

while game_inProgress:
    if gammer_answer == 0:
        print(text_dic['end'].format(magical_digit))
        game_inProgress = False
        break
    elif gammer_answer == 1:
        gammer_magical_digit = input(text_dic['answer'])
        if gammer_magical_digit.isdigit():
            if int(gammer_magical_digit) == magical_digit:
                print(text_dic['win'])
                break
            else:
                print(text_dic['wrong_number'])
                gammer_answer = 9999
                continue
        elif gammer_magical_digit == '#':
            gammer_answer = 9999
        else:
            continue
    elif gammer_answer == 2:
        if min_num_range < magical_digit-1:
            range_min = random.randint(min_num_range,magical_digit)
        if max_num_range > magical_digit+2:
            range_max = random.randint(magical_digit,max_num_range)
        min_num_range = range_min
        max_num_range = range_max
        gammer_answer = 9999
        continue
    print(magical_digit)
    print(text_dic['init_promt'].format(range_min, range_max, num_numbers))
    print(text_dic['main'])
    gammer_answer = input(': ')
    if gammer_answer.isdigit():
        gammer_answer = int(gammer_answer)
        continue
    else:
        gammer_answer = 9999
