#!/usr/bin/env python3
"""
MSB Call Report XML Validation

This script validates XML files for Money Services Business Call Reports
against NMLS specifications and schema requirements.
"""

import argparse
import xml.etree.ElementTree as ET
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MSBCallReportValidator:
    """Validates MSB Call Report XML files according to NMLS specifications."""
    
    def __init__(self):
        """Initialize the validator."""
        self.errors = []
        self.warnings = []
        
    def validate_xml_structure(self, xml_file):
        """
        Validate basic XML structure and required elements.
        
        Args:
            xml_file (str): Path to the XML file to validate
            
        Returns:
            bool: True if validation passes, False otherwise
        """
        try:
            # Parse XML file
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            logger.info(f"Validating XML file: {xml_file}")
            
            # Check root element
            if root.tag != "MSBCallReport":
                self.errors.append("Root element must be 'MSBCallReport'")
                return False
            
            # Check required attributes
            required_attrs = ["FormVersion", "CompanyName", "CompanyID", "GenerationDate"]
            for attr in required_attrs:
                if attr not in root.attrib:
                    self.errors.append(f"Missing required attribute: {attr}")
            
            # Check required child elements
            required_elements = ["ReportingPeriod", "FinancialCondition", "CompanyTransactions"]
            for element in required_elements:
                if root.find(element) is None:
                    self.errors.append(f"Missing required element: {element}")
            
            # Validate reporting period
            self._validate_reporting_period(root)
            
            # Validate sections based on quarter
            self._validate_sections_by_quarter(root)
            
            # Check for any errors
            if self.errors:
                logger.error("Validation failed with the following errors:")
                for error in self.errors:
                    logger.error(f"  - {error}")
                return False
            
            if self.warnings:
                logger.warning("Validation completed with warnings:")
                for warning in self.warnings:
                    logger.warning(f"  - {warning}")
            
            logger.info("XML validation completed successfully")
            return True
            
        except ET.ParseError as e:
            logger.error(f"XML parsing error: {e}")
            return False
        except Exception as e:
            logger.error(f"Validation error: {e}")
            return False
    
    def _validate_reporting_period(self, root):
        """Validate the reporting period element."""
        reporting_period = root.find("ReportingPeriod")
        if reporting_period is not None:
            quarter = reporting_period.get("Quarter")
            year = reporting_period.get("Year")
            
            if not quarter or quarter not in ["Q1", "Q2", "Q3", "Q4"]:
                self.errors.append("Invalid quarter value in ReportingPeriod")
            
            if not year or not year.isdigit():
                self.errors.append("Invalid year value in ReportingPeriod")
    
    def _validate_sections_by_quarter(self, root):
        """Validate that required sections are present based on the quarter."""
        reporting_period = root.find("ReportingPeriod")
        if reporting_period is None:
            return
        
        quarter = reporting_period.get("Quarter")
        
        # Check for destination country detail in Q4
        if quarter == "Q4":
            if root.find("DestinationCountryDetail") is None:
                self.warnings.append("Q4 reports should include DestinationCountryDetail section")
        
        # Check for state transactions
        if root.find("StateTransactions") is None:
            self.warnings.append("StateTransactions section is typically required for multi-state operations")
    
    def validate_data_types(self, xml_file):
        """
        Validate data types and formats in the XML.
        
        Args:
            xml_file (str): Path to the XML file to validate
            
        Returns:
            bool: True if validation passes, False otherwise
        """
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Validate numeric fields
            self._validate_numeric_fields(root)
            
            # Validate date formats
            self._validate_date_formats(root)
            
            # Check for any new errors
            if self.errors:
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Data type validation error: {e}")
            return False
    
    def _validate_numeric_fields(self, root):
        """Validate that numeric fields contain valid numbers."""
        # Look for common numeric fields
        numeric_fields = ["TotalAssets", "TotalLiabilities", "NetWorth", "TotalVolume", "TransactionCount"]
        
        for field_name in numeric_fields:
            elements = root.findall(f".//{field_name}")
            for element in elements:
                if element.text:
                    try:
                        float(element.text)
                    except ValueError:
                        self.errors.append(f"Invalid numeric value in {field_name}: {element.text}")
    
    def _validate_date_formats(self, root):
        """Validate date format in GenerationDate attribute."""
        generation_date = root.get("GenerationDate")
        if generation_date:
            try:
                # Check if it's in YYYY-MM-DD format
                if not (len(generation_date) == 10 and 
                       generation_date[4] == "-" and 
                       generation_date[7] == "-"):
                    self.errors.append("GenerationDate must be in YYYY-MM-DD format")
            except Exception:
                self.errors.append("Invalid date format in GenerationDate")
    
    def generate_validation_report(self, output_file=None):
        """
        Generate a validation report.
        
        Args:
            output_file (str): Optional output file for the report
        """
        report = []
        report.append("MSB Call Report XML Validation Report")
        report.append("=" * 50)
        report.append("")
        
        if self.errors:
            report.append("ERRORS:")
            report.append("-" * 10)
            for error in self.errors:
                report.append(f"❌ {error}")
            report.append("")
        
        if self.warnings:
            report.append("WARNINGS:")
            report.append("-" * 12)
            for warning in self.warnings:
                report.append(f"⚠️  {warning}")
            report.append("")
        
        if not self.errors and not self.warnings:
            report.append("✅ All validations passed successfully!")
        
        report_text = "\n".join(report)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(report_text)
                logger.info(f"Validation report saved to: {output_file}")
            except Exception as e:
                logger.error(f"Error saving validation report: {e}")
        else:
            print(report_text)
        
        return report_text

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description='Validate MSB Call Report XML')
    parser.add_argument('--file', required=True,
                       help='XML file to validate')
    parser.add_argument('--output',
                       help='Output file for validation report')
    parser.add_argument('--strict', action='store_true',
                       help='Treat warnings as errors')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.file).exists():
        logger.error(f"File not found: {args.file}")
        return 1
    
    # Initialize validator
    validator = MSBCallReportValidator()
    
    # Perform validations
    structure_valid = validator.validate_xml_structure(args.file)
    data_valid = validator.validate_data_types(args.file)
    
    # Generate report
    report = validator.generate_validation_report(args.output)
    
    # Determine exit code
    if args.strict and (validator.warnings or not structure_valid or not data_valid):
        return 1
    elif not structure_valid or not data_valid:
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
