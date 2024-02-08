# flake8: noqa
from invoke import task
from pathlib import Path
import os
import shutil


assert Path.cwd() == Path(__file__).parent

@task
def check(ctx):
    """Runs ruff on whole project"""
    ctx.run("ruff check .")


@task
def rflint(ctx):
    """Runs rflint agains atests"""
    ctx.run(f"rflint --argumentfile .rflintrc atest{os.path.sep}")


def mypy(ctx):
    """Runs mypy against the codebase"""
    ctx.run("mypy --config mypy.ini")


@task
def black(ctx):
    """Reformat code with black"""
    ctx.run("black -l130 -tpy38 src")


@task
def test(ctx):
    """Runs robot acceptance tests"""
    ctx.run(f"python -m robot --pythonpath src --loglevel TRACE:TRACE {extras} atest{os.path.sep}")


@task
def clean(ctx):
    to_be_removed = [
        ".mypy_cache/",
        "dist/",
        "output/",
        "src/*.egg-info/",
        "output.xml",
        ".coveragedb",
        "*.html",
        "selenium-screenshot-*.png",
        "geckodriver-*.log",
    ]

    for item in to_be_removed:
        fs_entry = Path(item)
        if fs_entry.is_dir():
            shutil.rmtree(item)
        elif fs_entry.is_file():
            fs_entry.unlink()
        else:
            for fs_entry in Path().glob(item):
                fs_entry.unlink()
