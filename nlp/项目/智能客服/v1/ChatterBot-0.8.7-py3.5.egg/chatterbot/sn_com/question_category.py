#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata
from .jieba_cut import robot_jieba_cut
import time

class Question_Category(object):
    """
         功能：智能客服语义分析引擎-问题分类
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########

       ##加载问题类别：标准问题{问题分类：[问题1，问题2，问题3]}
        self.Category_ques = robotdata.Category_ques

        #问题分类
        # glove模型
        self._glove = robotdata._glove                      #glove词向量模型
        self.label_cut=[(robot_jieba_cut.jieba_cut(i), i) for i in list(robotdata.Category_ques.keys())]
        self.cate_topN=robotdata.config.cate_topN



    #######    STEP3：功能模块函数  #########


    def question_category(self,text):
        """
            功能：########【问题分类】加载训练好的Glove模型，计算输入问题域知识库问题相似度
            输入：切词后问题
            输出：问题归宿类别
        """
        t = sorted([(self._glove.wmdistance(label_cut[0], text), label_cut[1]) for label_cut in self.label_cut])   #label_cut:(['任性付'], '任性付')
        # print("t",t)
        cate = []
        for i in range(self.cate_topN):
            cate.append(t[i][1])
        return str(cate[self.cate_topN-1])


#实例化语义分析模型
robot_question_category=Question_Category()


def main(text):
    while True:
        try:
            text=input("输入测试问题：")
            time_start = time.time()
            question_cut=robot_jieba_cut.jieba_cut(text)
            cate=robot_question_category.question_category(question_cut)
            print("cate",cate)
        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

