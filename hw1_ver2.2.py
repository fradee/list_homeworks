print('Initial list:')
lst = [1, [2, 3], 4, [[6, 7]],[[[[8,[9000]]]]]]
print(lst)
#string = ''.join(str(elem) for elem in lst)
string = str(lst)
string = string.replace('[','').replace(']','').replace(' ','')
lst = list(string.split(','))
print('Final list:')
lst = [int(x) for x in lst]
print(lst)