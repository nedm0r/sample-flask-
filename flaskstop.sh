#!/bin/bash

PIDS=$(sudo lsof -t -i :5000)

if [ -z "$PIDS" ]; then
  echo "No processes found running on port 5000"
else
  for PID in $PIDS; do
    sudo kill -9 $PID
    echo "Process with PID $PID has been terminated"
  done
fi
