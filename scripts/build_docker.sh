#!/bin/bash
set -e 

docker build \
    -t dev.local/sample-project \
    .
