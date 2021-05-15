import pytest

word = 'Apple'


@pytest.fixture(name='tmp_dir_path', autouse=True)
def fixture_tmp_dir_path(tmp_path):
    parent = tmp_path / 'test_pygrep'
    parent.mkdir()
    return parent


@pytest.fixture(name='response_line')
def fixture_response_line(tmp_dir_path):
    response_line = ''
    for file in ['test2.file', 'test.file']:
        normal_in_parent = tmp_dir_path / file
        normal_in_parent.write_text(word, 'utf-8')
        response_line += '{} line=1: {}\n'.format(tmp_dir_path / file, word)
    extra_file = tmp_dir_path / 'extra.file'
    extra_file.write_text('blank')
    return response_line


@pytest.fixture(name='hidden_file')
def fixture_hidden_file(tmp_path):
    hidden = tmp_path / '.test_pygrep'
    hidden.mkdir()
    normal_in_hidden = hidden / '.test.file'
    normal_in_hidden.write_text(word, 'utf-8')
    return normal_in_hidden


@pytest.fixture(name='binary')
def fixture_binary(tmp_dir_path):
    binary_in_parent = tmp_dir_path / 'binary.file'
    binary_in_parent.write_bytes(b'\xDE\xAD\xBE\xEF')
    return tmp_dir_path, binary_in_parent
