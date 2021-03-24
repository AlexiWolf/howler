# Howler Blog

Howler is a light and fast blogging backend.

## Development Setup

To install the project dependencies.
```commandline
pipenv sync
```

### Running Tests

Pytest-Django requires the settings module to be set.  This can be done by creating a `.env` file and adding the
following:

```dotenv
DJANGO_SETTINGS_MODULE="dev_server.settings"
```

The tests can be run with Pipenv and Pytest:

```commandline
pipenv run pytest
```

### The Development Server

To start the development server, run:

```commandline
pipenv run python manage.py runserver
```


### Code Cleanup

Code cleanup should be run before changes are pushed.

Code formatting is handled by Black.

```commandline
pipenv run black
```

Check for problems with Flake8.

```commandline
pipenv run flake8
```

## License

Copyright (C) 2021 AlexiWolf

Howler is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Howler is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Howler.  If not, see <https://www.gnu.org/licenses/>.