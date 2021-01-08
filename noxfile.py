import os
import nox
import shutil


BLACK_VERSION = "black==19.10b0"
BLACK_PATHS = ["docs", "sample_package", "tests", "noxfile.py", "setup.py"]
DEFAULT_PYTHON_VERSION = "3.7"


@nox.session
def lint(session):
    """
    Run linters

    Returns a failure if the linters find linting errors or sufficiently
    serious code quality issues.
    """
    session.install("flake8")
    session.run("flake8", "sample_package", "tests")


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest", "-v", "tests")


@nox.session
def black(session):
    session.install(BLACK_VERSION)
    session.run("black", "--check", *BLACK_PATHS)


@nox.session
def coverage(session):
    session.install("mock", "pytest", "pytest-cov")
    session.install("-e", ".")
    session.run("py.test", "--quiet", "--cov=sample_package.sample_module")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover_report(session):
    """Run the final coverage report.
    This outputs the coverage report aggregating coverage from the unit
    test runs (not system test runs), and then erases coverage data.
    """
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing", "--fail-under=97")

    session.run("coverage", "erase")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def docs(session):
    """Build the docs for this library."""

    session.install("-e", ".")
    session.install("sphinx<3.0.0", "alabaster", "recommonmark")

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-W",  # warnings as errors
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )
