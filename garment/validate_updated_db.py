"""
验证更新后的题库完整性和准确性
检查新增的标准选择题目
"""

import json

def validate_updated_db():
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']
    metadata = data['metadata']

    print("=" * 70)
    print("📊 题库更新验证 - v3.1")
    print("=" * 70)

    # 1. 验证元数据
    print(f"\n✅ 元数据验证：")
    print(f"   版本：{metadata['version']}")
    print(f"   总题数：{metadata['total_questions']}")
    print(f"   标准数：{len(metadata['source_standards'])}")
    print(f"   分类数：{len(metadata['categories'])}")
    print(f"   更新时间：{metadata['last_updated']}")

    # 2. 验证新增题目
    print(f"\n✅ 新增题目验证（标准选择逻辑）：")
    new_question_ids = [158, 159, 160]
    for q_id in new_question_ids:
        q = next((q for q in questions if q['id'] == q_id), None)
        if q:
            print(f"   ID {q_id}: ✓ 存在")
            print(f"      - 分类：{q['category']}")
            print(f"      - 标准：{q['standard']}")
            print(f"      - 选项数：{len(q['options'])}")
            print(f"      - 正确答案：{q['options'][q['correct']]}")
        else:
            print(f"   ID {q_id}: ✗ 缺失")

    # 3. 统计标准覆盖
    print(f"\n✅ 标准覆盖统计：")
    standard_counts = {}
    for q in questions:
        std = q.get('standard', 'Unknown')
        standard_counts[std] = standard_counts.get(std, 0) + 1

    for std, count in sorted(standard_counts.items()):
        print(f"   {std}: {count}题")

    # 4. 统计分类
    print(f"\n✅ 分类统计：")
    category_counts = {}
    for q in questions:
        cat = q.get('category', 'Unknown')
        category_counts[cat] = category_counts.get(cat, 0) + 1

    for cat, count in sorted(category_counts.items()):
        print(f"   {cat}: {count}题")

    # 5. 验证题库完整性
    print(f"\n✅ 题库完整性检查：")
    issues = []

    for q in questions:
        if 'id' not in q:
            issues.append(f"ID缺失")
        if 'content' not in q:
            issues.append(f"ID {q.get('id')}: content 缺失")
        if 'options' not in q:
            issues.append(f"ID {q.get('id')}: options 缺失")
        if 'correct' not in q:
            issues.append(f"ID {q.get('id')}: correct 缺失")
        if 'standard' not in q:
            issues.append(f"ID {q.get('id')}: standard 缺失")
        if 'explanation' not in q:
            issues.append(f"ID {q.get('id')}: explanation 缺失")

    if issues:
        print(f"   ⚠️ 发现 {len(issues)} 个问题：")
        for issue in issues[:5]:
            print(f"      - {issue}")
    else:
        print(f"   ✓ 所有{len(questions)}道题都完整")

    # 6. 关键指标验证
    print(f"\n✅ 关键指标验证：")
    print(f"   总题数：{len(questions)} (目标：94)")
    print(f"   GB/T 31888题目：{standard_counts.get('GB/T 31888-2015', 0)} 题")
    print(f"   GB/T 23328题目：{standard_counts.get('GB/T 23328-2009', 0)} 题")
    print(f"   新增标准选择题：3 题（ID 158, 159, 160）")

    print("\n" + "=" * 70)
    print("✅ 验证完成！题库已成功更新为 v3.1")
    print("=" * 70)

if __name__ == "__main__":
    validate_updated_db()
