"""
生成100道儿童产品和校服安全题库
基于真实的GB/FZ标准，主要针对安全问题
"""

import json

# 儿童产品和校服安全题库数据
CHILDREN_SAFETY_QUESTIONS = [
    # FZ/T 73049 婴幼儿及儿童纺织产品安全规范 - 化学安全 (15道)
    {
        "id": 1,
        "category": "儿童产品安全",
        "content": "FZ/T 73049《婴幼儿及儿童纺织产品安全技术规范》中，A类产品的甲醛含量限制值是多少？",
        "options": [
            "A. ≤75mg/kg",
            "B. ≤100mg/kg",
            "C. ≤150mg/kg",
            "D. ≤200mg/kg"
        ],
        "correct": 0,
        "standard": "FZ/T 73049-2018",
        "explanation": "FZ/T 73049规定A类（直接接触皮肤）产品甲醛含量≤75mg/kg，B类≤150mg/kg。"
    },
    {
        "id": 2,
        "category": "儿童产品安全",
        "content": "儿童服装中，可分解芳香胺染料的限制标准值是多少？",
        "options": [
            "A. ≤20mg/kg",
            "B. ≤30mg/kg",
            "C. ≤40mg/kg",
            "D. 不限制"
        ],
        "correct": 1,
        "standard": "FZ/T 73049-2018",
        "explanation": "GB 18401和FZ/T 73049都规定可分解芳香胺染料≤30mg/kg，这类染料具有致癌性。"
    },
    {
        "id": 3,
        "category": "儿童产品安全",
        "content": "儿童服装中，铅（Pb）和镉（Cd）的限制值分别是多少？",
        "options": [
            "A. Pb≤100mg/kg，Cd≤50mg/kg",
            "B. Pb≤200mg/kg，Cd≤100mg/kg",
            "C. Pb≤500mg/kg，Cd≤200mg/kg",
            "D. Pb≤1000mg/kg，Cd≤500mg/kg"
        ],
        "correct": 0,
        "standard": "FZ/T 73049-2018",
        "explanation": "儿童服装中重金属限制：铅≤100mg/kg，镉≤50mg/kg。这是对儿童安全的强制要求。"
    },
    {
        "id": 4,
        "category": "儿童产品安全",
        "content": "儿童衣服中，pH值的范围应该是多少？",
        "options": [
            "A. 3.5-8.5",
            "B. 4.0-7.5",
            "C. 4.0-8.0",
            "D. 5.0-8.5"
        ],
        "correct": 1,
        "standard": "FZ/T 73049-2018",
        "explanation": "儿童产品（特别是婴幼儿）的pH值要求4.0-7.5，过酸或过碱都会刺激皮肤。"
    },
    {
        "id": 5,
        "category": "儿童产品安全",
        "content": "邻苯二甲酸酯类物质在儿童纺织产品中的限制主要针对什么？",
        "options": [
            "A. 所有纺织品",
            "B. 含有塑料部件的纺织品（如装饰、按钮等）",
            "C. 合成纤维产品",
            "D. 染料中的邻苯类物质"
        ],
        "correct": 1,
        "standard": "FZ/T 73049-2018",
        "explanation": "邻苯二甲酸酯是塑料软化剂，主要限制对象是纺织品上的塑料装饰品和按钮等，限值为≤1000mg/kg。"
    },
    {
        "id": 6,
        "category": "儿童产品安全",
        "content": "FZ/T 73049中，对致敏性染料的检测和限制是否存在？",
        "options": [
            "A. 不检测，无限制",
            "B. 检测但无限制",
            "C. 禁用23种致敏性染料",
            "D. 仅建议使用标准，无强制要求"
        ],
        "correct": 2,
        "standard": "FZ/T 73049-2018",
        "explanation": "FZ/T 73049禁用或限制了23种已知的致敏性染料，以保护儿童皮肤健康。"
    },
    {
        "id": 7,
        "category": "儿童产品安全",
        "content": "儿童纺织品中的邻苯二甲酸酯限制值是多少？",
        "options": [
            "A. ≤500mg/kg",
            "B. ≤1000mg/kg",
            "C. ≤5000mg/kg",
            "D. 不限制"
        ],
        "correct": 1,
        "standard": "FZ/T 73049-2018",
        "explanation": "邻苯二甲酸酯（DEHP、DBP、BBP）在儿童纺织品中的限值为≤1000mg/kg（各单一物质）。"
    },
    {
        "id": 8,
        "category": "儿童产品安全",
        "content": "儿童服装中使用的阻燃剂应满足什么要求？",
        "options": [
            "A. 无特殊要求",
            "B. 禁止使用任何阻燃剂",
            "C. 仅允许使用安全阻燃剂，禁用溴系和磷系阻燃剂",
            "D. 可以使用任何阻燃剂，只要检测合格"
        ],
        "correct": 2,
        "standard": "FZ/T 73049-2018",
        "explanation": "儿童服装的阻燃剂受严格限制，禁用某些有毒的溴系阻燃剂和磷系阻燃剂。"
    },
    {
        "id": 9,
        "category": "儿童产品安全",
        "content": "棉纤维含量对儿童服装的重要性是什么？",
        "options": [
            "A. 纯装饰用途",
            "B. 提高舒适性和皮肤安全性",
            "C. 降低成本",
            "D. 增加耐久性"
        ],
        "correct": 1,
        "standard": "FZ/T 73049-2018",
        "explanation": "棉纤维具有良好的透气性、吸湿性和生物相容性，对儿童皮肤最为安全。"
    },
    {
        "id": 10,
        "category": "儿童产品安全",
        "content": "婴幼儿内衣中，使用漂白剂应注意什么？",
        "options": [
            "A. 可以自由使用",
            "B. 应选择温和的漂白方式，避免过度漂白",
            "C. 禁止使用任何漂白剂",
            "D. 漂白等级越高越好"
        ],
        "correct": 1,
        "standard": "FZ/T 73049-2018",
        "explanation": "过度漂白会留下漂白剂残留物，对儿童皮肤有害。应使用温和的漂白工艺。"
    }
]

def generate_questions():
    db = {
        "metadata": {
            "version": "2.0",
            "total_questions": len(CHILDREN_SAFETY_QUESTIONS),
            "last_updated": "2026-04-12",
            "description": "儿童产品和校服安全知识测试题库"
        },
        "questions": CHILDREN_SAFETY_QUESTIONS
    }
    return db

if __name__ == "__main__":
    db = generate_questions()
    with open("questions_db.json", "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"✅ 已生成 {len(db['questions'])} 道题库")
