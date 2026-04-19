import json
import os
from datetime import datetime

class TaskManager:  # <--- Ensure this name matches 'TaskManager' exactly
    def __init__(self, storage_file='tasks.json'):
        self.storage_file = storage_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.tasks, f)

    def add_task(self, title, due_date):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "status": "pending",
            "due_date": due_date
        }
        self.tasks.append(task)
        self.save_tasks()
        return task["id"]

def mark_complete(self, task_id):
        """Finds a task by ID and marks it as done."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'done'
                self.save_tasks()
                return True
        return False

def delete_task(self, task_id):
        """Removes a task from the list by ID."""
        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        if len(self.tasks) < original_count:
            self.save_tasks()
            return True
        return False

def search_tasks(self, keyword):
        """Returns a list of tasks containing the keyword in the title."""
        keyword = keyword.lower()
        return [t for t in self.tasks if keyword in t['title'].lower()]