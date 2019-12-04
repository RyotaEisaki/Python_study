# -*- coding:utf-8 -*-
"""

sum2.pyプログラム
和、二乗和を求めるプログラム
標準出浴から実数を読み取り、
和と二乗和を逐次出力します
数値以外の入力で終了します
使い方　c:\>python sum2.python
"""

#メイン実行部
#初期設定
sum=0.0 #和
sum2=0.0 #２乗和

#繰り返し処理
while True: #数値以外が入力されるまで繰り返す
    try:
        data=float(input("数値を入力:"))
    except ValueError:#入力終了
        break
    sum +=data #sumの計算
    sum2+=data*data #sum2の計算
    print("{:.15F} {:.15F}".format(sum, sum2))
#sum2.pyの終わり
