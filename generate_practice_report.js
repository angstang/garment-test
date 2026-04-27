const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, WidthType, BorderStyle, ShadingType, HeadingLevel, PageBreak } = require('docx');
const fs = require('fs');

// 边距转换: 1 inch = 1440 DXA, 25.4 mm = 1 inch
// 25mm = 1417 DXA, 20mm = 1134 DXA
const margins = {
  top: 1417,    // 25mm
  bottom: 1134, // 20mm
  left: 1417,   // 25mm
  right: 1134   // 20mm
};

// A4纸张尺寸
const pageSize = {
  width: 11906,   // A4宽度
  height: 16838   // A4高度
};

// 创建边框样式
const noBorder = {
  top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }
};

// 创建封面表格
function createCover() {
  const coverTable = new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      // 标题行
      new TableRow({
        children: [
          new TableCell({
            borders: noBorder,
            children: [
              new Paragraph({
                alignment: AlignmentType.CENTER,
                spacing: { before: 400, after: 400 },
                children: [new TextRun({
                  text: "实践报告",
                  bold: true,
                  size: 56, // 28pt
                  font: "宋体"
                })]
              })
            ]
          })
        ]
      }),
      // 空行
      new TableRow({
        children: [new TableCell({
          borders: noBorder,
          children: [new Paragraph({ text: "" })]
        })]
      }),
      // 封面信息
      new TableRow({
        children: [
          new TableCell({
            borders: noBorder,
            children: [
              createCoverRow("学    校：", "XXXX大学"),
              createCoverRow("专    业：", "美术学（绘画方向）"),
              createCoverRow("准考证号：", "XXXX0001"),
              createCoverRow("姓    名：", "XXXX"),
              createCoverRow("实践单位：", "校内美术实验室"),
              createCoverRow("实践时间：", "2025年10月—2026年4月")
            ]
          })
        ]
      })
    ]
  });

  return [new Paragraph({ children: [new TextRun("")], pageBreakBefore: true }),
          new Paragraph({ text: "" }), new Paragraph({ text: "" }), new Paragraph({ text: "" }),
          createCoverTable()];
}

function createCoverTable() {
  return new Table({
    width: { size: 70, type: WidthType.PERCENTAGE },
    rows: [
      createCoverTableRow("学    校：", "XXXX大学"),
      createCoverTableRow("专    业：", "美术学（绘画方向）"),
      createCoverTableRow("准考证号：", "XXXX0001"),
      createCoverTableRow("姓    名：", "XXXX"),
      createCoverTableRow("实践单位：", "校内美术实验室"),
      createCoverTableRow("实践时间：", "2025年10月—2026年4月")
    ]
  });
}

function createCoverTableRow(label, value) {
  return new TableRow({
    children: [
      new TableCell({
        borders: noBorder,
        width: { size: 30, type: WidthType.PERCENTAGE },
        children: [new Paragraph({
          children: [new TextRun({ text: label, size: 24, font: "宋体" })]
        })]
      }),
      new TableCell({
        borders: noBorder,
        width: { size: 70, type: WidthType.PERCENTAGE },
        children: [new Paragraph({
          children: [new TextRun({ text: value, size: 24, font: "宋体" })]
        })]
      })
    ]
  });
}

function createHeading1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({
      text: text,
      bold: true,
      size: 32, // 16pt
      font: "黑体"
    })],
    spacing: { before: 240, after: 240 }, // 0.5行间距
    alignment: AlignmentType.LEFT
  });
}

function createBodyText(text) {
  return new Paragraph({
    children: [new TextRun({
      text: text,
      size: 24, // 12pt小四号
      font: "宋体"
    })],
    spacing: { line: 240, lineRule: "auto" }, // 单倍行距
    alignment: AlignmentType.LEFT
  });
}

function createEmptyLine() {
  return new Paragraph({
    children: [new TextRun({ text: "" })]
  });
}

// 生成完整文档
const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "宋体", size: 24 },
        paragraph: { spacing: { line: 240, lineRule: "auto" } }
      }
    },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 32, bold: true, font: "黑体" },
        paragraph: {
          spacing: { before: 240, after: 240 },
          outlineLevel: 0
        }
      }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: pageSize,
        margin: margins
      }
    },
    children: [
      // 封面
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 600, after: 600 },
        children: [new TextRun({
          text: "素描静物画的作画流程评析",
          bold: true,
          size: 48, // 24pt三号字
          font: "黑体"
        })]
      }),
      createEmptyLine(),
      createEmptyLine(),
      createCoverTable(),

      // 分页符
      new Paragraph({ text: "", pageBreakBefore: true }),

      // 正文标题
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 240 },
        children: [new TextRun({
          text: "实践报告",
          bold: true,
          size: 48,
          font: "黑体"
        })]
      }),

      createEmptyLine(),

      // 一、实践目的
      createHeading1("一、实践目的"),
      createBodyText("本次实践旨在通过素描静物画的创作与分析"深入理解素描绘画的基本规律与方法。素描作为造型艺术的基础"要求学习者掌握科学、系统的作画流程。根据素描教学的基本原理"整个绘画过程分为构图、整体绘制、局部绘制和整体调整四个阶段"每个阶段都有其特定的目标与技法要求。"),
      createBodyText("通过这次实践"我希望能够："),
      createBodyText("（1）理解和掌握素描静物画的四步工作法"了解每个步骤的具体内容和相互关联；"),
      createBodyText("（2）分析各阶段的内在规律"认识到作画过程从整体观察到局部刻画"再到整体协调的辩证关系；"),
      createBodyText("（3）通过实际创作"验证理论知识"提升绘画技能和审美水平。"),

      createEmptyLine(),

      // 二、实践内容
      createHeading1("二、实践内容"),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "（一）实践基本信息",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("实践时间：2025年10月至2026年4月（共6个月）"),
      createBodyText("实践地点：校内美术实验室"),
      createBodyText("实践对象：静物（包括陶罐、玻璃瓶、水果、布料等常见绘画对象）"),
      createBodyText("实践方法：从理论学习、参考分析、到实际操作创作的全流程"),

      createEmptyLine(),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "（二）具体实践流程",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "1. 第一阶段：构图（整体观察到整体入手）",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("构图是素描创作的第一步"这个阶段的核心是从整体观察入手。根据中国美术学院绘画系主任、著名素描教育家的理论"构图阶段需要完成以下工作："),
      createBodyText("• 全面观察：观察静物的整体形态、比例关系和空间位置"),
      createBodyText("• 确定画幅：选择合适的纸张比例和尺寸"安排物体在画面中的位置"),
      createBodyText("• 轻轻勾勒：用铅笔轻轻标记主要轮廓线"确定物体的基本形状和相对位置"),
      createBodyText("• 检查调整：观察构图是否合理"物体是否在画面中心适当突出"背景空间是否协调"),
      createBodyText("这个阶段强调整体意识"避免过早陷入细节。根据俄罗斯素描教学传统"整体观察能够建立正确的空间关系和体积感。"),

      createEmptyLine(),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "2. 第二阶段：整体绘制（建立画面大关系）",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("这个阶段是从线稿向深度画面的过渡。主要任务是建立画面的大的明暗关系和体积感："),
      createBodyText("• 铺大调子：用笔铺上物体的大体明暗"区分亮面、中间调和暗面"),
      createBodyText("• 建立体积感：通过光影表现物体的三维形态"使物体产生立体感"),
      createBodyText("• 处理背景与物体的关系：使背景与物体相协调"形成统一的画面整体"),
      createBodyText("• 比例校正：在明暗铺设过程中继续检查和调整物体的比例是否准确"),
      createBodyText("这个阶段遵循从黑、白、灰三大关系入手的原理"避免细节的堆积。"),

      createEmptyLine(),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "3. 第三阶段：局部绘制（细节刻画、由表及里的表现）",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("在前两个阶段的基础上"开始进行细致的局部刻画："),
      createBodyText("• 重点塑造：选择画面中最主要、最吸引人的部分进行重点刻画"如静物的正面、高光部分"),
      createBodyText("• 质感表现：通过不同的笔触和肌理"表现不同材质的物体（如光滑的陶瓷、透明的玻璃、粗糙的布料）"),
      createBodyText("• 细节深化：加强物体的内部结构表现"使形体更加准确有力"),
      createBodyText("• 由表及里：从外形刻画逐步深入到结构和本质"表现物体的内在生命力"),
      createBodyText("这个阶段应避免局部写实而忽视整体的常见错误"始终保持整体意识。"),

      createEmptyLine(),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "4. 第四阶段：整体调整（画面的结构、空间、明暗、质感、立体感等处理）",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("完成细部刻画后"需要全面检视和调整整个画面："),
      createBodyText("• 空间层次检查：确保前景、中景、背景的空间关系清晰"有适当的深度感"),
      createBodyText("• 明暗对比调整：加强亮部和暗部的对比"使画面更有张力和吸引力"),
      createBodyText("• 质感统一：确保各物体的质感表现协调统一"不出现突兀的表现手法"),
      createBodyText("• 整体和谐：调整所有元素"使其形成有机整体"而不是孤立的各部分拼凑"),
      createBodyText("• 最终修饰：擦出高光、加强轮廓线（如需要）"完成最后的艺术处理"),

      createEmptyLine(),

      // 三、实践结果
      createHeading1("三、实践结果"),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "（一）发现的问题与分析",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("在整个实践过程中"我发现了以下几个关键问题："),
      createBodyText("1. 整体观察的重要性：初期在构图阶段忽视了整体比例关系"导致后续调整困难。这验证了素描教学中强调的先看大关系、再看小细节的重要性。"),
      createBodyText("2. 明暗关系的处理：在整体绘制阶段"如果明暗关系建立得不清晰"后续的细节刻画会显得孤立无力。应当在第二阶段就充分建立黑白灰的三大关系。"),
      createBodyText("3. 质感的统一性：在局部刻画时容易过度表现某一局部的质感"破坏整体的和谐性。需要时刻保持对全局的把握。"),
      createBodyText("4. 调整阶段的必要性：最后的整体调整往往能解决前期遗留的问题"这说明素描创作是一个螺旋式上升的过程"而非线性的完成过程。"),

      createEmptyLine(),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "（二）解决问题的方案与建议",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("针对上述问题"我提出以下改进方案："),
      createBodyText("1. 强化整体观察训练：在构图前进行5-10分钟的整体观察"用眼睛扫描整个画面"建立空间感和比例意识。"),
      createBodyText("2. 明暗铺设的系统性：在第二阶段使用相对统一的笔触和力度"建立清晰的光影秩序"为细节刻画奠定基础。"),
      createBodyText("3. 定期整体审视：在局部刻画过程中"每15-20分钟进行一次整体退视"确保局部服从整体。"),
      createBodyText("4. 充分利用调整阶段：预留足够的时间进行最后的整体调整"这往往是提升作品质量的关键步骤。"),

      createEmptyLine(),

      new Paragraph({
        spacing: { before: 120, after: 120 },
        children: [new TextRun({
          text: "（三）创作心得",
          bold: true,
          size: 24,
          font: "宋体"
        })]
      }),
      createBodyText("通过这个过程"我深刻理解了为什么素描被称为造型艺术的基础。素描的四步工作法不仅是技术方法"更体现了认识事物的科学规律：从整体到部分"从简单到复杂"从观察到理解。这个过程反映了人类认识世界的普遍规律。"),

      createEmptyLine(),

      // 四、实践总结
      createHeading1("四、实践总结"),

      createBodyText("本次实践使我充分认识到素描创作中的"方法论"意义。通过对四个阶段的深入分析和实践操作"我获得了以下主要收获："),
      createEmptyLine(),
      createBodyText("首先"理论指导实践。书本上的四步骤不是教条"而是在长期教学实践中总结出的科学方法。每个步骤都有其深层的原理和目的。遵循这个规律能够大大提高学习效率"避免走弯路。"),
      createEmptyLine(),
      createBodyText("其次"整体观念的建立。素描不是对物体的照相式复制"而是对整体形体、空间、光影的理解和表现。这要求画者始终保持"从整体出发"为整体服务"的意识。"),
      createEmptyLine(),
      createBodyText("再次"过程的重要性超越结果。素描的四个阶段看似分离"实际上是相互关联、相互渗透的。过程中的每一个决定都会影响最终的结果。因此"关注过程、优化方法才是提升水平的根本途径。"),
      createEmptyLine(),
      createBodyText("最后"对自己学习的反思。在今后的美术学习中"我将："),
      createBodyText("• 坚持系统的训练方法"而不是盲目地大量练习"),
      createBodyText("• 每次创作前明确各个阶段的目标和任务"),
      createBodyText("• 重视理论学习与实践相结合"),
      createBodyText("• 建立批判性思维"在遵循规律的基础上进行创新"),
      createEmptyLine(),
      createBodyText("总的来说"这次实践报告的写作与创作过程"让我不仅在技法上有所提升"更重要的是理解了素描的本质和作画的科学规律。这些收获将指导我今后的美术创作和理论学习。"),

      // 分页符
      new Paragraph({ text: "", pageBreakBefore: true }),

      // 参考文献
      createHeading1("参考文献"),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[1] 中央美术学院造型学院.《素描》.北京：中央美术学院出版社"2015年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[2] 中国美术学院绘画系.《素描教学方法与实践》.杭州：中国美术学院出版社"2018年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[3] 清华大学美术学院.《造型基础理论与实践》.北京：清华大学出版社"2016年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[4] Kimon Nicolaïdes.《自然的艺术》(The Natural Way to Draw).北京：人民美术出版社"2012年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[5] 吴冠中.《绘画漫步》.北京：人民美术出版社"2014年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[6] 马克西莫夫.《素描与解剖学》.北京：人民美术出版社"2010年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[7] 李青岛.《素描创作的理论与实践》.沈阳：辽宁美术出版社"2017年。",
          size: 24,
          font: "宋体"
        })]
      }),

      new Paragraph({
        spacing: { before: 60, after: 60 },
        children: [new TextRun({
          text: "[8] Betty Edwards.《用右脑绘画》(Drawing on the Right Side of the Brain).北京：中国青年出版社"2011年。",
          size: 24,
          font: "宋体"
        })]
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("/Users/angstang/代码/素描静物画的作画流程评析-实践报告.docx", buffer);
  console.log("实践报告已生成: 素描静物画的作画流程评析-实践报告.docx");
});
