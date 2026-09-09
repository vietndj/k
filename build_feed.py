#!/usr/bin/env python3
"""
build_feed.py (Proxy to indexer.py)
Tự động đồng bộ và tái lập chỉ mục danh sách bài viết cho FEDU Podcast Intelligence (fedu.vn/k).
"""
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
indexer_path = os.path.join(base_dir, "indexer.py")

if os.path.exists(indexer_path):
    os.execv(sys.executable, [sys.executable, indexer_path])
