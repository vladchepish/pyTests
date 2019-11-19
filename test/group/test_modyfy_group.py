from model.group import Group


def test_modify_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    added_group = Group(name="new pyTestsGroup")
    added_group.id = old_groups[0].id
    app.group.modify_first_group(Group(name="new pyTestsGroup"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)
    old_groups[0] = added_group
    assert sorted(old_groups, key=Group.sor_by_id) == sorted(new_group, key=Group.sor_by_id)


def test_modify_group_header(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new pyTestsHeader"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)
