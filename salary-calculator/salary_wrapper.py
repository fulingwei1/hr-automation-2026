#!/usr/bin/env python3
"""
salary-calculator Skill Wrapper
包装salary考勤薪资核算系统，供Claude Code调用

Usage:
    python salary_wrapper.py --month 2025-01 --attendance-file path/to/file.xlsx
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

# 指向salary项目根目录
SALARY_PROJECT_ROOT = Path.home() / "salary"
SALARY_WEB_APP = SALARY_PROJECT_ROOT / "web_app"


def validate_environment():
    """检查环境是否正确配置"""
    if not SALARY_PROJECT_ROOT.exists():
        print(f"❌ 错误: salary项目不存在于 {SALARY_PROJECT_ROOT}")
        return False

    if not (SALARY_WEB_APP / "attendance").exists():
        print(f"❌ 错误: attendance模块不存在于 {SALARY_WEB_APP}")
        return False

    return True


def run_salary_calculation(month, attendance_file, employee_file=None, leave_file=None,
                          overtime_file=None, output_dir=None, config_overrides=None):
    """
    执行薪资计算

    Args:
        month: 计算月份 (格式: YYYY-MM)
        attendance_file: 打卡数据文件路径
        employee_file: 员工信息文件路径 (可选)
        leave_file: 请假申请文件路径 (可选)
        overtime_file: 加班/出差文件路径 (可选)
        output_dir: 输出目录 (可选，默认为 ~/salary_output/)
        config_overrides: 配置覆盖字典 (可选)

    Returns:
        dict: 包含计算结果和输出文件路径的字典
    """

    # 添加salary项目到Python路径
    sys.path.insert(0, str(SALARY_WEB_APP))

    try:
        # 导入salary计算核心模块
        from attendance.pipeline import process_attendance_data
        from attendance.io_utils import load_attendance_file, load_employee_file
        import pandas as pd

        # 验证输入文件
        attendance_df = pd.read_excel(attendance_file)
        print(f"✅ 成功加载打卡数据: {len(attendance_df)} 条记录")

        # 加载其他可选文件
        employee_df = None
        if employee_file and Path(employee_file).exists():
            employee_df = pd.read_excel(employee_file)
            print(f"✅ 成功加载员工信息: {len(employee_df)} 条记录")

        leave_df = None
        if leave_file and Path(leave_file).exists():
            leave_df = pd.read_excel(leave_file)
            print(f"✅ 成功加载请假数据: {len(leave_df)} 条记录")

        # 执行核心计算流程
        print("\n📊 正在执行薪资计算流程...")

        results = process_attendance_data(
            attendance_data=attendance_df,
            employee_data=employee_df,
            leave_data=leave_df,
            month=month,
            config_overrides=config_overrides
        )

        # 确定输出目录
        if not output_dir:
            output_dir = Path.home() / "salary_output" / month.replace("-", "_")
        else:
            output_dir = Path(output_dir)

        output_dir.mkdir(parents=True, exist_ok=True)

        # 保存输出文件
        output_files = {}

        # 日级明细表
        if "daily_details" in results:
            daily_file = output_dir / f"日级考勤明细_{month}.xlsx"
            results["daily_details"].to_excel(daily_file, index=False)
            output_files["daily_details"] = str(daily_file)
            print(f"✅ 已保存日级明细表: {daily_file}")

        # 月度汇总表
        if "monthly_summary" in results:
            monthly_file = output_dir / f"月度考勤汇总_{month}.xlsx"
            results["monthly_summary"].to_excel(monthly_file, index=False)
            output_files["monthly_summary"] = str(monthly_file)
            print(f"✅ 已保存月度汇总表: {monthly_file}")

        # 迟到稽核表
        if "late_audit" in results:
            audit_file = output_dir / f"迟到稽核报表_{month}.xlsx"
            results["late_audit"].to_excel(audit_file, index=False)
            output_files["late_audit"] = str(audit_file)
            print(f"✅ 已保存迟到稽核表: {audit_file}")

        # 工资表
        if "payroll" in results:
            payroll_file = output_dir / f"工资汇总表_{month}.xlsx"
            results["payroll"].to_excel(payroll_file, index=False)
            output_files["payroll"] = str(payroll_file)
            print(f"✅ 已保存工资汇总表: {payroll_file}")

        # 数据质量报告
        if "quality_report" in results:
            quality_file = output_dir / f"数据质量报告_{month}.txt"
            with open(quality_file, 'w', encoding='utf-8') as f:
                f.write(results["quality_report"])
            output_files["quality_report"] = str(quality_file)
            print(f"✅ 已保存质量报告: {quality_file}")

        return {
            "status": "success",
            "month": month,
            "message": f"✅ {month} 月份薪资计算成功完成",
            "output_dir": str(output_dir),
            "output_files": output_files,
            "statistics": {
                "total_employees": len(attendance_df['姓名'].unique()) if '姓名' in attendance_df.columns else 0,
                "total_records": len(attendance_df),
                "calculation_time": datetime.now().isoformat()
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "month": month,
            "message": f"❌ 计算过程出错: {str(e)}",
            "error_details": str(e)
        }


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description="salary-calculator: 考勤与薪资自动核算"
    )

    parser.add_argument(
        "--month",
        required=True,
        help="计算月份 (格式: YYYY-MM, 例: 2025-01)"
    )

    parser.add_argument(
        "--attendance-file",
        required=True,
        help="打卡数据文件路径"
    )

    parser.add_argument(
        "--employee-file",
        help="员工信息文件路径 (可选)"
    )

    parser.add_argument(
        "--leave-file",
        help="请假申请文件路径 (可选)"
    )

    parser.add_argument(
        "--overtime-file",
        help="加班/出差文件路径 (可选)"
    )

    parser.add_argument(
        "--output-dir",
        help="输出目录 (可选，默认为 ~/salary_output/YYYY_MM/)"
    )

    parser.add_argument(
        "--late-deduction",
        type=int,
        help="迟到扣款额 (可选，默认50元)"
    )

    parser.add_argument(
        "--meal-allowance",
        type=int,
        help="每日餐补 (可选，默认15元)"
    )

    args = parser.parse_args()

    # 验证环境
    if not validate_environment():
        sys.exit(1)

    # 准备配置覆盖
    config_overrides = {}
    if args.late_deduction:
        config_overrides["late_deduction"] = args.late_deduction
    if args.meal_allowance:
        config_overrides["meal_allowance"] = args.meal_allowance

    # 执行计算
    result = run_salary_calculation(
        month=args.month,
        attendance_file=args.attendance_file,
        employee_file=args.employee_file,
        leave_file=args.leave_file,
        overtime_file=args.overtime_file,
        output_dir=args.output_dir,
        config_overrides=config_overrides if config_overrides else None
    )

    # 输出结果
    print("\n" + "="*60)
    print(result["message"])
    if result["status"] == "success":
        print(f"📁 输出目录: {result['output_dir']}")
        print(f"👥 处理员工数: {result['statistics']['total_employees']}")
        print(f"📊 打卡记录数: {result['statistics']['total_records']}")
        print("\n📄 生成的文件:")
        for file_type, file_path in result["output_files"].items():
            print(f"  - {file_type}: {file_path}")
    else:
        print(f"❌ 错误详情: {result.get('error_details', '未知错误')}")
    print("="*60)

    return 0 if result["status"] == "success" else 1


if __name__ == "__main__":
    sys.exit(main())
