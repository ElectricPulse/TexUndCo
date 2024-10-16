#!/bin/bash

location="$(dirname $0)"

export PYTHONDONTWRITEBYTECODE=1
scons -QC "$location/build" "$@"
