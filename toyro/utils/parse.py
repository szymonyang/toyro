
from typing import List, Optional
from toyro.constant import PLACE, MOVE, LEFT, RIGHT, REPORT
import re


def parse(line: str) -> List:
    """Parse an string and return command or command with coord
    e.g. [MOVE]    or [PLACE, 0,0,NORTH]
    """

    split = line.strip().split()
    command = split[0]
    if command not in {PLACE, MOVE, LEFT, RIGHT, REPORT}:
        return []

    if command == PLACE:
        r = re.compile(r"^PLACE\s(\d),(\d),(NORTH|WEST|EAST|SOUTH)$")
        match = r.match(line)
        if match:
            return [PLACE, int(match.group(1)), int(match.group(2)), match.group(3)]
        else:
            return []

    if command in {LEFT, RIGHT, REPORT, MOVE}:
        return [command]
