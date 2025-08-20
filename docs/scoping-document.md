# Shopify MTL: Money Services Businesses Call Report
**Finance - Controllership**  
**June 2025**

## TL:DR
**We need to build an XML report that can be uploaded quarterly (upload has to be manual currently).**

## Overview
The NMLS MSB Call Report aims to:
- Standardize and automate reporting for state financial regulators
- Help regulators with tasks like examination scheduling, risk assessment, and monitoring compliance
- Allow regulators to develop detailed transactional activity reports and compare them across states
- Enable licensees to automate the provision of financial condition, transactional data, and permissible investment amounts to multiple state regulators in a uniform manner
- Provide licensees with standard reporting frequencies

## Who Needs to File
- Companies holding an MSB license during a calendar quarter for activities such as: money transmission, check cashing, issuing or selling travelers checks, issuing or selling drafts, foreign currency dealing and exchange, issuing or selling money orders, bill paying, issuing or selling prepaid access/stored value products, and virtual currency
- The report must be submitted through NMLS, so entities need an active record in NMLS

## Report Sections and Requirements
The report has several sections, and companies only need to complete data fields relevant to their MSB activities (as selected on the Company Form MU1).

- **Section I: Financial Condition Report:** Required once per quarter, even if licensed in multiple states
- **Section II(a): Company-wide Transactions Detail:** Required once per quarter, even if licensed in multiple states
- **Section II(b): State Transaction Detail:** Required once per quarter for each state that adopts the NMLS MSB Call Report and in which the company is licensed
- **Section III: Permissible Investments Report:** Required only for licensees conducting activities relevant to permissible investment requirements. This is submitted once per quarter
- **Section IV(a) and IV(b): Destination Country Detail:**
  - Must only be submitted as part of the fourth quarter submission
  - Applies to money transmission licensees engaged in foreign money transmission activity
  - Data must include all foreign transactions completed during the entire calendar year
  - Section IV(b) is an optional section for states to adopt

## Reporting Frequency and Deadlines
- The report is required on a calendar year basis, with quarters defined as:
  - Q1: January, February, March
  - Q2: April, May, June
  - Q3: July, August, September
  - Q4: October, November, December
- Licensees with a fiscal year not ending on December 31st must still file on a calendar year basis
- The report must be submitted within 45 days after the end of the calendar quarter
- The Destination Country Detail (Section IV(a) and IV(b)) for foreign money transmission is due 45 days after the end of the fourth quarter and covers the entire calendar year

## Submission of Report
- The NMLS MSB Call Report may only be submitted through NMLS
- All required report sections must be submitted at the same time but can be prepared in the system prior to final submission
- Submission options include manual data field entry and a bulk upload functionality via an .xml file or .csv spreadsheet

## Consequences of Non-Submission
- Failure to submit the report within 45 days of the end of the calendar quarter results in a license item being placed on relevant licenses held by the company
- This may result in regulatory action and could prevent the renewal of the entity's license

## General Notes
- Approximately 36 states require licensed MSBs to submit quarterly or annual reports on transactional activity and permissible investment amounts
- States that adopt the report adopt all sections, except for the optional Section IV(b)
- For companies licensed in multiple states that adopt the report, the company-level sections (Financial Condition, Company-wide Transactions, Permissible Investments) are submitted once

## Filing Deadlines
| Filing | Reporting Period | Due Date |
|--------|------------------|----------|
| Q1 | January 1 - March 31 | May 15 |
| Q2 | April 1 - June 30 | August 14 |
| Q3 | July 1 - September 30 | November 14 |
| Q4 | October 1 - December 31 | February 14 |

## XML FAQ

### Will the user be able to automatically upload the data to NMLS?
No. The user providing the MSBCR XML file must log into NMLS and manually start the MSBCR filing. The MSBCR XML file has to be manually uploaded to NMLS by browsing to the file that is stored on the user accessible file system and then uploading the file. Afterwards, the user will have to complete the filing. Regardless of the feature used to populate the MSBCR and similar to other filings, the user will need to run completeness checks, attest, and submit the MSBCR through NMLS.

### Will the user be able to upload data from multiple systems that each contain their own parts of the data? Or will the customer need to submit all data at once?
The user will be able to upload multiple MSBCR XML files that are used to complete one MSBCR filing. The user will also be able to manually enter data in the NMLS before and after the MSBCR XML upload as another means to complete the MSBCR filing. Please note that data that coincides between multiple files will result in the prior information being overwritten by the subsequent information. If the subsequent upload occurs after the filing has been submitted it will create an amendment to the submitted filing.

## Data Required
**Data required to be submitted in the MSB Call Report:**

**Does Shopify have the required data?**

**If Shopify has the data, develop quick and accurate ways to obtain the data**

## Links
1. [NMLS Resource Center - Money Services Businesses Call Report](https://mortgage.nationwidelicensingsystem.org/slr/common/SitePages/MoneyServicesBusinessesCallReport.aspx)
2. [NMLS Money Services Businesses (MSB) Call Report Overview](https://mortgage.nationwidelicensystem.org/licensees/resources/LicenseeResources/MSBCR%20Overview%20-%202024.1.pdf)
3. [XML Upload Specifications](https://mortgage.nationwidelicensystem.org/licensees/resources/LicenseeResources/MSB%20Call%20Report%20XML%20Upload%20Specifications%20v4.pdf)
