def get_evaluation(prompt):
    while True:
        try:
            detail = float(input(prompt + "细节评分: "))
            size = float(input(prompt + "规模评分: "))
            overall_planning = float(input(prompt + "整体规划评分: "))

            if not (0 <= detail <= 10):
                raise ValueError("细节评分必须在0到10之间")
            if not (0 <= size <= 3):
                raise ValueError("规模评分必须在0到3之间")
            if not (0 <= overall_planning <= 5):
                raise ValueError("整体规划评分必须在0到5之间")

            return detail, size, overall_planning
        except ValueError as e:
            print("输入有误:", e)
def scoring(prompt):
    while True:
        try:
            score = float(input(prompt + "卷面得分: "))
            projects = int(input(prompt + "团队项目数: "))
            Number = int(input(prompt + "个人作品数: "))

            if not (0 <= score <= 10):
                raise ValueError("卷面得分必须在0到10之间")
            if not (0 <= projects <= 100):
                raise ValueError("卷面得分必须在0到10之间")
            if not (0 <= Number <= 100):
                raise ValueError("卷面得分必须在0到10之间")
            
            return score,Number,projects
        except ValueError as e:
            print("输入有误: ", e)

detail_1, size_1, overall_planning_1 = get_evaluation("[一号评分员] ")
detail_2, size_2, overall_planning_2 = get_evaluation("[二号评分员] ")
rating_1 = (detail_1 / size_1 / 3 + overall_planning_1 / 5) * 33.33
rating_2 = (detail_2 / size_2 / 3 + overall_planning_2 / 5) * 33.33
average = (rating_1 + rating_2) / 2

score,projects,Number = scoring("")
pretrial = (score*max(1,(projects+Number)/2+1))/8
Final = average * max(1,pretrial)

if Final >= 70 :
    print("通过")
else:
    print("未通过")   

print("[平均分]: "+str(average))
print("[预审分数]: "+str(pretrial))
print("[终审分数]: "+str(Final))