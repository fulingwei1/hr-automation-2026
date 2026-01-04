# salary-calculator Skill 路径配置说明

## ⚠️ 重要提示

salary-calculator Skill 依赖于salary项目，**salary项目的位置不能随意移动**。

如果salary项目位置改变，必须更新Skill的配置文件。

---

## 当前配置

**salary项目位置:** `/Users/flw/salary`

**web_app位置:** `/Users/flw/salary/web_app`

**配置文件:** `~/.claude/skills/salary-calculator/salary_config.json`

---

## 如果salary项目位置改变了怎么办？

### 步骤1: 找到新位置
```bash
# 查找salary项目在哪里
find ~ -name "salary" -type d -maxdepth 3
```

### 步骤2: 更新配置文件
编辑 `~/.claude/skills/salary-calculator/salary_config.json`

**修改前:**
```json
{
  "project_root": "/Users/flw/salary",
  "web_app_path": "/Users/flw/salary/web_app",
  ...
}
```

**修改后（假设移动到 /opt/salary）:**
```json
{
  "project_root": "/opt/salary",
  "web_app_path": "/opt/salary/web_app",
  ...
}
```

### 步骤3: 验证配置
运行以下命令验证配置是否正确：
```bash
python ~/.claude/skills/salary-calculator/salary_wrapper.py --help
```

如果输出"环境检查通过"，说明配置成功。

---

## 文件结构检查

确保salary项目的目录结构完整：

```
/Users/flw/salary/
├── web_app/                    ✅ 必须存在
│   ├── attendance/             ✅ 必须存在（核心模块）
│   │   ├── pipeline.py
│   │   ├── daily_calc.py
│   │   ├── monthly_agg.py
│   │   └── ... 其他模块
│   ├── app.py
│   ├── models.py
│   └── ... 其他文件
├── CLAUDE.md                   ✅ 推荐有
├── requirements.txt            ✅ 推荐有
└── ... 其他文件
```

**关键检查:**
- [ ] `/Users/flw/salary/` 目录存在
- [ ] `/Users/flw/salary/web_app/` 目录存在
- [ ] `/Users/flw/salary/web_app/attendance/` 目录存在
- [ ] `attendance/` 下有Python模块文件

---

## 配置文件说明

`salary_config.json` 包含以下配置项：

### 必需配置
```json
{
  "project_root": "/Users/flw/salary",
  "web_app_path": "/Users/flw/salary/web_app"
}
```

### 可选配置（默认值）
```json
{
  "output_base_dir": "~/salary_output",

  "default_config": {
    "work_start_time": "09:00",        // 上班时间
    "work_end_time": "18:00",          // 下班时间
    "work_hours_per_day": 8,           // 日标准时长
    "meal_allowance": 15,              // 餐补(元/天)
    "late_deduction": 50,              // 迟到扣款(元/次)
    "saturday_allowance": 50,          // 周六补贴
    "holiday_allowance": 100,          // 节假日补贴
    "perfect_attendance_bonus": 200    // 满勤奖
  }
}
```

---

## 故障排除

### 问题1: "❌ salary项目不存在"
```
错误信息: salary项目不存在于 /Users/flw/salary

解决方案:
1. 检查salary项目是否移动了
   find ~ -name "web_app" -path "*/salary/*" | head -5
2. 更新salary_config.json中的project_root
3. 重新尝试
```

### 问题2: "❌ attendance模块不存在"
```
错误信息: attendance核心模块不存在于 /Users/flw/salary/web_app/attendance

解决方案:
1. 检查salary项目结构是否完整
   ls -la /Users/flw/salary/web_app/
2. 如果attendance目录缺失，可能需要重新克隆salary项目
3. 或者检查是否在salary_config.json中指定了错误的路径
```

### 问题3: "❌ 配置加载失败"
```
错误信息: 配置加载失败: ...

解决方案:
1. 检查salary_config.json是否有效JSON格式
   python -m json.tool ~/.claude/skills/salary-calculator/salary_config.json
2. 检查文件权限
   ls -l ~/.claude/skills/salary-calculator/salary_config.json
3. 检查JSON中的路径是否正确且存在
```

---

## 推荐做法

### ✅ 正确的做法
1. **将salary项目放在一个固定位置**
   - 推荐：`/Users/flw/salary`（当前配置）
   - 不要放在临时目录或移动频繁的地方

2. **备份配置文件**
   - 如果修改了salary_config.json，建议保存备份
   - 特别是在做salary项目迁移时

3. **定期检查**
   - 定期运行验证命令确保配置有效
   - 如果salary项目升级或移动，及时更新配置

### ❌ 避免的做法
- ❌ 不要将salary项目放在桌面或下载目录
- ❌ 不要删除salary项目中的web_app目录
- ❌ 不要在salary项目中随意移动文件结构
- ❌ 不要修改salary_config.json中的project_root而不告诉IT

---

## 快速参考

| 场景 | 操作 |
|------|------|
| 移动salary项目 | 1. 移动项目 2. 更新salary_config.json 3. 验证 |
| 检查当前配置 | `cat ~/.claude/skills/salary-calculator/salary_config.json` |
| 验证路径是否正确 | `python ~/.claude/skills/salary-calculator/salary_wrapper.py --help` |
| 重置为默认配置 | 使用原始salary_config.json（见本目录） |
| 查看所有配置 | 打开salary_config.json（JSON格式） |

---

## 技术细节（给管理员）

### Skill如何查找salary项目

1. **加载配置** → salary_wrapper.py读取salary_config.json
2. **获取路径** → 从配置中读取project_root和web_app_path
3. **验证存在** → 检查目录是否存在
4. **导入模块** → sys.path.insert()添加web_app到Python路径
5. **执行计算** → 导入并运行attendance.pipeline模块

### 配置变更的影响范围

```
salary_config.json 变更
    ↓
只影响这次运行和后续运行
（不需要重启Claude Code或其他应用）

salary项目文件变更
    ↓
需要保证结构完整
（特别是web_app/attendance目录）
```

---

## 联系方式

- **配置问题** → IT部 (舒盼)
- **salary项目问题** → IT部或Claude Code
- **路径查询问题** → 本文档或查看salary_config.json

---

**版本**: 1.0 | **最后更新**: 2026年1月4日
