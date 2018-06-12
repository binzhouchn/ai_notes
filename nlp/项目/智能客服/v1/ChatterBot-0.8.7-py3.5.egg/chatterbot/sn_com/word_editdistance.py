#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata
import Levenshtein
import time
from .question_category import robot_question_category
from .jieba_cut import robot_jieba_cut

class Word_Editdistance(object):
    """
         功能：智能客服语义分析分模块功能函数
         输入：初始化模型数据
         输出：各个模块函数
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########

        # 加载知识库标准问题字典---格式：{标准问：[标准问切词,标准答案,分类,ID]}
        self.Ques_Dict = robotdata.Ques_Dict
        # 格式：{标准问：[pc端答案，微信端答案，app端答案]}
        self.Ques_Answer = robotdata.Ques_Answer
        ##加载问题类别：标准问题{问题分类：[问题1，问题2，问题3]}
        self.Category_ques = robotdata.Category_ques

    #######    STEP3：功能模块函数  #########

    def word_editdistance_sort(self,text_list,cate,source):
        """
            功能：########【编辑距离求相似度】计算文本与知识库的编辑，计算输入问题域知识库问题相似度，排序并提取Top1
            输入：切词后问题sorted、类别、问题来源
            输出：相似问、相似置信度、ID、答案
        """
        simi_question= {}
        answer={}
        simi_editdistance=[]
        text_list_sort=sorted(text_list)
        for ques in self.Category_ques[cate]:
            # print("sorted(self.Ques_Dict[ques][0])",sorted(self.Ques_Dict[ques][0]))
            simi_edit=Levenshtein.seqratio(sorted(self.Ques_Dict[ques][0]),text_list_sort)
            dist_dict =(ques,simi_edit)
            simi_editdistance.append(dist_dict)
        simi = sorted(simi_editdistance, key=lambda item: item[1],reverse=True)
       # print("simi",simi)
        if simi[0][1]>0:
            if simi[0][1]> robotdata.config.simi_threshold:
                if source == 1:
                    answer['answare_text'] = self.Ques_Answer[simi[0][0]][0]  # 返回pc端答案
                elif source == 2:
                    answer['answare_text'] = self.Ques_Answer[simi[0][0]][1]  # 返回微信端答案
                elif source == 3:
                    answer['answare_text'] = self.Ques_Answer[simi[0][0]][2]  # 返回app端答案
                else:
                    answer['answare_text'] = self.Ques_Dict[simi[0][0]][1]  # 返回默认标准答案

                simi_question['answer']=answer
                sm = []
                for j in simi[1:]:
                    if j[1]>robotdata.config.simi_threshold:
                        sm.append({'sm_id':self.Ques_Dict[j[0]][3],'smq':j[0]})
                simi_question['Confidence']=simi[0][1]
            else:
                simi_question['answer'] = {}
        else:
            simi_question['answer'] = {}

        # print("simi_question",simi_question)
        return simi_question

    def word_editdistance(self,text_list,cate):
        """
            功能：########【问题编辑距离求相似度】计算文本与知识库的编辑，计算输入问题域知识库问题相似度，排序并提取Top1
            输入：切词后问题sorted、类别
            输出：相似问、相似置信度、ID、答案
        """
        simi_question= {}
        answer={}
        simi_editdistance=[]
        for ques in self.Category_ques[cate]:
            # print("sorted(self.Ques_Dict[ques][0])",sorted(self.Ques_Dict[ques][0]))
            simi_edit=Levenshtein.seqratio(self.Ques_Dict[ques][0],text_list)
            dist_dict =(ques,simi_edit)
            simi_editdistance.append(dist_dict)
        simi = sorted(simi_editdistance, key=lambda item: item[1],reverse=True)
       # print("simi",simi)
        if simi[0][1]>0:
            if simi[0][1]> robotdata.config.simi_threshold:
                answer['answare_text']=self.Ques_Dict[simi[0][0]][1]
                simi_question['answer']=answer
                sm = []
                for j in simi[1:]:
                    if j[1]>robotdata.config.simi_threshold:
                        sm.append({'sm_id':self.Ques_Dict[j[0]][3],'smq':j[0]})
                simi_question['Confidence']=simi[0][1]
            else:
                simi_question['answer'] = {}
        else:
            simi_question['answer'] = {}

        # print("simi_question",simi_question)
        return simi_question

#实例化语义分析模型
robot_word_editdistance_sort=Word_Editdistance()

def main(text):
    while True:
        try:
            text=input("输入测试问题：")
            time_start = time.time()
            question_cut=robot_jieba_cut.jieba_cut(text)
            cate=robot_question_category.question_category(question_cut)
            print("cate",cate,question_cut)
            simi_question=robot_word_editdistance_sort.word_editdistance(text_list=question_cut,cate=cate)
            print("simi_question",simi_question)
            print("use_time:",time.time()-time_start)

        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

