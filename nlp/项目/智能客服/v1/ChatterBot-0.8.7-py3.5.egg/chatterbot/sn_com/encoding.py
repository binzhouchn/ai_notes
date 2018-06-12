#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

class Encoding(object):
    """
         功能：智能客服语义分析引擎--标准化编码
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########
        pass

    #######    STEP3：功能模块函数  #########

    def encoding(self,question, in_coding='utf-8', out_coding='utf-8', return_bytes=False):
        """
            功能：########【问题编码标准化】######
            输入：标准问题
            输出：标准问题UTF_8编码
        """
        # 判断是否为字节
        if isinstance(question, bytes):
            s = question.decode(in_coding)
        else:
            s = question.encode(in_coding).decode(in_coding)
        if return_bytes:
            return s.encode(out_coding)
        # print("s.encode(out_coding).decode(out_coding)",s.encode(out_coding).decode(out_coding))
        return s.encode(out_coding).decode(out_coding)

robot_encoding = Encoding()

def main(text):
    while True:
        try:
            text=input("输入测试问题：")
            question=robot_encoding.encoding(text)
        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

