#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from sn_com.robot_init import robotdata
import time
from sn_com.question_category import robot_question_category
from sn_com.jieba_cut import robot_jieba_cut

class Word2vec_Wmddistance(object):
    """
         功能：智能客服语义分析引擎-词向量相似度计算
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########

        # 加载知识库标准问题字典---格式：{标准问：[标准问切词,标准答案,分类,ID]}
        self.Ques_Dict = robotdata.Ques_Dict

        #格式：{标准问：[pc端答案，微信端答案，app端答案]}
        self.Ques_Answer=robotdata.Ques_Answer

        ##加载问题类别：标准问题{问题分类：[问题1，问题2，问题3]}
        self.Category_ques = robotdata.Category_ques

        #相似问
        self.CateSimi_model=robotdata.wmdsimilarity_model()        #分类类别相似度模型

    #######    STEP3：功能模块函数  #########

    def word2vec_wmddistance(self,text_list,cate,source):
        """
            功能：########【7、相似问模块】加载训练好的word2vec模型，计算输入问题域知识库问题相似度，排序并提取Top1
            输入：切词后问题、类别、问题来源
            输出：相似问、相似置信度、ID、答案
        """
        simi_question= {}
        answer={}
        simi=self.CateSimi_model[cate][text_list]                  #根据相似度模型求相似问
        # print("simi",simi)
        if len(simi)>0:
            if simi[0][1]> robotdata.config.simi_threshold:
                if source==1:
                    answer['answare_text'] = self.Ques_Answer[self.Category_ques[cate][simi[0][0]]][0]    #返回pc端答案
                elif source==2:
                    answer['answare_text'] = self.Ques_Answer[self.Category_ques[cate][simi[0][0]]][1]    #返回微信端答案
                elif source==3:
                    answer['answare_text'] = self.Ques_Answer[self.Category_ques[cate][simi[0][0]]][2]      #返回app端答案
                else:
                    answer['answare_text']=self.Ques_Dict[self.Category_ques[cate][simi[0][0]]][1]          #返回默认标准答案
                simi_question['answer']=answer
                sm = []
                for j in simi[1:]:
                    if j[1]>robotdata.config.simi_threshold:
                        sm.append({'sm_id':self.Ques_Dict[self.Category_ques[cate][j[0]]][3],'smq':self.Category_ques[cate][j[0]]})
                simi_question['Confidence']=simi[0][1]
            else:
                simi_question['answer'] = {}
        else:
            simi_question['answer'] = {}

        # print("simi_question",simi_question)
        return simi_question


#实例化语义分析模型
robot_word2vec_wmddistance=Word2vec_Wmddistance()


def main(text):
    # semantic_analysis = Semantic_Analysis()
    while True:
        try:
            text=input("输入测试问题：")
            time_start = time.time()
            question_cut=robot_jieba_cut.jieba_cut(text)
            print("question_cut",question_cut)
            cate=robot_question_category.question_category(question_cut)
            print("cate",cate,question_cut)
            simi_question=robot_word2vec_wmddistance.word2vec_wmddistance(text_list=question_cut,cate=cate,source=1)
            print("simi_question",simi_question)
            print("use_time:",time.time()-time_start)

        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

