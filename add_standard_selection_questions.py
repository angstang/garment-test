"""
添加关于校服标准选择的题目
重点：根据纤维成分选择合适的标准
- GB/T 31888-2015：通用校服标准（夏季服装棉含量≥35%）
- GB/T 23328-2009：机织校服标准（全涤产品适用）
- GB/T 22854-2009：针织校服标准（全涤产品适用）
"""

import json

def add_standard_selection_questions():
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']

    # 查找最大ID
    max_id = max(q['id'] for q in questions)
    print(f"当前最大ID: {max_id}")

    # 新增题目：关于标准选择的关键题目
    new_questions = [
        {
            "id": max_id + 1,
            "category": "校服安全",
            "content": "某服装厂计划生产100%涤纶的夏季校服裤子，应该执行以下哪个标准？",
            "options": [
                "A. GB/T 31888-2015（中小学生校服）",
                "B. GB/T 23328-2009（机织学生服装）",
                "C. 两个标准都可以执行",
                "D. 无需执行任何标准"
            ],
            "correct": 1,
            "standard": "GB/T 31888-2015",
            "explanation": "GB/T 31888-2015规定，夏季服装的棉含量必须≥35%。全涤纶产品无法满足此要求，应改为执行GB/T 23328-2009（机织学生服装标准）。这是行业内常见的做法：不同纤维成分的产品需要选择合适的标准执行。"
        },
        {
            "id": max_id + 2,
            "category": "校服安全",
            "content": "GB/T 31888-2015与GB/T 23328-2009在标准选择上有什么关键区别？",
            "options": [
                "A. GB/T 31888适用于所有校服，GB/T 23328已过时",
                "B. GB/T 31888要求夏季棉含量≥35%；全涤产品应执行GB/T 23328",
                "C. GB/T 31888仅适用于棉织面料",
                "D. 两个标准的技术要求完全相同"
            ],
            "correct": 1,
            "standard": "GB/T 31888-2015",
            "explanation": "GB/T 31888-2015（2015年颁布）是通用校服标准，但规定了夏季服装棉含量≥35%的要求。GB/T 23328-2009是机织校服的基础标准。对于无法满足GB/T 31888棉含量要求的全涤纶产品，企业应执行GB/T 23328标准。这种标准选择在工艺师、设计师和品质部门的决策中非常重要。"
        },
        {
            "id": max_id + 3,
            "category": "校服工艺",
            "content": "校服工艺部门收到一份全涤纶面料的夏季校服生产计划，应该如何确定执行的标准？",
            "options": [
                "A. 仍按GB/T 31888执行，不考虑棉含量要求",
                "B. 与设计部门沟通，改变纤维成分以满足GB/T 31888的棉含量要求",
                "C. 将标准改为GB/T 23328或GB/T 22854（视织物类型而定）",
                "D. 不需要改变任何内容，任何标准都可以"
            ],
            "correct": 1,
            "standard": "GB/T 31888-2015",
            "explanation": "工艺师的职责是确保选定的面料能够符合适用的标准。对于全涤纶面料，由于无法满足GB/T 31888-2015的夏季棉含量≥35%要求，应与设计部门沟通改用GB/T 23328（机织）或GB/T 22854（针织）。这是产品开发阶段必须解决的关键问题，避免后续生产中出现不合格。"
        }
    ]

    # 添加新题目
    for q in new_questions:
        questions.append(q)
        print(f"✅ 添加题目 ID {q['id']}: {q['content'][:50]}...")

    # 保存修改
    with open('questions_db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 已添加 {len(new_questions)} 道关于标准选择的题目")
    print(f"✅ 题库规模已更新为 {len(questions)} 道题")
    print("✅ 已保存修改后的questions_db.json")

    return len(new_questions)

if __name__ == "__main__":
    add_standard_selection_questions()
