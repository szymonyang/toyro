from toyro.commands.base_command import BaseCommand


class PlaceCommand(BaseCommand):
    def __init__(self, robot) -> None:
        super().__init__(robot)

    def execute(self):
        self.robot
