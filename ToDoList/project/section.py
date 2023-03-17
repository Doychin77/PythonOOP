from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {str(Task.details)} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        Task.completed = True
        return f"Completed task {Task.name}"




section = Section("Daily tasks")
print(section.add_task(Task))
second_task = Task("Make bed", "27/05/2020")
