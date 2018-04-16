import random
game_dificult = (('Easy'),('Hard'))
game_dificult_choice = int()
min_num_range = 1
max_num_range = 99999
magical_digit = random.randint(min_num_range,max_num_range)
#gamer_name = input('Ім\'я гравця: ')
gamer_answer = int()












range_min = int(random.triangular(min_num_range,magical_digit,220))
range_max = int(random.triangular(magical_digit,max_num_range,220))


print(magical_digit)
print(range_min)
print(range_max)