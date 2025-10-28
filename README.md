This project is a simple yet functional Python application developed for tracking sold products, checking warranty periods, and recording service operations. It can be used both via the command line (terminal interface) and a graphical user interface (GUI).

project-folder/
|── service.py
├── menu.py
├── gui.py
├── example.csv           ← Sample product catalog (not included in version control)
├── .gitignore
├── README.md
└── service.db            ← SQLite database (created automatically when run)


🧩 File Descriptions

**service.py**
Contains the application's database infrastructure and business logic.

3 tables are created using SQLite:

product_catalog: Information such as brand, model, and warranty period.

products: Sell date and serial number of sold products.

service_records: Products sent for service, fault description, service fee, and status.

Additionally:

Warranty checks can be performed.

Product and service records can be listed.

Service status can be updated.

Products can be loaded from a CSV file (must be in UTF-8-BOM format).

**menu.py**
Provides user interaction via the terminal.

Through the main menu system:

Product and service records can be added.
Warranty status can be queried.

GUI can be launched.



**gui.py**
Contains the graphical user interface (developed with Tkinter).

Product adding, listing, and querying operations can be done through the interface.

Detailed information can be seen by examining the GUI code.

**example.csv**

A file containing a sample product catalog.

Shows users how to perform bulk data transfer.

Excluded from Git version control (excluded in .gitignore).

**service.db**
The SQLite database file.

Automatically created when the application is run for the first time.

All product and service information is stored in this file.

⚙️ Features
Warranty Check: The warranty period of products is automatically calculated based on the sell date.

Fee Calculation: Service fee is entered if the warranty period has expired; otherwise, it is recorded as 0.

Service Status: Information such as "In Service" or "Completed" is recorded.

CSV Support: External product data can be easily imported.

GUI: Provides the possibility of usage with a visual interface in addition to the command line.

🔒 **.gitignore** File
The .gitignore file in the project ensures that the following files and folders are not tracked by Git:

__pycache__/, *.pyc: Compilation caches 

*.db: SQLite database files (because they contain personal and dynamic data) 

example.csv: May contain user-specific sample data 

Requirements

Python 3.7 or higher 

Required libraries:

pip install python-dateutil


📄 Lisans

This project is licensed under the MIT License.

The license permits the free use, modification, and distribution of this project. However, the software is provided "as is" and offers no warranty.

For detailed information, please review the [LICENSE](LICENSE) file.
