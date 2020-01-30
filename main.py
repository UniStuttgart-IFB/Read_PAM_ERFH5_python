#!/usr/bin/python
import sys
import os
from typing import List, Tuple
from erhf5_Data import erhf5_Data


def read_arguments(argv: List[str]) -> Tuple[str, str, str]:
    path = os.path.normpath(argv[0])
    file_x = os.path.normpath(argv[1])
    print("Data:")
    print('File X = "', file_x)
    return path, file_x


if __name__ == "__main__":
    path = ""
    file_x = ""
    file_2 = ""
    if len(sys.argv[1:]) == 0:
        path = "FOLDER"
        file_x = "NAME_FILE_X"

    path, file_x = read_arguments(sys.argv[1:])

    data_file_x = erhf5_Data(path, file_x)
