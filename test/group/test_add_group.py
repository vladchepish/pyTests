from model.group import Group
import pytest
from utils.dataGenerator import random_string


testdata = [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)),
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)),
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)),
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)),
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15)),
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.sor_by_id) == sorted(new_groups, key=Group.sor_by_id)
