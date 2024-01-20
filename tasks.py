from invoke import  task

@task
def start(ctx):
    print("Suoritetaan testejä:")
    ctx.run("pytest Koodi")
    print("Käynnistetään sovellus:")
    ctx.run("python Koodi/kayttoliittyma.py")

@task
def test(ctx):
    ctx.run("pytest Koodi")

@task
def generateReport(ctx):
    ctx.run("coverage run --branch -m pytest")
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint Koodi")
