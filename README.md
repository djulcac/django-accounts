# DJANGO-ACCOUNTS

## Install

[Pypi](https://pypi.org/project/djulcac-django-accounts/)

    pip install djulcac-django-accounts


## Packaging

Based on this [documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/)


Generating distribution archives

    python3 -m pip install --upgrade build
    python3 -m build

Uploading the distribution archives

    python3 -m pip install --upgrade twine
    python3 -m twine upload dist/*


## Test current versions

    pip install git+ssh://git@github.com/djulcac/django-accounts.git
    pip install git+ssh://git@github.com/djulcac/django-accounts.git@1-add-app


@143
