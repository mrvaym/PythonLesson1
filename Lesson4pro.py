f = open('log')

last_record = [0, 0, 0, 0, 0, 0]
rec = [0, 0, 0, 0, 0, 0]

def func(rec, x=0, y=0):
    a = last_record[x]
    b = rec[y]
    if a < b:
        return rec
    elif a==b:
        return func(rec, x + 1, y + 1)
    else:
        return last_record

for log_line in f.readlines():
    rec[0] = int(log_line[0:4]) # year
    rec[1] = int(log_line[5:7]) # month
    rec[2] = int(log_line[8:10]) # date
    rec[3] = int(log_line[11:13]) # hours
    rec[4] = int(log_line[14:16]) # minutes
    rec[5] = int(log_line[17:19]) # seconds
    last_record = list(func(rec))

print(f'Последняя запись:',last_record[3],':',last_record[4],':',last_record[5],'  ',last_record[2],'.',last_record[1],'.',last_record[0])
