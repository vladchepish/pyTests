from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    added_group = Group(name="pyTestsGroup", header="header", footer="footer")
    app.group.create(added_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.sor_by_id) == sorted(new_groups, key=Group.sor_by_id)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    added_group = Group(name="", header="", footer="")
    app.group.create(added_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.sor_by_id) == sorted(new_groups, key=Group.sor_by_id)
