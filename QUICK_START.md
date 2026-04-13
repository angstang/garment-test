# 🚀 快速开始指南

## ✅ 现在已配置完成

您的飞书 Webhook 已配置到系统中：
```
https://ki5kgs18g46.feishu.cn/base/automation/webhook/event/MVGNateX1wsewghhGaPcNobonpd
```

## 🧪 测试系统

### 方法1：完整的答题流程测试（推荐）

1. **打开应用**
   - 用浏览器打开 `garment_test_v2.html`

2. **开始测试**
   - 点击"开始测试"按钮

3. **填写信息**
   - 姓名：张三（测试用）
   - 工号：T001（可选）
   - 部门：选择 "设计部"
   - 联系方式：13800138000（可选）

4. **快速完成答题**
   - 不需要认真答题，快速选择选项
   - 或等待30秒每题自动跳过
   - 或等待15分钟自动交卷

5. **查看结果**
   - 显示成绩页面
   - 打开浏览器开发者工具（F12）→ Console
   - 查看是否有 `✅ 数据已成功同步到飞书` 的信息

6. **验证飞书**
   - 打开飞书多维表格
   - 检查是否出现新的记录
   - 确认字段是否正确

### 方法2：快速测试（仅验证配置）

在浏览器控制台执行以下代码：

```javascript
// 测试配置是否正确加载
console.log('飞书配置:', FEISHU_CONFIG);

// 检查webhook是否有效
fetch('https://ki5kgs18g46.feishu.cn/base/automation/webhook/event/MVGNateX1wsewghhGaPcNobonpd', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        data: {
            "姓名": "测试用户",
            "工号": "TEST001",
            "部门": "测试部门",
            "联系方式": "测试",
            "成绩": "100%",
            "答对": "30/30",
            "答题时间": "5分钟",
            "超时": "否",
            "测试时间": new Date().toLocaleString('zh-CN')
        }
    })
}).then(r => {
    console.log('响应状态:', r.status);
    if (r.ok) console.log('✅ Webhook 可用');
    else console.log('❌ Webhook 响应异常');
}).catch(e => console.error('❌ 错误:', e));
```

## 📊 验证数据同步

### 在飞书中查看数据

1. 打开飞书多维表格
2. 刷新页面
3. 查看最新的记录
4. 确认以下字段：
   - ✅ 姓名
   - ✅ 工号
   - ✅ 部门
   - ✅ 联系方式
   - ✅ 成绩
   - ✅ 答对/总题数
   - ✅ 答题时间
   - ✅ 超时状态
   - ✅ 测试时间

### 在浏览器中查看本地数据

打开浏览器开发者工具（F12）：

```
步骤1: 按 F12 打开开发者工具
步骤2: 选择 "Application" 或 "应用" 标签
步骤3: 在左侧找到 "Local Storage"
步骤4: 选择当前网址
步骤5: 找到 "testRecords" 键
步骤6: 查看所有测试记录（JSON格式）
```

或在控制台执行：
```javascript
// 查看所有本地记录
const records = JSON.parse(localStorage.getItem('testRecords') || '[]');
console.table(records);

// 查看最新的一条记录
if (records.length > 0) {
    console.log('最新记录:', records[records.length - 1]);
}
```

## 🔧 如果出现问题

### 问题1：飞书没有收到数据

**检查清单：**
- [ ] 飞书多维表格是否已创建？
- [ ] Webhook URL 是否正确？
- [ ] 字段名是否与表格一致？

**排查步骤：**

1. 打开浏览器 F12 → Console
2. 完成一次答题
3. 查看是否出现以下信息：
   ```
   ✅ 数据已保存到本地存储
   🔄 正在同步数据到飞书...
   📡 飞书服务器响应: 200
   ✅ 数据已成功同步到飞书
   ```

4. 如果看到错误信息，记录下来：
   - `❌ 飞书同步失败`
   - `❌ 飞书同步错误`

### 问题2：字段名不匹配

如果飞书表格中的字段名不同，需要修改 HTML 中的字段映射。

找到 `syncToFeishuWebhook()` 函数，修改 `data` 对象中的键：

```javascript
const payload = {
    data: {
        "你的字段名1": reportData.name,
        "你的字段名2": reportData.empId,
        // ...
    }
};
```

### 问题3：CORS 或网络错误

如果出现 CORS 错误，这通常表示：
- Webhook URL 不支持跨域请求
- 或网络连接有问题

**解决方案：**
1. 确保 Webhook URL 是公开可访问的
2. 检查飞书设置中是否需要授权
3. 尝试在手机上测试（使用不同的网络）

## 📋 系统检查清单

在部署前，请确认：

- [ ] 飞书 Webhook 已配置（`config.js` 中 `enabled: true`）
- [ ] 飞书多维表格已创建
- [ ] 至少完成一次测试答题
- [ ] 数据已在飞书表格中出现
- [ ] 所有字段名称都正确匹配
- [ ] 时间限制按预期工作（15分钟 + 30秒/题）
- [ ] 用户信息正确收集
- [ ] 本地备份数据可用

## 🎯 常见使用场景

### 场景1：公司员工培训

1. 在飞书中创建共享表格
2. 分享 `garment_test_v2.html` 链接给员工
3. 员工完成答题
4. 成绩自动同步到表格
5. 导出表格查看培训效果

### 场景2：部门考评

1. 为不同部门定制题库（已支持）
2. 设置合适的时间限制
3. 每周进行一次考评
4. 在飞书中追踪员工进度

### 场景3：在线考试

1. 配置足够的题库（100+道/部门）
2. 启用时间限制防作弊
3. 定期备份飞书数据
4. 导出最终成绩报告

## 📞 需要帮助？

### 检查日志信息

在浏览器 F12 → Console 中查看详细的日志：

```javascript
// 显示所有日志
console.clear();
// 然后重新完成一次答题，观察所有输出
```

### 导出诊断信息

```javascript
// 导出完整的诊断信息
const diagnostic = {
    config: FEISHU_CONFIG,
    timeConfig: TIME_CONFIG,
    testConfig: TEST_CONFIG,
    localStorage: localStorage.getItem('testRecords'),
    appState: appState
};
console.log(JSON.stringify(diagnostic, null, 2));
```

### 重置系统状态

```javascript
// 清除所有本地数据（谨慎使用！）
localStorage.clear();
location.reload();
```

## 📚 更多信息

详细文档：
- [系统升级说明](SYSTEM_UPGRADE_NOTES.md)
- [飞书集成指南](FEISHU_INTEGRATION_GUIDE.md)
- [完整更新日志](CHANGELOG_v4.1.md)

---

**现在您可以：**
1. ✅ 打开 HTML 文件完成答题
2. ✅ 数据自动保存到本地
3. ✅ 数据自动同步到飞书
4. ✅ 在飞书中查看和分析成绩

祝使用愉快！🎉
