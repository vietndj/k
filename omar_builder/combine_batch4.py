# -*- coding: utf-8 -*-
import json

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch4_part1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch4_part2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)

BATCH_4 = p1 + p2
print(f"Tổng cộng BATCH_4 có: {len(BATCH_4)} tập")

with open('/Users/vietmac/Documents/CODE/k/omar_builder/episodes_batch4.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
"""
episodes_batch4.py
Batch 4: 10 Episodes (OE31 - OE40)
"""

BATCH_4 = ''' + json.dumps(BATCH_4, ensure_ascii=False, indent=4) + '\n')

print("Đã ghi thành công episodes_batch4.py!")
