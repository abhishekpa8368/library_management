# Library Management Module for Odoo 18

![Library Module Screenshot](static/description/screenshot.png)

A comprehensive library management system built as an Odoo module to manage books, members, and loans with additional features like late penalties and reporting.

## Features

- **Book Management**:
  - Add/edit books with titles, authors, ISBNs
  - Categorize books with hierarchical categories
  - Track availability status

- **Member Management**:
  - Maintain member records with contact details
  - Track membership types (Regular/Premium)
  - View borrowing history

- **Loan System**:
  - Check books in/out with status tracking
  - Automatic due date calculation (14 days)
  - Late return detection with penalties ($10/day)
  - Email notifications for loans

- **Reporting & Analytics**:
  - Printable book listings
  - Dashboard with visualizations
  - Late loan reports

## Installation

1. Place the module in your Odoo addons directory:
   ```bash
   cp -r library_management /path/to/odoo/addons/
## torun project
./odoo-bin --addons-path=/home/abhishekpal/workspace/custom_modules,/home/abhishekpal/workspace/server/18.0C/addons
