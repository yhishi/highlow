# 1分足を5分足にまとめる。
#coding:utf-8連続ではない
import csv   #csvモジュールをインポートする
import os

header = ['date','O','H','L','C']

# 
r = open('', 'rb')
dataReader = csv.reader(r)
header = next(dataReader)

w = open('INPUT/','wb')
writer = csv.writer(w, lineterminator='\n')
writer.writerow(header)

w.close()

    