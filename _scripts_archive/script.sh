#!/bin/zsh
ARTIFACTS_DIR="/Users/vietmac/.gemini/antigravity/brain/38ae31d9-78b8-48e9-b19d-28b1bddd132f"

# Move images
cp $ARTIFACTS_DIR/poster_306_*.jpg "assets/covers/sir-roger-penrose-giai-ma-khong-gian-y-thuc.jpg"
cp $ARTIFACTS_DIR/poster_307_*.jpg "assets/covers/su-vo-nghia-ma-ban-dang-cam-thay-khong-phai-vi-ban-yeu-kem-ma-vi-ban-dang-dung-nao-trai-tu-duy-ky-thuat-thuat-toan-cuon-man-hinh-de-co-giai.jpg"
cp $ARTIFACTS_DIR/poster_308_*.jpg "assets/covers/system-9-the-biggest-ai-opportunity-is-missed.jpg"
cp $ARTIFACTS_DIR/poster_309_*.jpg "assets/covers/titlesu-that-ve-gan-nhiem-mo-tieu-duong-type-2-cach-chuyen-hoa-carbohydrate-thai-doc-co-the-va-dao-nguoc-benh-ly-bang-phuong-phap-low-carb.jpg"

# Create mapping
cat << 'JSON_EOF' > temp_mapping_306.json
{
  "sir-roger-penrose-giai-ma-khong-gian-y-thuc.html": "assets/covers/sir-roger-penrose-giai-ma-khong-gian-y-thuc.jpg",
  "su-vo-nghia-ma-ban-dang-cam-thay-khong-phai-vi-ban-yeu-kem-ma-vi-ban-dang-dung-nao-trai-tu-duy-ky-thuat-thuat-toan-cuon-man-hinh-de-co-giai.html": "assets/covers/su-vo-nghia-ma-ban-dang-cam-thay-khong-phai-vi-ban-yeu-kem-ma-vi-ban-dang-dung-nao-trai-tu-duy-ky-thuat-thuat-toan-cuon-man-hinh-de-co-giai.jpg",
  "system-9-the-biggest-ai-opportunity-is-missed.html": "assets/covers/system-9-the-biggest-ai-opportunity-is-missed.jpg",
  "titlesu-that-ve-gan-nhiem-mo-tieu-duong-type-2-cach-chuyen-hoa-carbohydrate-thai-doc-co-the-va-dao-nguoc-benh-ly-bang-phuong-phap-low-carb.html": "assets/covers/titlesu-that-ve-gan-nhiem-mo-tieu-duong-type-2-cach-chuyen-hoa-carbohydrate-thai-doc-co-the-va-dao-nguoc-benh-ly-bang-phuong-phap-low-carb.jpg"
}
JSON_EOF

python3 update_covers.py temp_mapping_306.json
rm -f .git/index.lock
git add .
git commit -m 'feat: posters 306-309' || true
while ! git push; do git pull --rebase; sleep 2; done

