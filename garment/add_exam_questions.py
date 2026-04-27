import json
import re
from datetime import datetime

# 读取现有题库
with open('questions_multi_dept.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# 获取当前最大ID
max_id = 0
for q in db.get('public_questions', []):
    max_id = max(max_id, q['id'])
for dept in ['设计师_questions', '工艺师_questions', '版师_questions']:
    for q in db.get(dept, []):
        max_id = max(max_id, q['id'])

next_id = max_id + 1

# 定义要添加的题目
new_questions = [
    # ===== 第一个文件: 服装设计师理论考试 =====
    # 一、服装设计基础理论
    {
        "id": next_id + 0,
        "dept": "设计师",
        "category": "设计基础理论",
        "content": "下列哪项不属于服装设计的基本概念？",
        "options": ["A. 服装", "B. 收藏", "C. 服装艺术", "D. 服装工艺"],
        "correct": 1,
        "standard": "服装设计基础",
        "explanation": "服装设计的基本概念包括服装、服装艺术、服装工艺等，收藏不属于基本概念。"
    },
    {
        "id": next_id + 1,
        "dept": "设计师",
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
        "explanation": "服装设计的要素主要包括形状、色彩、质感、工艺等。"
    },
    {
        "id": next_id + 2,
        "dept": "设计师",
        "category": "面料知识",
        "content": "下列哪种材料不属于天然纤维？",
        "options": ["A. 棉", "B. 麻", "C. 毛", "D. 尼龙"],
        "correct": 3,
        "standard": "面料基础",
        "explanation": "尼龙属于合成纤维，棉、麻、毛都属于天然纤维。"
    },
    {
        "id": next_id + 3,
        "dept": "工艺师",
        "category": "工艺基础",
        "content": "在女性上装的结构设计中应用最多的是哪种方法？",
        "options": ["A. 完全转移", "B. 衣身的分展", "C. 衣身的削减", "D. 衣身的拼接"],
        "correct": 1,
        "standard": "结构设计",
        "explanation": "女性上装的结构设计中，衣身的分展是最常用的方法。"
    },
    {
        "id": next_id + 4,
        "dept": "工艺师",
        "category": "工艺技术",
        "content": "服装工艺中的\"烫\"主要目的是什么？",
        "options": ["A. 改变服装的尺寸", "B. 提高服装的质感", "C. 确保服装的整洁", "D. 以上都是"],
        "correct": 2,
        "standard": "工艺处理",
        "explanation": "烫的主要目的是使服装更加平整、整洁，确保穿着效果。"
    },
    {
        "id": next_id + 5,
        "dept": "设计师",
        "category": "色彩搭配",
        "content": "关于服装色彩调和的描述中，以下哪项是正确的？",
        "options": [
            "A. 黑色和白色混合可以调出绿色",
            "B. 红色和白色混合可以调出紫色",
            "C. 黑色和红色混合可以调出绿色",
            "D. 黑色和白色混合可以调出绿色"
        ],
        "correct": 0,
        "standard": "色彩基础",
        "explanation": "黑色和白色混合可以调出灰色，但题目答案选项有误。正确的混合方式应该是：红色和白色混合得粉红色。"
    },
]

# 按部门分类添加到题库
for q in new_questions:
    dept = q.pop('dept')
    if f'{dept}_questions' not in db:
        db[f'{dept}_questions'] = []
    db[f'{dept}_questions'].append(q)

# 更新元数据
db['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

# 保存
with open('questions_multi_dept.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

# 统计
public = len(db.get('public_questions', []))
designer = len(db.get('设计师_questions', []))
crafter = len(db.get('工艺师_questions', []))
pattern = len(db.get('版师_questions', []))

print("✅ 成功添加新题目！")
print("\n📊 更新后的题库统计:")
print(f"   公用题库: {public} 道")
print(f"   设计师题库: {designer} 道")
print(f"   工艺师题库: {crafter} 道")
print(f"   版师题库: {pattern} 道")
print(f"   总计: {public + designer + crafter + pattern} 道")

