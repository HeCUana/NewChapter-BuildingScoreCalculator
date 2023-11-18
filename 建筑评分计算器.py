import tkinter as tk
from tkinter import ttk
import math

def 计算预审分(卷面得分, 团队项目数, 个人作品数):
    预审分 = 卷面得分 * max(1, (团队项目数 + 个人作品数) / 2 + 1) / 8
    return max(1, 预审分)  # 确保预审分至少为1

def 计算终审分(审核建筑评分, 预审分):
    return 审核建筑评分 * max(1, 预审分)

def 计算组队得分(审核建筑评分, 人数):
    return 审核建筑评分 / 1.4 ** (人数 - 1)

def 计算平均分(分数1, 分数2):
    return (分数1 + 分数2) / 2

def 提交评分():
    细节分1 = float(细节分1输入框.get()) / 10
    规模分1 = float(规模分1输入框.get()) / 3
    规划分1 = float(规划分1输入框.get()) / 5

    细节分2 = float(细节分2输入框.get()) / 10
    规模分2 = float(规模分2输入框.get()) / 3
    规划分2 = float(规划分2输入框.get()) / 5

    团队项目数 = int(团队项目数输入框.get())
    个人作品数 = int(个人作品数输入框.get())
    卷面得分 = float(卷面得分输入框.get())

    是否组队 = 团队情况选择框.get()
    团队人数 = 1
    if 是否组队 == '是':
        团队人数 = int(团队人数输入框.get())

    # 限制输入范围
    if not (0 <= 细节分1 <= 1 and 0 <= 规模分1 <= 1 and 0 <= 规划分1 <= 1):
        结果标签.config(text="Error: 评分范围错误")
        return

    if not (0 <= 细节分2 <= 1 and 0 <= 规模分2 <= 1 and 0 <= 规划分2 <= 1):
        结果标签.config(text="Error: 评分范围错误")
        return

    if not (0 <= 卷面得分 <= 10):
        结果标签.config(text="Error: 卷面得分范围错误")
        return

    if not (0 <= 团队项目数 and 0 <= 个人作品数):
        结果标签.config(text="Error: 参与团队项目数和个人作品数必须大于等于0")
        return

    建筑得分1 = (细节分1 + 规模分1 + 规划分1) * 33.33
    建筑得分2 = (细节分2 + 规模分2 + 规划分2) * 33.33

    预审分1 = 计算预审分(卷面得分, 团队项目数, 个人作品数)
    预审分2 = 计算预审分(卷面得分, 团队项目数, 个人作品数)

    终审分1 = 计算终审分(建筑得分1, 预审分1)
    终审分2 = 计算终审分(建筑得分2, 预审分2)

    if 团队人数 > 1:
        终审分1 = 计算组队得分(终审分1, 团队人数)
        终审分2 = 计算组队得分(终审分2, 团队人数)

    平均分 = 计算平均分(终审分1, 终审分2)

    结果标签.config(text=f"平均分：{平均分:.2f}")

    # 预审分数
    预审分数标签.config(text=f"预审分数：{预审分1:.2f}, {预审分2:.2f}")

    # 终审分数
    终审分数标签.config(text=f"终审分数：{终审分1:.2f}, {终审分2:.2f}")

    # 是否通过
    通过状态 = "通过" if 平均分 >= 70 else "未通过"
    是否通过标签.config(text=f"是否通过：{通过状态}")

# 创建主窗口
root = tk.Tk()
root.title("建筑评分系统")

# 主题颜色
主题颜色 = "#3498db"

# 字体设置
标题字体 = ('Helvetica', 16, 'bold')
正文字体 = ('Helvetica', 12)

# 添加评分员1的输入框和标签
frame1 = ttk.LabelFrame(root, text="评分员1", labelanchor='n', padding=(10, 5))
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

tk.Label(frame1, text="细节表现力：", font=正文字体).grid(row=1, column=0, sticky="w", pady=5)
细节分1输入框 = ttk.Entry(frame1)
细节分1输入框.grid(row=1, column=1)

tk.Label(frame1, text="建筑规模：", font=正文字体).grid(row=2, column=0, sticky="w", pady=5)
规模分1输入框 = ttk.Entry(frame1)
规模分1输入框.grid(row=2, column=1)

tk.Label(frame1, text="整体规划：", font=正文字体).grid(row=3, column=0, sticky="w", pady=5)
规划分1输入框 = ttk.Entry(frame1)
规划分1输入框.grid(row=3, column=1)

# 添加评分员2的输入框和标签
frame2 = ttk.LabelFrame(root, text="评分员2", labelanchor='n', padding=(10, 5))
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Label(frame2, text="细节表现力：", font=正文字体).grid(row=1, column=0, sticky="w", pady=5)
细节分2输入框 = ttk.Entry(frame2)
细节分2输入框.grid(row=1, column=1)

tk.Label(frame2, text="建筑规模：", font=正文字体).grid(row=2, column=0, sticky="w", pady=5)
规模分2输入框 = ttk.Entry(frame2)
规模分2输入框.grid(row=2, column=1)

tk.Label(frame2, text="整体规划：", font=正文字体).grid(row=3, column=0, sticky="w", pady=5)
规划分2输入框 = ttk.Entry(frame2)
规划分2输入框.grid(row=3, column=1)

# 添加卷面得分的输入框和标签
frame3 = ttk.LabelFrame(root, text="其他信息", labelanchor='n', padding=(10, 5))
frame3.grid(row=0, column=2, padx=10, pady=10, sticky="w")

tk.Label(frame3, text="卷面得分：", font=正文字体).grid(row=0, column=0, sticky="w", pady=5)
卷面得分输入框 = ttk.Entry(frame3)
卷面得分输入框.grid(row=0, column=1)

# 添加团队情况的下拉框和人数输入框
tk.Label(frame3, text="是否有组队情况：", font=正文字体).grid(row=1, column=0, sticky="w", pady=5)
团队情况选择框 = ttk.Combobox(frame3, values=["是", "否"], font=正文字体)
团队情况选择框.grid(row=1, column=1)
团队情况选择框.set("否")

tk.Label(frame3, text="团队人数：", font=正文字体).grid(row=2, column=0, sticky="w", pady=5)
团队人数输入框 = ttk.Entry(frame3)
团队人数输入框.grid(row=2, column=1)

# 添加团队项目数和作品数的输入框和标签
tk.Label(frame3, text="参与团队项目数：", font=正文字体).grid(row=3, column=0, sticky="w", pady=5)
团队项目数输入框 = ttk.Entry(frame3)
团队项目数输入框.grid(row=3, column=1)

tk.Label(frame3, text="个人作品数：", font=正文字体).grid(row=4, column=0, sticky="w", pady=5)
个人作品数输入框 = ttk.Entry(frame3)
个人作品数输入框.grid(row=4, column=1)

# 添加计算按钮
计算按钮 = ttk.Button(root, text="计算平均分", command=提交评分, style='TButton')
计算按钮.grid(row=1, column=0, columnspan=3, pady=10)

# 显示结果的标签
frame4 = ttk.LabelFrame(root, text="评分结果", labelanchor='n', padding=(10, 5))
frame4.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

结果标签 = ttk.Label(frame4, text="", font=正文字体)
结果标签.grid(row=0, column=0)

# 预审分数标签
预审分数标签 = ttk.Label(frame4, text="", font=正文字体)
预审分数标签.grid(row=1, column=0)

# 终审分数标签
终审分数标签 = ttk.Label(frame4, text="", font=正文字体)
终审分数标签.grid(row=2, column=0)

# 是否通过标签
是否通过标签 = ttk.Label(frame4, text="", font=正文字体)
是否通过标签.grid(row=3, column=0)

# 主题颜色设置
style = ttk.Style()
style.configure('TButton', foreground='white', background=主题颜色, font=正文字体)
style.map('TButton',
          foreground=[('pressed', 'black'), ('active', 'white')],
          background=[('pressed', '!disabled', 'gray'), ('active', 主题颜色)])

# 启动主循环
root.mainloop()
