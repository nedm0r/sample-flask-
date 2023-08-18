#!/bin/bash

RELEASE_NAME=helm-project
CHART_REPO=helm-project-1093
CHART_NAME=my-flask-app-chart
if helm list -q | grep -q "^$RELEASE_NAME$"; then
  helm upgrade "$RELEASE_NAME" "$CHART_REPO/$CHART_NAME"
else
  helm install "$RELEASE_NAME" "$CHART_REPO/$CHART_NAME"
fi
