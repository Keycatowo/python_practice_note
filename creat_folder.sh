#!/bin/bash

# 檢查使用者是否輸入了檔案名稱
if [ -z "$1" ]; then
  echo "請輸入要建立資料夾的檔案名稱"
  exit 1
fi

# 以讀取使用者指定的檔案的方式，逐行建立資料夾
while read line; do
    mkdir "$line"         # 使用目前讀取的行內容建立資料夾
    touch "$line/README.md"  # 在剛剛建立的資料夾下建立 README.md 檔案
done < "$1"
