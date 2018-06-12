#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata


class Search_Trie(object):
    """
         功能：智能客服语义分析引擎-闲聊树搜索
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP2：功能模块数据  #########
        #Trie树 字典数据，常用问句
        self.Comques_Trie=robotdata.Comques_Trie

    def search_trie(self,question):
        """
            功能：########【闲聊树搜索】Trie树搜索 闲聊问题
            输入：问题
            输出：相似问
        """
        simi_question={}
        answer = {}
        simi_ques=self.Comques_Trie.longest_prefix_item(question, default=-1)   #Trie最大前缀匹配
        # print("simi_ques",simi_ques)
        if  simi_ques != -1:
            answer['answare_text'] = simi_ques[1][0]
            simi_question['answer'] = answer
            simi_question['Confidence'] = 1
        else:
            simi_question['answer'] = {}
        return simi_question

robot_search_trie=Search_Trie()

def main(text):
    while True:
        try:
            question=input("输入测试问题：")
            print("len(question)",len(question))
            if len(question)<7:
                simi_question=robot_search_trie.search_trie(question)
                print("aaaa",simi_question,type(simi_question))
                if simi_question:
                    print("simi_question1",simi_question)
                    # return simi_question
                else:
                    pass
            else:
                pass
        except Exception as e:
            raise e


if __name__=='__main__':
    main(text="")

