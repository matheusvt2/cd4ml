#!/usr/bin/env bash
IMAGE_REPO_NAME="matheusvt/cd4ml-app"
IMAGE_TAG="latest"
CONTAINER_NAME="cd4ml-app"

set -e

if [ "$(docker ps -q -a -f name=$CONTAINER_NAME)" ]; then
    docker kill $CONTAINER_NAME || true
    docker rm -f $CONTAINER_NAME || true
    echo "removed container"
fi

if [ "$(docker images $IMAGE_REPO_NAME -q)" ]; then
    docker rmi  $IMAGE_REPO_NAME:$IMAGE_TAG || true
    echo "removed image"
fi


