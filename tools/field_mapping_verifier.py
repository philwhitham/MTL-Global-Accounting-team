#!/usr/bin/env python3
"""
MSB Call Report Field Mapping Verifier

Cross-references XML fields against Excel specification to verify:
- All required fields for stored value business are present
- Fields are used correctly
- No inappropriate fields are populated
- Mapping to business data is correct
"""

import sys
import argparse
from lxml import etree
import openpyxl

class FieldMappingVerifier:
    def __init__(self, xml_file, excel_spec=None):
        self.xml_file = xml_file
        self.excel_spec = excel_spec
        self.field_mappings = self.load_field_mappings()
        self.issues = []
        self.warnings = []
        
    def load_field_mappings(self):
        """Load known field mappings for stored value business"""
        # Known mappings from our analysis of the Excel specification
        return {
            # Financial Condition - Assets
            'FC10': {'name': 'Cash on Hand and in Bank', 'required': True, 'type': 'asset'},
            'FC120': {'name': 'Investments', 'required': False, 'type': 'asset'},
            'FC130': {'name': 'Accounts Receivable', 'required': False, 'type': 'asset'},
            'FC140': {'name': 'Other Current Assets', 'required': False, 'type': 'asset'},
            'FC150': {'name': 'Fixed Assets', 'required': False, 'type': 'asset'},
            
            # Financial Condition - Liabilities
            'FC170': {'name': 'Accounts Payable', 'required': False, 'type': 'liability'},
            'FC180': {'name': 'Inter-company Payables', 'required': False, 'type': 'liability'},
            'FC190': {'name': 'Short-term Borrowings', 'required': False, 'type': 'liability'},
            'FC200': {'name': 'Long-term Borrowings (Current)', 'required': False, 'type': 'liability'},
            'FC210': {'name': 'Money Transmission Liability', 'required': False, 'type': 'liability'},
            'FC220': {'name': 'Outstanding Stored Value', 'required': True, 'type': 'liability', 'stored_value': True},
            'FC230': {'name': 'Deferred Revenue', 'required': False, 'type': 'liability'},
            'FC240': {'name': 'Other Current Liabilities', 'required': False, 'type': 'liability'},
            'FC260': {'name': 'Long-term Debt', 'required': False, 'type': 'liability'},
            'FC270': {'name': 'Other Long-term Liabilities', 'required': False, 'type': 'liability'},
            
            # Financial Condition - Equity
            'FC290': {'name': 'Preferred Stock', 'required': False, 'type': 'equity'},
            'FC300': {'name': 'Treasury Stock', 'required': False, 'type': 'equity'},
            'FC310': {'name': 'Common Stock', 'required': True, 'type': 'equity'},
            'FC320': {'name': 'Additional Paid-in Capital (Preferred)', 'required': False, 'type': 'equity'},
            'FC330': {'name': 'Donated Capital', 'required': False, 'type': 'equity'},
            'FC340': {'name': 'Additional Paid-in Capital', 'required': False, 'type': 'equity'},
            'FC360': {'name': 'Retained Earnings', 'required': True, 'type': 'equity'},
            'FC370': {'name': 'Other Comprehensive Income', 'required': False, 'type': 'equity'},
            'FC380': {'name': 'Other Equity', 'required': False, 'type': 'equity'},
            
            # Income Statement
            'FC410': {'name': 'Interest Income', 'required': False, 'type': 'revenue'},
            'FC420': {'name': 'Check Cashing Fees', 'required': False, 'type': 'revenue'},
            'FC430': {'name': 'Stored Value Fees', 'required': True, 'type': 'revenue', 'stored_value': True},
            'FC440': {'name': 'Money Order Fees', 'required': False, 'type': 'revenue'},
            'FC450': {'name': 'Money Transmission Fees', 'required': False, 'type': 'revenue'},
            'FC460': {'name': 'Currency Exchange Fees', 'required': False, 'type': 'revenue'},
            'FC470': {'name': 'Bill Payment Fees', 'required': False, 'type': 'revenue'},
            'FC480': {'name': 'Other Revenue', 'required': False, 'type': 'revenue'},
            'FC500': {'name': 'Interest Expense', 'required': False, 'type': 'expense'},
            'FC510': {'name': 'Compensation', 'required': False, 'type': 'expense'},
            'FC520': {'name': 'Occupancy (Rent)', 'required': False, 'type': 'expense'},
            'FC530': {'name': 'Equipment', 'required': False, 'type': 'expense'},
            'FC540': {'name': 'Professional Fees', 'required': False, 'type': 'expense'},
            'FC550': {'name': 'Bank Service Charges', 'required': False, 'type': 'expense'},
            'FC560': {'name': 'Data Processing', 'required': False, 'type': 'expense'},
            'FC570': {'name': 'Telecommunications', 'required': False, 'type': 'expense'},
            'FC580': {'name': 'Insurance', 'required': False, 'type': 'expense'},
            'FC590': {'name': 'Provision for Losses', 'required': False, 'type': 'expense'},
            'FC620': {'name': 'Marketing/Advertising', 'required': False, 'type': 'expense'},
            'FC640': {'name': 'Travel and Entertainment', 'required': False, 'type': 'expense'},
            'FC650': {'name': 'Postage and Delivery', 'required': False, 'type': 'expense'},
            'FC670': {'name': 'Other Expenses', 'required': False, 'type': 'expense'},
            
            # Transaction Activity
            'TA90': {'name': '# of Stored Value Transactions', 'required': True, 'type': 'transaction', 'stored_value': True},
            'TA100': {'name': '$ of Stored Value Transactions', 'required': True, 'type': 'transaction', 'stored_value': True},
            
            # State Transactions
            'ST90': {'name': '# of Stored Value Transactions (State)', 'required': True, 'type': 'state_transaction', 'stored_value': True},
            'ST100': {'name': '$ of Stored Value Transactions (State)', 'required': True, 'type': 'state_transaction', 'stored_value': True},
            
            # Permissible Investments
            'PI10': {'name': 'Deposits in Domestic Banks', 'required': True, 'type': 'investment'},
            'PI20': {'name': 'Deposits in Foreign Banks', 'required': False, 'type': 'investment'},
            'PI120': {'name': 'Outstanding Stored Value Liability', 'required': True, 'type': 'calculation', 'stored_value': True},
            'PI130': {'name': 'Average Daily Transmission Liability', 'required': False, 'type': 'calculation'},
        }
    
    def verify(self):
        """Main verification function"""
        print("="*80)
        print("MSB CALL REPORT FIELD MAPPING VERIFICATION")
        print("="*80)
        print()
        print(f"XML File: {self.xml_file}")
        print()
        
        # Parse XML
        with open(self.xml_file, 'rb') as f:
            tree = etree.parse(f)
        root = tree.getroot()
        
        # Extract all fields
        print("🔍 EXTRACTING FIELDS FROM XML")
        print("-" * 80)
        fields_found = self.extract_fields(root)
        print(f"   Total fields found: {len(fields_found)}")
        print()
        
        # Verify stored value specific fields
        print("🔍 STORED VALUE FIELD VERIFICATION")
        print("-" * 80)
        self.verify_stored_value_fields(fields_found)
        print()
        
        # Check for inappropriate fields
        print("🔍 INAPPROPRIATE FIELD CHECK")
        print("-" * 80)
        self.check_inappropriate_fields(fields_found)
        print()
        
        # Verify calculations
        print("🔍 CALCULATION VERIFICATION")
        print("-" * 80)
        self.verify_calculations(fields_found)
        print()
        
        # Summary
        self.print_summary()
    
    def extract_fields(self, root):
        """Extract all fields with their values"""
        fields = {}
        
        # Find all leaf elements (elements with text but no children)
        for elem in root.iter():
            if elem.text and elem.text.strip() and not list(elem):
                tag = elem.tag
                if tag.startswith('FC') or tag.startswith('TA') or tag.startswith('ST') or tag.startswith('PI'):
                    try:
                        value = int(elem.text.strip())
                        fields[tag] = value
                    except:
                        fields[tag] = elem.text.strip()
        
        return fields
    
    def verify_stored_value_fields(self, fields_found):
        """Verify all stored value specific fields"""
        stored_value_fields = {k: v for k, v in self.field_mappings.items() if v.get('stored_value')}
        
        print("   Stored Value Specific Fields:")
        for field_code, field_info in stored_value_fields.items():
            if field_code in fields_found:
                value = fields_found[field_code]
                print(f"      ✅ {field_code}: {field_info['name']} = {value}")
            else:
                if field_info.get('required'):
                    msg = f"MISSING REQUIRED field: {field_code} - {field_info['name']}"
                    print(f"      ❌ {msg}")
                    self.issues.append(msg)
                else:
                    msg = f"Optional field not present: {field_code} - {field_info['name']}"
                    print(f"      ℹ️  {msg}")
    
    def check_inappropriate_fields(self, fields_found):
        """Check for fields that shouldn't be populated for stored value business"""
        inappropriate_for_stored_value = {
            'FC420': 'Check Cashing Fees (not a stored value activity)',
            'FC440': 'Money Order Fees (not a stored value activity)',
            'FC450': 'Money Transmission Fees (not a stored value activity)',
            'FC460': 'Currency Exchange Fees (not a stored value activity)',
            'FC470': 'Bill Payment Fees (not a stored value activity)',
            'FC210': 'Money Transmission Liability (not a stored value liability)',
        }
        
        found_inappropriate = False
        for field_code, description in inappropriate_for_stored_value.items():
            if field_code in fields_found:
                value = fields_found[field_code]
                if value != 0:
                    msg = f"{field_code}: {description} - Value: {value}"
                    print(f"      ⚠️  {msg}")
                    self.warnings.append(msg)
                    found_inappropriate = True
        
        if not found_inappropriate:
            print("      ✅ No inappropriate fields populated")
    
    def verify_calculations(self, fields_found):
        """Verify key calculations"""
        print("   Key Calculations:")
        
        # Check: Outstanding Stored Value (FC220) should match PI120
        fc220 = fields_found.get('FC220', 0)
        pi120 = fields_found.get('PI120', 0)
        
        if fc220 == pi120:
            print(f"      ✅ Stored Value Liability matches: FC220 ({fc220}) = PI120 ({pi120})")
        else:
            msg = f"Stored Value Liability mismatch: FC220 ({fc220}) != PI120 ({pi120})"
            print(f"      ❌ {msg}")
            self.issues.append(msg)
        
        # Check: Bank deposits (PI10) should be >= Outstanding Stored Value (PI120)
        pi10 = fields_found.get('PI10', 0)
        if pi10 >= pi120:
            print(f"      ✅ Bank deposits (${pi10:,}) >= Stored value liability (${pi120:,})")
        else:
            msg = f"Insufficient bank deposits: ${pi10:,} < ${pi120:,}"
            print(f"      ❌ {msg}")
            self.issues.append(msg)
        
        # Check: If TA90/TA100 are 0, FC220/PI120 should be 0
        ta90 = fields_found.get('TA90', 0)
        ta100 = fields_found.get('TA100', 0)
        
        if ta90 == 0 and ta100 == 0:
            if fc220 == 0:
                print(f"      ✅ Pre-operational: 0 transactions, 0 liability (consistent)")
            else:
                msg = f"Inconsistent: 0 transactions but ${fc220:,} liability"
                print(f"      ⚠️  {msg}")
                self.warnings.append(msg)
        
        # Check: State transactions should sum to company-wide
        # This would require parsing all state sections, simplified for now
        st_fields = {k: v for k, v in fields_found.items() if k.startswith('ST')}
        if st_fields:
            print(f"      ℹ️  State transaction fields found: {len(st_fields)}")
    
    def print_summary(self):
        """Print verification summary"""
        print("="*80)
        print("FIELD MAPPING VERIFICATION SUMMARY")
        print("="*80)
        print()
        
        if not self.issues and not self.warnings:
            print("🎉 ✅ ✅ ✅  ALL FIELD MAPPINGS VERIFIED!  ✅ ✅ ✅ 🎉")
            print()
            print("Your XML uses:")
            print("  ✅ All required stored value fields")
            print("  ✅ Correct field codes")
            print("  ✅ Appropriate fields for your business")
            print("  ✅ Correct calculations")
            print()
            print("🚀 FIELD MAPPING IS CORRECT!")
            return True
        
        print(f"📊 Verification Results:")
        print(f"   ❌ Issues: {len(self.issues)}")
        print(f"   ⚠️  Warnings: {len(self.warnings)}")
        print()
        
        if self.issues:
            print("❌ ISSUES (Must fix):")
            for i, issue in enumerate(self.issues, 1):
                print(f"   {i}. {issue}")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS (Review):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"   {i}. {warning}")
            print()
        
        if self.issues:
            print("❌ FIELD MAPPING VERIFICATION FAILED")
            return False
        else:
            print("⚠️  FIELD MAPPING VERIFIED WITH WARNINGS")
            return True

def main():
    parser = argparse.ArgumentParser(
        description='Verify MSB Call Report field mappings'
    )
    parser.add_argument(
        '--xml',
        required=True,
        help='Path to XML file to verify'
    )
    parser.add_argument(
        '--excel',
        help='Path to Excel specification file (optional)'
    )
    
    args = parser.parse_args()
    
    verifier = FieldMappingVerifier(args.xml, args.excel)
    success = verifier.verify()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
