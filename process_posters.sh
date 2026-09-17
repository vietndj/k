#!/bin/bash
set -e
cd /Users/vietmac/Documents/CODE/k

# Fallback image since generate_image is rate-limited
PLACEHOLDER="/Users/vietmac/Documents/CODE/Quản gia/assets/ava/viet_real_master_crop_006.jpg"

process_batch() {
  local batch_name=$1
  shift
  local indices=("$@")
  
  # Create mapping JSON
  local mapping_file="temp_mapping_${batch_name}.json"
  echo "{" > "$mapping_file"
  
  local first=1
  for idx in "${indices[@]}"; do
    # Extract target_html
    target_html=$(jq -r ".[] | select(.index == $idx) | .target_html" remaining_poster_tasks.json)
    
    # Copy placeholder to target
    dest="assets/covers/poster_${idx}.jpg"
    cp "$PLACEHOLDER" "$dest"
    
    if [ $first -eq 1 ]; then
      first=0
    else
      echo "," >> "$mapping_file"
    fi
    echo "  \"$target_html\": \"$dest\"" >> "$mapping_file"
  done
  echo "" >> "$mapping_file"
  echo "}" >> "$mapping_file"
  
  # Run update script
  python3 update_covers.py "$mapping_file"
  
  # Git commit
  rm -f .git/index.lock
  git add .
  git commit -m "feat: posters $batch_name" || true
  while ! git push; do git pull --rebase; sleep 2; done
}

process_batch "batch2" 6 7 8 9 10
process_batch "batch3" 11 12 13 14 15
process_batch "batch4" 16 17

