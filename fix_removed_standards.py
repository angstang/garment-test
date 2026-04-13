"""
修复题库中残留的已删除标准引用
1. 清理元数据中的FZ/T 73049和QB/T 2397
2. 修复题目解释中的错误引用
3. 根据GB/T 31888-2015和GB 31701-2015更正技术指标
"""

import json
from pathlib import Path

def fix_removed_standards():
    # 加载题库
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. 更新元数据 - 删除已删除的标准
    print("📝 修复元数据中的标准引用...")
    data['metadata']['source_standards'] = [
        "GB 31701-2015 婴幼儿及儿童纺织产品安全技术规范",
        "GB 18401-2010 国家纺织品基本安全技术规范",
        "GB/T 31888-2015 中小学生校服",
        "GB/T 23328-2009 机织学生服装",
        "GB/T 22849-2024 纽扣安全要求"
    ]

    # 2. 修复题目解释中的错误引用
    print("🔧 修复题目解释中的错误标准引用...")
    fixes = {
        # ID 33: 修复QB/T 2397引用
        33: {
            'explanation': 'A类产品的pH值应保持在4.0-7.5范围内，过酸或过碱都会刺激皮肤。'
        },
        # ID 42: 修复QB/T 2397引用
        42: {
            'explanation': '婴幼儿穿着时口腔液体（唾液）可能溶解或释放服装中的有毒物质，这是为什么婴幼儿产品需要更严格标准的原因。'
        }
    }

    questions = data['questions']
    fixed_count = 0

    for q in questions:
        q_id = q['id']

        # 修复指定ID的题目
        if q_id in fixes:
            q['explanation'] = fixes[q_id]['explanation']
            fixed_count += 1
            print(f"✅ 修复ID {q_id}: {q['content'][:40]}...")

        # 扫描所有解释中的错误引用
        if 'QB/T 2397' in q.get('explanation', ''):
            print(f"⚠️ 警告 ID {q_id}: 仍含有QB/T 2397引用")
            print(f"   内容: {q['explanation'][:60]}...")

        if 'FZ/T 73049' in q.get('explanation', '') and '针织口罩' not in q.get('explanation', ''):
            print(f"⚠️ 警告 ID {q_id}: 仍含有FZ/T 73049引用")

    print(f"\n✅ 已修复 {fixed_count} 道题目的解释")

    # 3. 验证标准引用
    print("\n📊 验证所有题目的标准引用...")
    valid_standards = {
        "GB 31701-2015",
        "GB 18401-2010",
        "GB/T 31888-2015",
        "GB/T 23328-2009",
        "GB/T 22849-2024",
        "校服面料",
        "校服工艺",
        "检测方法",
        "GB/T 3917.3-2025",
        "GB/T 7573-2025",
        "GB/T 4802.1-2008",
        "GB/T 4802.2-2008",
        "GB/T 5453-2025",
        "GB/T 5326-2025",
        "GB/T 19980-2025",
        "GB/T 31902-2025",
        "GB/T 32612-2025",
        "GB/T 21655.1-2023",
        "GB/T 21655.2-2019"
    }

    invalid_standards = set()
    for q in questions:
        standard = q.get('standard', '')
        if standard and standard not in valid_standards:
            invalid_standards.add(standard)

    if invalid_standards:
        print(f"⚠️ 发现不在官方清单中的标准: {invalid_standards}")
    else:
        print("✅ 所有题目的标准引用都有效")

    # 保存修复后的数据
    with open('questions_db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n✅ 已保存修复后的questions_db.json")

    return fixed_count

if __name__ == "__main__":
    fix_removed_standards()
