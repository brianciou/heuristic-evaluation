#!/usr/bin/env python3
"""
Invoke Virtual Expert - Generate evaluation report in Evaluation Form format.

Usage:
    python invoke_virtual_expert.py --findings findings.json --product-name "Product Name" --evaluator "Your Name" --output report.xlsx
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    print("Error: openpyxl is required. Install it with: pip install openpyxl")
    exit(1)


def create_evaluation_form(wb, findings):
    """Create Evaluation Form sheet with findings."""
    ws = wb.create_sheet("Evaluation Form", 0)
    
    headers = ["Task", "Violated Heuristic", "Description", "Screenshot", "Severity"]
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True)
    
    for col, header in enumerate(headers, 1):
        cell = ws.cell(1, col, header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='top', wrap_text=True)
    
    # Nielsen's 10 Heuristics dropdown
    heuristics_list = (
        "1. Visibility of system status,"
        "2. Match between system and real world,"
        "3. User control and freedom,"
        "4. Consistency and standards,"
        "5. Error prevention,"
        "6. Recognition rather than recall,"
        "7. Flexibility and efficiency of use,"
        "8. Aesthetic and minimalist design,"
        "9. Help users recognize/diagnose/recover from errors,"
        "10. Help and documentation"
    )
    
    heuristic_validation = DataValidation(type="list", formula1=f'"{heuristics_list}"')
    ws.add_data_validation(heuristic_validation)
    
    severity_validation = DataValidation(type="list", formula1='"Critical,High,Medium,Low"')
    ws.add_data_validation(severity_validation)
    
    # Add findings
    for row_idx, finding in enumerate(findings, 2):
        # Task (from location) - Bold font
        task_cell = ws.cell(row_idx, 1, finding.get('location', ''))
        task_cell.font = Font(bold=True)
        task_cell.alignment = Alignment(wrap_text=True, vertical='top')
        
        # Violated Heuristic
        heuristic_cell = ws.cell(row_idx, 2, finding.get('heuristic', ''))
        heuristic_cell.alignment = Alignment(wrap_text=True, vertical='top')
        
        # Description (problem + recommendation)
        description = finding.get('description', '')
        recommendation = finding.get('recommendation', '')
        combined_desc = f"{description}\n\nRecommendation: {recommendation}" if recommendation else description
        desc_cell = ws.cell(row_idx, 3, combined_desc)
        desc_cell.alignment = Alignment(wrap_text=True, vertical='top')
        
        # Screenshot (empty or note)
        screenshot_cell = ws.cell(row_idx, 4, finding.get('screenshot', ''))
        screenshot_cell.alignment = Alignment(wrap_text=True, vertical='top')
        
        # Severity
        severity = finding.get('severity', 'Medium')
        severity_cell = ws.cell(row_idx, 5, severity)
        severity_cell.alignment = Alignment(horizontal='center', vertical='top')
        
        # Apply validation
        heuristic_validation.add(heuristic_cell)
        severity_validation.add(severity_cell)
        
        # Color coding for severity (softer colors)
        if severity == "Critical":
            severity_cell.fill = PatternFill(start_color="FF6B6B", end_color="FF6B6B", fill_type="solid")
            severity_cell.font = Font(bold=True)
        elif severity == "High":
            severity_cell.fill = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid")
            severity_cell.font = Font(bold=True)
        elif severity == "Medium":
            severity_cell.fill = PatternFill(start_color="FFD93D", end_color="FFD93D", fill_type="solid")
            severity_cell.font = Font(bold=True)
        else:  # Low
            severity_cell.fill = PatternFill(start_color="95D5B2", end_color="95D5B2", fill_type="solid")
            severity_cell.font = Font(bold=True)
    
    # Column widths
    ws.column_dimensions['A'].width = 20  # Task
    ws.column_dimensions['B'].width = 35  # Violated Heuristic
    ws.column_dimensions['C'].width = 50  # Description
    ws.column_dimensions['D'].width = 15  # Screenshot
    ws.column_dimensions['E'].width = 12  # Severity
    
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f"A1:E{len(findings) + 1}"


def main():
    parser = argparse.ArgumentParser(description='Invoke Virtual Expert - Generate evaluation report')
    parser.add_argument('--findings', required=True, help='Path to findings JSON file')
    parser.add_argument('--product-name', required=True, help='Product name')
    parser.add_argument('--evaluator', required=True, help='Evaluator name')
    parser.add_argument('--output', default='virtual-expert-report.xlsx', help='Output Excel file')
    
    args = parser.parse_args()
    
    with open(args.findings, 'r', encoding='utf-8') as f:
        findings = json.load(f)
    
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    create_evaluation_form(wb, findings)
    
    output_path = Path(args.output)
    wb.save(output_path)
    
    print(f"✓ Virtual Expert report generated: {output_path.absolute()}")
    print(f"  Total findings: {len(findings)}")
    print(f"  Product: {args.product_name}")
    print(f"  Evaluated by: {args.evaluator}")


if __name__ == '__main__':
    main()
