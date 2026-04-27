#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path

def parse_choice_answer(answer_str):
    """将选项字母转换为索引 (0-3)"""
    mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    match = re.search(r'[ABCD]', str(answer_str).strip())
    if match:
        return mapping[match.group()]
    return 0

def parse_file1():
    """解析第一个文件：服装设计师理论考试"""
    questions = []
    
    # 手动输入第一个文件的核心题目
    file1_data = [
        ("1ï¼", "D", "服装艺术", "服装设计的基本概念不包括什么？"),
        ("2ï¼", "B", "经济性要素", "服装设计的基本要素中不包括以下哪项？"),
        ("3ï¼", "A", "形状、色彩、质感、工艺", "服装设计的要素主要包括哪些？"),
    ]
    
    # 这里简化处理，实际应该完整解析
    return questions

def load_and_merge():
    """加载现有题库并合并新题目"""
    # 读取现有题库
    with open('questions_multi_dept.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data

if __name__ == '__main__':
    data = load_and_merge()
    
    # 计算统计信息
    public_count = len(data.get('public_questions', []))
    designer_count = len(data.get('设计师_questions', []))
    crafter_count = len(data.get('工艺师_questions', []))
    pattern_count = len(data.get('版师_questions', []))
    
    print("📊 当前题库统计:")
    print(f"   公用题库: {public_count} 道")
    print(f"   设计师题库: {designer_count} 道")
    print(f"   工艺师题库: {crafter_count} 道")
    print(f"   版师题库: {pattern_count} 道")
    print(f"   总计: {public_count + designer_count + crafter_count + pattern_count} 道")

parse_file1()
