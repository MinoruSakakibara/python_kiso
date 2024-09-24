# Pythonルール
print('あいうえお')
print('かきくけこ')
print('さしすせそ')

# 変数
apple_price = 100
print(apple_price)

apple_price = 200
print(apple_price)

x = 10
y = 100
x = y
print(x)

# 型
apple_price = 100
a_type = type(apple_price)

name = '斎藤'
n_type = type(name)

weight = 54.5
w_type = type(weight)

print(a_type, n_type, w_type)

# 埋め込み文字列
price = 100
text = f'この商品は{price}円です'
print(text)

# リスト
student_names = ['斎藤', '小林', '佐々木', '田中']
a = student_names[0]
b = student_names[2]
c = student_names[-1]
d = student_names[-3]

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
y = x[1:3]

scores = [82, 74, 60, 92, 70]
avg_score = sum(scores) / len(scores)
print(avg_score)

# 辞書
prices = {'りんご': 100, 'いちご':150, 'バナナ':200}
result = prices['いちご']
print(result)

prices['みかん'] = 300
print(prices)

fruits = list(prices.keys())
print(fruits)

fruits_values = list(prices.values())
print(fruits_values)

# 集合、タプル
# 集合
x = {0, 1, 3, 6}
y = {0, 2, 5, 6}

z = x | y
print(z)

z = x - y
print(z)

z = x & y
print(z)

# タプル
tp = (1, 2, 4)
tpel = tp[1]
print(tpel)

# if文
prefecture = "ワシントン"

if prefecture == '東京':
    print('日本の首都です')
elif prefecture == 'ワシントン':
    print('アメリカの首都です')

number = 11

if number % 2 == 0:
    print('偶数です')
else:
    print('奇数です')

# for文
scores = [90, 30, 49]

for x in scores:
    print(x)
    
fruits = {'apple': 130, 'banana': 350, 'lemon': 100}

for name, price in fruits.items():
    print(f'{name}は{price}円です')
    
for x in range(5):
    print(x)
    
for x in range(1, 6):
    print(x)
    
numbers = [10, 21, 100, 18, 2]

for n in numbers:
    if n >= 100:
        break
    print(f'{n}: 繰り返し')
print('for文の外')

numbers = [10, 21, 32, 65]

for n in numbers:
    print(f'{n}: 前処理')
    if n % 2 == 0:
        continue
    print(f'{n}: 後処理')
    
names = ['斎藤', '佐藤', '鈴木']

for x in names:
    print(f'{x}さん')
    
scores = {'数学': 82, '国語': 74, '英語': 60,
          '理科': 92, '社会': 70}

for k, v in scores.items():
    print(f'{k}は{v}点です')

for i in range(1, 11):
    print(i)

# 関数
def print_hello():
    print('こんにちは')

print_hello()

def add_sub_numbers(a, b):
    c = a + b
    d = a - b
    return c, d

# 位置引数
added, subed = add_sub_numbers(10, 100)
print(added, subed)

# キーワード引数
added, subed = add_sub_numbers(b=10, a=100)
print(added, subed)

def is_leap_years(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = 2024
result = is_leap_years(year)
print(result)

# クラス
# テストの平均点を計算するアプリを考える
class Student:
    def __init__(self, name, math, japanese,
                 english, science, society):
        self.neme = name
        self.math = math
        self.japanese = japanese
        self.english = english
        self.science =science
        self.society = society
    
    def average_score(self):
        avg = (self.math + self.japanese + self.english
                + self.science + self.society) / 5
        return avg
    
student_1 = Student('斎藤そうま', 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(s1_avg)

student_2 = Student('田中かなで', 75, 78, 80, 85, 68)
s2_avg = student_2.average_score()
print(s2_avg)

# クラス変数を使ってみる
class SchoolReport:
    school_name = '榊原中学校'
    def __init__(self, student_name):
        self.student_name = student_name

print(SchoolReport.school_name)

sr_a = SchoolReport('田中 A')       
print(sr_a.school_name)

# モジュール
# script.py、my_module.py参照

# 継承
class JobClass:
    def __init__(self):
        print('JobClassのinit')
        self.hp = 100
        
class WizardClass(JobClass):
    def __init__(self):
        super().__init__()
        self.mp = 50
        
    def output_info(self):
        print(f'現在のHPは{self.hp}で、'
              f'MPは{self.hp}です。')

wizard = WizardClass()
wizard.output_info() 