# coding:utf-8
import csv
import os

#元ファイル読み込み
r = open('INPUT/AUDJPY_20150501.csv', 'rb')

reader = csv.reader(r)
header = next(reader)

#5分足書き込み
x = open('OUTPUT/out-5hun.csv', 'wb')
writer = csv.writer(x, lineterminator='\n')

time = 0
start = 0
max = 0
min = 0
end = 0
cnt = 1

for row in reader:
    
    #5セットのうち1行目の時
    if cnt % 5 == 1:
        
        time = row[0]  #1行目の時間を記録
        start = row[1] #1行目の始値を記録
        max = row[2]
        min = row[3]
        end = 0
    
    #最大値
    if row[2] > max:
        max = row[2]
    
    #最小値
    if row[3] < min:
        min = row[3]

    #5セットのうち5行目の時、出力用文字列作成
    if cnt % 5 == 0:
        end = row[4] #5行目の終値を記録
        
        row1gyou = "" #1行分の変数
        row1gyou = str(time) + "," + str(start) + "," + str(max) + "," + str(min) + "," + str(end)
        
        #リスト形式に変換
        a = []
        a.append(row1gyou)
        
        writer.writerow(a)
        
    cnt = cnt + 1

#ファイルクローズ    
r.close()
x.close()


