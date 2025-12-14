#!/bin/sh
echo "Building $1:$2"
docker build -t $1:$2 .
echo "Build complete!"
