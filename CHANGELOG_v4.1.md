# 更新日志 - v4.1 版本

## 🎉 新增功能

### 1. ⏱️ 时间限制与倒计时

**功能描述**：
- **全局倒计时**：15分钟完成30道题（自动交卷）
- **单题倒计时**：每题30秒，超时自动跳过
- **实时显示**：在答题界面显示剩余总时间和本题剩余时间
- **智能警告**：最后60秒总时间时变红显示

**使用方式**：
```
顶部右侧显示：
- 总时间: 14:32 (超过60秒时为蓝色，剩余≤60秒时为红色)
- 本题: 28s (最后5秒时为红色)
```

**配置**：
编辑 `config.js` 文件：
```javascript
const TIME_CONFIG = {
    totalTime: 15 * 60,      // 修改为你想要的总时间（秒）
    questionTime: 30,         // 修改为你想要的单题时间（秒）
};
```

### 2. 👤 用户信息收集

**新增字段**：
- ✅ 姓名（必填）
- ✅ 工号（可选）
- ✅ 部门（必填）
- ✅ 联系方式（可选）

**数据流向**：
1. 用户填写信息并开始答题
2. 答题完成后自动收集所有信息
3. 同步到飞书多维表格（如已配置）
4. 保存到浏览器本地存储（作为备份）

**本地数据查看**：
打开浏览器开发者工具 → Application → Local Storage → 查找 `testRecords`

### 3. 🔄 飞书多维表格同步

**功能说明**：
自动将每个用户的答题成绩同步到飞书，包括：
- 基本信息：姓名、工号、部门、联系方式
- 答题结果：成绩、答对数、总题数
- 答题过程：耗时、是否超时
- 时间戳：测试时间

**同步数据示例**：
```json
{
    "姓名": "张三",
    "工号": "E001",
    "部门": "设计部",
    "联系方式": "13800138000",
    "成绩": "85%",
    "答对": "25/30",
    "答题时间": "12分34秒",
    "超时": "否",
    "测试时间": "2026-04-13 14:30:45"
}
```

**快速配置**：
1. 打开飞书，创建多维表格
2. 获取 Webhook URL
3. 编辑 `config.js`：
   ```javascript
   const FEISHU_CONFIG = {
       enabled: true,
       webhookUrl: 'https://open.feishu.cn/...' // 你的URL
   };
   ```
4. 完成一次答题测试

**详细配置指南**：
参见 `FEISHU_INTEGRATION_GUIDE.md` 文件

### 4. 📊 本地数据存储

**功能**：
- 所有答题数据自动保存到浏览器 LocalStorage
- 即使飞书配置失败也能保存数据
- 支持查看历史记录和导出

**查看历史数据**：
```javascript
// 在浏览器控制台执行：
const records = JSON.parse(localStorage.getItem('testRecords'));
console.table(records);
```

**导出数据**：
```javascript
// 点击"下载JSON"按钮可导出成绩报告
// 或执行以下代码导出所有历史记录：
const records = JSON.parse(localStorage.getItem('testRecords'));
const blob = new Blob([JSON.stringify(records, null, 2)], { type: 'application/json' });
const url = URL.createObjectURL(blob);
const a = document.createElement('a');
a.href = url;
a.download = 'test_records.json';
a.click();
```

### 5. 🎨 简化的欢迎页面

**改进**：
- ✨ 移除冗长的标准列表
- ✨ 显示核心规则（题量、时间、每题30秒）
- ✨ 更清爽的视觉设计

## 📋 文件结构

```
/代码/
├── garment_test_v2.html                    # 主应用（已更新v4.1）
├── questions_multi_dept.json               # 多岗位题库
├── config.js                               # ⭐ 新增：配置文件
├── SYSTEM_UPGRADE_NOTES.md                 # v4.0升级说明
├── FEISHU_INTEGRATION_GUIDE.md             # ⭐ 新增：飞书集成指南
├── CHANGELOG_v4.1.md                       # 本文件
└── questions_db.json                       # 原始题库（备用）
```

## 🔧 配置指南

### 简单配置（推荐）

编辑 `config.js` 文件：

```javascript
// 1. 启用飞书（可选）
const FEISHU_CONFIG = {
    enabled: true,
    webhookUrl: 'https://...' // 从飞书复制
};

// 2. 调整时间限制（可选）
const TIME_CONFIG = {
    totalTime: 15 * 60,     // 15分钟
    questionTime: 30        // 每题30秒
};

// 3. 调整出题数（可选）
const TEST_CONFIG = {
    questionsPerTest: 30    // 每次30道题
};
```

### HTML中引入配置

在 `garment_test_v2.html` 的 `<head>` 中添加：

```html
<script src="config.js"></script>
```

然后修改JavaScript中的配置读取（如需）：

```javascript
const feishuConfig = FEISHU_CONFIG;
```

## 📱 使用流程

1. **打开系统** → 点击"开始测试"
2. **填写信息** → 输入姓名、工号、部门、联系方式
3. **开始答题** → 开始15分钟倒计时
4. **实时显示**：
   - 顶部显示总剩余时间
   - 右上角显示本题剩余秒数
5. **自动交卷**：
   - 15分钟后自动提交
   - 或完成30道题后手动提交
6. **查看成绩** → 显示成绩和分类评分
7. **数据同步**：
   - 自动保存到本地
   - 自动同步到飞书（如配置）

## ⚙️ 关键变更

### JavaScript 函数

**新增函数**：
- `formatTime(seconds)` - 格式化时间显示
- `startGlobalTimer()` - 启动全局倒计时
- `startQuestionTimer()` - 启动单题倒计时
- `stopAllTimers()` - 停止所有计时
- `prepareReportData()` - 准备成绩报告
- `syncToFeishuWebhook()` - 同步到飞书
- `saveToLocalStorage()` - 保存到本地

**修改函数**：
- `submitInfo()` - 添加了新字段和计时启动
- `showQuestion()` - 添加单题计时启动
- `showResult()` - 添加数据同步逻辑

### appState 新增字段

```javascript
appState = {
    // ... 原有字段
    empId: "",                  // 工号
    phone: "",                  // 联系方式
    testEndTime: null,          // 答题结束时间
    // 时间管理
    totalTimeLimit: 15 * 60,   // 15分钟
    questionTimeLimit: 30,      // 30秒/题
    remainingTime: 15 * 60,    // 剩余时间
    globalTimer: null,         // 全局计时器ID
    questionTimer: null,       // 单题计时器ID
    timeExpired: false        // 是否超时
};
```

## ⚠️ 重要提示

1. **浏览器兼容性**：
   - Chrome 80+
   - Firefox 75+
   - Safari 13+
   - Edge 80+

2. **飞书配置**：
   - Webhook URL 必须来自官方飞书
   - 不要在代码中暴露敏感信息
   - 建议定期更换 Webhook

3. **数据隐私**：
   - 本地存储的数据仅在本设备可见
   - 关闭浏览器数据清除后本地数据会丢失
   - 建议定期导出备份

4. **时间同步**：
   - 计时基于客户端系统时间
   - 用户可能通过修改系统时间作弊
   - 如需防作弊，建议在后端验证

## 🚀 性能优化建议

1. **题库优化**：
   - 如果题库超过500道，建议分页加载
   - 考虑压缩 JSON 文件

2. **数据库同步**：
   - 使用异步请求避免阻塞
   - 添加失败重试机制
   - 考虑使用队列处理离线情况

3. **缓存策略**：
   - 题库可以缓存到本地
   - 减少重复的网络请求

## 📞 常见问题

**Q: 时间到了答题会怎样？**
A: 自动交卷，显示最后的成绩，无法继续答题。

**Q: 单题超时怎么办？**
A: 系统自动选择第一个选项并跳到下一题。

**Q: 数据没有同步到飞书怎么办？**
A: 检查：
1. 是否启用了飞书配置
2. Webhook URL 是否正确
3. 浏览器控制台是否有错误信息
4. 数据已保存到本地，可稍后导出

**Q: 如何导出所有学生的成绩？**
A: 可以：
1. 直接在飞书多维表格导出
2. 或使用浏览器导出 JSON 文件
3. 或编写脚本从飞书 API 获取

## 🔄 更新历史

- **v4.0** (2026-04-13): 多岗位题库系统
- **v4.1** (2026-04-13): 时间限制、用户信息收集、飞书同步

---

**当前版本**：v4.1  
**最后更新**：2026-04-13  
**作者**：新益服装  
**支持**：https://github.com/xinyi-fashion/test-system
