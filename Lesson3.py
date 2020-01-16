import pymorphy2
morph = pymorphy2.MorphAnalyzer()
# Читаем из файла
f = open('text.txt',encoding='utf-8')
text=f.read()
# Заменяем знаки препинания на ПРОБЕЛ
str=text
symbol_list=[' ','.',',','?','!','-','–','—',"'",'"','«','»',':',';','(',')','\n'] # Список знаков препинания
for a in range(len(symbol_list)):
    str=str.replace(symbol_list[a],' ')
print('Заменяем знаки препинания на ПРОБЕЛ')
print(str)
# Создаём List
text_list=str.split()
print('Создаём List')
print(text_list)
# Приводим к нижнему регистру
text_list=list(map(lambda x: x.lower(),text_list))
print('Приводим к нижнему регистру')
print(text_list)
# Получаем нормальную форму
text_list=list(map(lambda x: morph.parse(x)[0].normal_form,text_list))
print('Получаем нормальную форму')
print(text_list)
# Создание словаря СЛОВО:ВСТРЕЧАЕТСЯ
text_dict={a:text_list.count(a) for a in text_list}
print('Создание словаря СЛОВО:ВСТРЕЧАЕТСЯ')
print(text_dict)
# 5 наиболее встречающихся
sort_list=list(text_dict.items())
sort_list.sort(key=lambda i: i[1],reverse=True)
print('5 наиболее встречающихся')
print(sort_list[:5])
# Количество разных слов в тексте
text_set=set(text_list)
print('Количество разных слов в тексте')
print(len(text_set))
