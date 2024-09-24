# 閏年かどうか判別する
year = 1900

if year % 400 == 0:
    print('閏年です')
elif year % 100 == 0:
    print('平年です')
elif year % 4 == 0:
    print('閏年です')
else:
    print('平年です')