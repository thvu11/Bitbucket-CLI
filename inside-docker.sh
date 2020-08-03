#!/bin/bash

pip install --quiet --editable .
bb "$@"
