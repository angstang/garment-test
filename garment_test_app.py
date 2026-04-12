"""
服装行业标准知识测试应用
针对内部设计、工艺、版师对国标及行业标准的了解程度进行评估
"""

import json
import sys
from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum


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
        self.user_name = ""
        self.user_dept = None
        self.user_answers: Dict[int, int] = {}

    def _load_questions(self) -> List[Question]:
        """加载测试题目"""
        return [
            # 设计标准题
            Question(
                id=1,
                category="设计",
                content="GB/T 5296.4《消费品使用说明 第4部分：纺织品和服装》规定，标签上应标注哪些基本信息？",
                options=[
                    "A. 仅标注成分和含量",
                    "B. 成分、含量、洗涤方法、规格尺寸等",
                    "C. 仅标注价格和生产日期",
                    "D. 生产地和生产商名称",
                ],
                correct_answer=1,
                standard="GB/T 5296.4-2012",
                explanation="消费品使用说明标准要求标注成分含量、洗涤保养方法、规格尺寸、生产商信息等完整信息。",
            ),
            Question(
                id=2,
                category="设计",
                content="FZ/T 01053《针织T恤衫》标准中，对成品缩率的要求是多少？",
                options=[
                    "A. 长度不超过3%，宽度不超过4%",
                    "B. 长度不超过5%，宽度不超过5%",
                    "C. 长度不超过2%，宽度不超过2%",
                    "D. 无缩率要求",
                ],
                correct_answer=0,
                standard="FZ/T 01053-2019",
                explanation="针织T恤衫标准规定成品缩率：长度方向不超过3%，宽度方向不超过4%。",
            ),
            # 工艺标准题
            Question(
                id=3,
                category="工艺",
                content="GB/T 2918《纺织品 试样的采取和处理方法》中，条件1级是指什么环境？",
                options=[
                    "A. 温度20±2°C，相对湿度50±2%",
                    "B. 温度25±2°C，相对湿度65±2%",
                    "C. 温度15±2°C，相对湿度45±2%",
                    "D. 温度30°C，相对湿度70%",
                ],
                correct_answer=0,
                standard="GB/T 2918-2018",
                explanation="条件1级（标准条件）是温度20±2°C，相对湿度50±2%RH，用于各类纺织品测试。",
            ),
            Question(
                id=4,
                category="工艺",
                content="GB/T 3917.1《纺织品 破裂强度的测定 第1部分 撕裂强度》中，何为'起始撕口'？",
                options=[
                    "A. 布料的最初缺陷",
                    "B. 长度至少15mm，由机器或手工切割的裂口",
                    "C. 布料自然的断裂部位",
                    "D. 印染过程中产生的缺陷",
                ],
                correct_answer=1,
                standard="GB/T 3917.1-2016",
                explanation="起始撕口是测试前在试样上制作的标准缺口，长度至少15mm，用于测定撕裂强度。",
            ),
            # 版师标准题
            Question(
                id=5,
                category="版师",
                content="GB/T 1335.2《服装号型 女装》标准中，女装的号型如何表示？",
                options=[
                    "A. 仅用号（尺寸）表示",
                    "B. 用型（体型代码）和号（尺寸）表示，如165/88A",
                    "C. 仅用胸围表示",
                    "D. 用身高和体重表示",
                ],
                correct_answer=1,
                standard="GB/T 1335.2-2008",
                explanation="女装号型由号（身高）和型（体型）组成，如165表示身高165cm，88表示胸围88cm，A表示体型。",
            ),
            Question(
                id=6,
                category="版师",
                content="GB/T 6390《服装号型 男装》标准中，衣长是指哪两个部位之间的距离？",
                options=[
                    "A. 肩点到袖口",
                    "B. 颈点到衣服下摆",
                    "C. 腋点到衣服下摆",
                    "D. 肩点到衣服下摆",
                ],
                correct_answer=3,
                standard="GB/T 6390-2008",
                explanation="衣长是指从肩点到衣服下摆的距离，是服装长度的重要尺寸标准。",
            ),
            # 通用题
            Question(
                id=7,
                category="通用",
                content="FZ/T 73049《婴幼儿及儿童纺织产品安全技术规范》中，A类和B类产品的定义区别是什么？",
                options=[
                    "A. 根据价格区分",
                    "B. A类：直接与皮肤接触；B类：不直接与皮肤接触",
                    "C. A类用于儿童，B类用于婴幼儿",
                    "D. 根据颜色区分",
                ],
                correct_answer=1,
                standard="FZ/T 73049-2018",
                explanation="A类：直接与皮肤接触的产品；B类：不直接与皮肤接触的产品。A类标准更严格。",
            ),
            Question(
                id=8,
                category="通用",
                content="GB 18401《国家纺织品基本安全技术规范》对甲醛含量的要求是什么？",
                options=[
                    "A. 不限制",
                    "B. A类≤75mg/kg，B类≤300mg/kg，C类≤500mg/kg",
                    "C. 所有类别≤100mg/kg",
                    "D. ≤1000mg/kg",
                ],
                correct_answer=1,
                standard="GB 18401-2010",
                explanation="甲醛含量标准：A类（婴幼儿）≤75mg/kg，B类（直接接触皮肤）≤300mg/kg，C类（其他）≤500mg/kg。",
            ),
        ]

    def display_welcome(self):
        """显示欢迎界面"""
        print("\n" + "=" * 60)
        print("欢迎使用 服装行业标准知识测试系统".center(60))
        print("=" * 60)
        print("\n该系统用于评估员工对国家标准和行业标准的了解程度")
        print("共有 {} 道题目，耗时约 15-20 分钟\n".format(len(self.questions)))

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

    def display_question(self, q: Question, index: int):
        """显示单个题目"""
        print(f"\n{'='*60}")
        print(f"第 {index}/{len(self.questions)} 题")
        print(f"分类: {q.category} | 涉及标准: {q.standard}")
        print(f"{'='*60}")
        print(f"\n{q.content}\n")
        for i, option in enumerate(q.options):
            print(f"{option}")

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
        """运行测试"""
        self.display_welcome()
        self.get_user_info()

        print(f"\n开始测试，{self.user_name} - {self.user_dept.value}")
        print("按 Enter 键开始...\n")
        input()

        for i, question in enumerate(self.questions, 1):
            self.display_question(question, i)
            user_answer = self.get_user_answer()
            self.user_answers[question.id] = user_answer

            # 显示答题结果
            is_correct = user_answer == question.correct_answer
            status = "✓ 正确" if is_correct else "✗ 错误"
            print(f"\n{status}")
            print(f"解释: {question.explanation}")

            if not is_correct:
                correct_option = chr(ord('A') + question.correct_answer)
                print(f"正确答案: {correct_option}")

            if i < len(self.questions):
                input("\n按 Enter 键继续下一题...")

    def calculate_score(self) -> Tuple[int, int, float]:
        """计算成绩"""
        total = len(self.questions)
        correct = sum(
            1 for qid, answer in self.user_answers.items()
            if answer == next(q.correct_answer for q in self.questions if q.id == qid)
        )
        percentage = (correct / total) * 100
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
        print(f"\n分类成绩统计:")
        categories = {}
        for question in self.questions:
            if question.category not in categories:
                categories[question.category] = {"total": 0, "correct": 0}

            categories[question.category]["total"] += 1
            if self.user_answers[question.id] == question.correct_answer:
                categories[question.category]["correct"] += 1

        for category, stats in categories.items():
            cat_percentage = (stats["correct"] / stats["total"]) * 100
            print(f"  {category}: {stats['correct']}/{stats['total']} ({cat_percentage:.1f}%)")

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
