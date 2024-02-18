# 定义一个函数，用于获取评价数据，prompt是提示语
def get_evaluation(prompt):
    while True:
        try:
            # 获取细节评分
            detail = float(input(prompt + "细节评分: "))
            # 获取规模评分
            size = float(input(prompt + "规模评分: "))
            # 获取整体规划评分
            overall_planning = float(input(prompt + "整体规划评分: "))

            # 检查评分范围是否正确
            if not (0 <= detail <= 10) or not (0 <= size <= 3) or not (0 <= overall_planning <= 5):
                raise ValueError("评分范围错误")

            # 返回评价数据
            return detail, size, overall_planning
        except ValueError as e:
            # 如果输入有误，打印错误信息并重新获取输入
            print("输入有误:", e)

# 定义一个函数，用于获取评分数据，prompt是提示语
def scoring(prompt):
    while True:
        try:
            # 获取卷面得分
            score = float(input(prompt + "卷面得分: "))
            # 获取团队项目数
            projects = int(input(prompt + "团队项目数: "))
            # 获取个人作品数
            number = int(input(prompt + "个人作品数: "))
            # 获取人数
            toll = int(input(prompt + "人数: "))

            # 检查输入范围是否正确
            if not (0 <= score <= 10) or not (0 <= projects <= 100) or not (0 <= number <= 100) or not (0 <= toll <= 3):
                raise ValueError("输入范围错误")

            # 返回评分数据
            return score, number, projects, toll
        except ValueError as e:
            # 如果输入有误，打印错误信息并重新获取输入
            print("输入有误: ", e)

# 获取第一个评分员的评价数据
detail_1, size_1, overall_planning_1 = get_evaluation("[一号评分员] ")
# 获取第二个评分员的评价数据
detail_2, size_2, overall_planning_2 = get_evaluation("[二号评分员] ")

# 计算第一个评分员的综合评分
rating_1 = (detail_1 / 10 + size_1 / 3 + overall_planning_1 / 5) * 33.33
# 计算第二个评分员的综合评分
rating_2 = (detail_2 / 10 + size_2 / 3 + overall_planning_2 / 5) * 33.33
# 计算平均综合评分
average = (rating_1 + rating_2) / 2

# 获取评审的卷面得分、团队项目数、个人作品数和人数
score, projects, number, toll = scoring("")

# 计算预审分数
pretrial = (score * max(1, (projects + number) / 2 + 1)) / 8

# 如果人数大于1，计算终审分数
if toll > 1:
    rating_3 = average / (1.4 ** (toll - 1))
    final = min(rating_3 * max(1, pretrial), 100)  # 终审分数最大为100
else:
    final = min(average * max(1, pretrial), 100)  # 平均分最大为100

# 输出平均分、预审分数和终审分数
print("[平均分]: {:.2f}".format(min(average, 100)))
print("[预审分数]: {:.2f}".format(pretrial))
print("[终审分数]: {:.2f}".format(final))

# 根据终审分数判断是否通过
if toll <= 1:
    if final >= 70:
        print("通过")
    else:
        print("未通过")
