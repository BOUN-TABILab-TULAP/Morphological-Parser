#!/bin/sh
gunicorn -w 2 --chdir ./morphological_parser/ api:app -b 0.0.0.0:4444