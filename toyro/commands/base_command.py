from toyro.robot import Robot
from toyro.exceptions import InvalidCoordException, NotPlacedException
import logging


class BaseCommand:
    def __init__(self, robot: Robot) -> None:
        self._robot = robot

    def catch_operaltional_exception(func):
        """_summary_
        a decorator to catch InvalidCoordException and NotPlaceException
        show warning message in logging 
        """

        def wrapper(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except InvalidCoordException as invalidCoordExce:
                logging.warning(
                    str(invalidCoordExce) + f" when executing {self.__class__.__name__}")
            except NotPlacedException as notPlacedExce:
                logging.warning(
                    str(notPlacedExce) + f" when executing {self.__class__.__name__}")
            except Exception as exec:
                logging.error(
                    f"Exception when executing {self.__class__.__name__}")
                raise exec

        return wrapper

    def execute(self):
        pass
