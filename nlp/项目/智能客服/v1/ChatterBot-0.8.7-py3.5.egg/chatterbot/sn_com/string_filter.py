#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

import re

class String_Filter(object):
    """
         功能：智能客服语义分析引擎-字符纯化
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########

        pass

    #######    STEP3：功能模块函数  #########

    def string_filter(self,question, ic='utf-8'):
        """
            功能：########【问题文本纯化】######
            输入：标准问题
            输出：纯化后的问题
            目前包含的有【CJK统一表意符号、英文、阿拉伯数字、欧洲、希腊文、阿拉伯文、泰文、越南傣语】
        """
        re_han_default = re.compile(
            "([^a-zA-Z0-9+#@￥$&\.,?!_%，。？！；\s+\u4E00-\u9FD5\u0370-\u03FF\u0600-\u06FF\u0E00-\u0E7F\u20A0-\u20CF\uAB00-\uAB5F]+)", \
            re.U)
        return re_han_default.sub('', question)

robot_string_filter = String_Filter()

def main(text):

    while True:
        try:
            question=input("输入测试问题：")
            question=robot_string_filter.string_filter(question)
            print("question",question)
        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

