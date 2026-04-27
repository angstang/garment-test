#!/bin/bash
cd "$(dirname "$0")"
echo "🚀 启动本地web服务器..."
echo "📍 访问地址: http://localhost:8000/garment_test_v2.html"
echo ""
python3 -m http.server 8000
