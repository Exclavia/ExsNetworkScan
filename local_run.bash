#! /bin/sh
DIR=$(dirname "$0")
if [ -z "$PYTHON" ]
then
  PYTHON=${PYTHON:-python3}
fi
$PYTHON --version > /dev/null 2>&1
if [ ! $? -eq 0 ]
then
  echo "WARNING: '$PYTHON' not found, using 'python' instead."
  PYTHON=python
fi
PYTHONPATH=$DIR exec "$PYTHON" src/main.py