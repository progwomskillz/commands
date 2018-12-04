from abc import ABC, abstractmethod

from ..exceptions.command_cannot_be_undone import CommandCannotBeUndone


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        raise CommandCannotBeUndone('This command cannot be undone')
