#!/usr/bin/env python3
"""
MSB Call Report XML Validator
Validates XML files against the official XSD schema
"""

import sys
import argparse
from lxml import etree

def validate_xml(xml_file, xsd_file):
    """
    Validate an XML file against an XSD schema.
    
    Args:
        xml_file (str): Path to the XML file to validate
        xsd_file (str): Path to the XSD schema file
        
    Returns:
        tuple: (is_valid, messages) where is_valid is boolean and messages is list of strings
    """
    messages = []
    
    try:
        # Parse the XSD schema
        messages.append(f"📄 Reading XSD schema: {xsd_file}")
        with open(xsd_file, 'rb') as f:
            schema_root = etree.XML(f.read())
        schema = etree.XMLSchema(schema_root)
        messages.append("✅ XSD schema parsed successfully")
        
        # Parse the XML file
        messages.append(f"\n📄 Reading XML file: {xml_file}")
        with open(xml_file, 'rb') as f:
            xml_doc = etree.parse(f)
        messages.append("✅ XML file parsed successfully")
        
        # Validate
        messages.append("\n🔍 Validating XML against schema...")
        is_valid = schema.validate(xml_doc)
        
        if is_valid:
            messages.append("✅ ✅ ✅ VALIDATION SUCCESSFUL! ✅ ✅ ✅")
            messages.append("\n🎉 The XML file is valid and conforms to the XSD schema.")
            return True, messages
        else:
            messages.append("❌ ❌ ❌ VALIDATION FAILED! ❌ ❌ ❌")
            messages.append("\n🚨 Validation errors found:")
            for error in schema.error_log:
                messages.append(f"   Line {error.line}, Column {error.column}: {error.message}")
            return False, messages
            
    except etree.XMLSyntaxError as e:
        messages.append(f"❌ XML Syntax Error: {e}")
        return False, messages
    except FileNotFoundError as e:
        messages.append(f"❌ File not found: {e}")
        return False, messages
    except Exception as e:
        messages.append(f"❌ Unexpected error: {e}")
        return False, messages

def main():
    parser = argparse.ArgumentParser(
        description='Validate MSB Call Report XML against XSD schema'
    )
    parser.add_argument(
        '--xml',
        required=True,
        help='Path to XML file to validate'
    )
    parser.add_argument(
        '--xsd',
        required=True,
        help='Path to XSD schema file'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Only show errors (no success messages)'
    )
    
    args = parser.parse_args()
    
    is_valid, messages = validate_xml(args.xml, args.xsd)
    
    # Print messages
    for msg in messages:
        print(msg)
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()
