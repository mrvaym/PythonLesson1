#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
i=0
for i in range(1,6):
    print(i,0)
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
number_of_five = 0
i = 0
while i < 10:
    i += 1
    number = input('Введите цифру ' + str(i) + ':')
    if number == '5':
        number_of_five+= 1
print('Количество пятёрок:',number_of_five)
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
i=100
sum=0
while i:
    sum+=i
    i-=1
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
mult=1
i=0
for i in range(1,11):
    mult*=i
print("произведение чисел :",mult)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
num=int(input("Введите целое число:"))
if num==0:
    print(num)
#Количество цифр в числе
count=0
i=num
while i>0:
    count += 1
    i=i//10
#Вывод цифр числа по порядку в новой строчке
while num>0:
    count -= 1
    print(num//(10**count))
    num=num%(10**count)
'''
Задача 6
Найти сумму цифр числа.
'''
num=1238954
sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print(sum)


'''
Задача 7
Найти произведение цифр числа.
'''
num=1238954
mult=1
while num>0:
    mult=mult*(num%10)
    num=num//10
print(mult)
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
num=122201111
big=0
while num>0:
    if big>=num%10:
        num=num//10
    else:
        big=num%10
print(big)

'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number = 2134325137754
count5=0
while integer_number>0:
    if integer_number%10 == 5:
        count5+=1
    integer_number = integer_number//10
print(count5)