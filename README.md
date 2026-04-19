Python CLI Task Manager
A menu-driven terminal application for managing personal tasks, built as part of the Deckzi Software Developer Pre-Recruitment Program. This project demonstrates Python fundamentals, file persistence using JSON, and logic separation.

Features

Add Tasks: Create tasks with a title and due date.


View Tasks: List all saved tasks with their auto-incremented IDs and status.


Complete Tasks: Mark specific tasks as "done" by their ID.


Search: Find tasks using keywords in the title.


Delete: Remove tasks from the list by ID.


Persistence: All data is saved to tasks.json and loads automatically on startup.

Technical Stack

Language: Python 3.x.


Data Format: JSON.


Environment: Virtual environments (venv) and python-dotenv.

Setup Instructions
1. Clone the Repository
Bash
git clone https://github.com/your-username/python-task-manager.git
cd python-task-manager
2. Set Up Virtual Environment
Create and activate the virtual environment to manage dependencies:

Bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required packages listed in requirements.txt:

Bash
pip install -r requirements.txt
4. Configuration
Create a .env file based on the .env.example provided to manage environment variables.

Bash
cp .env.example .env
5. Run the Application
Start the program using the main entry point:

Bash
python main.py
Mandatory Guidelines Followed

No Hardcoded Secrets: Credentials are stored in .env and added to .gitignore.


Naming Conventions: All files and folders use lowercase letters and hyphens.


Error Handling: The application handles invalid inputs gracefully and does not crash.


Logic Separation: Core task logic is separated from the main menu entry point.


Public Repository: This project is hosted on a public GitHub repository with a clear README.

Final Check

Public Repo: Ensure the repository settings on GitHub are set to Public.


Ignored Files: Verify that venv/, .env, and tasks.json are not visible on GitHub.


Commit Messages: Ensure you have used meaningful, descriptive messages for your commits.
