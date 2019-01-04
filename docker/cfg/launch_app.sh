#!/bin/bash

# Set env var
export PATH="/usr/local/bin:"$PATH
export FLASK_APP=asset_planner
export FLASK_ENV=development
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Start server
cd /tmp/asset_planner
gunicorn -w 9 -t 90 -b 0.0.0.0:8090 "asset_planner:create_app()" --reload

