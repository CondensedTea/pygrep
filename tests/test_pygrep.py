from click.testing import CliRunner

from pygrep.pygrep import pygrep, run

word = 'Apple'


def test_click_bad_path():
    result = CliRunner().invoke(run, ['/tmp/unexpected/path/to/file/', 'somestring'])
    assert result.output == 'Given path does not exists\n'


def test_bad_path_return():
    assert pygrep('/tmp/unexpected/path/to/file/', 'somestring', 0) is False


def test_default_return(tmp_path):
    assert pygrep(tmp_path, word, 0) is True


def test_multiple_files_default_message(tmp_path, capsys, response_line):
    pygrep(tmp_path, word, 0)
    assert capsys.readouterr().out == response_line


def test_hidden_file_default_message(tmp_path, hidden_file, capsys):
    pygrep(tmp_path, word, 0)
    assert capsys.readouterr().out == '{} line=1: {}\n'.format(hidden_file, word)


def test_bad_path_message(tmp_path, capsys):
    bad_path = tmp_path / 'nothing'
    pygrep(bad_path, word, 0)
    assert capsys.readouterr().out == 'Given path does not exists\n'


def test_binary_message(capsys, binary):
    binary_path, binary_file = binary
    pygrep(binary_path, word, 0)
    assert capsys.readouterr().out == '{}: Can not process binary files\n'.format(
        binary_file
    )
