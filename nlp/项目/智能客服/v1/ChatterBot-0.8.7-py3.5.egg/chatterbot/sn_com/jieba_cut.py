#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata
import time

class Jieba_Cut(object):
    """
         功能：智能客服语义分析引擎-分词、去停用词
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########
        pass

    #
    def jieba_cut(self, text):
        """
            功能：########【分词，去停用词】# 定义切词函数，包装一下jieba分词函数
            输入：标准问题
            输出：切词后的问题List
        """
        return robotdata.jieba_cut(text)

robot_jieba_cut=Jieba_Cut()

def main(text):
    while True:
        try:
            text=input("输入测试问题：")
            time_start = time.time()
            text_cut=robot_jieba_cut.jieba_cut(text)
            print("aa",text_cut)

        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

