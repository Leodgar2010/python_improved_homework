
import pytest

from Lesson_13_5 import Project
from errors import AccessError, LevelError

@pytest.fixture()
def set_up():
    return Project()


def test_access_fail_1(set_up):

    with pytest.raises(AccessError):
        set_up.login('231', 'Мария')

def test_access(set_up):
    assert set_up.login('546', 'Мария') == '2'


def test_access_fail_2(set_up):
    with pytest.raises(LevelError):
       set_up.create_user('546', 'Мария', '678', 'Василий', '4')



if __name__ == '__main__':
    pytest(['-v'])