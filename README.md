# task_management

## Installation

#### Install Pipenv
`pip install pipenv`

#### Install Dependencies
`pipenv install`

`pipenv install --dev` for the dev libraries

#### Setup the Local.py
copy the content of `local.py.tempelate` and paste it in `local.py`

or

`cp local.py.tempelate local.py`

Then change the `DATABASE` setting in the local.py file to point it to local postgress database.


#### enable pre-commit
`pre-commit install`

## Executing commands
use ctrl+shift+P to open the VS code command pallet, search for `Tasks:Run Task` to run the task, select it, then select a command to execute following functions

- `debug server` : run the Django debug server
- `database migrations` : run the database migration
- `django shell` : to open the Django shell to check the individual commands
- `automated test` : to run the test suit
- `pylint` : to check the pylint score before pushing the code