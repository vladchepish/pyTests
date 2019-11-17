from model.group import Group


def test_removing_group(app):
    app.session.login(username="admin", password="secret")
    app.group.remove_frst_group()
    app.session.logout()