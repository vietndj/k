#!/bin/bash
ARTIFACT_DIR="/Users/vietmac/.gemini/antigravity/brain/3d710043-0768-4333-9d59-dc2375935dd5"
mkdir -p assets/covers

# 371
if ls $ARTIFACT_DIR/poster_371_*.jpg 1> /dev/null 2>&1; then
    mv $ARTIFACT_DIR/poster_371_*.jpg assets/covers/10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.jpg
fi
# 374
if ls $ARTIFACT_DIR/poster_374_*.jpg 1> /dev/null 2>&1; then
    mv $ARTIFACT_DIR/poster_374_*.jpg assets/covers/complex-5-anxiety-is-not-what-you-think.jpg
fi

cat << 'JSON_EOF' > temp_mapping_371.json
{
  "10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.html": "assets/covers/10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.jpg",
  "complex-5-anxiety-is-not-what-you-think.html": "assets/covers/complex-5-anxiety-is-not-what-you-think.jpg"
}
JSON_EOF

python3 update_covers.py temp_mapping_371.json
rm -f .git/index.lock
git add .
git commit -m 'feat: posters 371, 374' || true
while ! git push; do git pull --rebase; sleep 2; done
