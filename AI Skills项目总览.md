# 金凯博人力行政IT部 - AI Skills项目总览

> 项目状态：已完成 | 更新日期：2025年1月

---

## 一、项目概述

基于人力行政部76项工作任务分析，创建15个AI自动化技能，预计整体提效40%+。

---

## 二、已创建Skills清单

### 考勤薪酬（2个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 1 | attendance-report | 考勤智能统计、加班/餐补计算 | 2天/月 | ✅ 完成 |
| 2 | social-security-check | 社保公积金自动对账 | 1天/月 | ✅ 完成 |

### 招聘管理（2个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 3 | resume-screener | AI简历筛选与排名 | 50%时间 | ✅ 完成 |
| 4 | jd-generator | 多渠道招聘JD生成 | 30%时间 | ✅ 完成 |

### 员工管理（3个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 5 | roster-sync | 花名册/通讯录同步 | 1天/月 | ✅ 完成 |
| 6 | onboarding-flow | 入职10步自动化 | 80%效率 | ✅ 完成 |
| 7 | offboarding-flow | 离职11步自动化 | 60%效率 | ✅ 完成 |

### 培训绩效（2个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 8 | training-pack | 入职培训材料生成 | 50%时间 | ✅ 完成 |
| 9 | sales-analysis | KC销售数据分析与提成 | 50%时间 | ✅ 完成 |

### 行政事务（3个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 10 | meeting-notes | 会议纪要智能生成 | 30%时间 | ✅ 完成 |
| 11 | expense-reconcile | 顺丰/机票费用对账 | 60%时间 | ✅ 完成 |
| 12 | cert-reminder | 证书到期自动提醒 | 自动化 | ✅ 完成 |

### 法务合规（2个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 13 | contract-review | 合同风险智能审核 | 30%时间 | ✅ 完成 |
| 14 | policy-drafter | 企业制度起草 | 40%时间 | ✅ 完成 |

### 政府事务（1个）

| # | Skill名称 | 功能 | 预计节省 | 状态 |
|---|-----------|------|----------|------|
| 15 | gov-report-gen | 政府报表自动填报 | 5天/年 | ✅ 完成 |

---

## 三、配套文档清单

| 文档 | 位置 | 用途 |
|------|------|------|
| Skills使用指南.md | 2026规划/ | 详细使用说明 |
| Skills快速参考卡.md | 2026规划/ | 桌面速查卡 |
| 常用工作流程指南.md | 2026规划/ | 多技能组合使用 |
| 月度工作日历.md | 2026规划/ | 按时间安排任务 |

---

## 四、数据模板清单

| 模板 | 位置 | 对应Skill |
|------|------|-----------|
| 考勤数据模板.xlsx | Skills数据模板/ | attendance-report |
| 员工花名册模板.xlsx | Skills数据模板/ | roster-sync |
| 社保数据模板.xlsx | Skills数据模板/ | social-security-check |
| 证书清单模板.xlsx | Skills数据模板/ | cert-reminder |
| 销售数据模板.xlsx | Skills数据模板/ | sales-analysis |
| 顺丰账单模板.xlsx | Skills数据模板/ | expense-reconcile |
| 入职信息模板.xlsx | Skills数据模板/ | onboarding-flow |

---

## 五、Skill文件位置

所有Skill文件位于：`~/.claude/skills/`

```
~/.claude/skills/
├── attendance-report/
│   └── SKILL.md
├── social-security-check/
│   └── SKILL.md
├── resume-screener/
│   └── SKILL.md
├── jd-generator/
│   └── SKILL.md
├── roster-sync/
│   └── SKILL.md
├── onboarding-flow/
│   └── SKILL.md
├── offboarding-flow/
│   └── SKILL.md
├── training-pack/
│   └── SKILL.md
├── meeting-notes/
│   └── SKILL.md
├── expense-reconcile/
│   └── SKILL.md
├── cert-reminder/
│   └── SKILL.md
├── sales-analysis/
│   └── SKILL.md
├── contract-review/
│   └── SKILL.md
├── policy-drafter/
│   └── SKILL.md
└── gov-report-gen/
    └── SKILL.md
```

---

## 六、效益预估

### 时间节省

| 类别 | 月度节省 | 年度节省 |
|------|----------|----------|
| 考勤薪酬 | 3天 | 36天 |
| 员工管理 | 2天 | 24天 |
| 行政对账 | 2天 | 24天 |
| 招聘筛选 | 按需 | 约20天 |
| 政府报表 | - | 5天 |
| **合计** | **7天/月** | **109天/年** |

### 人效提升

- 原配置：6人
- AI辅助后：可优化至3+1配置
- 提效幅度：40%+

---

## 七、使用建议

1. **先熟悉常用技能**：从考勤统计、花名册更新开始
2. **使用标准模板**：确保数据格式正确
3. **人工复核**：AI输出需人工确认后使用
4. **逐步扩展**：熟练后再使用更多技能

---

## 八、后续维护

- **Skill更新**：根据实际使用反馈调整
- **模板优化**：根据业务变化更新模板
- **新增技能**：发现新的自动化机会时扩展

---

## 九、技术支持

- IT专员：舒盼
- 部门负责人：符凌维
- Claude Code：持续可用

---

*项目完成日期：2025年1月*
*由Claude Code自动生成*
