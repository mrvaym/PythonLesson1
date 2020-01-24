
from Lesson4 import randname

def test_1_randname():
    int_num = 100
    str = 'Абрам,Аваз,Август,Авдей,Автандил,Адам,Адис,Адольф,Адриан,Азарий,Аким,Алан,Александр,Алексей,Альберт,Альфред,Амадей,Амадеус,Амаяк,Анатолий'
    name_list = str.split(',')
    temp_list = []
    for i in range(int_num):
        rand_name_list = randname(int_num, name_list)
        temp_list.append(rand_name_list)
    assert temp_list!=[]
    assert len(temp_list)==int_num

def test_2_randname():
    int_num=100
    str = 'Абрам,Аваз,Август,Авдей,Автандил,Адам,Адис,Адольф,Адриан,Азарий,Аким,Алан,Александр,Алексей,Альберт,Альфред,Амадей,Амадеус,Амаяк,Анатолий'
    name_list = str.split(',')
    temp_list = []
    for i in range(int_num):
        rand_name_list = randname(int_num, name_list)
        temp_list.append(rand_name_list)
    for j in range(0, len(temp_list) - 1):
        x = temp_list[j]
        for k in range(j + 1, len(temp_list)):
            y = temp_list[k]
            assert x!=y # если функция выводит разные списки имён, то всё хорошо
