from pathlib import Path
from re import IGNORECASE, search

import click


@click.command()
@click.option(
    '--ignorecase', '-i', is_flag=True, help='Perform case insensitive matching'
)
@click.argument('path')
@click.argument('search_string')
def run(path, search_string, ignorecase):
    case = IGNORECASE if ignorecase else 0
    exit_code = pygrep(path, search_string, case)
    return exit_code


class OutputString:
    def __init__(self, file, line_count, line_value):
        self.file = file
        self.line_count = line_count
        self.line_value = line_value

    def __str__(self) -> str:
        return f'{self.file} line={self.line_count}: {self.line_value}'


def find_required_line(file, search_string, case):
    if file.is_file():
        for line_count, line in enumerate(file.open(), 1):
            if search(search_string, line, case):
                yield line_count, line.strip('\n')


def pygrep(path, search_string, case):
    p = Path(path)
    if not p.exists():
        print('Given path does not exists')
        return False
    for file in p.glob('**/*'):
        try:
            for line_count, line in find_required_line(file, search_string, case):
                print(OutputString(file, line_count, line))
        except UnicodeDecodeError:
            print('{}: Can not process binary files'.format(file))
    return True
