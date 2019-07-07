Coffee = 380
card = Coffee -10

#2か月間　計12杯のコーヒーを買い三か月目に入るところで
#会員証を買い,10円の割日で飲むことができるようになったとする
#Q 何杯飲めば元が取れるか?
#特になるのは何杯目から?

#元を計算する
moto = Coffee * 12
time = 0
print(moto)
while moto > 0:

    moto+=card-Coffee
    time+=1
print(time)
one_month = 8.5
time=time / one_month
print(time)
one_year = 12
time = time / one_year
print(time)
