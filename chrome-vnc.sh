#!/bin/bash
# Chrome launcher for VNC
export DISPLAY=:1
google-chrome --no-sandbox "$@" &
