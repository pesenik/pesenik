#!/usr/bin/env bash

pip-compile requirements.dev.in -o requirements.dev.txt
pip-compile requirements.in -o requirements.txt
