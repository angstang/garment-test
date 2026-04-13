"""
修复问题题库中的歧义 - 添加明确的年龄和分类定义
根据标准定义：
- 婴幼儿（FZ/T 73049）：0-3岁（0-36月龄）
- 儿童（FZ/T 73049）：3-14岁
- A类（GB 18401）：0-36月龄婴幼儿产品
- B类（GB 18401）：直接接触皮肤的产品
- C类（GB 18401）：其他产品
"""

import json
from pathlib import Path

def fix_questions():
    # 加载问题数据库
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']

    # 需要修复的问题ID列表（根据审计结果）
    problem_ids = [2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 15, 33, 42, 46, 51, 52, 53, 54,
                   56, 57, 58, 60, 61, 63, 65, 66, 68, 70, 71, 73, 74, 75, 77, 78, 80, 88, 90, 93, 100]

    modifications = {
        # 儿童产品安全类别 - 需要添加年龄定义
        2: {
            'explanation': '儿童服装（FZ/T 73049中定义为3-14岁）中，可分解芳香胺染料的限制值为≤30mg/kg，GB 18401同样规定，这类染料具有致癌性。'
        },
        3: {
            'explanation': '儿童服装（3-14岁）中重金属限制：铅≤100mg/kg，镉≤50mg/kg。这是对儿童安全的强制要求。'
        },
        4: {
            'explanation': '儿童产品（特别是婴幼儿，0-3岁/0-36月龄）的pH值要求4.0-7.5，过酸或过碱都会刺激皮肤。'
        },
        5: {
            'explanation': '邻苯二甲酸酯是塑料软化剂，主要限制对象是儿童纺织品（3-14岁）上的塑料装饰品和按钮等，限值为≤1000mg/kg。'
        },
        7: {
            'explanation': '邻苯二甲酸酯（DEHP、DBP、BBP）在儿童纺织品（3-14岁）中的限值为≤1000mg/kg（各单一物质）。'
        },
        8: {
            'explanation': '儿童服装（3-14岁）的阻燃剂受严格限制，禁用某些有毒的溴系阻燃剂和磷系阻燃剂，以保护儿童安全。'
        },
        9: {
            'explanation': '棉纤维具有良好的透气性、吸湿性和生物相容性，对儿童（3-14岁）皮肤最为安全，这也是为什么儿童衣物应优先选择棉质材料。'
        },
        10: {
            'explanation': '过度漂白会留下漂白剂残留物，对婴幼儿（0-3岁/0-36月龄）皮肤有害。应使用温和的漂白工艺，特别是对A类产品。'
        },
    }

    # 应用修复
    fixed_count = 0
    for q in questions:
        q_id = q['id']
        if q_id in modifications:
            q['explanation'] = modifications[q_id]['explanation']
            fixed_count += 1
            print(f"✅ 修复问题 {q_id}")

    print(f"\n已修复 {fixed_count} 道题目")

    # 保存修复后的数据
    with open('questions_db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ 已保存修复后的 questions_db.json")
    return fixed_count

if __name__ == "__main__":
    fix_questions()
