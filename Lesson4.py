import random
f = open('name.txt')
name_list= f.read().split()
print(f'В списке ',len(name_list),' имён')
int_num=int(input('Какое число случайных имён Вы хотите получить:'))

def randname(int_num,name_list):
    rand_name_list = []
    for i in range(int_num):
        num_name=name_list[random.randint(0,len(name_list)-1)]
        rand_name_list.append(num_name)
    return rand_name_list

def how_often(list_in):
    '''
    Поиск частого и редкого в списке
    :param list
        list_in: список
    :return: list,list
            often: самый частый
            rare: самый редкий
    '''
    max_of=0
    min_of = len(list_in)
    often=[]
    rare=[]
    temp_set=set(list_in) # убираем повторы
    for i in temp_set:
        name_count=list_in.count(i)
        if max_of < name_count:
            max_of = name_count
            often.clear()
            often.append(i)
        elif max_of == name_count: # если у нескольких элементов одинаковое количество повторений
            often.append(i)
        elif min_of==name_count: # если у нескольких элементов одинаковое количество повторений
            rare.append(i)
        elif min_of > name_count:
            min_of = name_count
            rare.clear()
            rare.append(i)
        else:
            continue
    return often,rare

def rare_letter(list_in):
    temp_list=list(map(lambda list_in: list_in[0],list_in)) # оставляем первую букву
    letter=how_often(temp_list)[1]
    return letter

rand_name_list=randname(int_num,name_list)
print(rand_name_list)
print(f'Самые частые имена в полученном списке',how_often(rand_name_list)[0])
print(f'Самые редкие буквы с которых начинаются имена в полученном списке',rare_letter(rand_name_list))