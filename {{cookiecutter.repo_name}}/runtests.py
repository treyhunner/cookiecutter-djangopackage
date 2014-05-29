import os
import sys

try:
    import django
    from django.conf import settings
except ImportError:
    raise ImportError("To fix this error, run: "
                      "pip install -r requirements-test.txt")

DEFAULT_SETTINGS = dict(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    ROOT_URLCONF="{{ cookiecutter.app_name }}.tests.urls",
    INSTALLED_APPS=[
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "{{ cookiecutter.app_name }}",
        "{{ cookiecutter.app_name }}.tests",
    ],
)


def run_tests(*test_args):
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    if hasattr(django, 'setup'):
        django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        test_args = ['{{ cookiecutter.app_name }}.tests']
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ['tests']

    failures = runner_class(
        verbosity=1, interactive=True, failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
