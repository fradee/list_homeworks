import random
text_dic = {'main': '''|________________________________________________________________________________
\nВаріанти для продовження:
    --- 1) відразу відгадати
    --- 2) взяти підказку
    --- 3) задати нижню межу
    --- 4) задати верхню межу
    --- 0) зупинити ігру''',
           'end': 'Ігру завершено і загадане число рівне {0}',
           'win': 'Ви відгадали число!',
           'wrong_number': 'Вказане вами число не збіграється з загаданим числом',
           'init_promt': "|  Загадано число, яке складається з {2} і знаходиться між {0} і {1}",
           'answer': 'Введіть загадане число або # для попереднього кроку: ',
           'get_min_range': 'Задайте нижню межу або # для попереднього кроку: ',
           'set_min_range': 'Задано нову нижню межу рівну: {0}',
           'set_min_range_error': 'Не можливо задати нову нижню межу рівну: {0}; пробуйте менше число.',
           'get_max_range': 'Задайте верхню межу або # для попереднього кроку: ',
           'set_max_range': 'Задано нову верхню межу рівну: {0}',
           'set_max_range_error': 'Не можливо задати нову верхню межу рівну: {0}; пробуйте більше число.',
           'set_range_win': 'Випадково натрапили на загадане число: {0}; Ви виграли! \n Випадковостей не буває :) ',
           'choice_dif': 'Виберіть скрадність ігри ',
           }
game_dificult_choice = int(0) 
game_dificult = [('Легко'),('Важко'),('Дуже Важко')]
while game_dificult_choice == 0:
    print(text_dic['choice_dif'])
    dz = 0
    for (key) in game_dificult:
        print('    --- {0}) {1}'.format(str(dz+1),key))
        dz +=1
    temp_choice = input(':  ')
    if temp_choice.isdigit() and int(temp_choice) >= 1 and int(temp_choice) <= 3:
        game_dificult_choice = int(temp_choice)
    else:
        continue
min_num_range = 1
if game_dificult_choice == 1:
    max_num_range = 99
elif game_dificult_choice == 2:
    max_num_range = 999
elif game_dificult_choice == 3:
    max_num_range = 9999
game_inProgress = True
magical_digit = 0
while not magical_digit >= min_num_range+2 or not magical_digit <= max_num_range-2:
    magical_digit = random.randint(min_num_range,max_num_range)
range_min = random.randint(min_num_range, magical_digit-1)
range_max = random.randint(magical_digit+1, max_num_range,)
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
gammer_answer = 9999
temporary_min_range = False
temporary_max_range = False
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
        if min_num_range < magical_digit-2:
            range_min = random.randint(min_num_range,magical_digit-1)
        if max_num_range > magical_digit+2:
            range_max = random.randint(magical_digit+1,max_num_range)
        min_num_range = range_min
        max_num_range = range_max
        gammer_answer = 9999
        continue
    elif gammer_answer == 3:
        if not temporary_min_range:
            temporary_min_range = input(text_dic['get_min_range'])
        
        if not temporary_min_range.isdigit():
            if temporary_min_range == '#':
                gammer_answer = 9999
                temporary_min_range = False
                continue
            else:
                temporary_min_range = False
                continue
        else:
            if int(temporary_min_range) == magical_digit:
                print(text_dic['set_range_win'].format(temporary_min_range))
                gammer_answer = 9999
                game_inProgress = False
                temporary_min_range = False
                continue
            elif int(temporary_min_range) < magical_digit:
                range_min = min_num_range = int(temporary_min_range)
                print(text_dic['set_min_range'].format(temporary_min_range))
                temporary_min_range = False
                gammer_answer = 9999
                continue
            elif int(temporary_min_range) > magical_digit:
                print(text_dic['set_min_range_error'].format(temporary_min_range))
                temporary_min_range = False
                continue
    elif gammer_answer == 4:
        if not temporary_max_range:
            temporary_max_range = input(text_dic['get_max_range'])
        
        if not temporary_max_range.isdigit():
            if temporary_max_range == '#':
                gammer_answer = 9999
                temporary_max_range = False
                continue
            else:
                temporary_max_range = False
                continue
        else:
            if int(temporary_max_range) == magical_digit:
                print(text_dic['set_range_win'].format(temporary_max_range))
                gammer_answer = 9999
                game_inProgress = False
                temporary_max_range = False
                continue
            elif int(temporary_max_range) > magical_digit:
                range_max = max_num_range = int(temporary_max_range)
                print(text_dic['set_max_range'].format(temporary_max_range))
                temporary_max_range = False
                gammer_answer = 9999
                continue
            elif int(temporary_max_range) < magical_digit:
                print(text_dic['set_max_range_error'].format(temporary_max_range))
                temporary_max_range = False
                continue
    print(' ________________________________________________________________________________')
    print('|  Складність: ' + game_dificult[game_dificult_choice-1] + " " + str(magical_digit))
    print(text_dic['init_promt'].format(range_min, range_max, num_numbers))
    print(text_dic['main'])
    gammer_answer = input(': ')
    if gammer_answer.isdigit():
        gammer_answer = int(gammer_answer)
        continue
    else:
        gammer_answer = 9999
