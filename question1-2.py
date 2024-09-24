# 全科目の平均点を求める
scores = {'数学': 82, '国語': 74, '英語': 60, 
          '理科': 92, '社会': 70}

scores_values = list(scores.values())
avg_score = sum(scores_values) / len(scores_values)
print(f'{avg_score}点')