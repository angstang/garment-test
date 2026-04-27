#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
女装甲级测试 - 525题导入脚本
将markdown格式的525道女装考试题目导入到题库
分配模式: Scheme B (混合分配) - 所有部门可访问所有题目
"""

import json
import re
from pathlib import Path
from typing import List, Dict


# 工作项目到分类的映射
WORKITEM_CATEGORY_MAP = {
    '01': '业界知识',
    '02': '工具使用',
    '03': '身体量测',
    '04': '设计',
    '05': '素材',
    '06': '制衣样衣试穿',
    '07': '缝制'
}


def parse_markdown_questions(file_path: str) -> List[Dict]:
    """
    解析markdown格式的考试题目文件

    预期格式:
    ## 工作项目01: 业界知识 (78题)

    1. (权重) 题目内容
    A. 选项A
    B. 选项B
    C. 选项C
    D. 选项D
    答: A
    解: 详细解释
    """

    questions = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ 文件未找到: {file_path}")
        return questions

    # 按工作项目分割
    workitem_pattern = r'## 工作项目(\d+)[:\s]+(.+?)\((\d+)题?\)'
    workitems = re.finditer(workitem_pattern, content)

    workitem_sections = []

    for match in workitems:
        workitem_id = match.group(1)
        workitem_name = match.group(2).strip()
        expected_count = int(match.group(3))
        section_start = match.end()
        workitem_sections.append({
            'id': workitem_id,
            'name': workitem_name,
            'expected_count': expected_count,
            'start': section_start
        })

    # 为每个工作项目设置结束位置
    for i, section in enumerate(workitem_sections):
        if i + 1 < len(workitem_sections):
            # 使用下一个section的start作为当前section的end
            section['end'] = workitem_sections[i + 1]['start']
        else:
            section['end'] = len(content)

    # 解析每个工作项目的题目
    for section in workitem_sections:
        workitem_content = content[section['start']:section['end']]
        section_questions = parse_workitem_section(
            workitem_content,
            section['id'],
            section['name']
        )
        questions.extend(section_questions)

        expected = section['expected_count']
        actual = len(section_questions)
        if actual != expected:
            print(f"⚠️  工作项目{section['id']}: 期望{expected}题, 实际解析{actual}题")

    return questions


def parse_workitem_section(content: str, workitem_id: str, workitem_name: str) -> List[Dict]:
    """
    解析单个工作项目的题目
    使用行级处理，更容易处理各种格式变化
    """
    questions = []
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 检查是否是题目开头 (数字. (权重) 内容)
        if not re.match(r'^\d+\.\s*\(', line):
            i += 1
            continue

        # 提取题号和题目文本
        header_match = re.match(r'(\d+)\.\s*\(([^)]*)\)\s*(.*)', line)
        if not header_match:
            i += 1
            continue

        question_text = header_match.group(3).strip()
        i += 1

        # 收集完整的题目文本 (直到遇到选项)
        while i < len(lines) and not re.match(r'^[A-D]\.\s*', lines[i].strip()):
            if lines[i].strip():
                question_text += ' ' + lines[i].strip()
            i += 1

        # 提取选项
        options = []
        while i < len(lines) and len(options) < 4:
            opt_line = lines[i].strip()
            opt_match = re.match(r'^([A-D])\.\s*(.*)', opt_line)

            if opt_match:
                letter = opt_match.group(1)
                text = opt_match.group(2).strip()
                options.append(f"{letter}. {text}")
                i += 1
            else:
                break

        if len(options) != 4:
            continue  # 选项不完整，跳过

        # 提取答案
        correct_index = 0
        answer_found = False
        for j in range(i, min(i + 5, len(lines))):
            ans_line = lines[j].strip()
            answer_match = re.match(r'^答[:\s]*([A-D]|[1-4])', ans_line)

            if answer_match:
                answer_str = answer_match.group(1).strip()
                correct_index = convert_answer_to_index(answer_str)
                answer_found = True
                i = j + 1
                break

        if not answer_found:
            continue

        # 提取解释
        explanation = "无"
        for j in range(i, min(i + 5, len(lines))):
            expl_line = lines[j].strip()
            expl_match = re.match(r'^解[:\s]*(.*)', expl_line)

            if expl_match:
                explanation = expl_match.group(1).strip()
                i = j + 1
                break

        # 创建题目对象
        question = {
            "category": workitem_name,
            "content": clean_question_text(question_text),
            "options": options,
            "correct": correct_index,
            "standard": f"女装甲级考试-{workitem_id}",
            "explanation": explanation[:500]
        }

        questions.append(question)

    return questions


def convert_answer_to_index(answer: str) -> int:
    """将答案(A-D或1-4)转换为索引(0-3)"""
    mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, '1': 0, '2': 1, '3': 2, '4': 3}
    return mapping.get(answer.upper(), 0)


def clean_question_text(text: str) -> str:
    """清理题目文本"""
    # 移除图片引用
    text = re.sub(r'!\[.+?\]\(.+?\)', '', text)
    # 移除多余空白
    text = ' '.join(text.split())
    return text


def integrate_questions(questions: List[Dict], db_path: str = 'questions_multi_dept.json'):
    """
    将题目集成到题库
    使用Scheme B: 所有题目分配到所有部门
    """

    # 加载现有题库
    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except FileNotFoundError:
        print(f"❌ 题库文件未找到: {db_path}")
        return False

    # 获取当前最大ID
    max_id = get_max_question_id(db)
    current_id = max_id + 1

    # 为每道题分配ID并添加到所有部门
    dept_keys = ['designer_questions', 'technician_questions', 'patternmaker_questions']

    for dept_key in dept_keys:
        if dept_key not in db:
            db[dept_key] = []

    added_count = 0
    for question in questions:
        question['id'] = current_id

        # 将题目复制到所有部门 (Scheme B: 混合分配)
        for dept_key in dept_keys:
            db[dept_key].append(question.copy())

        current_id += 1
        added_count += 1

    # 更新元数据
    db['metadata']['last_updated'] = '2026-04-26'
    db['metadata']['notes'] = f'已集成女装甲级测试 - {added_count}道题目 (Scheme B: 所有部门通用)'

    # 保存更新的题库
    try:
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False


def get_max_question_id(db: Dict) -> int:
    """获取题库中的最大ID"""
    max_id = 0

    all_keys = [k for k in db.keys() if k != 'metadata' and isinstance(db[k], list)]

    for key in all_keys:
        for question in db[key]:
            if 'id' in question:
                max_id = max(max_id, question['id'])

    return max_id


def generate_statistics(questions: List[Dict]) -> None:
    """生成导入统计"""
    print("\n" + "="*50)
    print("📊 女装甲级测试 - 题目导入统计")
    print("="*50)

    # 按分类统计
    category_counts = {}
    for q in questions:
        cat = q.get('category', '未分类')
        category_counts[cat] = category_counts.get(cat, 0) + 1

    print(f"\n✅ 成功解析 {len(questions)} 道题目\n")
    print("按工作项目分类统计:")
    for cat in sorted(category_counts.keys()):
        count = category_counts[cat]
        print(f"  {cat}: {count} 道")

    print("\n📌 分配方案: Scheme B (混合分配)")
    print("  - 所有 {0} 道题目将分配到:".format(len(questions)))
    print("    ✓ 设计师题库")
    print("    ✓ 工艺师题库")
    print("    ✓ 版师题库")
    print("  - 每个部门都可访问完整的 {0} 道题目".format(len(questions)))

    print("\n" + "="*50)


def main():
    """主函数"""
    import sys

    # 从命令行参数获取markdown文件路径
    if len(sys.argv) > 1:
        md_file = sys.argv[1]
    else:
        # 尝试自动查找
        possible_files = [
            '女装甲级测试.md',
            '女装甲級測試.md',
            'garment_exam_525.md',
            'exam_525.md'
        ]

        md_file = None
        for fname in possible_files:
            if Path(fname).exists():
                md_file = fname
                break

        if not md_file:
            print("❌ 使用方法: python3 import_525_questions.py <markdown_file>")
            print("\n或将markdown文件放在以下位置之一:")
            for fname in possible_files:
                print(f"  - {fname}")
            return

    print(f"📖 开始解析: {md_file}")

    # 解析题目
    questions = parse_markdown_questions(md_file)

    if not questions:
        print("❌ 无法解析题目, 请检查markdown文件格式")
        return

    # 生成统计
    generate_statistics(questions)

    # 集成到题库
    print("\n💾 正在集成到题库...")
    if integrate_questions(questions):
        print("✅ 成功集成!")

        # 显示数据库最终状态
        with open('questions_multi_dept.json', 'r', encoding='utf-8') as f:
            db = json.load(f)

        print("\n📈 题库最终状态:")
        for key in ['public_questions', 'designer_questions', 'technician_questions', 'patternmaker_questions']:
            if key in db:
                key_display = key.replace('_questions', '')
                count = len(db[key])
                print(f"  {key_display}: {count} 道")

        total = sum(len(db[k]) for k in db.keys() if k != 'metadata' and isinstance(db[k], list))
        print(f"  总计: {total} 道")
    else:
        print("❌ 集成失败")


if __name__ == '__main__':
    main()
