# 新益服装知识测试系统 v4.1

> 🎯 多岗位智能答题系统 + 飞书自动同步

## 📱 系统概览

一个专为服装行业设计的在线考试系统。

### 核心功能
- ✅ **多岗位题库** - 设计师、工艺师、版师等岗位专属题目
- ✅ **时间限制** - 15分钟/30题，每题30秒倒计时
- ✅ **用户信息收集** - 自动收集答题人员详细信息
- ✅ **飞书自动同步** - 成绩一键导入飞书多维表格
- ✅ **本地数据备份** - 所有数据自动保存到本地存储

## 🚀 快速开始（3步）

### 1️⃣ 打开系统
```
用浏览器打开: garment_test_v2.html
```

### 2️⃣ 完成答题
- 填写个人信息（姓名/部门等）
- 开始15分钟答题（自动倒计时）
- 每题30秒，超时自动跳过

### 3️⃣ 查看成绩
- 系统自动计算成绩
- 数据自动同步到飞书 ✅
- 本地保存备份

## ✅ 飞书Webhook配置状态

**已配置完成！**

```javascript
// config.js
const FEISHU_CONFIG = {
    enabled: true,
    webhookUrl: 'https://ki5kgs18g46.feishu.cn/base/automation/webhook/event/MVGNateX1wsewghhGaPcNobonpd'
};
```

## 📋 文件结构

| 文件 | 说明 |
|------|------|
| `garment_test_v2.html` | 📌 **主应用** - 打开此文件即可使用 |
| `config.js` | ⚙️ **配置文件** - 飞书Webhook已配置 |
| `questions_multi_dept.json` | 📚 **题库** - 各岗位题目 |
| `QUICK_START.md` | 🏃 **快速开始** - 测试指南 |
| `FEISHU_INTEGRATION_GUIDE.md` | 🔗 **集成指南** - 深入配置 |
| `CHANGELOG_v4.1.md` | 📝 **更新日志** - 功能列表 |

## ⏱️ 时间设置

- **总时间**：15分钟（自动交卷）
- **每题时间**：30秒（超时自动跳过）
- **显示方式**：右上角实时倒计时
- **可修改**：编辑 `config.js` 中的 `TIME_CONFIG`

## 👤 收集的信息

自动收集并同步到飞书：
- 姓名 ✓
- 工号 ✓
- 部门 ✓
- 联系方式 ✓
- 成绩 ✓
- 答题耗时 ✓
- 是否超时 ✓

## 🎯 现在您可以做什么

1. ✅ 打开 `garment_test_v2.html` 完成答题
2. ✅ 数据自动保存到本地浏览器
3. ✅ 数据自动同步到飞书多维表格
4. ✅ 在飞书中查看和分析所有成绩
5. ✅ 导出成绩报告（JSON/PDF）

## 🧪 测试方法

### 完整流程测试
1. 打开 `garment_test_v2.html`
2. 点击"开始测试"
3. 填写个人信息（测试数据即可）
4. 快速完成答题（可等待自动跳过）
5. 查看成绩，检查：
   - ✅ 本地数据：F12 → Application → Local Storage → testRecords
   - ✅ 飞书数据：打开飞书多维表格，刷新查看新记录

### 快速验证Webhook
在浏览器 F12 → Console 执行：
```javascript
// 查看配置
console.log(FEISHU_CONFIG);

// 查看本地数据
const records = JSON.parse(localStorage.getItem('testRecords'));
console.table(records);
```

## 🔧 自定义配置

### 修改时间限制

编辑 `config.js`：
```javascript
const TIME_CONFIG = {
    totalTime: 20 * 60,      // 改为 20 分钟
    questionTime: 45         // 改为 45 秒/题
};
```

### 修改出题数

编辑 `config.js`：
```javascript
const TEST_CONFIG = {
    questionsPerTest: 50     // 改为 50 道题
};
```

### 添加更多题目

编辑 `questions_multi_dept.json`，添加题目对象到相应的数组：
```json
{
    "id": 999,
    "category": "分类名",
    "content": "题目内容",
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
    "correct": 0,
    "standard": "GB/T XXXX",
    "explanation": "解释"
}
```

## 📊 数据同步到飞书

### 自动同步字段

| 字段 | 内容 | 示例 |
|------|------|------|
| 姓名 | 用户填写 | 张三 |
| 工号 | 用户填写（可选） | E001 |
| 部门 | 用户选择 | 设计部 |
| 联系方式 | 用户填写（可选） | 13800138000 |
| 成绩 | 自动计算 | 85% |
| 答对 | 正确数/总数 | 25/30 |
| 答题时间 | 实际耗时 | 12分34秒 |
| 超时 | 是/否 | 否 |
| 测试时间 | 时间戳 | 2026-04-13 14:30 |

### 验证同步

1. 完成一次答题
2. 打开飞书多维表格
3. 刷新页面
4. 查看是否出现新记录

## ⚠️ 常见问题

### Q: 飞书没有收到数据？

**A:** 检查以下几点：
1. F12 → Console 是否有错误信息
2. `config.js` 中 `enabled: true` 是否已设置
3. Webhook URL 是否正确（已自动配置）
4. 数据一定已保存到本地（即使飞书同步失败）

### Q: 时间到了会怎样？

**A:** 系统自动：
1. 显示 "⏱️ 时间到！系统已自动交卷"
2. 跳转到成绩页面
3. 无法继续答题

### Q: 如何查看本地数据？

**A:** 打开浏览器 F12：
```
F12 → Application 标签
→ Local Storage
→ 选择当前网址
→ 找到 testRecords 键
```

或在 Console 执行：
```javascript
JSON.stringify(JSON.parse(localStorage.getItem('testRecords')), null, 2)
```

## 📚 文档导航

- 📖 [快速开始指南](QUICK_START.md) - **从这里开始**
- 🔗 [飞书集成详解](FEISHU_INTEGRATION_GUIDE.md) - 深入配置
- 📝 [完整更新日志](CHANGELOG_v4.1.md) - 所有功能说明
- 📋 [系统升级说明](SYSTEM_UPGRADE_NOTES.md) - 技术细节

## 🎉 系统状态

```
✅ 应用层：正常运作
✅ 题库系统：已配置（多岗位支持）
✅ 时间限制：已启用（15分钟+30秒/题）
✅ 用户信息：已启用（4个字段）
✅ 飞书同步：✨ 已配置并启用 ✨
✅ 本地存储：已启用（自动备份）
✅ 文档完整：已提供
```

## 🚀 立即开始

1. **打开应用**
   ```
   用浏览器打开: garment_test_v2.html
   ```

2. **完成一次答题**
   - 填写测试信息
   - 快速完成答题

3. **验证数据**
   - 检查飞书表格
   - 检查本地存储

---

**版本** - v4.1  
**状态** - ✅ 已就绪，可立即使用  
**飞书** - ✅ Webhook 已配置  
**更新时间** - 2026-04-13

### 📞 需要帮助？
查看 [快速开始指南](QUICK_START.md) 或 [飞书集成指南](FEISHU_INTEGRATION_GUIDE.md)
