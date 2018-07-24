#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata


class Precise_Search(object):
    """
         功能：智能客服语义分析引擎-精确搜索
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP2：功能模块数据  #########
        #Trie树 字典数据，常用问句
        # 加载知识库标准问题字典---格式：{标准问：[标准问切词,标准答案,分类,ID]}
        self.Ques_Dict = robotdata.Ques_Dict
        # 格式：{标准问：[pc端答案，微信端答案，app端答案]}
        self.Ques_Answer = robotdata.Ques_Answer

    def precise_search(self,question,source):
        """
            功能：########【精确问题搜索】输入问题与知识库问题精确匹配
            输入：标准问题，来源编码
            输出：相似问
        """
        simi_question={}
        answer = {}
        simi_ques=self.Ques_Dict.has_key(question)      #判断知识库树，是否存在 输入问题
        # print("sddd",self.Ques_Dict)
        # print("simi_ques",simi_ques)
        if  simi_ques:
            answer['aid'] = self.Ques_Dict[question][3]
            if source == 1:
                answer['answare_text'] = self.Ques_Answer[question][0]  # 返回pc端答案
            elif source == 2:
                answer['answare_text'] = self.Ques_Answer[question][1]  # 返回微信端答案
            elif source == 3:
                answer['answare_text'] = self.Ques_Answer[question][2]  # 返回app端答案
            else:
                answer['answare_text'] = self.Ques_Dict[question][1]  # 返回默认标准答案
            answer['atype'] = 0
            simi_question['answer'] = answer
            simi_question['Confidence'] = 1
        else:
            simi_question['answer'] = {}
        return simi_question

robot_precise_search=Precise_Search()

def main(text):
    while True:
        try:
            question=input("输入测试问题：")
            print("len(question)",len(question))
            simi_question=robot_precise_search.precise_search(question)
            print("aaaa",simi_question,type(simi_question))
            if simi_question:
                print("simi_question1",simi_question)
                    # return simi_question
        except Exception as e:
            raise e


if __name__=='__main__':
    main(text="")

