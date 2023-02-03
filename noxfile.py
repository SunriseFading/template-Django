import nox


@nox.session
def format(session: nox.Session) -> None:
    session.install("brunette", "isort")
    session.run("brunette", "--config=setup.cfg", "app")
    session.run("isort", "--sp=setup.cfg", "app")


@nox.session
def lint(session: nox.Session) -> None:
    session.install("flake8", "mypy", "isort", "brunette")
    session.run("flake8", "--config=setup.cfg", "app")
    session.run("mypy", "--config-file=setup.cfg", "app")
