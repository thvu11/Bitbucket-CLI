#!/bin/bash

docker-compose run --rm test /test-dir/inside-docker.sh "$@"
