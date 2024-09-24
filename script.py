from my_module import Student

# 標準ライブラリの例
from datetime import datetime

student_1 = Student('斎藤そうま', 82, 74, 60, 92, 72)
s1_avg = student_1.average_score()
print(s1_avg)

t = datetime.today()
print(t)