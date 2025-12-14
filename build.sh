#!/bin/sh

echo "========================================"
echo "DOCKER IMAGE BUILD SCRIPT"
echo "========================================"
echo ""
echo "Parameters received:"
echo "  Image name: $1"
echo "  Tag: $2"
echo "  Build directory: $(pwd)"
echo ""

echo "Step 1: Checking Dockerfile..."
if [ -f "Dockerfile" ]; then
    echo "✅ Dockerfile found"
    echo "Contents:"
    cat Dockerfile
else
    echo "❌ ERROR: Dockerfile not found!"
    exit 1
fi

echo ""
echo "Step 2: Checking application files..."
if [ -f "app.py" ]; then
    echo "✅ app.py found"
    echo "  Size: $(wc -l < app.py) lines"
else
    echo "❌ ERROR: app.py not found!"
    exit 1
fi

echo ""
echo "Step 3: Building Docker image..."
echo "Command: docker build -t $1:$2 ."
docker build -t $1:$2 .

if [ $? -eq 0 ]; then
    echo "✅ Docker build successful!"
else
    echo "❌ Docker build failed!"
    exit 1
fi

echo ""
echo "Step 4: Tagging as latest..."
docker tag $1:$2 $1:latest
echo "✅ Image tagged as latest"

echo ""
echo "Step 5: Verification..."
echo "Images created:"
docker images $1 --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

echo ""
echo "========================================"
echo "BUILD COMPLETED SUCCESSFULLY"
echo "========================================"
echo "Image: $1:$2"
echo "Latest: $1:latest"
echo "========================================"
