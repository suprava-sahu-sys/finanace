
Personal Finance Management Application

Table of Contents
1. Project Overview
2. Installation
3. Application Setup
4. Features and Usage
5. Running the Application
6. Testing
7. Common Errors and Troubleshooting
8. Extending the Application
9. License

Project Overview
This Python-based Personal Finance Management Application allows individual users to manage their financial transactions, set monthly budgets by category, and get notified if they exceed their budgets.

Installation
Prerequisites
- Python 3.6 or newer

Step-by-Step
1. Clone or download the project files
2. Navigate to project folder: `cd path/to/your/project-folder`
3. (Optional) Create a virtual environment
4. Run: `python main.py`

Application Setup
On first run, the app will create `finance_app.db` and required tables automatically.

Features and Usage
1. User Registration
- Input username and password
- Returns success or duplicate warning

2. User Login
- Authenticate using stored credentials

3. Adding Transactions
- Enter date, category, amount, and type

4. Setting and Monitoring Budgets
- Set monthly limits by category
- Get alerts if exceeded

. Backup and Restore
- Backup creates a timestamped `.db` file
- Restore loads data from a selected backup

Running the Application
python main.py

Testing
Run tests using:
python -m unittest discover tests

Extending the Application
- Add visualization
- Implement password hashing
- Monthly reports

License
Licensed under MIT License.
