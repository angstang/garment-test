# 飞书多维表格集成指南

## 🎯 功能说明

系统支持将每个用户的答题成绩自动同步到飞书多维表格，包括：
- 姓名、工号、部门、联系方式
- 成绩（百分比）、答对题数
- 答题耗时、是否超时、测试时间

## 📋 同步字段

| 字段 | 说明 | 示例 |
|------|------|------|
| 姓名 | 考生姓名 | 张三 |
| 工号 | 员工工号 | E001 |
| 部门 | 所在部门 | 设计部 |
| 联系方式 | 手机或邮箱 | 13800138000 |
| 成绩 | 百分比成绩 | 85% |
| 答对 | 答对题数/总题数 | 25/30 |
| 答题时间 | 实际耗时 | 12分34秒 |
| 超时 | 是否在规定时间内完成 | 否 |
| 测试时间 | 测试时间戳 | 2026-04-13 14:30:45 |

## 🔧 配置方法

### 方法一：使用飞书Webhook（推荐，简单）

#### 步骤1：在飞书中创建多维表格

1. 打开飞书 → 创建文档 → 选择"多维表格"
2. 创建以下字段：
   - 姓名（文本）
   - 工号（文本）
   - 部门（单选或多选）
   - 联系方式（文本）
   - 成绩（文本/数字）
   - 答对（文本）
   - 答题时间（文本）
   - 超时（勾选）
   - 测试时间（日期时间）

#### 步骤2：获取Webhook URL

1. 在多维表格中点击"自动化"或"API"选项
2. 如果没有，使用以下方法：
   - 在飞书开放平台申请应用
   - 或使用飞书的"自定义工作流"功能
   - 获取Webhook URL

#### 步骤3：在HTML中配置

找到HTML文件中的以下代码：

```javascript
const feishuConfig = {
    webhookUrl: 'https://open.feishu.cn/open-apis/... (你的Webhook URL)',
    enabled: true
};
```

替换 `webhookUrl` 为你获取的实际URL，并将 `enabled` 改为 `true`。

#### 步骤4：测试

1. 完成一次答题
2. 打开浏览器开发者工具（F12）→ 控制台（Console）
3. 查看是否有 `✅ 数据已同步到飞书` 的消息
4. 检查飞书多维表格中是否出现新记录

### 方法二：使用飞书 API（高级）

如果你有飞书应用权限，可以使用API进行同步：

1. 在飞书开放平台创建应用
2. 获取 `App ID` 和 `App Secret`
3. 获取多维表格的 `Table ID`
4. 修改代码中的 `syncToFeishuAPI()` 函数

## 💾 本地数据存储

即使飞书未配置或同步失败，系统也会将数据保存到浏览器本地存储：

- **位置**：浏览器的 LocalStorage
- **查看方法**：
  1. 打开浏览器开发者工具（F12）
  2. 选择"应用"或"Application"标签
  3. 在左侧找到"本地存储"或"Local Storage"
  4. 选择当前网址
  5. 查找 `testRecords` 键，可以看到所有测试记录

## 🔐 数据安全注意事项

1. **Webhook URL 安全**：
   - 不要在代码中硬编码敏感的API密钥
   - 考虑使用环境变量或配置服务

2. **数据隐私**：
   - 确保飞书表格的访问权限设置正确
   - 不要与未授权的人分享Webhook URL

3. **CORS 问题**：
   - 如果遇到跨域问题，需要配置飞书Webhook的CORS策略
   - 或使用后端代理

## 📊 查看历史记录

### 在浏览器中查看

```javascript
// 在浏览器开发者工具的控制台执行：
const records = JSON.parse(localStorage.getItem('testRecords'));
console.table(records);
```

### 导出所有记录

```javascript
// 导出为JSON文件
const records = JSON.parse(localStorage.getItem('testRecords'));
const dataStr = JSON.stringify(records, null, 2);
const dataBlob = new Blob([dataStr], { type: 'application/json' });
const url = URL.createObjectURL(dataBlob);
const link = document.createElement('a');
link.href = url;
link.download = 'test_records.json';
link.click();
```

## ⚠️ 故障排除

### 问题1：数据未同步到飞书

**检查清单**：
- [ ] Webhook URL 是否正确配置
- [ ] `enabled` 是否设置为 `true`
- [ ] 网络连接是否正常
- [ ] 浏览器控制台是否有错误信息

**解决方法**：
1. 打开浏览器控制台（F12 → Console）
2. 查看是否有错误信息
3. 检查Webhook URL是否有效
4. 确认飞书多维表格可以接收数据

### 问题2：CORS 错误

**错误信息**：`Access to XMLHttpRequest blocked by CORS policy`

**解决方法**：
1. 确保Webhook URL允许跨域请求
2. 考虑使用后端代理
3. 或使用飞书的官方SDK

### 问题3：数据格式不匹配

**症状**：数据已同步但字段为空或显示错误

**解决方法**：
1. 检查飞书多维表格的字段名是否与代码中的字段名一致
2. 修改 `syncToFeishuWebhook()` 函数中的字段映射

## 🚀 高级配置

### 自定义字段映射

如需修改同步的字段，编辑 `syncToFeishuWebhook()` 函数中的 `payload` 对象：

```javascript
const payload = {
    data: {
        "你的字段名1": reportData.name,
        "你的字段名2": reportData.empId,
        // ... 添加更多字段
    }
};
```

### 添加额外的处理逻辑

在 `prepareReportData()` 函数中添加评价等级：

```javascript
let rating = '';
if (percentage >= 90) rating = '优秀';
else if (percentage >= 75) rating = '良好';
else if (percentage >= 60) rating = '及格';
else rating = '需改进';

return {
    // ... 其他字段
    rating: rating
};
```

## 📞 技术支持

如有问题，请检查：
1. 飞书 API 文档：https://open.feishu.cn/document
2. Webhook 配置是否正确
3. 浏览器控制台的错误信息

---

**最后更新**：2026-04-13  
**支持版本**：v4.0+
