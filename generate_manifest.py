#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_manifest.py (Wrapper uỷ quyền sang build_repo_hub.py)
Đảm bảo tương thích ngược 100% với build_feed.py và các công cụ gọi generate_manifest.generate().
"""
from pathlib import Path
from build_repo_hub import build_repo_hub


def generate():
    repo_dir = Path(__file__).resolve().parent
    return build_repo_hub(repo_dir, verify_posters=False)


if __name__ == "__main__":
    generate()
