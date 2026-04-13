"""
验证题库中的技术指标是否与标准完全吻合
重点检查：缩水率、接缝强力、色牢度等关键指标
"""

import json

def verify_technical_accuracy():
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']
    issues = []

    print("=" * 70)
    print("技术指标准确性验证")
    print("=" * 70)

    for q in questions:
        q_id = q['id']
        content = q['content']
        explanation = q['explanation']
        standard = q['standard']

        # 1. 检查缩水率表述
        if '缩水' in content or '缩水' in explanation:
            # GB/T 31888规定缩水率是双向的，不是单向的"不超过"
            if 'GB/T 31888' in standard or 'GB/T 23328' in standard:
                if '≤' in explanation and '缩水' in explanation:
                    # 检查是否正确表述了双向性
                    if '～' not in explanation and '-' not in explanation:
                        issues.append({
                            'id': q_id,
                            'type': '缩水率表述错误',
                            'content': content[:50],
                            'problem': '缩水率应表述为双向范围（可缩小或扩大），不是单向"不超过"',
                            'example': '例：经向-1.5～+1.5%，纬向-2.5～+1.5%'
                        })

        # 2. 检查接缝强力表述
        if '接缝强力' in content or '接缝强力' in explanation:
            if 'GB/T 31888' in standard or 'GB/T 23328' in standard:
                # 接缝强力应是具体的N值，而不是与面料强力的百分比
                if '百分比' in explanation or '%' in explanation:
                    issues.append({
                        'id': q_id,
                        'type': '接缝强力表述错误',
                        'content': content[:50],
                        'problem': 'GB/T 31888规定接缝强力为具体值（圆料≥140N，里料≥80N），不是百分比',
                        'correct': '接缝强力应为：圆料≥140N，里料≥80N'
                    })

        # 3. 检查色牢度等级要求
        if '色牢度' in content or '色牢度' in explanation:
            if 'GB/T 23328' in standard:
                # GB/T 23328表1中耐皂洗要求3-4级（不是简单的≥3级）
                if '≥3级' in explanation and '3-4' not in explanation:
                    if '耐皂洗' in explanation or '耐皂洗' in content:
                        issues.append({
                            'id': q_id,
                            'type': '色牢度等级精度不足',
                            'content': content[:50],
                            'problem': 'GB/T 23328耐皂洗色牢度要求3-4级，应更明确',
                            'note': '各类色牢度具体要求见GB/T 31888表1'
                        })

        # 4. 检查深色产品的色牢度要求
        if '深色' in explanation and '摩擦色牢度' in explanation:
            if 'GB 31701' in standard or 'GB 18401' in standard:
                # GB 31701中深色产品的耐湿摩擦色牢度可以是2-3级
                if '≥3' in explanation and '2-3' not in explanation:
                    issues.append({
                        'id': q_id,
                        'type': '深色产品色牢度要求不准确',
                        'content': content[:50],
                        'problem': 'GB 31701中深色产品耐湿摩擦色牢度可为2-3级，非必须≥3级',
                        'note': '只有浅色才要求≥3级'
                    })

    # 打印验证结果
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个技术指标问题:\n")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. ID {issue['id']}: {issue['type']}")
            print(f"   题目: {issue['content']}")
            print(f"   问题: {issue['problem']}")
            if 'correct' in issue:
                print(f"   建议: {issue['correct']}")
            if 'example' in issue:
                print(f"   示例: {issue['example']}")
            if 'note' in issue:
                print(f"   说明: {issue['note']}")
            print()
    else:
        print("\n✅ 所有技术指标都与标准吻合！")

    print("\n" + "=" * 70)
    print("关键技术指标参考")
    print("=" * 70)
    print("""
GB/T 31888-2015（中小学生校服）关键指标：
────────────────────────────────────────
□ 耐皂洗色牢度：3-4级
□ 耐摩擦色牢度（湿摩）：3级
□ 起球性：≥3-4级
□ 接缝强力：圆料≥140N，里料≥80N
□ 缩水率（机织）：经向-1.5～+1.5%，纬向-1.5～+1.5%
□ 顶破强力（机织）：≥250N
□ 断裂强力（机织）：≥200N

GB 31701-2015（儿童产品）关键指标：
────────────────────────────────────────
□ 耐湿摩擦色牢度：≥3级（深色2-3级）
□ 重金属（铅）：≤90mg/kg
□ 重金属（镉）：≤100mg/kg
□ 邻苯二甲酸酯：≤0.1%
□ 绳带长度限制：详见表3（按年龄分类）
""")

if __name__ == "__main__":
    verify_technical_accuracy()
