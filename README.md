# COSMarkdownPicker
# 基于腾讯优图（COS）的 markdown 上传脚本

以前用[markdownpicker](https://github.com/kingname/MarkdownPicPicker)但是觉得图床不太稳定，抽空做了一个基于腾讯云的上传

## init 

### 1.change following config in qcloud_cos/uploader.py

  secret_id = '????'     # 替换为用户的secret_id
  secret_key = '????'     # 替换为用户的secret_key
  region = '????'    # 替换为用户的region
  bucket= '????'  # Bucket由bucketname-appid组成
  token = ''                 # 使用临时秘钥需要传入Token，默认为空,可不填
  
### install cos-python-sdk

pip install -U cos-python-sdk-v5

## how to use

python MarkdownPicPicker.py
