#!/usr/bin/env python3
"""
MSB Call Report XML Generator

This script generates XML files for Money Services Business Call Reports
according to NMLS specifications for Shopify's compliance requirements.
"""

import argparse
import xml.etree.ElementTree as ET
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MSBCallReportGenerator:
    """Generates MSB Call Report XML files according to NMLS specifications."""
    
    def __init__(self, company_name, company_id, form_version="2024.8"):
        """
        Initialize the MSB Call Report generator.
        
        Args:
            company_name (str): Name of the company filing the report
            company_id (str): NMLS company ID
            form_version (str): MSB Call Report form version
        """
        self.company_name = company_name
        self.company_id = company_id
        self.form_version = form_version
        
    def create_base_structure(self):
        """Create the base XML structure for the MSB Call Report."""
        # Create root element
        root = ET.Element("MSBCallReport")
        root.set("xmlns", "http://www.nmls.org/msbcr")
        root.set("FormVersion", self.form_version)
        root.set("CompanyName", self.company_name)
        root.set("CompanyID", self.company_id)
        root.set("GenerationDate", datetime.now().strftime("%Y-%m-%d"))
        
        return root
    
    def add_financial_condition(self, root, data):
        """
        Add Financial Condition Report (Section I).
        
        Args:
            root: XML root element
            data: Dictionary containing financial condition data
        """
        fc_section = ET.SubElement(root, "FinancialCondition")
        
        # Add required financial condition fields
        # This will be expanded based on the actual specifications
        for key, value in data.items():
            field = ET.SubElement(fc_section, key)
            field.text = str(value)
            
        return fc_section
    
    def add_company_transactions(self, root, data):
        """
        Add Company-wide Transactions Detail (Section II(a)).
        
        Args:
            root: XML root element
            data: Dictionary containing company-wide transaction data
        """
        ta_section = ET.SubElement(root, "CompanyTransactions")
        
        # Add required transaction fields
        # This will be expanded based on the actual specifications
        for key, value in data.items():
            field = ET.SubElement(ta_section, key)
            field.text = str(value)
            
        return ta_section
    
    def add_state_transactions(self, root, state_data):
        """
        Add State Transaction Detail (Section II(b)).
        
        Args:
            root: XML root element
            state_data: Dictionary containing state-specific transaction data
        """
        st_section = ET.SubElement(root, "StateTransactions")
        
        # Add state transaction data for each state
        for state, data in state_data.items():
            state_element = ET.SubElement(st_section, "State")
            state_element.set("StateCode", state)
            
            for key, value in data.items():
                field = ET.SubElement(state_element, key)
                field.text = str(value)
                
        return st_section
    
    def add_permissible_investments(self, root, data):
        """
        Add Permissible Investments Report (Section III).
        
        Args:
            root: XML root element
            data: Dictionary containing permissible investment data
        """
        pi_section = ET.SubElement(root, "PermissibleInvestments")
        
        # Add required permissible investment fields
        # This will be expanded based on the actual specifications
        for key, value in data.items():
            field = ET.SubElement(pi_section, key)
            field.text = str(value)
            
        return pi_section
    
    def add_destination_country_detail(self, root, data):
        """
        Add Destination Country Detail (Section IV(a) and IV(b)).
        Only required for Q4 reports.
        
        Args:
            root: XML root element
            data: Dictionary containing destination country data
        """
        dc_section = ET.SubElement(root, "DestinationCountryDetail")
        
        # Add required destination country fields
        # This will be expanded based on the actual specifications
        for key, value in data.items():
            field = ET.SubElement(dc_section, key)
            field.text = str(value)
            
        return dc_section
    
    def generate_xml(self, quarter, year, data):
        """
        Generate the complete MSB Call Report XML.
        
        Args:
            quarter (str): Reporting quarter (Q1, Q2, Q3, Q4)
            year (int): Reporting year
            data (dict): Dictionary containing all required data
            
        Returns:
            str: Generated XML as a string
        """
        # Create base structure
        root = self.create_base_structure()
        
        # Add reporting period information
        reporting_period = ET.SubElement(root, "ReportingPeriod")
        reporting_period.set("Quarter", quarter)
        reporting_period.set("Year", str(year))
        
        # Add required sections based on data availability
        if "financial_condition" in data:
            self.add_financial_condition(root, data["financial_condition"])
            
        if "company_transactions" in data:
            self.add_company_transactions(root, data["company_transactions"])
            
        if "state_transactions" in data:
            self.add_state_transactions(root, data["state_transactions"])
            
        if "permissible_investments" in data:
            self.add_permissible_investments(root, data["permissible_investments"])
            
        # Destination Country Detail only for Q4
        if quarter == "Q4" and "destination_country" in data:
            self.add_destination_country_detail(root, data["destination_country"])
        
        # Convert to string with proper formatting
        ET.indent(root, space="  ")
        return ET.tostring(root, encoding='unicode')
    
    def save_xml(self, xml_content, output_path):
        """
        Save the generated XML to a file.
        
        Args:
            xml_content (str): XML content to save
            output_path (str): Path where to save the XML file
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(xml_content)
            logger.info(f"XML file saved to: {output_path}")
        except Exception as e:
            logger.error(f"Error saving XML file: {e}")
            raise

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description='Generate MSB Call Report XML')
    parser.add_argument('--quarter', required=True, choices=['Q1', 'Q2', 'Q3', 'Q4'],
                       help='Reporting quarter')
    parser.add_argument('--year', required=True, type=int,
                       help='Reporting year')
    parser.add_argument('--company-name', required=True,
                       help='Company name')
    parser.add_argument('--company-id', required=True,
                       help='NMLS company ID')
    parser.add_argument('--output', default='msb_call_report.xml',
                       help='Output XML file path')
    parser.add_argument('--data-file',
                       help='JSON file containing report data')
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = MSBCallReportGenerator(args.company_name, args.company_id)
    
    # For now, use sample data - this will be replaced with actual Shopify data
    sample_data = {
        "financial_condition": {
            "TotalAssets": "1000000.00",
            "TotalLiabilities": "500000.00",
            "NetWorth": "500000.00"
        },
        "company_transactions": {
            "TotalVolume": "5000000.00",
            "TransactionCount": "10000"
        }
    }
    
    # Generate XML
    xml_content = generator.generate_xml(args.quarter, args.year, sample_data)
    
    # Save to file
    generator.save_xml(xml_content, args.output)
    
    print(f"MSB Call Report XML generated successfully for {args.quarter} {args.year}")
    print(f"Output file: {args.output}")

if __name__ == "__main__":
    main()
