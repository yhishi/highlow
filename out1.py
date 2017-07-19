# coding:utf-8
import csv
import os

#元ファイル読み込み
r = open('INPUT/AUDJPY_20150501.csv', 'rb')

reader = csv.reader(r)
header = next(reader)



#1分足書き込み
w = open('OUTPUT/out-1hun.csv', 'wb')
writer = csv.writer(w, lineterminator='\n')
writer.writerow(header)

for row in reader:

    if row[1] < row[4]:
        highrow = 'HIGHやで～'
    else:
        highrow = 'LOWやで～'
    
    #要素の最後に追加
    row.append(highrow)
    
    #ファイル書き込み
    writer.writerow(row)

    
r.close()
w.close()



