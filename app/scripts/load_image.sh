#!/usr/bin/env bash
IMAGE_REPO_NAME="matheusvt/cd4ml-app"
IMAGE_TAG="latest"

set -e
#echo "docker login -u $DOCKER_USER -p $DOCKER_PASSWORD"
echo "docker pull $IMAGE_REPO_NAME:$IMAGE_TAG"
docker pull $IMAGE_REPO_NAME:$IMAGE_TAG
#docker logout
