from typing import Optional, Union
from dataclasses import dataclass
from ortools.sat.python import cp_model


@dataclass
class Task:
    """Class for identifying a task in a given job.

    Args:
        id (int): Task unique identifier
        machine (int): Machine ID where task runs
        duration (int): Task total duration
        start (int, cp_model.IntVar): Task start time - optimization goal
        end (int, cp_model.IntVar): Task end time - optimization goal
        interval (int, cp_model.IntervalVar): Task interval - optimization goal
    """

    id: int
    name: str
    machine: Union[int, str]
    duration: int
    start: Optional[cp_model.IntVar] = None
    end: Optional[cp_model.IntVar] = None
    interval: Optional[cp_model.IntervalVar] = None

    def __str__(self) -> str:
        return f"{self.name} ({self.duration}h)"
