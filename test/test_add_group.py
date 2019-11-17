from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="pyTestsGroup", header="header", footer="footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))