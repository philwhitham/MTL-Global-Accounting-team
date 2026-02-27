# MTL Global Accounting Team - MSB Call Report XML Project

## Overview
This repository contains the implementation for generating Money Services Business (MSB) Call Report XML files for Shopify's compliance with NMLS (Nationwide Multistate Licensing System & Registry) requirements.

## Project Purpose
The MSB Call Report aims to:
- Standardize and automate reporting for state financial regulators
- Help regulators with examination scheduling, risk assessment, and compliance monitoring
- Allow licensees to automate provision of financial condition, transactional data, and permissible investment amounts
- Provide standard reporting frequencies for MSB activities

## Repository Contents

### Documentation
- `docs/msb-specifications.md` - Extracted MSB Call Report XML specifications
- `docs/scoping-document.md` - Project scoping and requirements document
- `docs/msb-specifications.txt` - Raw extracted text from the PDF specifications

### Tools
- `tools/pdf_reader.py` - PDF text extraction utility
- `tools/xml_generator.py` - XML generation script (to be developed)
- `tools/validation.py` - XML validation script (to be developed)

### Templates
- `templates/msb_call_report_template.xml` - Base XML template
- `templates/schema/` - XSD schema files for validation

### Data
- `data/shopify_transactions/` - Sample Shopify transaction data structure
- `MSB Call Reports/` - Generated MSB Call Report XML files organized by year/quarter

### SOX (internal controls)
- `SOX/` - SOX control framework and control matrix for MTL/stored value; build controls before materiality

## MSB Call Report Requirements

### Who Needs to File
Companies holding an MSB license during a calendar quarter for activities such as:
- Money transmission
- Check cashing
- Issuing or selling travelers checks
- Issuing or selling drafts
- Foreign currency dealing and exchange
- Issuing or selling money orders
- Bill paying
- Issuing or selling prepaid access/stored value products
- Virtual currency

### Report Sections
1. **Section I: Financial Condition Report** - Required once per quarter
2. **Section II(a): Company-wide Transactions Detail** - Required once per quarter
3. **Section II(b): State Transaction Detail** - Required for each licensed state
4. **Section III: Permissible Investments Report** - Required for relevant activities
5. **Section IV(a) and IV(b): Destination Country Detail** - Q4 only, for foreign transactions

### Reporting Deadlines
| Filing | Reporting Period | Due Date |
|--------|------------------|----------|
| Q1 | January 1 - March 31 | May 15 |
| Q2 | April 1 - June 30 | August 14 |
| Q3 | July 1 - September 30 | November 14 |
| Q4 | October 1 - December 31 | February 14 |

## Getting Started

### Prerequisites
- Python 3.7+
- Required packages: `PyPDF2`, `lxml` (for XML validation)

### Installation
```bash
pip install -r requirements.txt
```

### Usage
1. Extract specifications: `python tools/pdf_reader.py input_pdfs/MSB\ Call\ Report\ XML\ Upload\ Specifications\ v4.pdf`
2. Generate XML: `python tools/xml_generator.py --quarter Q1 --year 2025`
3. Validate XML: `python tools/validation.py --file "MSB Call Reports/2025/Q1/msb_report_q1_2025.xml"`

## Development Status
- [x] PDF specifications extracted
- [x] Project structure created
- [x] Basic tools framework
- [ ] XML generation logic
- [ ] Shopify data integration
- [ ] Validation implementation
- [ ] Testing and documentation

## Contributing
This project is for Shopify's MTL Global Accounting Team. Please follow internal development guidelines.

## Resources
- [NMLS Resource Center - MSB Call Report](https://mortgage.nationwidelicensingsystem.org/slr/common/SitePages/MoneyServicesBusinessesCallReport.aspx)
- [MSB Call Report Overview](https://mortgage.nationwidelicensingsystem.org/licensees/resources/LicenseeResources/MSBCR%20Overview%20-%202024.1.pdf)
- [XML Upload Specifications](https://mortgage.nationwidelicensingsystem.org/licensees/resources/LicenseeResources/MSB%20Call%20Report%20XML%20Upload%20Specifications%20v4.pdf)

## License
Internal use only - Shopify MTL Global Accounting Team
