"""学生成绩记录的解析工具。"""


def parse_student(line):
    """将 ``name,score`` 文本解析为包含 name 与 score 的字典。

    字段数量、姓名、分数格式和 0--100 的分数范围不符合要求时抛出 ValueError。
    """
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("记录必须包含姓名和成绩两个字段")

    name = parts[0].strip()
    score_text = parts[1].strip()
    if not name:
        raise ValueError("姓名不能为空")

    try:
        score = int(score_text)
    except ValueError as error:
        raise ValueError("成绩必须是整数") from error

    if not 0 <= score <= 100:
        raise ValueError("成绩必须在 0 到 100 之间")

    return {"name": name, "score": score}
