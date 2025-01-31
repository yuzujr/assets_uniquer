# 删除typora在assets生成的重复图片

import os
import hashlib
import re
import argparse

def extract_timestamp(filename):
    """从文件名中提取时间戳数字(如 'image-20250130155013464.png' 返回 20250130155013464)"""
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

def file_hash(filepath):
    """计算文件的MD5哈希"""
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main(target_dir, dry_run=True):
    files = []
    # 查找所有png文件,并且提取时间戳
    for fname in os.listdir(target_dir):
        if fname.lower().endswith('.png'):
            timestamp = extract_timestamp(fname)
            full_path = os.path.join(target_dir, fname)
            files.append((timestamp, full_path, fname))
    
    # 按时间戳从小到大排序（越早的文件越靠前）
    files.sort(key=lambda x: x[0])
    
    hashes = set()
    duplicates = []

    # 依据MD5查找重复文件
    for timestamp, full_path, fname in files:
        current_hash = file_hash(full_path)
        if current_hash in hashes:
            duplicates.append(full_path)
        else:
            hashes.add(current_hash)
    
    # 处理重复文件
    print("搜索文件夹:",target_dir)
    if duplicates:
        print("发现以下重复文件:")
        for dup in duplicates:
            print(f"  - {dup}")
        
        if not dry_run:
            for dup in duplicates:
                os.remove(dup)
            print(f"已删除 {len(duplicates)} 个重复文件.")
    else:
        print("未发现重复文件.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="删除内容重复的图片文件（保留最早版本）",allow_abbrev=False)
    parser.add_argument(
        "target_dir",
        help="目标文件夹路径（例如：./assets）"
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="启用此选项以实际删除文件（默认仅列出重复文件不删除）"
    )
    args,unknown_args = parser.parse_known_args()

    # 如果有未知参数,则报错
    if unknown_args:
        print(f"错误：检测到未知参数 {' '.join(unknown_args)}")
        exit(1)

    # 检查目录是否存在
    if not os.path.isdir(args.target_dir):
        print(f"错误：目录 '{args.target_dir}' 不存在")
        exit(1)

    # dry_run默认为True，仅当 --delete 被指定时为False
    main(args.target_dir, dry_run=not args.delete)
