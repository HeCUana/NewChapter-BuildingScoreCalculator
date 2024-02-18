# 建筑评分系统

这是一个简单的建筑评分系统，使用 Python 的 tkinter 库进行图形用户界面（GUI）开发。

一般情况下，终审分数按如下计算：
终审分数=审核建筑评分*max(1,预审分数) ，通过审核分数线是 70。
审核建筑评分=(细节表现力（1~10）/10+建筑规模（1~3）/3+整体规划（1~5）
/5)*33.33
审核建筑评分计算时应取两位审核员各项打分平均值。
如果有组队审核的情况，审核建筑得分=原审核建筑得分/(1.4^(人数-1))，要
求人数不得多于 3 人。
预审分数=(卷面得分*max(1,(参与团队项目数+作品数)/2+1))/8。

## 如何使用

1. 安装 Python（如果尚未安装）：[https://www.python.org/downloads/](https://www.python.org/downloads/)

2. 克隆或下载该仓库：

```bash
git clone https://github.com/HeCUana/-New-Chapter-Building-Score-Calculator.git
