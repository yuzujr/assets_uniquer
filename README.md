# assets_uniquer
基于文件名时间戳删除typora中误操作出现的重复图片,默认为png图片
注意:此脚本假设md文件中保留最早的图片,即之后的重复图片将被删除.

## Usage

`assets_uniquer.py [-h] [--delete] target_dir`

(Optional): 和[fd](https://github.com/sharkdp/fd)一起使用,批量处理assets文件夹
```
fd 'assets' -t directory ~/Documents/Note/ -x python assets_uniquer.py {} --delete
```

**位置参数:**

`target_dir`  目标文件夹路径（例如：./assets）

**选项:**

`-h`, `--help`  显示帮助

  `--delete`    启用此选项以实际删除文件（默认仅列出重复文件不删除）
