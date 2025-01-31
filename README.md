# assets_uniquer
基于文件名时间戳删除typora中误操作出现的重复图片,默认为png图片

## Usage

`assets_uniquer.py [-h] [--delete] target_dir`

和[fd](https://github.com/sharkdp/fd)一起使用,批量处理assets文件夹
```
fd 'assets' -t directory ~/Documents/Note/ -x python assets_uniquer.py {} --delete
未发现重复文件.
未发现重复文件.
未发现重复文件.
未发现重复文件.
未发现重复文件.
未发现重复文件.
未发现重复文件.
发现以下重复文件:
  - /home/yuzujr/Documents/Note/汇编语言/assets/image-20240808150124675.png
已删除 1 个重复文件.
未发现重复文件.
发现以下重复文件:
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240607162724034.png
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240709131629952.png
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240709133012740.png
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240709134443434.png
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240711181145980.png
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240714173759484.png
  - /home/yuzujr/Documents/Note/C++/C++ Primer/assets/image-20240720203751222.png
已删除 7 个重复文件.
```

**位置参数:**

`target_dir`  目标文件夹路径（例如：./assets）

**选项:**

`-h`, `--help`  显示帮助

  `--delete`    启用此选项以实际删除文件（默认仅列出重复文件不删除）
