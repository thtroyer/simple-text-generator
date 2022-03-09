import abc
from typing import Tuple


class WorkItem:
    """
    Interface for the 2 classes below
    """

    def __init__(self, items_to_complete: int):
        self._items_to_complete = items_to_complete

    @abc.abstractmethod
    def get_time_estimate(self, generation_rate: float = 0.0, training_rate: float = 0.0):
        pass


class TrainingWorkItem(WorkItem):
    def get_time_estimate(self, generation_rate: float = 0.0, training_rate: float = 0.0):
        return self._items_to_complete / training_rate


class GeneratingWorkItem(WorkItem):
    def get_time_estimate(self, generation_rate: float = 0.0, training_rate: float = 0.0):
        return self._items_to_complete / generation_rate


class WorkList:
    def __init__(self, items_to_complete: Tuple[WorkItem, ...]):
        self._progress_current_task = 0
        self._items_to_complete = items_to_complete
        self._current_item_index = 0
        self._training_rate = 0
        self._generating_rate = 0

    def get_time_estimate(self):
        total_seconds = 0
        current_task = True
        for work_item in self._items_to_complete[self._current_item_index:]:
            modifier = 1
            if current_task:
                modifier = (1 - self._progress_current_task)
                current_task = False

            total_seconds += modifier * work_item.get_time_estimate(self._generating_rate, self._training_rate)
        return total_seconds

    def advance_index(self):
        self._current_item_index += 1

    def set_training_rate(self, training_rate: float):
        self._training_rate = training_rate

    def set_generating_rate(self, generating_rate: float):
        self._generating_rate = generating_rate

    def set_progress_on_current_work_item(self, progress: float):
        self._progress_current_task = progress
