import json
import re

# 读取当前题库
with open('questions_multi_dept.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取当前最大ID
max_id = 0
for q in data.get('public_questions', []):
    if q['id'] > max_id:
        max_id = q['id']
for dept in ['设计师', '工艺师', '版师']:
    for q in data.get(f'{dept}_questions', []):
        if q['id'] > max_id:
            max_id = q['id']

current_id = max_id + 1

# 第一份文件题目（服装设计师专业理论考试）
file1_questions = [
    # 第一部分：服装设计基础理论
    {
        "category": "设计基础理论",
        "content": "下列哪项不属于服装设计的基本概念？",
        "options": ["A. 服装", "B. 收藏", "C. 服装艺术", "D. 服装工艺"],
        "correct": 3,
        "standard": "服装设计基础",
        "explanation": "服装设计的基本概念包括服装、收藏、服装艺术、服装工艺等，B项收藏不属于基本概念。"
    },
    {
        "category": "设计基础理论",
        "content": "服装设计的基本要素中不包括以下哪项？",
        "options": ["A. 适用性要素", "B. 经济性要素", "C. 美观性要素", "D. 实用性要素"],
        "correct": 1,
        "standard": "服装设计基础",
        "explanation": "服装设计的基本要素包括适用性、美观性、实用性等，经济性要素不属于基本要素。"
    },
    {
        "category": "设计要素",
        "content": "服装设计的要素主要包括哪些？",
        "options": [
            "A. 形状、色彩、质感、工艺",
            "B. 收藏、流行、审美、个性",
            "C. 经济性、经济性、美观性、实用性",
            "D. 功能性、安全性、便捷性、美观性"
        ],
        "correct": 0,
        "standard": "设计要素",
        "explanation": "服装设计的要素主要包括形状、色彩、质感、工艺等，这些要素是设计的核心。"
    }
]

# 第二份文件题目（制版师工艺技术理论考试）
file2_questions = [
    {
        "category": "工艺基础",
        "content": "在女性上装的结构设计中应用最多的是哪种方法？",
        "options": ["A. 完全转移", "B. 衣身的分展", "C. 衣身的削减", "D. 衣身的拼接"],
        "correct": 1,
        "standard": "结构设计",
        "explanation": "女性上装的结构设计中，衣身的分展是最常用的方法，用于造型塑形。"
    },
    {
        "category": "工艺基础",
        "content": "当衣物拢钉精钉时，如果中线歪斜，通常的处理方法是？",
        "options": ["A. 往后带", "B. 往前带", "C. 保持不变", "D. 重新裁剪"],
        "correct": 1,
        "standard": "工艺处理",
        "explanation": "中线歪斜时需要往前带来进行调整，确保衣物穿着时的平衡性。"
    },
    {
        "category": "面料知识",
        "content": "下列哪种面料不属于天然纤维？",
        "options": ["A. 棉", "B. 麻", "C. 毛", "D. 尼龙"],
        "correct": 3,
        "standard": "面料基础",
        "explanation": "尼龙属于合成纤维，而棉、麻、毛都属于天然纤维。"
    }
]

# 合并所有新题目
all_new_questions = file1_questions + file2_questions

# 添加到设计师题库
if '设计师_questions' not in data:
    data['设计师_questions'] = []

for q in all_new_questions:
    q['id'] = current_id
    current_id += 1
    # 根据category分配到相应部门
    if '工艺' in q['category']:
        if '工艺师_questions' not in data:
            data['工艺师_questions'] = []
        data['工艺师_questions'].append(q)
    else:
        data['设计师_questions'].append(q)

# 更新元数据
data['metadata']['last_updated'] = '2026-04-26'
data['metadata']['notes'] = '包含2025年服装设计师和制版师专业理论知识考试试卷的全部题目'

# 保存更新后的题库
with open('questions_multi_dept.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 成功添加 {len(all_new_questions)} 道新题目")
print(f"   - 设计师题库: {len(data.get('设计师_questions', []))} 道")
print(f"   - 工艺师题库: {len(data.get('工艺师_questions', []))} 道")
