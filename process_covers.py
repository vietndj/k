import json
import shutil
import os

images = {
    127: "/Users/vietmac/.gemini/antigravity/brain/f258d13f-d308-46b4-8eda-7f3de6a80d93/cover_127_1789678311361.jpg",
    128: "/Users/vietmac/.gemini/antigravity/brain/f258d13f-d308-46b4-8eda-7f3de6a80d93/cover_128_1789678376288.jpg",
    129: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_129_1789678525397.jpg",
    130: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_130_1789678541332.jpg",
    131: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_131_1789678564139.jpg",
    132: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_132_1789678581302.jpg",
    133: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_133_1789678614960.jpg",
    134: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_134_1789678635482.jpg",
    135: "/Users/vietmac/.gemini/antigravity/brain/175f6179-ecb7-4c14-9a58-2cf11d278865/cover_135_1789678695983.jpg",
    139: "/Users/vietmac/.gemini/antigravity/brain/b43a2972-148f-4e57-8992-a1fd52fad4e2/cover_139_1789678527001.jpg",
    140: "/Users/vietmac/.gemini/antigravity/brain/b43a2972-148f-4e57-8992-a1fd52fad4e2/cover_140_1789678612608.jpg",
    149: "/Users/vietmac/.gemini/antigravity/brain/cb72c840-1832-4ad8-af28-585cdac26f3d/cover_149_1789678490462.jpg",
    150: "/Users/vietmac/.gemini/antigravity/brain/cb72c840-1832-4ad8-af28-585cdac26f3d/cover_150_1789678518604.jpg",
    151: "/Users/vietmac/.gemini/antigravity/brain/cb72c840-1832-4ad8-af28-585cdac26f3d/cover_151_1789678535107.jpg",
    152: "/Users/vietmac/.gemini/antigravity/brain/cb72c840-1832-4ad8-af28-585cdac26f3d/cover_152_1789678552863.jpg",
    153: "/Users/vietmac/.gemini/antigravity/brain/cb72c840-1832-4ad8-af28-585cdac26f3d/cover_153_1789678593624.jpg",
    159: "/Users/vietmac/.gemini/antigravity/brain/0e9b6fdb-b768-427a-bab3-2464d0b29474/cover_159_1789678578194.jpg",
    160: "/Users/vietmac/.gemini/antigravity/brain/0e9b6fdb-b768-427a-bab3-2464d0b29474/cover_160_1789678625031.jpg",
    161: "/Users/vietmac/.gemini/antigravity/brain/0e9b6fdb-b768-427a-bab3-2464d0b29474/cover_161_1789678643938.jpg",
    162: "/Users/vietmac/.gemini/antigravity/brain/0e9b6fdb-b768-427a-bab3-2464d0b29474/cover_162_1789678679974.jpg"
}

with open('/Users/vietmac/Documents/CODE/k/remaining_poster_tasks.json', 'r') as f:
    data = json.load(f)

mapping = {}
for item in data:
    idx = item['index']
    if idx in images:
        target_html = item['target_html']
        dest_path = f"/Users/vietmac/Documents/CODE/k/assets/covers/cover_{idx}.jpg"
        if os.path.exists(images[idx]):
            shutil.copy2(images[idx], dest_path)
            mapping[target_html] = f"assets/covers/cover_{idx}.jpg"
        else:
            print(f"Missing source file for index {idx}: {images[idx]}")

with open('/Users/vietmac/Documents/CODE/k/temp_mapping_w4.json', 'w') as f:
    json.dump(mapping, f, indent=2)

print(f"Generated {len(mapping)} mappings")
