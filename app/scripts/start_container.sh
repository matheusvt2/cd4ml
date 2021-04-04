#!/usr/bin/env bash
IMAGE_REPO_NAME="matheusvt/cd4ml-app"
IMAGE_TAG="latest"
CONTAINER_NAME="cd4ml-app"

set -e

docker run -d --name $CONTAINER_NAME -p 80:5000  $IMAGE_REPO_NAME:$IMAGE_TAG