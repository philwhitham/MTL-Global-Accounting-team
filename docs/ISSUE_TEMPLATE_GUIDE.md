# GitHub Issue Template Guide

## How to Create MSB Call Report Approval Issues

This guide explains how to create approval issues for each quarterly report using the GitHub issue template.

---

## 📋 **Step-by-Step Process**

### **Step 1: Navigate to Create Issue**
1. Go to: https://github.com/philwhitham/MTL-Global-Accounting-team/issues/new/choose
2. Click on "MSB Call Report Approval"

### **Step 2: Fill in Placeholders**

The template has several placeholders you need to replace:

#### **In the Title**:
- Replace `[QUARTER]` with: Q1, Q2, Q3, or Q4
- Replace `[YEAR]` with: 2026, 2027, etc.
- Example: `[APPROVAL] Q1 2026 MSB Call Report`

#### **In the Description**:
- Replace `[QUARTER]` with: Q1, Q2, Q3, or Q4
- Replace `[YEAR]` with: 2026, 2027, etc.
- Replace `[START DATE]` with quarter start date
- Replace `[END DATE]` with quarter end date
- Replace `[DUE DATE]` with the NMLS deadline
- Replace `[DATE]` in timeline with your target dates

### **Step 3: Update Labels** (Optional)
- Change `msb-report` to `msb-report-q1-2026` (or appropriate quarter)
- Add year label if desired

### **Step 4: Assign Reviewers**
- Add Finance team member
- Add Legal/Compliance team member
- Add yourself as coordinator

---

## 📅 **Quick Reference Table**

Use this table to quickly fill in dates for each quarter:

| Quarter | Period | Start Date | End Date | Due Date | Target Review | Target Approval | Target Submit |
|---------|--------|------------|----------|----------|---------------|-----------------|---------------|
| **Q1** | Jan-Mar | January 1 | March 31 | May 15 | April 30 | May 5 | May 6 |
| **Q2** | Apr-Jun | April 1 | June 30 | August 15 | July 31 | August 5 | August 6 |
| **Q3** | Jul-Sep | July 1 | September 30 | November 15 | October 31 | November 5 | November 6 |
| **Q4** | Oct-Dec | October 1 | December 31 | February 15 | January 28 | February 2 | February 6 |

**Note**: Target dates assume 9-day submission buffer. Adjust based on workload.

---

## 📁 **File Path Reference**

Reports are organized in this structure:

```
MSB Call Reports/
├── 2025/
│   └── Q4/
│       ├── SHOPIFY_FS_Q4_2025_MSB_REPORT.xml
│       ├── Q4_2025_REPORT_SUMMARY.md
│       ├── PRE_SUBMISSION_VALIDATION.md
│       ├── SUBMISSION_TIMELINE.md
│       └── APPROVALS.md
├── 2026/
│   ├── Q1/
│   │   ├── SHOPIFY_FS_Q1_2026_MSB_REPORT.xml
│   │   ├── Q1_2026_REPORT_SUMMARY.md
│   │   └── ...
│   ├── Q2/
│   ├── Q3/
│   └── Q4/
└── 2027/
    └── ...
```

---

## 📝 **Example: Q1 2026 Issue**

### **Title**:
```
[APPROVAL] Q1 2026 MSB Call Report
```

### **Description** (filled in):
```markdown
## 📋 MSB Call Report Approval Request

**Report Period**: Q1 2026 (January 1 - March 31, 2026)  
**Due Date**: May 15, 2026  
**NMLS ID**: 2689562  

---

## 📁 Files for Review

**Location**: `MSB Call Reports/2026/Q1/`

Navigate to the folder above and review:
- **XML Report**: `SHOPIFY_FS_Q1_2026_MSB_REPORT.xml`
- **Summary**: `Q1_2026_REPORT_SUMMARY.md`
- **Validation**: `PRE_SUBMISSION_VALIDATION.md`
- **Timeline**: `SUBMISSION_TIMELINE.md`
- **Approvals**: `APPROVALS.md`

**Quick Links**:
- [Navigate to Q1 2026 Report Folder](https://github.com/philwhitham/MTL-Global-Accounting-team/tree/main/MSB%20Call%20Reports/2026/Q1)
- [View All MSB Reports](https://github.com/philwhitham/MTL-Global-Accounting-team/tree/main/MSB%20Call%20Reports)

---

## 📅 Timeline

- **Target Review Completion**: April 30, 2026
- **Final Approval**: May 5, 2026
- **Target Submission Date**: May 6, 2026 (9 days before deadline)
- **NMLS Submission Deadline**: May 15, 2026

[... rest of template ...]
```

### **Labels**:
- `approval`
- `msb-report`
- `q1-2026`

### **Assignees**:
- @finance-reviewer
- @legal-reviewer
- @philwhitham

---

## 💡 **Tips**

### **Before Creating the Issue**:
1. ✅ Ensure the quarterly report has been generated
2. ✅ Verify all files exist in the correct folder
3. ✅ Run comprehensive validation
4. ✅ Update the specific file links if you want direct links

### **After Creating the Issue**:
1. Update the "Quick Links" section with the actual quarter folder
2. Add any quarter-specific notes or context
3. Notify reviewers via @mention in a comment

### **Optional: Add Direct File Links**:

If you want direct links to files (instead of just folder), manually add them after creating the issue:

```markdown
**Direct File Links**:
- [📄 XML Report](https://github.com/philwhitham/MTL-Global-Accounting-team/blob/main/MSB%20Call%20Reports/2026/Q1/SHOPIFY_FS_Q1_2026_MSB_REPORT.xml)
- [📊 Summary](https://github.com/philwhitham/MTL-Global-Accounting-team/blob/main/MSB%20Call%20Reports/2026/Q1/Q1_2026_REPORT_SUMMARY.md)
- [✅ Validation](https://github.com/philwhitham/MTL-Global-Accounting-team/blob/main/MSB%20Call%20Reports/2026/Q1/PRE_SUBMISSION_VALIDATION.md)
- [📅 Timeline](https://github.com/philwhitham/MTL-Global-Accounting-team/blob/main/MSB%20Call%20Reports/2026/Q1/SUBMISSION_TIMELINE.md)
- [✍️ Approvals](https://github.com/philwhitham/MTL-Global-Accounting-team/blob/main/MSB%20Call%20Reports/2026/Q1/APPROVALS.md)
```

---

## 🔄 **Quarterly Workflow**

### **Week 1-2 of Final Month**:
1. Generate quarterly report from NetSuite
2. Create XML and supporting documents
3. Run all validations
4. Create GitHub approval issue

### **Week 3 of Final Month**:
5. Finance team review (via issue)
6. Legal/Compliance team review (via issue)
7. Address feedback

### **Week 4 of Final Month**:
8. Final approval
9. Submit to NMLS (9 days early)

### **Following Month (1-9 days)**:
10. Monitor NMLS for acceptance
11. Address any issues
12. Close GitHub issue when accepted

---

## 🚨 **Common Issues**

### **Issue: Links don't work**
**Solution**: Use the "Navigate to Report Folder" link and browse manually

### **Issue: Files not found**
**Solution**: Verify report generation completed and files are in correct folder

### **Issue: Wrong quarter showing in template**
**Solution**: Template is generic - replace all placeholders before saving

---

## 📚 **Related Documentation**

- **Approval Workflow Guide**: `docs/APPROVAL_WORKFLOW_OPTIONS.md`
- **Submission Timeline**: In each quarter's folder
- **Validation Guide**: `MSB Call Reports/[YEAR]/[QUARTER]/PRE_SUBMISSION_VALIDATION.md`

---

**Last Updated**: January 21, 2026  
**Maintainer**: Phil Whitham
