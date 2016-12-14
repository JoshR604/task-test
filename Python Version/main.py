""" Todo:
        - Alter the complete_tasks method so that it only calls 'complete' on
            non-completed task.
        - Add a remove_task method that removes only one task by id

        - Upon calling complete() on a task, set _value of that task object to the number of occurrences of the
            string "CCN" (case in-sensitive) that appears in the task's name.

        - Fix the Task object id, so that it is unique for each new task. (please consider scalability and
            what else the Id could be used for)

        - Fix other bugs and make improvements where you see fit
        - Add error handling where you see fit

    Note:
        - You cannot edit/change the TaskManager class directly. Think of it as a 3rd party library
        - You can create new objects, etc
"""

from task_manager import Task, TaskManager

class TaskManagerChild(TaskManager):
    def __init__(self):
        super(TaskManagerChild, self).__init__()

    def complete_tasks(self):
        """Overriding parent method and not calling super due to implementation change"""
        if self._tasks:
            if not all([task.is_completed for task in self._tasks]):
                for task in self._tasks:
                    if not task.is_completed:
                        task.complete()
                        print('task {name} completed!'.format(name=task.name))
                    else:
                        print('task {name} already completed!'.format(name=task.name))

    def remove_task(self, task):
        if self._tasks:
            for idx, aTask in enumerate(self._tasks):
                # Since we did an Override on Task's equatable we are checking by ID
                if aTask == task:
                    print('found task {name} and removing it'.format(name=task.name))
                    del self._tasks[idx]
                    break

class TaskApp(object):
    def __init__(self):
        self.task_manager = TaskManagerChild()

    def run(self):
        first_task = Task('!!nZ@xr>492CCN;SDRC2#6CcN_$5UcCNq]*m44AhW`')
        second_task = Task('g}~x?C*n9K|LccN_YEL@<=44jkc.dB-v{!#;7*[[')
        third_task = Task('ekCcN,h9=!B46)j6acCN;`n68M+2ZR2CCn^:CUw')

        self.task_manager.import_task(first_task)
        self.task_manager.import_task(second_task)
        self.task_manager.import_task(third_task)

        self.task_manager.complete_tasks()

        last_task = Task('>.`8tCcn{xsS3sa!G@{cCn(w},U+s)**sACc]NAn#')
        self.task_manager.import_task(last_task)
        self.task_manager.complete_tasks()

        #try out the new remove task method..
        self.task_manager.remove_task(first_task)

        #remove all tasks
        self.task_manager.remove_tasks()

if __name__ == "__main__":
    app = TaskApp()
    app.run()