# 答题系统调试指南

## 问题：第24题（最后一题）无法提交答案

如果您在答题过程中遇到无法提交答案的问题，请按以下步骤诊断：

### 步骤1：打开浏览器控制台

1. 按 `F12` 或 `Ctrl+Shift+I` (Windows/Linux) / `Cmd+Option+I` (Mac)
2. 切换到 **Console** 标签
3. 刷新页面 `F5` 或 `Ctrl+R`

### 步骤2：查看控制台输出

正常的提交流程应该显示：

```
✅ 提交答案: 第 24/24 题, 是否为最后一题: true
🔄 调用 showResult()...
🏁 开始计算成绩...
📊 成绩: XX/24 (XX%)
✅ 成绩已保存到本地存储
✅ 飞书同步完成
✅ 成功切换到结果屏幕
```

### 步骤3：诊断常见问题

#### 问题A：提交按钮无响应
**症状**：点击"提交答案"没有任何反应

**可能原因**：
1. JavaScript错误导致事件处理器未触发
2. 答案未被正确选中

**解决方案**：
- 在控制台查看是否有红色错误信息
- 确保在点击提交前选择了答案（选项旁会显示蓝色高亮）

#### 问题B：显示错误消息
**症状**：看到"提交答案时出错"或"成绩计算时出现问题"

**可能原因**：
1. 飞书同步失败（可以忽略，不影响答题）
2. 题库数据格式问题
3. 浏览器存储问题

**解决方案**：
- 检查控制台红色错误信息
- 清除浏览器缓存：`Ctrl+Shift+Delete` (Windows/Linux) 或 `Cmd+Shift+Delete` (Mac)
- 重新加载页面

#### 问题C：结果页面没有显示
**症状**：提交答案后页面无变化

**可能原因**：
1. 数据计算出错
2. DOM元素不存在
3. showScreen()函数失败

**解决方案**：
- 检查控制台是否有错误消息
- 手动刷新页面
- 使用不同浏览器测试

### 步骤4：收集调试信息

如果问题仍未解决，请收集以下信息：

```javascript
// 在控制台运行以下代码获取当前状态

// 显示应用状态
console.log(JSON.stringify(appState, null, 2));

// 显示题库信息
console.log('总题数:', appState.selectedQuestions.length);
console.log('当前题号:', appState.currentQuestion);
console.log('已回答题数:', Object.keys(appState.answers).length);
```

### 常见错误信息说明

#### "答案计算出错"
- 可能是题库格式问题
- 检查题库JSON是否有效：`json`复制粘贴到 [JSONLint](https://jsonlint.com/)

#### "飞书同步失败"
- 这是非关键错误，答题系统仍可正常使用
- 可以忽略此错误继续答题
- 成绩已保存到本地存储

### 网络问题诊断

如果遇到"飞书同步失败"错误：

1. **检查网络连接**
   - 确保网络正常
   - 检查防火墙设置

2. **检查飞书配置**
   - 打开 `config.js` 文件
   - 检查 `FEISHU_CONFIG.enabled` 是否为 `true`
   - 检查 `FEISHU_CONFIG.webhookUrl` 是否正确

3. **临时禁用飞书同步**
   - 在 `config.js` 中设置：
     ```javascript
     FEISHU_CONFIG.enabled = false;
     ```

### 本地存储检查

答题成绩已保存到本地浏览器存储：

```javascript
// 在控制台运行
console.log(localStorage.getItem('testRecords'));
```

### 日志收集

遇到问题时，右键点击控制台，选择"Save as..."保存完整日志：

1. 选中所有控制台输出
2. 右键 → 复制
3. 保存到文本文件
4. 发送给技术支持

### 相关资源

- [浏览器控制台使用教程](https://developer.mozilla.org/zh-CN/docs/Tools/Browser_Console)
- [JSON验证工具](https://jsonlint.com/)
- [Chrome DevTools调试指南](https://developer.chrome.com/docs/devtools/)

### 快速修复步骤（按顺序尝试）

1. ✅ 清除缓存并刷新：`Ctrl+Shift+R` (Windows/Linux) 或 `Cmd+Shift+R` (Mac)
2. ✅ 关闭并重新打开浏览器
3. ✅ 在隐身/无痕模式下测试
4. ✅ 使用不同的浏览器测试
5. ✅ 检查网络连接和防火墙

---

**需要进一步帮助？** 请提供：
- 浏览器类型和版本
- 错误消息的完整文本
- 控制台日志截图
