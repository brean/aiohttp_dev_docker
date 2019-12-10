#!/bin/bash
BASE_PATH="/virtualenv"
APP_PATH="/web"
VENV_PATH="$BASE_PATH/virtualenv"
VENV_BIN="$VENV_PATH/bin"
VENV_ACTIVATE="$VENV_BIN/activate"

VENV_PIP="$VENV_BIN/pip3"
if [ ! -f $VENV_ACTIVATE ]; then
  python3 -m venv $VENV_PATH
  source $VENV_ACTIVATE
  pip3 install wheel
fi

source $VENV_ACTIVATE
pip3 install -r /web/requirements.txt

echo "$@"
exec "$@"
