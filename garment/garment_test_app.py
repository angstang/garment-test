"""
服装行业标准知识测试应用 v2.0
针对儿童产品和校服安全的专业知识评估
支持100道题库，每次随机抽取30道题
"""

import json
import sys
import random
from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional
from enum import Enum
from pathlib import Path


class Department(Enum):
    """部门枚举"""
    DESIGN = "设计部"
    CRAFT = "工艺部"
    PATTERN = "版师部"


@dataclass
class Question:
    """测试题目"""
    id: int
    category: str
    content: str
    options: List[str]
    correct_answer: int
    standard: str  # 涉及的标准
    explanation: str  # 解释


class GarmentTestApp:
    """服装行业标准测试应用"""

    def __init__(self):
        self.questions = self._load_questions()
        self.test_questions = []  # 本次测试的题目列表
        self.user_name = ""
        self.user_dept = None
        self.user_answers: Dict[int, int] = {}

    def _load_questions(self) -> List[Question]:
        """从JSON文件加载题库，支持100道题"""
        questions = []
        try:
            # 尝试从questions_db.json加载
            json_path = Path(__file__).parent / 'questions_db.json'
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for q in data.get('questions', []):
                    questions.append(Question(
                        id=q['id'],
                        category=q['category'],
                        content=q['content'],
                        options=q['options'],
                        correct_answer=q['correct'],
                        standard=q['standard'],
                        explanation=q['explanation']
                    ))
            print(f"✅ 已加载{len(questions)}道题库")
        except FileNotFoundError:
            print("⚠️ 未找到questions_db.json，使用内置题库")
            questions = self._get_builtin_questions()

        return questions

    def _get_builtin_questions(self) -> List[Question]:
        """内置题库（备用）"""
        return [
            Question(
                id=1,
                category="儿童产品安全",
                content="FZ/T 73049中，A类产品的甲醛含量限制值是多少？",
                options=["A. ≤75mg/kg", "B. ≤100mg/kg", "C. ≤150mg/kg", "D. ≤200mg/kg"],
                correct_answer=0,
                standard="FZ/T 73049-2018",
                explanation="A类（直接接触皮肤）产品甲醛含量≤75mg/kg，B类≤150mg/kg。"
            ),
            Question(
                id=2,
                category="校服安全",
                content="QB/T 2397规定的校服色牢度最低等级是多少？",
                options=["A. 2级", "B. 3级", "C. 4级", "D. 5级"],
                correct_answer=1,
                standard="QB/T 2397-2019",
                explanation="校服耐皂洗色牢度不应低于3级。"
            ),
        ]

    def display_welcome(self):
        """显示欢迎界面"""
        print("\n" + "=" * 70)
        print("欢迎使用 服装行业标准知识测试系统 v2.0".center(70))
        print("=" * 70)
        print("\n👕 针对儿童产品和校服安全标准的专业知识评估\n")
        print(f"📚 题库规模: {len(self.questions)} 道题")
        print(f"🎲 每次抽取: 30 道题（随机）")
        print(f"⏱️  耗时: 约 15-20 分钟")
        print(f"\n✅ 覆盖标准:")
        print("   • FZ/T 73049-2018  婴幼儿及儿童纺织产品安全规范")
        print("   • QB/T 2397-2019   中小学生校服")
        print("   • GB 18401-2010    国家纺织品基本安全技术规范")
        print("   • GB/T 5296.4      消费品使用说明")
        print()

    def get_user_info(self):
        """获取用户信息"""
        self.user_name = input("请输入姓名: ").strip()
        print("\n请选择所在部门:")
        for i, dept in enumerate(Department, 1):
            print(f"{i}. {dept.value}")

        while True:
            try:
                choice = int(input("请选择 (1-3): "))
                self.user_dept = list(Department)[choice - 1]
                break
            except (ValueError, IndexError):
                print("输入无效，请重新选择。")

    def display_question(self, q: Question, index: int, total: int = None):
        """显示单个题目"""
        if total is None:
            total = len(self.questions)

        # 计算进度百分比
        progress = int((index / total) * 100)
        progress_bar = "█" * (progress // 5) + "░" * (20 - progress // 5)

        print(f"\n{'='*70}")
        print(f"第 {index}/{total} 题  [{progress_bar}] {progress}%")
        print(f"分类: {q.category:15} | 标准: {q.standard}")
        print(f"{'='*70}")
        print(f"\n📋 {q.content}\n")
        for i, option in enumerate(q.options):
            print(f"  {option}")

    def get_user_answer(self) -> int:
        """获取用户答案"""
        while True:
            try:
                answer = input("\n请选择答案 (A/B/C/D): ").strip().upper()
                answer_map = {"A": 0, "B": 1, "C": 2, "D": 3}
                if answer not in answer_map:
                    print("输入无效，请选择 A/B/C/D")
                    continue
                return answer_map[answer]
            except Exception:
                print("输入错误，请重试。")

    def run_test(self):
        """运行测试，随机抽取30道题"""
        self.display_welcome()
        self.get_user_info()

        # 随机抽取30道题
        selected_questions = random.sample(self.questions, min(30, len(self.questions)))

        print(f"\n开始测试，{self.user_name} - {self.user_dept.value}")
        print(f"本次共有 {len(selected_questions)} 道题（从{len(self.questions)}道题库中随机抽取）")
        print("按 Enter 键开始...\n")
        input()

        for i, question in enumerate(selected_questions, 1):
            self.display_question(question, i, len(selected_questions))
            user_answer = self.get_user_answer()
            self.user_answers[question.id] = user_answer

            # 显示答题结果
            is_correct = user_answer == question.correct_answer
            status = "✅ 正确" if is_correct else "❌ 错误"
            print(f"\n{status}")
            print(f"📖 解释: {question.explanation}")

            if not is_correct:
                correct_option = chr(ord('A') + question.correct_answer)
                print(f"正确答案: {correct_option}")

            if i < len(selected_questions):
                input("\n按 Enter 键继续下一题...")

        # 保存本次测试的题目列表用于评分
        self.test_questions = selected_questions

    def calculate_score(self) -> Tuple[int, int, float]:
        """计算成绩"""
        test_questions = getattr(self, 'test_questions', self.questions)
        total = len(test_questions)
        correct = sum(
            1 for q in test_questions
            if q.id in self.user_answers and self.user_answers[q.id] == q.correct_answer
        )
        percentage = (correct / total) * 100 if total > 0 else 0
        return correct, total, percentage

    def generate_report(self):
        """生成测试报告"""
        correct, total, percentage = self.calculate_score()

        print("\n" + "=" * 60)
        print("测试完成！".center(60))
        print("=" * 60)
        print(f"\n姓名: {self.user_name}")
        print(f"部门: {self.user_dept.value}")
        print(f"\n成绩统计:")
        print(f"  正确题数: {correct}/{total}")
        print(f"  得分: {percentage:.1f}%")

        # 根据分数给出评价
        if percentage >= 90:
            rating = "优秀 - 对国标和行业标准掌握很好"
        elif percentage >= 75:
            rating = "良好 - 对国标和行业标准掌握较好"
        elif percentage >= 60:
            rating = "及格 - 需要进一步学习相关标准"
        else:
            rating = "需改进 - 建议参加标准培训课程"

        print(f"\n评价: {rating}")

        # 分类统计
        print(f"\n📊 分类成绩统计:")
        categories = {}
        test_questions = getattr(self, 'test_questions', self.questions)

        for question in test_questions:
            if question.category not in categories:
                categories[question.category] = {"total": 0, "correct": 0}

            categories[question.category]["total"] += 1
            if question.id in self.user_answers and self.user_answers[question.id] == question.correct_answer:
                categories[question.category]["correct"] += 1

        for category, stats in categories.items():
            cat_percentage = (stats["correct"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            print(f"  • {category:15}: {stats['correct']}/{stats['total']:2} ({cat_percentage:5.1f}%)")

        print("\n" + "=" * 60)

    def save_report(self):
        """保存测试报告到文件"""
        correct, total, percentage = self.calculate_score()

        report_data = {
            "user_name": self.user_name,
            "department": self.user_dept.value,
            "total_questions": total,
            "correct_answers": correct,
            "score_percentage": percentage,
            "answers": self.user_answers,
        }

        filename = f"report_{self.user_name}_{self.user_dept.value}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)

        print(f"\n报告已保存: {filename}")


def main():
    """主程序"""
    try:
        app = GarmentTestApp()
        app.run_test()
        app.generate_report()

        save = input("\n是否保存测试报告? (y/n): ").strip().lower()
        if save == 'y':
            app.save_report()

        print("\n感谢参加测试！")
    except KeyboardInterrupt:
        print("\n\n测试已取消。")
        sys.exit(0)
    except Exception as e:
        print(f"\n发生错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
