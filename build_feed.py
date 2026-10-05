#!/usr/bin/env python3
"""
build_feed.py (Proxy to indexer & manifest)
Tự động đồng bộ và tái lập chỉ mục (Search) và Manifest (Giao diện Masonry) cho FEDU Podcast Intelligence (fedu.vn/k).
"""
import os
import subprocess
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
indexer_path = os.path.join(base_dir, "indexer.py")
manifest_path = os.path.join(base_dir, "generate_manifest.py")

print("[*] Chạy Indexer (Tái lập catalog & search_index)...")
if os.path.exists(indexer_path):
    subprocess.run([sys.executable, indexer_path], check=True)

print("[*] Chạy Generate Manifest (Cập nhật posts-manifest.json cho UI)...")
if os.path.exists(manifest_path):
    subprocess.run([sys.executable, "-c", "import generate_manifest; generate_manifest.generate()"], check=True)

print("[*] Hoàn tất đồng bộ toàn diện!")
