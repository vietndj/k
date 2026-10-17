import os, sys, json, shutil

def record(index, html, artifact_path):
    covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
    os.makedirs(covers_dir, exist_ok=True)
    filename = os.path.basename(artifact_path)
    dst = os.path.join(covers_dir, filename)
    if os.path.exists(artifact_path):
        shutil.move(artifact_path, dst)
    elif not os.path.exists(dst):
        raise FileNotFoundError(f"Neither {artifact_path} nor {dst} exists")

    map_file = "/Users/vietmac/Documents/CODE/k/temp_mapping_w1.json"
    if os.path.exists(map_file):
        with open(map_file, "r") as f:
            mapping = json.load(f)
    else:
        mapping = []

    # Check if already present
    for item in mapping:
        if item.get("index") == index:
            item["html"] = html
            item["image_path"] = dst
            break
    else:
        mapping.append({
            "index": index,
            "html": html,
            "image_path": dst
        })

    mapping.sort(key=lambda x: x["index"])
    with open(map_file, "w") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"Recorded index {index} -> {dst}")

if __name__ == "__main__":
    idx = int(sys.argv[1])
    html = sys.argv[2]
    art = sys.argv[3]
    record(idx, html, art)