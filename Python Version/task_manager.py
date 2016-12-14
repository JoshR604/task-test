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
import uuid
import re

class Task(object):

    def __init__(self, name):
        self._id = uuid.uuid4()
        self._name = name
        self._value = None
        self._completed = False

    def __eq__(self, other):
        """Override the default Equatable behaviour"""
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False

    def complete(self):
        self.is_completed = True

    def __update_value(self):
        """Assuming Python3.x -- for Python2.x use 'basestring' """
        if isinstance(self._name, str):
            occurances = re.findall('CCN', self._name, flags=re.IGNORECASE)
            if occurances:
                self._value = len(occurances)
            else:
                self._value = None
        else:
            self._value = None

        print('Value {value} for {name}'.format(value=self._value, name=self._name))

    @property
    def is_completed(self):
        return self._completed

    @is_completed.setter
    def is_completed(self, val):
        self._completed = val
        self.__update_value()

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        self._id

    @property
    def value(self):
        return self._value


# This class cannot be edited directly
class TaskManager(object):

    def __init__(self):
        self._tasks = []

    def import_task(self, task):
        self._tasks.append(task)

    def complete_tasks(self):
        if len(self._tasks) > 0:
            if not all([task.is_completed for task in self._tasks]):
                for task in self._tasks:
                    task.complete()
                    print('task {name} completed'.format(name=task.name))

    def remove_tasks(self):
        while len(self._tasks) > 0:
            self._tasks.pop()
