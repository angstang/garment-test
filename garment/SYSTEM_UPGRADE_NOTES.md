# 新益服装知识测试系统 v4.0 - 多岗位版本

## 🎉 主要升级内容

### 1. **新增多岗位题库系统**
- ✅ **公用题库**：所有岗位员工通用（3道题）
- ✅ **设计师专属题库**：服装设计基础、结构设计、风格流派、市场营销（20道题）
- ✅ **工艺师专属题库**：面料知识、工艺技术、质量检测（10道题）
- ✅ **版师专属题库**：版型设计、纸样制作、放码技巧（10道题）

### 2. **智能题目混合机制**
系统会根据选择的岗位，自动混合：
- **固定加载**：公用题库中的所有题目
- **动态加载**：相应岗位的专属题库

例如：设计师会获得 = 公用题库(3道) + 设计师专属(27道随机)

### 3. **更新的文件结构**

```
/代码/
├── garment_test_v2.html           # 主应用文件（已更新）
├── questions_multi_dept.json      # 新的多岗位题库文件 ⭐
├── questions_db.json              # 保留的原始题库（备用）
└── SYSTEM_UPGRADE_NOTES.md        # 本文件
```

## 📋 岗位映射关系

| 选择的部门 | 使用的题库 | 题目来源 |
|-----------|----------|--------|
| 设计部 | 公用 + 设计师专属 | public_questions + designer_questions |
| 工艺部 | 公用 + 工艺师专属 | public_questions + technician_questions |
| 版师部 | 公用 + 版师专属 | public_questions + patternmaker_questions |
| 品质部 | 公用 + 工艺师专属 | public_questions + technician_questions |
| 管理层 | 仅公用 | public_questions |
| 其他 | 仅公用 | public_questions |

## 🔄 用户流程

1. **开始测试** - 点击"开始测试"按钮
2. **加载屏幕** - 系统加载题库（通常<1秒）
3. **填写信息** - 输入姓名和选择部门 ⭐ **关键步骤**
4. **智能题库混合** - 系统根据部门选择题库 ⭐ **新增功能**
5. **开始答题** - 随机抽取30道题目
6. **查看结果** - 显示成绩和分类评分

## 💾 新增的JSON结构

`questions_multi_dept.json` 包含以下顶级字段：

```json
{
  "metadata": { /* 系统元数据 */ },
  "public_questions": [ /* 公用题库 */ ],
  "designer_questions": [ /* 设计师专属 */ ],
  "technician_questions": [ /* 工艺师专属 */ ],
  "patternmaker_questions": [ /* 版师专属 */ ]
}
```

每个题目包含：
- `id`: 题目ID
- `category`: 题目分类
- `content`: 题目内容
- `options`: 4个选项 (A/B/C/D)
- `correct`: 正确答案索引 (0-3)
- `standard`: 对应的技术标准
- `explanation`: 答案解释

## 🔧 JavaScript主要改动

### 1. 新增状态字段
```javascript
appState.allDeptQuestions = {} // 存储各部门的题库
```

### 2. 更新的函数

**loadAllQuestions()** - 加载多部门题库
- 优先加载 `questions_multi_dept.json`
- 失败时回退到 `questions_db.json`

**selectRandomQuestions(count = 30)** - 智能混合题库
- 始终包含公用题库
- 根据 appState.department 添加对应的专属题库
- 随机打乱后抽取30道

**submitInfo(event)** - 在提交信息时抽取题目
- 确保在用户选择部门后执行
- 根据部门准确混合题库

### 3. 部门映射表
```javascript
const deptMap = {
  '设计部': 'designer',
  '工艺部': 'technician',
  '版师部': 'patternmaker',
  '品质部': 'technician',
  '管理层': null,
  '其他': null
};
```

## 📊 题库统计

| 类型 | 题目数 |
|------|-------|
| 公用题库 | 3道 |
| 设计师专属 | 20道 |
| 工艺师专属 | 10道 |
| 版师专属 | 10道 |
| **总计** | **43道** |

*注：建议扩展各题库的规模，目前内容较为精简*

## 🚀 如何使用新系统

### 本地测试
1. 确保 `garment_test_v2.html` 和 `questions_multi_dept.json` 在同一目录
2. 用浏览器打开 HTML 文件
3. 选择不同的部门测试题库加载

### 扩展题库
编辑 `questions_multi_dept.json`，在相应的数组中添加题目：

```json
{
  "id": 999,
  "category": "新分类",
  "content": "题目内容...",
  "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
  "correct": 0,
  "standard": "GB/T XXXX",
  "explanation": "解释..."
}
```

### 自定义部门映射
修改 `selectRandomQuestions()` 中的 `deptMap` 对象：

```javascript
const deptMap = {
  '你的部门名': '对应的题库key',
  // ...
};
```

## ⚠️ 注意事项

1. **题库文件路径**：确保 `questions_multi_dept.json` 与 HTML 文件在同目录
2. **浏览器缓存**：更新题库后可能需要清除浏览器缓存
3. **回退机制**：如果新题库加载失败，系统会自动回退到旧的 `questions_db.json`
4. **编码格式**：JSON 文件必须使用 UTF-8 编码

## 📈 后续改进建议

- [ ] 扩展各部门题库，至少100道题/岗位
- [ ] 添加权重算法，调整公用题库和专属题库的比例
- [ ] 实现题库版本控制，支持多套标准题库
- [ ] 添加导师管理后台，支持动态修改题库
- [ ] 实现成绩数据库，记录历史成绩
- [ ] 添加按标准筛选功能（GB/T XXXX）

## 📞 技术支持

如有问题或建议，请检查：
1. 浏览器控制台是否有错误信息
2. JSON 文件格式是否正确（可用在线JSON验证器）
3. 部门名称是否与代码中的映射表一致

---

**系统版本**：v4.0  
**更新日期**：2026-04-13  
**兼容性**：Chrome/Firefox/Safari/Edge 最新版本
