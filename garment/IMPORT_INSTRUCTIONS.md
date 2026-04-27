# 导入525道题库 - 操作指南

## 当前状态

✅ **系统已准备完毕，可以导入525道题库**

- 导入脚本: `import_525_questions.py`
- 规范化脚本: `normalize_database.py`
- 题库文件: `questions_multi_dept.json` (支持多部门题库)
- 测试文件: `sample_questions_test.md` (6题示例)

## 导入步骤 (三步完成)

### 步骤1: 准备Markdown文件

将包含525道题目的markdown文件放在 `/Users/angstang/代码/garment/` 目录，命名为以下任意一种：
- `女装甲级测试.md` ⭐ 推荐
- `garment_exam_525.md`
- `女装甲級測試.md`
- `exam_525.md`

### 步骤2: 运行导入脚本

在 `/Users/angstang/代码/garment/` 目录执行：

```bash
cd /Users/angstang/代码/garment
python3 import_525_questions.py 女装甲级测试.md
```

或不指定文件（脚本会自动查找）：

```bash
python3 import_525_questions.py
```

### 步骤3: 验证导入

导入完成后，可以看到统计信息：

```
✅ 成功解析 525 道题目
  业界知识: 78 道
  工具使用: 60 道
  身体量测: 31 道
  设计: 86 道
  素材: 174 道
  制衣样衣试穿: 64 道
  缝制: 32 道

📈 题库最终状态:
  designer: 525+ 道
  technician: 525+ 道
  patternmaker: 525+ 道
```

## Markdown文件格式

### 完整示例结构

```markdown
# 女装甲级测试

## 工作项目01: 业界知识 (78题)

1. (易) 服装行业的基本特征是什么？
A. 生产成本高
B. 技术要求低
C. 与人体密切相关
D. 市场需求稳定
答: C
解: 服装行业与人体密切相关，需要充分考虑穿着者的身体特征和需求。

2. (中) 下一题...
A. 选项A
B. 选项B
C. 选项C
D. 选项D
答: A
解: 解释文本...

## 工作项目02: 工具使用 (60题)

1. (易) ...
...
```

### 关键要点

- **工作项目标题**: `## 工作项目XX: 名称 (题数)`
  - 例如: `## 工作项目05: 素材 (174题)`

- **题号**: `数字. (难度) 题目文本`
  - 例如: `1. (易) 题目内容`
  - 难度可选，支持: 易、中、难

- **选项**: 按顺序，每行一个
  ```
  A. 选项内容
  B. 选项内容
  C. 选项内容
  D. 选项内容
  ```

- **答案**: `答: A` 或 `答: 1` (支持字母或数字)

- **解释**: `解: 详细解释文本`

## 数据库结构

导入后生成的 `questions_multi_dept.json` 结构：

```json
{
  "metadata": {
    "version": "2.0",
    "total_questions": 525,
    "last_updated": "2026-04-28",
    "description": "女装甲级测试题库"
  },
  "designer_questions": [...],      // 设计师题库
  "technician_questions": [...],    // 工艺师题库
  "patternmaker_questions": [...],  // 版师题库
  "public_questions": [...]         // 公用题库 (可选)
}
```

## 网站测试

导入完成后，访问:
- 本地: `http://localhost:8000/garment_test_v2.html`
- GitHub Pages: `https://angstang.github.io/garment-test/garment_test_v2.html`

应该能看到:
- ✅ 题目数量显著增加
- ✅ 随机出题功能正常
- ✅ 所有部门都能访问完整题库

## 故障排除

### Q: 导入后网页还是加载旧题库？
A: 
1. 清除浏览器缓存 (Ctrl+Shift+Delete)
2. 强制刷新 (Ctrl+Shift+R)
3. 检查DevTools Console是否有错误

### Q: 题目数量不对？
A: 检查markdown格式：
- 每道题是否有完整的A/B/C/D四个选项
- 答案标记是否正确 (`答: A` 或 `答: 1`)
- 是否有多余空白行干扰解析

### Q: 如何重新导入（覆盖现有数据）？
A: 
```bash
# 删除旧数据库
rm questions_multi_dept.json

# 重新运行导入
python3 import_525_questions.py 女装甲级测试.md
```

### Q: 如何只保留某些工作项目？
A: 修改markdown文件，只保留需要的工作项目段落，脚本会自动处理。

## 性能优化

网站已实现以下优化：

✅ **懒加载**: 题库仅在用户点击"开始测试"时加载  
✅ **随机化**: 使用Fisher-Yates算法进行真正的随机出题  
✅ **多部门支持**: 自动为所有部门分配题库  
✅ **路径自适应**: 支持从root或/garment/访问  

## 快速命令参考

```bash
# 进入garment目录
cd /Users/angstang/代码/garment

# 导入题库
python3 import_525_questions.py

# 规范化数据库键名 (仅在需要时)
python3 normalize_database.py

# 查看题库统计
python3 -c "
import json
with open('questions_multi_dept.json') as f:
    data = json.load(f)
for key in data:
    if key != 'metadata' and isinstance(data[key], list):
        print(f'{key}: {len(data[key])} 道')
"

# 启动本地服务
python3 -m http.server 8000
```

## 下一步

1. ✅ 准备525道题目的markdown文件
2. ✅ 运行导入脚本
3. ✅ 本地测试验证
4. ✅ 同步到GitHub（自动部署）

---

**需要帮助?** 检查markdown文件格式是否符合要求，或查看 `sample_questions_test.md` 了解正确格式。
