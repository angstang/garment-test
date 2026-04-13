"""
添加校服面料知识和检测方法标准的题目
涵盖：面料纤维、特性、性能指标、检测方法等
"""

import json
from pathlib import Path

def add_fabric_and_testing_questions():
    # 加载现有题库
    with open('questions_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data['questions']

    # 找到最大的ID
    max_id = max(q['id'] for q in questions)
    next_id = max_id + 1

    # 新增题目（校服面料和检测方法）
    new_questions = [
        # ===== 面料纤维成分和特性 =====
        {
            "id": next_id,
            "category": "校服面料",
            "content": "校服面料中，纯棉纤维相比涤纶的主要优势是什么？",
            "options": [
                "A. 耐磨性更好",
                "B. 透气性和吸湿性更好",
                "C. 色牢度更高",
                "D. 缩水率更小"
            ],
            "correct": 1,
            "standard": "GB/T 31888-2015",
            "explanation": "纯棉具有优良的透气性、吸湿性和生物相容性，穿着舒适，特别适合儿童和学生长时间穿着。涤纶则具有更好的耐磨性和尺寸稳定性。"
        },
        {
            "id": next_id + 1,
            "category": "校服面料",
            "content": "棉涤混纺（如65%棉/35%涤纶）用于校服的主要目的是什么？",
            "options": [
                "A. 降低成本",
                "B. 提高强度和耐久性",
                "C. 改善透气性",
                "D. 增加面料厚度"
            ],
            "correct": 1,
            "standard": "GB/T 31888-2015",
            "explanation": "棉涤混纺结合了棉的舒适性和涤纶的耐久性、尺寸稳定性，提高了校服的穿着寿命和洗涤耐受性。是最常用的校服面料组成。"
        },
        {
            "id": next_id + 2,
            "category": "校服面料",
            "content": "校服面料克重通常范围是多少？（单位：g/m²）",
            "options": [
                "A. 80-120",
                "B. 120-200",
                "C. 200-280",
                "D. 280-380"
            ],
            "correct": 1,
            "standard": "GB/T 23328-2009",
            "explanation": "机织校服面料克重通常为120-200g/m²，保证足够的强度和耐久性。过轻则强度不足，过重则穿着不舒适。"
        },
        {
            "id": next_id + 3,
            "category": "校服面料",
            "content": "什么是面料密度？对校服质量有什么影响？",
            "options": [
                "A. 单位长度的纱线数，密度越高强度越强",
                "B. 面料的厚度，厚度越厚越好",
                "C. 纤维细度，纤维越细越好",
                "D. 色牢度，色牢度越高越好"
            ],
            "correct": 0,
            "standard": "GB/T 31888-2015",
            "explanation": "面料密度是指单位长度（1英寸或10cm）内的经纱和纬纱根数。密度高的面料强度好，耐磨性强，但透气性相对较差。校服需在强度和舒适性间找到平衡。"
        },
        # ===== 面料性能指标 =====
        {
            "id": next_id + 4,
            "category": "校服面料",
            "content": "GB/T 3917.3《色牢度试验方法 耐皂洗色牢度》中，3级色牢度表示什么意思？",
            "options": [
                "A. 最好的色牢度",
                "B. 洗涤后轻微褪色，可接受",
                "C. 洗涤后明显褪色，不可接受",
                "D. 完全掉色，报废"
            ],
            "correct": 1,
            "standard": "GB/T 3917.3-2025",
            "explanation": "色牢度等级1-5级，其中3级为轻微褪色但在可接受范围内。校服通常要求≥3级，确保正常洗涤中颜色稳定。"
        },
        {
            "id": next_id + 5,
            "category": "校服面料",
            "content": "GB/T 7573《纺织品 水洗后尺寸变化的测定》规定，校服经向缩水率超过多少时视为不合格？",
            "options": [
                "A. 2%",
                "B. 3%",
                "C. 4%",
                "D. 5%"
            ],
            "correct": 1,
            "standard": "GB/T 7573-2025",
            "explanation": "校服洗涤缩水率要求：经向≤3%，纬向≤4%。超过这个限值会导致校服变小，无法继续穿着。"
        },
        {
            "id": next_id + 6,
            "category": "校服面料",
            "content": "GB/T 4802《纺织品 织物起毛起球性能的评定》中，防起球性3级表示什么？",
            "options": [
                "A. 无起球",
                "B. 轻微起球，可接受",
                "C. 明显起球，不合格",
                "D. 严重起球，报废"
            ],
            "correct": 1,
            "standard": "GB/T 4802.1-2008",
            "explanation": "防起球性分为5级，3级表示轻微起球但在可接受范围内。校服要求≥3级，保证穿着外观质量。"
        },
        {
            "id": next_id + 7,
            "category": "校服面料",
            "content": "GB/T 21655《纺织品 拉伸弹性的测定 应力应变法》主要用于检测面料的什么性能？",
            "options": [
                "A. 耐磨性",
                "B. 拉伸强力和弹性恢复",
                "C. 透气性",
                "D. 吸水性"
            ],
            "correct": 1,
            "standard": "GB/T 21655.1-2023",
            "explanation": "拉伸强力是面料的重要性能指标，反映面料的强度和耐用性。校服接缝强力应≥面料强力的75%。"
        },
        {
            "id": next_id + 8,
            "category": "校服面料",
            "content": "什么是面料的接缝强力？为什么校服对接缝强力有严格要求？",
            "options": [
                "A. 缝线的强度，强度高缝线就不易断",
                "B. 缝接部分面料的强度，这是校服最容易损坏的地方",
                "C. 整块面料的平均强度",
                "D. 面料与线的摩擦力"
            ],
            "correct": 1,
            "standard": "GB/T 23328-2009",
            "explanation": "接缝强力是指沿缝线的面料强度。校服在穿着和洗涤过程中，接缝部分是受力最大且最容易损坏的地方，因此要求≥面料强力的75%。"
        },
        # ===== 面料在不同工序中的应用 =====
        {
            "id": next_id + 9,
            "category": "校服工艺",
            "content": "设计师选择校服面料时，首先应考虑的因素是什么？",
            "options": [
                "A. 面料价格最低",
                "B. 面料外观好看",
                "C. 穿着舒适性和安全标准符合性",
                "D. 面料厚度最厚"
            ],
            "correct": 2,
            "standard": "GB/T 31888-2015",
            "explanation": "设计师必须优先确保所选面料符合GB/T 31888、GB/T 23328等校服标准，同时兼顾穿着舒适性（透气性、吸湿性）和儿童/学生的皮肤安全。"
        },
        {
            "id": next_id + 10,
            "category": "校服工艺",
            "content": "工艺师在制定校服生产工艺时，需要重点关注面料的哪个性质？",
            "options": [
                "A. 面料的纤维成分",
                "B. 面料的缩水率，以确定预缩处理工艺",
                "C. 面料的颜色",
                "D. 面料的进价成本"
            ],
            "correct": 1,
            "standard": "GB/T 7573-2025",
            "explanation": "工艺师需要根据面料的缩水特性制定预缩处理、裁剪尺寸调整等工艺，确保最终产品经洗涤后符合GB/T 23328的缩水率要求。"
        },
        {
            "id": next_id + 11,
            "category": "校服工艺",
            "content": "校服经过预缩处理的主要目的是什么？",
            "options": [
                "A. 改变面料颜色",
                "B. 降低面料成本",
                "C. 预先消除面料的大部分缩水，确保成品洗后符合尺寸要求",
                "D. 增加面料厚度"
            ],
            "correct": 2,
            "standard": "GB/T 7573-2025",
            "explanation": "预缩处理（蒸汽处理或水洗处理）可以释放面料的内部应力，预先消除大部分缩水。这样最终校服即使经过多次洗涤，也能保持尺寸稳定性。"
        },
        {
            "id": next_id + 12,
            "category": "校服工艺",
            "content": "版师在设计校服纸样时，需要根据面料的哪些性质调整裁剪尺寸？",
            "options": [
                "A. 只需考虑面料克重",
                "B. 需要考虑面料纤维成分、缩水率和伸缩性",
                "C. 只需考虑面料颜色",
                "D. 只需考虑面料价格"
            ],
            "correct": 1,
            "standard": "GB/T 7573-2025",
            "explanation": "版师需要根据：①纤维成分（棉、涤纶特性不同）、②缩水率（需要增加裁剪余量）、③面料伸缩性等调整纸样，确保成衣质量符合标准。"
        },
        {
            "id": next_id + 13,
            "category": "校服工艺",
            "content": "品质部在验收校服面料时，主要检查项目包括哪些？（多选中选择最重要的3项）",
            "options": [
                "A. 纤维含量、克重、色牢度、缩水率、起球性、强力",
                "B. 只检查颜色是否满意",
                "C. 只检查价格是否符合预算",
                "D. 只检查面料是否厚"
            ],
            "correct": 0,
            "standard": "GB/T 31888-2015",
            "explanation": "品质部需要按照GB/T 31888、GB/T 3917.3、GB/T 7573、GB/T 4802等标准检验进厂面料，确保纤维含量、克重、色牢度、缩水率、起球性、拉伸强力等关键指标符合要求。"
        },
        # ===== 检测方法标准基础 =====
        {
            "id": next_id + 14,
            "category": "检测方法",
            "content": "GB/T 5453《纺织品 织物断裂强力和断裂伸长率的测定 条样法》的主要目的是什么？",
            "options": [
                "A. 检测面料的颜色",
                "B. 测定面料的拉伸强度和延伸性能",
                "C. 检测面料的厚度",
                "D. 检测面料的价格"
            ],
            "correct": 1,
            "standard": "GB/T 5453-2025",
            "explanation": "这个标准规定了测定织物强度和伸长率的方法。校服的接缝强力必须≥面料强力的75%，因此需要先通过本标准测定面料的原始强力。"
        },
        {
            "id": next_id + 15,
            "category": "检测方法",
            "content": "在进行色牢度检测时，为什么要用标准贴衬织物？",
            "options": [
                "A. 只是为了增加测试成本",
                "B. 为了观察被测织物脱落的染料对相邻织物的污染程度",
                "C. 为了美化测试样品",
                "D. 没有特殊理由"
            ],
            "correct": 1,
            "standard": "GB/T 3917.3-2025",
            "explanation": "标准贴衬织物用来检测被测织物脱落的染料是否会污染其他衣物（如皮肤、其他衣物接触时）。这是评估色牢度等级的重要方法。"
        },
        {
            "id": next_id + 16,
            "category": "检测方法",
            "content": "GB/T 19980《纺织品 织物有机溶剂干洗后的变化测定 四氯乙烯法》适用于什么情况？",
            "options": [
                "A. 仅用于测试日常家庭洗涤",
                "B. 用于测试干洗对织物的影响",
                "C. 用于测试面料的防水性",
                "D. 用于测试面料的阻燃性"
            ],
            "correct": 1,
            "standard": "GB/T 19980-2025",
            "explanation": "虽然校服通常进行水洗，但某些高端校服可能需要干洗。本标准规定了用四氯乙烯进行干洗前后织物尺寸变化的测定方法。"
        },
        {
            "id": next_id + 17,
            "category": "检测方法",
            "content": "GB/T 5326《纺织品 织物缝线连续撕裂强力的测定 撕裂法》主要检测的是什么？",
            "options": [
                "A. 整块面料的强力",
                "B. 经纬方向面料各自的强力",
                "C. 沿着缝线方向的面料撕裂强力",
                "D. 接缝强力"
            ],
            "correct": 2,
            "standard": "GB/T 5326-2025",
            "explanation": "这个标准规定了测定织物撕裂强力的方法。当面料有缝线或受到局部撕裂力时，用本方法评估面料的抗撕裂性能。"
        },
        {
            "id": next_id + 18,
            "category": "检测方法",
            "content": "为什么GB/T 4802.2《织物耐皮肤摩擦色牢度测定 摩擦法》对校服检验很重要？",
            "options": [
                "A. 测试面料的价格",
                "B. 测试面料与皮肤接触时是否掉色（接触摩擦），防止被衣物污染皮肤",
                "C. 测试面料的透气性",
                "D. 测试面料的厚度"
            ],
            "correct": 1,
            "standard": "GB/T 4802.2-2008",
            "explanation": "校服与皮肤直接接触，需要检测面料的摩擦掉色。特别是深色校服，摩擦掉色过多会污染皮肤和其他衣物，可能含有有害物质。"
        },
        {
            "id": next_id + 19,
            "category": "检测方法",
            "content": "GB/T 31902《纺织品 织物耐汗渍色牢度测定》对校服的检测意义是什么？",
            "options": [
                "A. 测试校服在干燥环境下的表现",
                "B. 测试学生出汗时校服的色牢度，防止汗液溶解的染料伤害皮肤",
                "C. 测试校服的防水性",
                "D. 测试校服的韧性"
            ],
            "correct": 1,
            "standard": "GB/T 31902-2025",
            "explanation": "学生活跃运动会出汗，汗液可能溶解某些染料。本标准测试汗液（酸性和碱性）对校服的影响，确保汗液中的染料不会伤害学生皮肤。"
        },
        {
            "id": next_id + 20,
            "category": "检测方法",
            "content": "GB/T 32612《纺织品 织物及其制品霉菌和细菌抗菌性能的评价》对校服的适用场景是什么？",
            "options": [
                "A. 普通校服不需要进行此项检测",
                "B. 仅用于运动校服和特殊功能性校服的检测",
                "C. 用于测试校服的颜色",
                "D. 用于测试校服的厚度"
            ],
            "correct": 1,
            "standard": "GB/T 32612-2025",
            "explanation": "运动校服和长时间穿着的校服，特别是在温暖潮湿环境下，可能面临霉菌和细菌问题。本标准规定了抗菌性能的评价方法。"
        }
    ]

    # 添加新题目
    for question in new_questions:
        questions.append(question)

    # 更新元数据
    data['metadata']['total_questions'] = len(questions)
    data['metadata']['last_updated'] = "2026-04-13"
    data['metadata']['description'] = "服装行业标准知识测试题库（校服安全、面料知识、检测方法）"

    # 更新categories
    if "校服面料" not in data['metadata']['categories']:
        data['metadata']['categories'].append("校服面料")
    if "校服工艺" not in data['metadata']['categories']:
        data['metadata']['categories'].append("校服工艺")
    if "检测方法" not in data['metadata']['categories']:
        data['metadata']['categories'].append("检测方法")

    # 保存更新后的题库
    with open('questions_db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 成功添加 {len(new_questions)} 道新题目")
    print(f"📊 题库总数现在为：{len(questions)} 道题")
    print(f"\n新增题目分类：")
    print(f"  • 校服面料知识: 10道题 (纤维、特性、性能指标)")
    print(f"  • 校服工艺应用: 5道题 (设计、工艺、版师、品质)")
    print(f"  • 检测方法标准: 5道题 (GB/T 5453、3917.3、7573等)")

    return len(new_questions)

if __name__ == "__main__":
    add_fabric_and_testing_questions()
