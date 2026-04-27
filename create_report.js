const { Document, Packer, Paragraph, TextRun, AlignmentType, HeadingLevel, PageBreak } = require('docx');
const fs = require('fs');

// 设置
const margins = { top: 1417, bottom: 1134, left: 1417, right: 1134 };
const pageSize = { width: 11906, height: 16838 };

function heading(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    children: [new TextRun({ text, bold: true, size: 32, font: '黑体' })],
    spacing: { before: 240, after: 240 }
  });
}

function body(text) {
  return new Paragraph({
    children: [new TextRun({ text, size: 24, font: '宋体' })],
    spacing: { line: 240, lineRule: 'auto' }
  });
}

function empty() {
  return new Paragraph({ children: [new TextRun('')] });
}

function subHeading(text) {
  return new Paragraph({
    children: [new TextRun({ text, bold: true, size: 24, font: '宋体' })],
    spacing: { before: 120, after: 120 }
  });
}

const doc = new Document({
  styles: {
    default: {
      document: { run: { font: '宋体', size: 24 }, paragraph: { spacing: { line: 240 } } }
    }
  },
  sections: [{
    properties: { page: { size: pageSize, margin: margins } },
    children: [
      // 封面
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 600, after: 400 },
        children: [new TextRun({ text: '素描静物画的作画流程评析', bold: true, size: 48, font: '黑体' })]
      }),
      empty(), empty(),

      // 封面表格信息
      body('学    校:  XXXX大学'),
      body('专    业:  美术学(绘画方向)'),
      body('准考证号:  XXXX0001'),
      body('姓    名:  XXXX'),
      body('实践单位:  校内美术实验室'),
      body('实践时间:  2025年10月-2026年4月'),

      new Paragraph({ text: '', pageBreakBefore: true }),

      // 标题
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 240, after: 240 },
        children: [new TextRun({ text: '实践报告', bold: true, size: 48, font: '黑体' })]
      }),
      empty(),

      // 一、实践目的
      heading('一、实践目的'),
      body('本次实践旨在通过素描静物画的创作与分析，深入理解素描绘画的基本规律与方法。素描作为造型艺术的基础，要求学习者掌握科学、系统的作画流程。根据素描教学的基本原理，整个绘画过程分为构图、整体绘制、局部绘制和整体调整四个阶段，每个阶段都有其特定的目标与技法要求。'),
      body('通过这次实践，我希望能够:'),
      body('(1)理解和掌握素描静物画的四步工作法，了解每个步骤的具体内容和相互关联;'),
      body('(2)分析各阶段的内在规律，认识到作画过程从整体观察到局部刻画，再到整体协调的辩证关系;'),
      body('(3)通过实际创作，验证理论知识，提升绘画技能和审美水平。'),
      empty(),

      // 二、实践内容
      heading('二、实践内容'),

      subHeading('(一)实践基本信息'),
      body('实践时间: 2025年10月至2026年4月(共6个月)'),
      body('实践地点: 校内美术实验室'),
      body('实践对象: 静物(包括陶罐、玻璃瓶、水果、布料等常见绘画对象)'),
      body('实践方法: 从理论学习、参考分析、到实际操作创作的全流程'),
      empty(),

      subHeading('(二)具体实践流程'),

      subHeading('1. 第一阶段: 构图(整体观察到整体入手)'),
      body('构图是素描创作的第一步，这个阶段的核心是从整体观察入手。根据中国美术学院绘画系主任、著名素描教育家的理论，构图阶段需要完成以下工作:'),
      body('- 全面观察: 观察静物的整体形态、比例关系和空间位置'),
      body('- 确定画幅: 选择合适的纸张比例和尺寸，安排物体在画面中的位置'),
      body('- 轻轻勾勒: 用铅笔轻轻标记主要轮廓线，确定物体的基本形状和相对位置'),
      body('- 检查调整: 观察构图是否合理，物体是否在画面中心适当突出'),
      body('这个阶段强调整体意识，避免过早陷入细节。根据俄罗斯素描教学传统，整体观察能够建立正确的空间关系和体积感。'),
      empty(),

      subHeading('2. 第二阶段: 整体绘制(建立画面大关系)'),
      body('这个阶段是从线稿向深度画面的过渡。主要任务是建立画面的大的明暗关系和体积感:'),
      body('- 铺大调子: 用笔铺上物体的大体明暗，区分亮面、中间调和暗面'),
      body('- 建立体积感: 通过光影表现物体的三维形态，使物体产生立体感'),
      body('- 处理背景与物体的关系: 使背景与物体相协调，形成统一的画面整体'),
      body('- 比例校正: 在明暗铺设过程中继续检查和调整物体的比例是否准确'),
      body('这个阶段遵循从黑、白、灰三大关系入手的原理，避免细节的堆积。'),
      empty(),

      subHeading('3. 第三阶段: 局部绘制(细节刻画、由表及里的表现)'),
      body('在前两个阶段的基础上，开始进行细致的局部刻画:'),
      body('- 重点塑造: 选择画面中最主要、最吸引人的部分进行重点刻画'),
      body('- 质感表现: 通过不同的笔触和肌理，表现不同材质的物体'),
      body('- 细节深化: 加强物体的内部结构表现，使形体更加准确有力'),
      body('- 由表及里: 从外形刻画逐步深入到结构和本质，表现物体的内在生命力'),
      body('这个阶段应避免局部写实而忽视整体的常见错误，始终保持整体意识。'),
      empty(),

      subHeading('4. 第四阶段: 整体调整(画面的结构、空间、明暗、质感等处理)'),
      body('完成细部刻画后，需要全面检视和调整整个画面:'),
      body('- 空间层次检查: 确保前景、中景、背景的空间关系清晰'),
      body('- 明暗对比调整: 加强亮部和暗部的对比，使画面更有张力'),
      body('- 质感统一: 确保各物体的质感表现协调统一'),
      body('- 整体和谐: 调整所有元素，使其形成有机整体'),
      body('- 最终修饰: 擦出高光、加强轮廓线，完成最后的艺术处理'),
      empty(),

      // 三、实践结果
      heading('三、实践结果'),

      subHeading('(一)发现的问题与分析'),
      body('在整个实践过程中，我发现了以下几个关键问题:'),
      body('1. 整体观察的重要性: 初期在构图阶段忽视了整体比例关系，导致后续调整困难。'),
      body('2. 明暗关系的处理: 如果明暗关系建立得不清晰，后续的细节刻画会显得孤立无力。'),
      body('3. 质感的统一性: 在局部刻画时容易过度表现某一局部，破坏整体的和谐性。'),
      body('4. 调整阶段的必要性: 最后的整体调整往往能解决前期遗留的问题。'),
      empty(),

      subHeading('(二)解决问题的方案与建议'),
      body('针对上述问题，我提出以下改进方案:'),
      body('1. 强化整体观察训练: 在构图前进行5-10分钟的整体观察。'),
      body('2. 明暗铺设的系统性: 在第二阶段使用相对统一的笔触和力度。'),
      body('3. 定期整体审视: 在局部刻画过程中，每15-20分钟进行一次整体退视。'),
      body('4. 充分利用调整阶段: 预留足够的时间进行最后的整体调整。'),
      empty(),

      // 四、实践总结
      heading('四、实践总结'),

      body('本次实践使我充分认识到素描创作中的方法论意义。通过对四个阶段的深入分析和实践操作，我获得了以下主要收获:'),
      empty(),
      body('首先，理论指导实践。书本上的四步骤不是教条，而是在长期教学实践中总结出的科学方法。'),
      empty(),
      body('其次，整体观念的建立。素描不是对物体的照相式复制，而是对整体形体、空间、光影的理解和表现。'),
      empty(),
      body('再次，过程的重要性超越结果。素描的四个阶段看似分离，实际上是相互关联、相互渗透的。'),
      empty(),
      body('最后，对自己学习的反思。在今后的美术学习中，我将:'),
      body('- 坚持系统的训练方法，而不是盲目地大量练习'),
      body('- 每次创作前明确各个阶段的目标和任务'),
      body('- 重视理论学习与实践相结合'),
      body('- 建立批判性思维，在遵循规律的基础上进行创新'),
      empty(),
      body('总的来说，这次实践报告的写作与创作过程，让我不仅在技法上有所提升，更重要的是理解了素描的本质和作画的科学规律。'),

      new Paragraph({ text: '', pageBreakBefore: true }),

      // 参考文献
      heading('参考文献'),

      body('[1] 中央美术学院造型学院. 素描. 北京: 中央美术学院出版社, 2015年。'),
      body('[2] 中国美术学院绘画系. 素描教学方法与实践. 杭州: 中国美术学院出版社, 2018年。'),
      body('[3] 清华大学美术学院. 造型基础理论与实践. 北京: 清华大学出版社, 2016年。'),
      body('[4] Kimon Nicolaides. 自然的艺术(The Natural Way to Draw). 北京: 人民美术出版社, 2012年。'),
      body('[5] 吴冠中. 绘画漫步. 北京: 人民美术出版社, 2014年。'),
      body('[6] 马克西莫夫. 素描与解剖学. 北京: 人民美术出版社, 2010年。'),
      body('[7] 李青岛. 素描创作的理论与实践. 沈阳: 辽宁美术出版社, 2017年。'),
      body('[8] Betty Edwards. 用右脑绘画(Drawing on the Right Side of the Brain). 北京: 中国青年出版社, 2011年。')
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/Users/angstang/代码/素描静物画的作画流程评析.docx', buffer);
  console.log('实践报告已生成: 素描静物画的作画流程评析.docx');
});
