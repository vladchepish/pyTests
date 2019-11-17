from model.group import Group


def test_removing_group(app):
    app.group.remove_frst_group()