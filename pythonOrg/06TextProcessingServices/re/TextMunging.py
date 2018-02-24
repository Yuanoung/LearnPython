import random
import re


# 文本显示
# sub()用字符串或函数的结果替换模式的每一次出现

def repl(m):
    # <1>对于匹配Professor的情况，m.groups的值为['P', 'rofesso', 'r'], m.group(2)取得的值为rofesso，也就是说所以是从1开始的
    _ = m.groups()
    inner_word = list(m.group(2))  # <1>
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)


if __name__ == "__main__":
    text = "Professor Abdolmalek, please report your absences promptly."
    _ = re.sub(r"(\w)(\w+)(\w)", repl, text)  # 首先匹配Professor，　处理完毕后匹配Abdolmalek，以此类推
    print(_)
    _ = re.sub(r"(\w)(\w+)(\w)", repl, text)
    print(_)
    print(re.match(r"(\w)(\w+)(\w)", text).group(2))
