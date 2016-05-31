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


manager.add_command(initdb)

if __name__ == '__main__':
    manager()
