# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
# 2) выводит список всех делителей числа;
# 3) выводит самый большой простой делитель числа.
# PRO:
# LIGHT +
# 4) функция выводит каноническое разложение числа (https://zaochnik.com/spravochnik/matematika/delimost/razlozhenie-chisel-na-prostye-mnozhiteli/) на простые множители;
# 5)функция выводит самый большой делитель (не обязательно простой) числа.

def min(list_a):
    ''' min значение в списке'''
    if list_a != []:
        y = list_a[0]
        for x in list_a:
            if x < y:
                y = x
            else:
                continue
        return y
    else:
        return []


def max(list_a):
    ''' max значение в списке'''
    if list_a != []:
        y = list_a[0]
        for x in list_a:
            if x > y:
                y = x
            else:
                continue
        return y
    else:
        return []


def devisor(a, b):
    ''' Является ли b делителем числа a без остатка'''
    if a % b == 0:
        return b
    else:
        return 0


def simple(a):
    '''проверка числа на простоту'''
    list_a = devisors(a)
    if a > 1:
        list_a.remove(a)
        list_a.remove(1)
    if list_a == []:
        return 1
    else:
        return 0


def devisors(a):
    '''выводит список всех делителей числа'''
    devisors_list = []
    for b in range(1, int(a)+ 1):
        if devisor(a, b):
            devisors_list.append(b)
        else:
            continue
    return devisors_list


def simple_devisor(a):
    '''Выводит список простых делителей числа'''
    list_b = devisors(a)
    simple_devisor_list = []
    for i in list_b:
        if simple(i):
            simple_devisor_list.append(i)
    return simple_devisor_list


def prime_factorization(a):
    '''Каноническое разложение числа на простые множители'''
    prime_factorization_list = []
    while a != 1:
        b = min(simple_devisor(a))
        a = a // b
        prime_factorization_list.append(b)
        if simple(a):
            prime_factorization_list.append(a)
            return prime_factorization_list
        else:
            continue
    return prime_factorization_list


def devisor_not_num(a):
    ''' Делители числа большего 1, не равные самому числу'''
    devisor_list = devisors(a)
    if a != 1:  # Если число равно 1 вернёт единственный делитель:1
        devisor_list.remove(a)
    return devisor_list


def greatest_common_divisor(list_n):
    '''Наибольший общий делитель чисел'''
    list_n=list(map(lambda list_n: int(list_n),list_n))
    common_divisor_list = []
    list_a = devisors(list_n[0])
    for i in range(1, len(list_n)):
        list_b = devisors(list_n[i])
        for x in list_a:
            for y in list_b:
                if x == y:
                    common_divisor_list.append(y)
        list_a = list(common_divisor_list)
        common_divisor_list.clear()
    return max(list_a)

'''Test'''
if __name__ == '__main__':
    x = [48, 3, 4, 577, 18, 578, 2, 206, 27, 378, 2310, 289, 1]
    for i in x:
        print('Число', i)
        print('Список делителей', devisors(i))
        if simple(i):
            print('Простое')
        else:
            print('Не простое')
        print('Список простых делителей', simple_devisor(i))
        print('Наибольший простой делитель', max(simple_devisor(i)))
        print('Наименьший простой делитель', min(simple_devisor(i)))
        print('Разложенние на простые множители', prime_factorization(i))
        print('Самый большой делитель не равный числу', max(devisor_not_num(i)))
        print('_________________________________________')
    x = [[792, 1188], [18, 12, 66, 6000, 3102], [12, 24, 30, 48]]
    for i in x:
        print(f'Наибольший общий делитель для чисел', i, 'равен', greatest_common_divisor(i))
