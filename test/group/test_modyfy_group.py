from model.group import Group


def test_modify_group_name(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="new pyTestsGroup"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)


def test_modify_group_header(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="new pyTestsHeader"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)
