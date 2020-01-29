import datetime, json, csv, timeit
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

'''DOC'''
start_time = datetime.datetime.now()

with open('car_data') as f:
    temp_data = f.readlines()
    car_brand = temp_data[0].strip()
    car_model = temp_data[1].strip()
    car_fuel = temp_data[2].strip()
    car_price = temp_data[3].strip()


def get_context(car_brand, car_model, car_fuel, car_price):  # возвращает словарь аргуменов
    return {
        'brand': car_brand,
        'model': car_model,
        'fuel': car_fuel,
        'price': car_price
    }


def from_template(car_brand, car_model, car_fuel, car_price, template, photo):
    template = DocxTemplate(template)
    context = get_context(car_brand, car_model, car_fuel, car_price)  # gets the context used to render the document

    img_size = Cm(15)  # sets the size of the image
    acc = InlineImage(template, photo, img_size)
    context['photo'] = acc

    template.render(context)

    global start_time
    finish_time = datetime.datetime.now()
    report_time = finish_time - start_time

    template.save(f'{car_brand} _{report_time.microseconds}_report.docx')
    print('doc', start_time, finish_time, report_time)


def generate_report(car_brand, car_model, car_fuel, car_price, photo):
    template = 'template.docx'

    document = from_template(car_brand, car_model, car_fuel, car_price, template, photo)


generate_report(car_brand, car_model, car_fuel, car_price, 'subaru-forester.jpg')

'''JSON'''
start_time = datetime.datetime.now()
with open('car_data_to_json.json', 'w') as f:
    context = get_context(car_brand, car_model, car_fuel, car_price)
    json.dump(context, f, indent=4)
    finish_time = datetime.datetime.now()
    report_time = (finish_time - start_time).microseconds
    time_row = {'Время, затраченное на генерацию отчета:': str(report_time)}
    json.dump(time_row, f, ensure_ascii=False)
    print('json', start_time, finish_time, report_time)

'''CSV'''

csv_code='''   
import csv 
with open('car_data') as f:
    temp_data = f.readlines()
    car_brand = temp_data[0].strip()
    car_model = temp_data[1].strip()
    car_fuel = temp_data[2].strip()
    car_price = temp_data[3].strip()
    
with open('car_data_to_csv.csv', 'w') as f:
    fields = ['brand', 'model', 'fuel', 'price']
    car_data=[car_brand, car_model, car_fuel, car_price]
    write_csv = csv.writer(f, delimiter=';')
    write_csv.writerow(fields)
    write_csv.writerow(car_data)
'''

report_time=timeit.timeit(csv_code,number=1) # измерение времени на генерацию отчёта в CSV
with open('car_data_to_csv.csv', 'a') as f:
    time_row = ['Время, затраченное на генерацию отчета:', str(report_time)]
    write_csv = csv.writer(f, delimiter=' ')
    write_csv.writerow(time_row)
print('csv',  report_time)
