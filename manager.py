import getpass
import click

@click.group()
def manager():
    pass

@click.command()
def initdb():
    from ezlog3.model import User, Site
    from ezlog3.config import conf
    if Site.objects().first() is None:
        site = Site(name=conf.SITENAME, 
                    site_version=conf.SITE_VERSION,
                    model_version=conf.MODEL_VERSION)
        site.save()
    if User.get_user_by_username("demo") is None:
        user = User(username="demo", password="demo")
        user.save()
    click.echo("done!")

@click.command()
def create_user():
    from ezlog3.model import User
    user = User.objects().first()
    if user is not None:
        click.echo("we only allow one user!")
        click.echo("you will change %s to :"%user.nickname)
        user = User()
    else:
        click.echo("Username: ")
    username = raw_input()
    password = getpass.getpass("Password: ")
    user.username = username
    user.password = password
    user.save()
    click.echo("done!")

manager.add_command(initdb)
manager.add_command(create_user)

if __name__ == '__main__':
    manager()
