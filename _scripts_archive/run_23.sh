#!/bin/bash
ARTIFACTS_DIR="/Users/vietmac/.gemini/antigravity/brain/67f00c28-a1ef-4bfc-a2c0-b168d8ab467e"
mkdir -p assets/covers

mv $ARTIFACTS_DIR/poster_376_*.jpg assets/covers/law-5-stress-is-not-what-happens-to-you.jpg
mv $ARTIFACTS_DIR/poster_377_*.jpg assets/covers/toi-uu-hieu-suat-nao-bo-suc-manh-nootropic-tu-creatine-va-che-do-an-thit-carnivore-dinh-cao-toi-gian-nang-luong-tu-joe-rogan-elon-musk.jpg
mv $ARTIFACTS_DIR/poster_378_*.jpg assets/covers/su-giau-co-va-thanh-cong-tot-dinh-khong-bat-dau-tu-chien-thuat-kinh-doanh-hao-nhoang-ma-khoi-nguon-tu-nang-luc-quan-tri-tam-tri-ban-phai-thiet-ke-mot-moi-truong-khien-ky-luat-tro-nen-de-dang.jpg
mv $ARTIFACTS_DIR/poster_379_*.jpg assets/covers/no-den-tu-long-dung-cam-dam-lam-ra-nhung-video-toi-te-ban-dau-kien-tri-cai-thien-1-moi-ngay-va-tap-trung-phuc-vu-sau-sac-cho-nhom-khan-gia-ngach-dang-chiu-chung-noi-dau-ma-ban-tung-vuot-qua-podcast.jpg
mv $ARTIFACTS_DIR/poster_380_*.jpg assets/covers/be-khoa-thuat-toan-xay-kenh-niche-podcast.jpg

cat << 'JSON' > temp_mapping_376.json
{
  "law-5-stress-is-not-what-happens-to-you.html": "assets/covers/law-5-stress-is-not-what-happens-to-you.jpg",
  "toi-uu-hieu-suat-nao-bo-suc-manh-nootropic-tu-creatine-va-che-do-an-thit-carnivore-dinh-cao-toi-gian-nang-luong-tu-joe-rogan-elon-musk.html": "assets/covers/toi-uu-hieu-suat-nao-bo-suc-manh-nootropic-tu-creatine-va-che-do-an-thit-carnivore-dinh-cao-toi-gian-nang-luong-tu-joe-rogan-elon-musk.jpg",
  "su-giau-co-va-thanh-cong-tot-dinh-khong-bat-dau-tu-chien-thuat-kinh-doanh-hao-nhoang-ma-khoi-nguon-tu-nang-luc-quan-tri-tam-tri-ban-phai-thiet-ke-mot-moi-truong-khien-ky-luat-tro-nen-de-dang.html": "assets/covers/su-giau-co-va-thanh-cong-tot-dinh-khong-bat-dau-tu-chien-thuat-kinh-doanh-hao-nhoang-ma-khoi-nguon-tu-nang-luc-quan-tri-tam-tri-ban-phai-thiet-ke-mot-moi-truong-khien-ky-luat-tro-nen-de-dang.jpg",
  "no-den-tu-long-dung-cam-dam-lam-ra-nhung-video-toi-te-ban-dau-kien-tri-cai-thien-1-moi-ngay-va-tap-trung-phuc-vu-sau-sac-cho-nhom-khan-gia-ngach-dang-chiu-chung-noi-dau-ma-ban-tung-vuot-qua-podcast.html": "assets/covers/no-den-tu-long-dung-cam-dam-lam-ra-nhung-video-toi-te-ban-dau-kien-tri-cai-thien-1-moi-ngay-va-tap-trung-phuc-vu-sau-sac-cho-nhom-khan-gia-ngach-dang-chiu-chung-noi-dau-ma-ban-tung-vuot-qua-podcast.jpg",
  "be-khoa-thuat-toan-xay-kenh-niche-podcast.html": "assets/covers/be-khoa-thuat-toan-xay-kenh-niche-podcast.jpg"
}
JSON

python3 update_covers.py temp_mapping_376.json
rm -f .git/index.lock
git add .
git commit -m 'feat: posters 376-380' || true
while ! git push; do git pull --rebase; sleep 2; done
