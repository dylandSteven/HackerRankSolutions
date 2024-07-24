import sys
import re
pattern = r'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\S'
lines = sys.stdin.read().splitlines()
valid_hex_color = []
for line in lines:
    matches = re.findall(pattern, line.rstrip())
    valid_hex_color.extend(matches)
print(*valid_hex_color, sep='\n')