#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
规范化题库数据库键名，从中文转换为英文
"""

import json
from pathlib import Path


def normalize_questions_multi_dept(db_path: str = 'questions_multi_dept.json') -> bool:
    """
    将questions_multi_dept.json中的中文键转换为英文键

    转换映射:
    - 设计师_questions → designer_questions
    - 工艺师_questions → technician_questions
    - 版师_questions → patternmaker_questions
    """

    try:
        with open(db_path, 'r', encoding='utf-8') as f:
            db = json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件未找到: {db_path}")
        return False

    # 键名映射
    key_mapping = {
        '设计师_questions': 'designer_questions',
        '工艺师_questions': 'technician_questions',
        '版师_questions': 'patternmaker_questions',
        '公用题库': 'public_questions'
    }

    # 执行转换
    converted_db = {'metadata': db.get('metadata', {})}

    for old_key, new_key in key_mapping.items():
        if old_key in db:
            converted_db[new_key] = db[old_key]
            print(f"✅ 转换: {old_key} → {new_key} ({len(db[old_key])} 道题目)")
        else:
            # 初始化空数组
            converted_db[new_key] = []

    # 保留其他未映射的键
    for key in db.keys():
        if key not in key_mapping and key != 'metadata':
            converted_db[key] = db[key]
            print(f"⚠️  保留未映射的键: {key}")

    # 保存转换后的数据
    try:
        with open(db_path, 'w', encoding='utf-8') as f:
            json.dump(converted_db, f, ensure_ascii=False, indent=2)

        print(f"\n✅ 题库已规范化，已保存到 {db_path}")

        # 显示最终统计
        print("\n📈 规范化后的题库统计:")
        for key in ['designer_questions', 'technician_questions', 'patternmaker_questions', 'public_questions']:
            if key in converted_db:
                count = len(converted_db[key])
                print(f"  {key}: {count} 道")

        return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False


if __name__ == '__main__':
    normalize_questions_multi_dept()
