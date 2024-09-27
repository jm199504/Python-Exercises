## 7.11-实现一个简单的问答系统

### 问题描述

提供以下的问题与答案库，实现文本匹配回答问题

| question               | answer                                               |
| ---------------------- | ---------------------------------------------------- |
| 中国总面积             | 中国的总面积约为960万平方公里（约为370万平方英里）。 |
| 陆地上最大的动物是什么 | 大象                                                 |
| 中国总人口             | 截至2022年，中国的人口约为14亿。                     |

### 输入输出示例

```
陆地上最大的动物是什么
大象

中国总面积
中国的总面积约为960万平方公里（约为370万平方英里）。

```

### 示例代码

```python
# 问答库
qa_database = {
    "中国总面积": "中国的总面积约为960万平方公里（约为370万平方英里）。",
    "陆地上最大的动物是什么": "大象",
    "中国总人口": "截至2022年，中国的人口约为14亿。",
}

def answer_question(user_question):
    # 查找问题，返回对应的答案
    return qa_database.get(user_question, "抱歉，我无法回答这个问题。")

def main():
    print("请问有什么问题需要解答？")
    while True:
        user_input = input()
        if user_input.lower() in ["exit", "quit"]:
            print("谢谢使用，再见！")
            break
        answer = answer_question(user_input)
        print(answer)

if __name__ == "__main__":
    main()
```

