from ImageGrab import ImageGrab
from qcloud_cos.uploader import Uploader
import sys
import os

__version__ = '0.0.1'
__author__ = 'jft0m'


class MarkrdownPicPicker(object):
    def __init__(self):
        self.picture_folder = 'markdownPic'
        self.picture_suffix = 'png'
        self.uploader = None
        self.imageGrab = None
        self.init_environment()
        self.upload_picture()

    def _to_string(self):
        """
        To test if the config reading is ok
        :return: None
        """
        print("folder", self.picture_folder)
        print("suffix", self.picture_suffix)

    def init_environment(self):
        if not os.path.exists(self.picture_folder):
            os.makedirs(self.picture_folder)
        self.uploader = Uploader()
        self.imageGrab = ImageGrab(self.picture_folder, self.picture_suffix) if ImageGrab else None

    def upload_picture(self):
        picture_path_list = self.imageGrab.save_picture()
        if len(picture_path_list) > 0:
            print('local file path:', picture_path_list)
            print('start upload')
            self.uploader.upload(picture_path_list[0])
            return True
        else:
            print('fail create image')
            return False

if __name__ == '__main__':
    MarkrdownPicPicker()


