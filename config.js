/**
 * 新益服装知识测试系统 - 配置文件
 * 请在这里配置飞书集成和其他选项
 */

// ========== 飞书多维表格配置 ==========
const FEISHU_CONFIG = {
    // 启用飞书同步 (true 或 false)
    enabled: true,

    // 方法1：使用Webhook（推荐）
    // 从飞书获取你的Webhook URL，格式如下：
    // https://open.feishu.cn/open-apis/bot/v2/hook/...
    webhookUrl: 'https://ki5kgs18g46.feishu.cn/base/automation/webhook/event/MVGNateX1wsewghhGaPcNobonpd',

    // 方法2：使用API（可选，需要飞书应用权限）
    appId: '',
    appSecret: '',
    tableId: '',
    useApi: false
};

// ========== 答题时间配置 ==========
const TIME_CONFIG = {
    // 总时间限制（秒）
    totalTime: 15 * 60,  // 15分钟

    // 单题时间限制（秒）
    questionTime: 30,    // 30秒

    // 是否显示时间警告
    showWarnings: true,

    // 最后剩余多少秒时显示红色警告
    warningThreshold: 60
};

// ========== 答题规则配置 ==========
const TEST_CONFIG = {
    // 每次出题数
    questionsPerTest: 30,

    // 超时时自动选择答案 (true) 或自动跳过 (false)
    autoSelectOnTimeout: true,

    // 是否显示答题反馈
    showFeedback: true,

    // 是否允许返回修改答案
    allowReviewAnswers: false
};

// ========== 用户信息配置 ==========
const USER_INFO_CONFIG = {
    // 必填字段
    required: ['username', 'department'],

    // 可选字段
    optional: ['empid', 'phone'],

    // 是否保存用户信息到浏览器（下次自动填充）
    saveToBrowser: true
};

// ========== 导出配置供HTML使用 ==========
// 如果通过<script>标签引入此文件，配置会自动可用
// 否则需要在HTML中导入：<script src="config.js"></script>

console.log('✅ 配置文件已加载');

// 快速测试配置
function testFeishuConfig() {
    if (FEISHU_CONFIG.enabled && !FEISHU_CONFIG.webhookUrl) {
        console.warn('⚠️ 飞书已启用但未配置Webhook URL');
    } else if (FEISHU_CONFIG.enabled) {
        console.log('✅ 飞书配置正确');
    }
}

// 显示当前配置
function showConfig() {
    console.table({
        '飞书启用': FEISHU_CONFIG.enabled,
        '总时间': TIME_CONFIG.totalTime + '秒',
        '单题时间': TIME_CONFIG.questionTime + '秒',
        '每次出题': TEST_CONFIG.questionsPerTest + '道',
        '本地保存': USER_INFO_CONFIG.saveToBrowser
    });
}
