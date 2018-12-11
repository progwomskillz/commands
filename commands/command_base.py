from abc import ABC, abstractmethod

from exceptions.commands.cant_be_undone import CantBeUndone


class CommandBase(ABC):
    @abstractmethod
    def execute(self):
        pass

    def undo(self):
        raise CantBeUndone('This command cannot be undone')
