#!/usr/bin/env python3
"""
Quick script to read Excel files and display their contents
"""
import pandas as pd
import sys

def read_excel_file(filepath):
    """Read an Excel file and print basic info about its sheets"""
    try:
        # Read all sheets
        excel_file = pd.ExcelFile(filepath)
        print(f"\n📊 Excel File: {filepath}")
        print(f"📋 Number of sheets: {len(excel_file.sheet_names)}")
        print(f"📝 Sheet names: {excel_file.sheet_names}\n")
        
        # Read each sheet and display
        for sheet_name in excel_file.sheet_names:
            print(f"\n{'='*80}")
            print(f"SHEET: {sheet_name}")
            print(f"{'='*80}\n")
            
            df = pd.read_excel(filepath, sheet_name=sheet_name)
            print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
            print(f"\nColumn names: {list(df.columns)}\n")
            print(df.head(50).to_string())
            print("\n")
            
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 read_excel.py <excel_file>")
        sys.exit(1)
    
    read_excel_file(sys.argv[1])
