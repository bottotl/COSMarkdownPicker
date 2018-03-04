# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError
import os
import sys

# 腾讯云COSV5Python SDK, 目前可以支持Python2.6与Python2.7

# pip安装指南:pip install -U cos-python-sdk-v5

# cos最新可用地域,参照https://www.qcloud.com/document/product/436/6224

# 设置用户属性, 包括secret_id, secret_key, region
# appid已在配置中移除,请在参数Bucket中带上appid。Bucket由bucketname-appid组成
secret_id = '????'     # 替换为用户的secret_id
secret_key = '????'     # 替换为用户的secret_key
region = '????'    # 替换为用户的region
bucket= '????'  # Bucket由bucketname-appid组成
token = ''                 # 使用临时秘钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, Secret_id=secret_id, Secret_key=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)

class Uploader(object):
    def upload(self, picture_path):
        file_name = os.path.basename(picture_path)
        with open(picture_path, 'rb') as fp:
            response = client.put_object(
                Bucket=bucket,
                Body=fp,
                Key=file_name,
                StorageClass='STANDARD',
                CacheControl='no-cache',
                ContentDisposition='download.txt'
            )
            file_url = 'http://' + bucket + '.cossh.myqcloud.com/' + file_name
            self.write_markdown_picture_url(file_url)

    def write_markdown_picture_url(self, file_url):
        platform = sys.platform
        command = ''
        if platform == 'win32':
            command = 'echo {} | clip'.format(file_url)
        elif platform == 'darwin':
            command = 'echo "{}" | pbcopy'.format(file_url)
        os.system(command)
        print file_url
        print('the url is already in your clipboard!')
