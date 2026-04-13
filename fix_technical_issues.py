"""
修复题库中发现的技术指标错误
1. ID 19, 120, 145：接缝强力表述 - 改为具体数值而非百分比
2. ID 20：缩水率表述 - 改为双向范围而非单向限制
"""

import json

def fix_technical_issues():
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']

    # 定义修复方案
    fixes = {
        # ID 19: 接缝强力 - 改为具体数值
        19: {
            'content': 'GB/T 23328-2009规定，校服面料的接缝强力最低要求是多少？',
            'options': [
                "A. 圆料≥100N，里料≥50N",
                "B. 圆料≥140N，里料≥80N",
                "C. 圆料≥200N，里料≥150N",
                "D. 圆料≥250N，里料≥200N"
            ],
            'correct': 1,
            'explanation': '根据GB/T 31888-2015，校服的接缝强力（缝处拉力）要求：圆料≥140N，里料≥80N。这是固定的性能指标要求，不是相对百分比。'
        },

        # ID 20: 缩水率 - 改为双向范围
        20: {
            'content': 'GB/T 31888-2015规定，机织校服的缩水率要求范围是多少？',
            'options': [
                "A. 经向-1.5～+1.5%，纬向-1.5～+1.5%",
                "B. 经向≤3%，纬向≤4%",
                "C. 经向≤5%，纬向≤5%",
                "D. 无缩水率要求"
            ],
            'correct': 0,
            'explanation': '根据GB/T 31888-2015表1，机织校服的缩水率为双向范围：经向-1.5～+1.5%，纬向-1.5～+1.5%。这意味着洗涤后可能缩小或扩大，但不应超过这个范围。'
        },

        # ID 120: 接缝强力 - 改为具体数值
        120: {
            'content': 'GB/T 31888中，校服接缝处的抗拉强力最低标准是多少？',
            'options': [
                "A. 面料强度的50%",
                "B. 面料强度的75%",
                "C. 圆料≥140N，里料≥80N",
                "D. 面料强度的90%"
            ],
            'correct': 2,
            'explanation': '根据GB/T 31888-2015，校服接缝强力的要求为：圆料≥140N，里料≥80N。这是基于实测尺度的具体数值要求，而不是相对于面料强力的百分比。'
        },

        # ID 145: 接缝强力定义 - 修正解释
        145: {
            'explanation': '接缝强力是指沿缝线方向的织物抗拉强力。根据GB/T 31888-2015，校服接缝强力的要求为：圆料≥140N，里料≥80N。接缝是校服最容易损坏的地方，因为受力最大，所以必须有严格的强力要求，确保校服穿着安全耐用。'
        }
    }

    fixed_count = 0
    for q in questions:
        q_id = q['id']
        if q_id in fixes:
            fix_data = fixes[q_id]

            if 'content' in fix_data:
                q['content'] = fix_data['content']
            if 'options' in fix_data:
                q['options'] = fix_data['options']
            if 'correct' in fix_data:
                q['correct'] = fix_data['correct']
            if 'explanation' in fix_data:
                q['explanation'] = fix_data['explanation']

            fixed_count += 1
            print(f"✅ 修复ID {q_id}: {fix_data.get('content', '')[:50]}...")

    # 保存修复后的数据
    with open('questions_db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 已修复 {fixed_count} 道题目的技术指标")
    print("✅ 已保存修复后的questions_db.json")

if __name__ == "__main__":
    fix_technical_issues()
