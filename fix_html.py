import re
import json

ids = {
    "Beneath_the_Open_Sky.mp3": "1N-iMTQFB3PmMSvFsQ58pjMog2d2_msUQ",
    "Cry_from_the_Frozen_Pass+.mp3": "17nRCnc6t48YbapJEIYF0CqbhvXOqKvP6",
    "Rite_of_the_Frozen_Peak+.mp3": "15TzGzvQ3p7LH-GCKt3q3OOlYnfBvek15",
    "Song_of_the_Red_Earth+.mp3": "15UArirfgNmY2fGzfcx4qHidi2xeBJvSB",
    "The_Final_Surge+.mp3": "1IVX8lpxYcaTHpzRat9s1In25eo_DseWc",
    "The_Gathering_at_the_Ridge+.mp3": "1a8N0hfT9XW-iCjmHuykTME9_MbbCsuA6",
    "The_Great_Ascent.mp3": "1qxjRH12etmRWuHuEd5vFna_-0A-Y9W8z",
    "The_Sovereign_Ascent+.mp3": "1AsZO0r2BNvTZcGHZwBQEkHyIaMudvWEp",
    "The_Unbroken_Line++.mp3": "1NjrlQ5V-o8tJOe8g-_PYuUKpJLu6X2Z-"
}

html_file = "/Users/vietmac/Documents/CODE/k/nhac.html"

with open(html_file, "r") as f:
    content = f.read()

for name, drive_id in ids.items():
    local_src = f'src="assets/audio/{name}"'
    drive_src = f'src="https://drive.google.com/uc?export=download&id={drive_id}"'
    content = content.replace(local_src, drive_src)

with open(html_file, "w") as f:
    f.write(content)

print("Done")
