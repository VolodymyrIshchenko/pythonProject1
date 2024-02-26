# var_dict = {k: v for k, v in ((1, 'a'), (2, 'b'), (3, 'c'))}
# print(var_dict)
#
#
# person = {}
# print(type(person))
# #dict = ([
# #(<key>, <value>),
# #(<key>, <value>),
# #])
# person['first_name'] = 'Volodymyr'
# person['last_name'] = 'Ishchenko'
# person['age'] = '20'
# person['city'] = 'Kyiv'
# person['occupation'] = ['Cars body repairer', 'cars repairer']
# person['interests'] = ['Cars', 'psychology', 'technics']
#
# print(person['occupation'][1])
# print(person['interests'][0])
#
# # Приклад словника з використанням dict comprehension та if-else
# numbers = [1, 2, 3, 4, 5]
# my_dict = {x: "парне" if x % 2 == 0 else "непарне" for x in numbers}
#
# # # Виведення результату
# # print(my_dict)
# #
# # asswords = (333, 4444, 55555, 4324124, 213122312)
# # print(type(passwords))
# #
# # dict_1 = {x: 'applicable' if len(str(x)) > 6 else 'not applicable' for x in passwords}
# # print(dict_1)

uy = 55
while uy != 0:
    uy -= 1
    if uy % 7 == 0:
        break
    print(uy, end=" ")

myL =[1, 2, 3]

sum = 0
for i in myL:
    sum += i
print(f'\nSum = {sum}')

myL1 = [1, 2, 3]
myL2 = [3, 4, 5]

for x in myL1:
    for y in myL2:
        sum += x*y

print(sum)

d1 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

replacements = {1: 'one', 4: 'four', 5: 'five'}
for i in list(d1):
    if i in replacements:
        d1[replacements[i]] = d1.pop(i)
print(replacements)

original_list = [True, False, None, True, None]

result_tuples = []

for index, value in enumerate(original_list):
    result_tuples.append((index, value))

print(result_tuples)

random_number = random_number.randint(1, 100)

user_number = 5

while user_number != random_number:
    if user_number > random_number:
        print("менше")
    else:
        print("більше")

    user_number = int(input("Введіть нове число: "))

print("Ви вгадали число", random_number)