#!/usr/bin/env python3
"""
MSB Call Report XML Side-by-Side Comparator

Compares your XML against the NMLS sample XML to identify:
- Structure differences
- Missing fields
- Extra fields
- Format differences
"""

import sys
import argparse
from lxml import etree
from typing import Dict, List, Set

class XMLComparator:
    def __init__(self, your_xml, sample_xml):
        self.your_xml = your_xml
        self.sample_xml = sample_xml
        self.differences = []
        self.missing_fields = []
        self.extra_fields = []
        self.format_differences = []
        
    def compare(self):
        """Main comparison function"""
        print("="*80)
        print("MSB CALL REPORT XML SIDE-BY-SIDE COMPARISON")
        print("="*80)
        print()
        print(f"Your XML:   {self.your_xml}")
        print(f"Sample XML: {self.sample_xml}")
        print()
        
        # Parse both files
        with open(self.your_xml, 'rb') as f:
            your_tree = etree.parse(f)
        with open(self.sample_xml, 'rb') as f:
            sample_tree = etree.parse(f)
        
        your_root = your_tree.getroot()
        sample_root = sample_tree.getroot()
        
        # Compare structure
        print("🔍 STRUCTURE COMPARISON")
        print("-" * 80)
        self.compare_structure(your_root, sample_root)
        print()
        
        # Compare attributes
        print("🔍 ATTRIBUTE COMPARISON")
        print("-" * 80)
        self.compare_attributes(your_root, sample_root)
        print()
        
        # Compare sections
        print("🔍 SECTION-BY-SECTION COMPARISON")
        print("-" * 80)
        self.compare_sections(your_root, sample_root)
        print()
        
        # Summary
        self.print_summary()
    
    def get_all_paths(self, element, prefix=""):
        """Get all element paths in XML tree"""
        paths = set()
        tag = element.tag
        current_path = f"{prefix}/{tag}" if prefix else tag
        paths.add(current_path)
        
        for child in element:
            child_paths = self.get_all_paths(child, current_path)
            paths.update(child_paths)
        
        return paths
    
    def compare_structure(self, your_root, sample_root):
        """Compare overall structure"""
        your_paths = self.get_all_paths(your_root)
        sample_paths = self.get_all_paths(sample_root)
        
        # Find differences
        only_in_yours = your_paths - sample_paths
        only_in_sample = sample_paths - your_paths
        in_both = your_paths & sample_paths
        
        print(f"   ✅ Common elements: {len(in_both)}")
        print(f"   ℹ️  In your XML only: {len(only_in_yours)}")
        print(f"   ℹ️  In sample only: {len(only_in_sample)}")
        
        if only_in_yours:
            print()
            print("   🔹 Elements in YOUR XML (not in sample):")
            for path in sorted(only_in_yours):
                print(f"      • {path}")
                self.extra_fields.append(path)
        
        if only_in_sample:
            print()
            print("   🔹 Elements in SAMPLE XML (not in yours):")
            for path in sorted(only_in_sample):
                print(f"      • {path}")
                self.missing_fields.append(path)
    
    def compare_attributes(self, your_root, sample_root):
        """Compare root attributes"""
        your_attrs = your_root.attrib
        sample_attrs = sample_root.attrib
        
        print(f"   Your Attributes:")
        for key, value in your_attrs.items():
            sample_value = sample_attrs.get(key)
            if sample_value:
                if value != sample_value:
                    print(f"      ⚠️  {key}: '{value}' (sample has '{sample_value}')")
                    self.format_differences.append(f"Attribute {key}: yours='{value}', sample='{sample_value}'")
                else:
                    print(f"      ✅ {key}: '{value}'")
            else:
                print(f"      ℹ️  {key}: '{value}' (not in sample)")
        
        print()
        print(f"   Sample Attributes:")
        for key, value in sample_attrs.items():
            if key not in your_attrs:
                print(f"      ⚠️  {key}: '{value}' (MISSING in your XML)")
                self.missing_fields.append(f"Root attribute: {key}")
    
    def compare_sections(self, your_root, sample_root):
        """Compare major sections"""
        sections = [
            ('Msbcrfc', 'Financial Condition'),
            ('Msbcrta', 'Company Transactions'),
            ('Msbcrst', 'State Transactions'),
            ('Msbcrpi', 'Permissible Investments'),
            ('Msbcrtda', 'Destination Country'),
        ]
        
        for section_tag, section_name in sections:
            print(f"\n   📁 {section_name} ({section_tag}):")
            
            your_sections = your_root.findall(f".//{section_tag}")
            sample_sections = sample_root.findall(f".//{section_tag}")
            
            if not your_sections and not sample_sections:
                print(f"      ℹ️  Not present in either file")
                continue
            
            if not your_sections:
                print(f"      ⚠️  MISSING in your XML")
                self.missing_fields.append(f"Section: {section_tag}")
                continue
            
            if not sample_sections:
                print(f"      ℹ️  Present in your XML, not in sample")
                continue
            
            # For state transactions, we may have different states
            if section_tag == 'Msbcrst':
                your_states = [s.get('stateCode') for s in your_sections]
                sample_states = [s.get('stateCode') for s in sample_sections]
                print(f"      Your states: {', '.join(your_states)}")
                print(f"      Sample states: {', '.join(sample_states)}")
                continue
            
            # Compare field counts
            your_section = your_sections[0]
            sample_section = sample_sections[0]
            
            your_fields = [elem.tag for elem in your_section.iter() if elem.text]
            sample_fields = [elem.tag for elem in sample_section.iter() if elem.text]
            
            print(f"      Your XML: {len(your_fields)} populated fields")
            print(f"      Sample XML: {len(sample_fields)} populated fields")
            
            # Find field differences
            your_field_set = set(your_fields)
            sample_field_set = set(sample_fields)
            
            only_yours = your_field_set - sample_field_set
            only_sample = sample_field_set - your_field_set
            
            if only_yours:
                print(f"      ℹ️  Fields only in your XML: {len(only_yours)}")
                for field in sorted(only_yours):
                    if field not in [section_tag, 'ExplanatoryNotesSection']:
                        print(f"         • {field}")
            
            if only_sample:
                print(f"      ℹ️  Fields only in sample: {len(only_sample)}")
                for field in sorted(only_sample):
                    if field not in [section_tag, 'ExplanatoryNotesSection']:
                        print(f"         • {field}")
    
    def print_summary(self):
        """Print comparison summary"""
        print("="*80)
        print("COMPARISON SUMMARY")
        print("="*80)
        print()
        
        total_issues = len(self.missing_fields) + len(self.format_differences)
        
        if total_issues == 0:
            print("🎉 ✅ NO CRITICAL DIFFERENCES FOUND!")
            print()
            print("Your XML structure matches the sample XML format.")
            print()
            print("ℹ️  Note: Some differences are expected:")
            print("   • Different values (your data vs sample data)")
            print("   • Different states (your licensed states vs sample)")
            print("   • Different number of populated fields (pre-operational vs operational)")
            print()
            return True
        
        print(f"📊 Comparison Results:")
        print(f"   ⚠️  Missing fields: {len(self.missing_fields)}")
        print(f"   ℹ️  Extra fields: {len(self.extra_fields)}")
        print(f"   ⚠️  Format differences: {len(self.format_differences)}")
        print()
        
        if self.missing_fields:
            print("⚠️  MISSING FIELDS (Review these):")
            for i, field in enumerate(self.missing_fields[:10], 1):
                print(f"   {i}. {field}")
            if len(self.missing_fields) > 10:
                print(f"   ... and {len(self.missing_fields) - 10} more")
            print()
        
        if self.format_differences:
            print("⚠️  FORMAT DIFFERENCES:")
            for i, diff in enumerate(self.format_differences, 1):
                print(f"   {i}. {diff}")
            print()
        
        print("ℹ️  RECOMMENDATION:")
        print("   Review the differences above. Many differences are expected")
        print("   (e.g., your data vs sample data, your states vs sample states).")
        print("   Focus on any structural or format differences.")
        
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Compare your MSB Call Report XML against NMLS sample XML'
    )
    parser.add_argument(
        '--your-xml',
        required=True,
        help='Path to your XML file'
    )
    parser.add_argument(
        '--sample-xml',
        required=True,
        help='Path to NMLS sample XML file'
    )
    
    args = parser.parse_args()
    
    comparator = XMLComparator(args.your_xml, args.sample_xml)
    comparator.compare()

if __name__ == "__main__":
    main()
