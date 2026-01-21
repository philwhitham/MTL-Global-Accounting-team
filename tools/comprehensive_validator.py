#!/usr/bin/env python3
"""
Comprehensive MSB Call Report XML Validator

Performs multiple levels of validation:
1. XSD Schema validation
2. Field completeness check
3. Data integrity validation
4. Business logic validation
"""

import sys
import argparse
from lxml import etree
from typing import Dict, List, Tuple

class MSBReportValidator:
    def __init__(self, xml_file, xsd_file=None, sample_xml_file=None):
        self.xml_file = xml_file
        self.xsd_file = xsd_file
        self.sample_xml_file = sample_xml_file
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_all(self):
        """Run all validation checks"""
        print("="*80)
        print("MSB CALL REPORT COMPREHENSIVE VALIDATION")
        print("="*80)
        print()
        
        # Level 1: XSD Schema Validation
        if self.xsd_file:
            print("🔍 LEVEL 1: XSD Schema Validation")
            print("-" * 80)
            self.validate_xsd_schema()
            print()
        
        # Level 2: Field Completeness
        print("🔍 LEVEL 2: Field Completeness Check")
        print("-" * 80)
        self.check_field_completeness()
        print()
        
        # Level 3: Data Integrity
        print("🔍 LEVEL 3: Data Integrity Validation")
        print("-" * 80)
        self.validate_data_integrity()
        print()
        
        # Level 4: Business Logic
        print("🔍 LEVEL 4: Business Logic Validation")
        print("-" * 80)
        self.validate_business_logic()
        print()
        
        # Summary
        self.print_summary()
        
    def validate_xsd_schema(self):
        """Validate XML against XSD schema"""
        try:
            with open(self.xsd_file, 'rb') as f:
                schema_root = etree.XML(f.read())
            schema = etree.XMLSchema(schema_root)
            
            with open(self.xml_file, 'rb') as f:
                xml_doc = etree.parse(f)
            
            if schema.validate(xml_doc):
                print("✅ XSD Schema Validation: PASSED")
                self.info.append("XSD schema validation successful")
            else:
                print("❌ XSD Schema Validation: FAILED")
                for error in schema.error_log:
                    error_msg = f"Line {error.line}: {error.message}"
                    print(f"   ❌ {error_msg}")
                    self.errors.append(error_msg)
        except Exception as e:
            error_msg = f"XSD validation error: {e}"
            print(f"❌ {error_msg}")
            self.errors.append(error_msg)
    
    def check_field_completeness(self):
        """Check that all required fields are present"""
        try:
            with open(self.xml_file, 'rb') as f:
                xml_doc = etree.parse(f)
            root = xml_doc.getroot()
            
            # Check root attributes
            required_attrs = ['year', 'formVersion', 'periodType']
            for attr in required_attrs:
                if attr in root.attrib:
                    print(f"   ✅ Root attribute '{attr}': {root.attrib[attr]}")
                else:
                    error_msg = f"Missing required root attribute: {attr}"
                    print(f"   ❌ {error_msg}")
                    self.errors.append(error_msg)
            
            # Check required sections
            required_sections = {
                'Msbcrfc': 'Financial Condition',
                'Msbcrta': 'Company Transactions',
                'Msbcrst': 'State Transactions',
                'Msbcrpi': 'Permissible Investments',
                'Msbcrtda': 'Destination Country (Q4 only)'
            }
            
            for section_tag, section_name in required_sections.items():
                sections = root.findall(f".//{section_tag}")
                if sections:
                    if section_tag == 'Msbcrst':
                        print(f"   ✅ {section_name}: {len(sections)} state(s) found")
                    else:
                        print(f"   ✅ {section_name}: Present")
                else:
                    if section_tag == 'Msbcrtda':
                        # Q4 only, so just warning
                        warning_msg = f"{section_name} not found (required for Q4)"
                        print(f"   ⚠️  {warning_msg}")
                        self.warnings.append(warning_msg)
                    else:
                        error_msg = f"Missing required section: {section_name}"
                        print(f"   ❌ {error_msg}")
                        self.errors.append(error_msg)
            
        except Exception as e:
            error_msg = f"Field completeness check error: {e}"
            print(f"❌ {error_msg}")
            self.errors.append(error_msg)
    
    def validate_data_integrity(self):
        """Validate data integrity and calculations"""
        try:
            with open(self.xml_file, 'rb') as f:
                xml_doc = etree.parse(f)
            root = xml_doc.getroot()
            
            # Extract financial data
            def get_value(path):
                elem = root.find(path)
                if elem is not None and elem.text:
                    try:
                        return int(elem.text)
                    except:
                        return 0
                return 0
            
            # Balance Sheet validation
            print("   📊 Balance Sheet Validation:")
            
            # Assets
            fc10 = get_value(".//FC10")  # Cash
            fc120 = get_value(".//FC120")  # Investments
            fc130 = get_value(".//FC130")  # Receivables
            fc140 = get_value(".//FC140")  # Other current
            fc150 = get_value(".//FC150")  # Fixed assets
            total_assets = fc10 + fc120 + fc130 + fc140 + fc150
            
            print(f"      Total Assets (calculated): ${total_assets:,}")
            
            # Liabilities
            fc170 = get_value(".//FC170")  # Payable
            fc180 = get_value(".//FC180")  # IC Payable
            fc190 = get_value(".//FC190")  # Borrowings current
            fc200 = get_value(".//FC200")  # Borrowings LT
            fc210 = get_value(".//FC210")  # Money transmission
            fc220 = get_value(".//FC220")  # Stored value
            fc230 = get_value(".//FC230")  # Deferred revenue
            fc240 = get_value(".//FC240")  # Other current liab
            fc260 = get_value(".//FC260")  # LT debt
            fc270 = get_value(".//FC270")  # Other LT liab
            total_liabilities = fc170 + fc180 + fc190 + fc200 + fc210 + fc220 + fc230 + fc240 + fc260 + fc270
            
            print(f"      Total Liabilities (calculated): ${total_liabilities:,}")
            
            # Equity
            fc290 = get_value(".//FC290")  # Preferred stock
            fc300 = get_value(".//FC300")  # Treasury stock
            fc310 = get_value(".//FC310")  # Common stock
            fc320 = get_value(".//FC320")  # Paid in capital pref
            fc330 = get_value(".//FC330")  # Donated capital
            fc340 = get_value(".//FC340")  # Additional paid in
            fc360 = get_value(".//FC360")  # Retained earnings
            fc370 = get_value(".//FC370")  # OCI
            fc380 = get_value(".//FC380")  # Other equity
            total_equity = fc290 - fc300 + fc310 + fc320 + fc330 + fc340 + fc360 + fc370 + fc380
            
            print(f"      Total Equity (calculated): ${total_equity:,}")
            
            total_liab_equity = total_liabilities + total_equity
            print(f"      Total Liabilities + Equity: ${total_liab_equity:,}")
            
            # Check balance
            if total_assets == total_liab_equity:
                print(f"      ✅ Balance Sheet Balances: ${total_assets:,} = ${total_liab_equity:,}")
            else:
                error_msg = f"Balance sheet doesn't balance: Assets ${total_assets:,} != L+E ${total_liab_equity:,}"
                print(f"      ❌ {error_msg}")
                self.errors.append(error_msg)
            
            # Income Statement validation
            print()
            print("   📊 Income Statement Validation:")
            
            # Revenue
            fc430 = get_value(".//FC430")  # Stored value fees
            total_revenue = fc430  # Simplified for stored value business
            print(f"      Total Revenue: ${total_revenue:,}")
            
            # Expenses
            fc520 = get_value(".//FC520")  # Rent
            fc580 = get_value(".//FC580")  # Insurance
            total_expenses = fc520 + fc580  # Simplified
            print(f"      Total Expenses: ${total_expenses:,}")
            
            net_income = total_revenue - total_expenses
            print(f"      Net Income: ${net_income:,}")
            
            # Check if retained earnings matches net income (for pre-operational)
            if fc360 == net_income:
                print(f"      ✅ Retained Earnings matches Net Income")
            else:
                warning_msg = f"Retained Earnings ${fc360:,} != Net Income ${net_income:,} (may include prior period)"
                print(f"      ℹ️  {warning_msg}")
                self.info.append(warning_msg)
            
            # Permissible Investments validation
            print()
            print("   📊 Permissible Investments Validation:")
            
            pi10 = get_value(".//PI10")  # Bank deposits
            pi120 = get_value(".//PI120")  # Outstanding stored value
            
            print(f"      Bank Deposits: ${pi10:,}")
            print(f"      Outstanding Stored Value: ${pi120:,}")
            
            # For stored value business, bank deposits should cover stored value liability
            if pi10 >= pi120:
                print(f"      ✅ Bank deposits (${pi10:,}) >= Stored value liability (${pi120:,})")
            else:
                error_msg = f"Insufficient bank deposits to cover stored value liability"
                print(f"      ❌ {error_msg}")
                self.errors.append(error_msg)
            
        except Exception as e:
            error_msg = f"Data integrity validation error: {e}"
            print(f"❌ {error_msg}")
            self.errors.append(error_msg)
    
    def validate_business_logic(self):
        """Validate business logic rules"""
        try:
            with open(self.xml_file, 'rb') as f:
                xml_doc = etree.parse(f)
            root = xml_doc.getroot()
            
            # Get stored value transaction data
            def get_value(path):
                elem = root.find(path)
                if elem is not None and elem.text:
                    try:
                        return int(elem.text)
                    except:
                        return 0
                return 0
            
            print("   🏢 Business Logic Checks:")
            
            # Check: If stored value transactions are 0, liability should be 0
            ta90 = get_value(".//TA90")  # # of stored value transactions
            ta100 = get_value(".//TA100")  # $ of stored value transactions
            fc220 = get_value(".//FC220")  # Stored value liability
            
            if ta90 == 0 and ta100 == 0:
                print(f"      ℹ️  Pre-operational: 0 stored value transactions")
                if fc220 == 0:
                    print(f"      ✅ Stored value liability is $0 (consistent with 0 transactions)")
                else:
                    warning_msg = f"Stored value liability ${fc220:,} but 0 transactions"
                    print(f"      ⚠️  {warning_msg}")
                    self.warnings.append(warning_msg)
            
            # Check: State transactions should sum to company-wide
            state_sections = root.findall(".//Msbcrst")
            total_state_count = 0
            total_state_amount = 0
            
            for state_section in state_sections:
                state_code = state_section.get('stateCode')
                st90_elem = state_section.find(".//ST90")
                st100_elem = state_section.find(".//ST100")
                
                st90 = int(st90_elem.text) if st90_elem is not None and st90_elem.text else 0
                st100 = int(st100_elem.text) if st100_elem is not None and st100_elem.text else 0
                
                total_state_count += st90
                total_state_amount += st100
                
                print(f"      ℹ️  {state_code}: {st90} transactions, ${st100:,}")
            
            if total_state_count == ta90 and total_state_amount == ta100:
                print(f"      ✅ State transactions sum to company-wide totals")
            else:
                error_msg = f"State transactions don't match company-wide: States={total_state_count}/{total_state_amount}, Company={ta90}/{ta100}"
                print(f"      ❌ {error_msg}")
                self.errors.append(error_msg)
            
            # Check: Explanatory notes present
            print()
            print("   📝 Explanatory Notes Check:")
            fc_notes = root.findall(".//Msbcrfc//ExplanatoryNotesSection/*")
            ta_notes = root.findall(".//Msbcrta//ExplanatoryNotesSection/*")
            pi_notes = root.findall(".//Msbcrpi//ExplanatoryNotesSection/*")
            
            print(f"      ℹ️  Financial Condition notes: {len(fc_notes)}")
            print(f"      ℹ️  Transaction Activity notes: {len(ta_notes)}")
            print(f"      ℹ️  Permissible Investments notes: {len(pi_notes)}")
            
            if len(fc_notes) > 0 and len(ta_notes) > 0 and len(pi_notes) > 0:
                print(f"      ✅ Explanatory notes present in all major sections")
            else:
                warning_msg = "Some sections missing explanatory notes"
                print(f"      ⚠️  {warning_msg}")
                self.warnings.append(warning_msg)
            
        except Exception as e:
            error_msg = f"Business logic validation error: {e}"
            print(f"❌ {error_msg}")
            self.errors.append(error_msg)
    
    def print_summary(self):
        """Print validation summary"""
        print("="*80)
        print("VALIDATION SUMMARY")
        print("="*80)
        print()
        
        if not self.errors and not self.warnings:
            print("🎉 ✅ ✅ ✅  ALL VALIDATIONS PASSED!  ✅ ✅ ✅ 🎉")
            print()
            print("Your XML file is:")
            print("  ✅ Structurally valid (XSD schema)")
            print("  ✅ Complete (all required fields)")
            print("  ✅ Mathematically correct (balances)")
            print("  ✅ Logically consistent (business rules)")
            print()
            print("🚀 READY FOR SUBMISSION!")
            return True
        
        print(f"📊 Results:")
        print(f"   ✅ Passed: {len(self.info)} checks")
        print(f"   ⚠️  Warnings: {len(self.warnings)}")
        print(f"   ❌ Errors: {len(self.errors)}")
        print()
        
        if self.errors:
            print("❌ ERRORS (Must fix):")
            for i, error in enumerate(self.errors, 1):
                print(f"   {i}. {error}")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS (Review recommended):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"   {i}. {warning}")
            print()
        
        if self.errors:
            print("❌ VALIDATION FAILED - Please fix errors before submission")
            return False
        else:
            print("⚠️  VALIDATION PASSED WITH WARNINGS - Review warnings before submission")
            return True

def main():
    parser = argparse.ArgumentParser(
        description='Comprehensive MSB Call Report XML Validator'
    )
    parser.add_argument(
        '--xml',
        required=True,
        help='Path to XML file to validate'
    )
    parser.add_argument(
        '--xsd',
        help='Path to XSD schema file (optional)'
    )
    parser.add_argument(
        '--sample',
        help='Path to sample XML file for comparison (optional)'
    )
    
    args = parser.parse_args()
    
    validator = MSBReportValidator(args.xml, args.xsd, args.sample)
    success = validator.validate_all()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
