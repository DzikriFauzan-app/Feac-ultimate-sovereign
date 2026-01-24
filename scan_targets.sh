#!/bin/bash
TARGET_FILE="targets.txt"
> $TARGET_FILE
echo "🔍 [SCANNING]: Mencari saraf lemah..."
find $(pwd) -name "*.ts" -not -path "*/node_modules/*" | while read file; do
    logic=$(grep -cE "try|catch|async|await" "$file")
    if [ $logic -lt 2 ]; then
        echo "$file" >> $TARGET_FILE
    fi
done
echo "✅ Target diperbarui: $(wc -l < $TARGET_FILE) file."
