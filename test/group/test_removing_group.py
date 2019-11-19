from model.group import Group


def test_removing_group(app):
    if app.group.group_count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.remove_frst_group()
    new_group = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_group)
    old_groups[0:1] = []
    assert old_groups == new_group
