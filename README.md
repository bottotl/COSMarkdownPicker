# COSMarkdownPicker
# 基于腾讯优图（COS）的 markdown 上传脚本

以前用[markdownpicker](https://github.com/kingname/MarkdownPicPicker)但是觉得图床不太稳定，抽空做了一个基于腾讯云的上传

## init 

### 1.Change following config in qcloud_cos/uploader.py

secret_id = '????'     # 替换为用户的secret_id

secret_key = '????'     # 替换为用户的secret_key

region = '????'    # 替换为用户的region

bucket= '????'  # Bucket由bucketname-appid组成

token = ''      # 使用临时秘钥需要传入Token，默认为空,可不填

![](http://jft0m-1254413962.cossh.myqcloud.com/2019-05-07-15-29-59.png)
 
![](http://jft0m-1254413962.cossh.myqcloud.com/2019-05-07-15-28-15.png)

### 2.Install tools

step 1: `pngpaste`

brew install pngpaste

step 2: [cos-python-sdk](https://github.com/tencentyun/cos-python-sdk-v5)

使用pip安装
pip install -U cos-python-sdk-v5

手动安装:
download [cos-python-sdk](https://github.com/tencentyun/cos-python-sdk-v5)
python setup.py install

## how to use

python MarkdownPicPicker.py
