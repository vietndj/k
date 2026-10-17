#!/bin/bash
ARTIFACTS_DIR="/Users/vietmac/.gemini/antigravity/brain/fa250ffa-5a1a-4447-83bb-6b566aecf048"
mv $ARTIFACTS_DIR/poster_311_*.jpg assets/covers/20-gio-de-hoc-bat-cu-thu-gi-podcast.jpg
mv $ARTIFACTS_DIR/poster_313_*.jpg assets/covers/tu-bo-y-chi-bat-dau-tu-dong-hoa-khoi-tai-san-podcast.jpg
mv $ARTIFACTS_DIR/poster_314_*.jpg assets/covers/so-tay-tu-duy-kien-tao-suc-manh-dich-thuc-podcast.jpg
mv $ARTIFACTS_DIR/poster_315_*.jpg assets/covers/su-that-ve-ung-thu-nang-luong-te-bao-science.jpg

cat << 'JSON_EOF' > temp_mapping_311.json
{
  "20-gio-de-hoc-bat-cu-thu-gi-podcast.html": "assets/covers/20-gio-de-hoc-bat-cu-thu-gi-podcast.jpg",
  "tu-bo-y-chi-bat-dau-tu-dong-hoa-khoi-tai-san-podcast.html": "assets/covers/tu-bo-y-chi-bat-dau-tu-dong-hoa-khoi-tai-san-podcast.jpg",
  "so-tay-tu-duy-kien-tao-suc-manh-dich-thuc-podcast.html": "assets/covers/so-tay-tu-duy-kien-tao-suc-manh-dich-thuc-podcast.jpg",
  "su-that-ve-ung-thu-nang-luong-te-bao-science.html": "assets/covers/su-that-ve-ung-thu-nang-luong-te-bao-science.jpg"
}
JSON_EOF

python3 update_covers.py temp_mapping_311.json
rm -f .git/index.lock
git add .
git commit -m 'feat: posters 311, 313, 314, 315' || true
while ! git push; do git pull --rebase; sleep 2; done
