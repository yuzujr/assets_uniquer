# assets_uniquer
基于文件名时间戳删除typora中误操作出现的重复图片,默认为png图片

#### Usage
assets_uniquer.py [-h] [--delete] target_dir

positional arguments:
  target_dir  目标文件夹路径（例如：./assets）

options:
  -h, --help  show this help message and exit
  --delete    启用此选项以实际删除文件（默认仅列出重复文件不删除）
