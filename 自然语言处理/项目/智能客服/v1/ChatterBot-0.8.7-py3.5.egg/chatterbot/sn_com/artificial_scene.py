#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata
from .jieba_cut import robot_jieba_cut

class Artificial_Scene(object):
    """
         功能：智能客服语义分析引擎-人工场景判断
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########
        # 格式---->>>>{标准问：(关键词,ID)}
        self.artificial_scene_dict=robotdata.artifical_scene_dict
        pass

    #######    STEP3：功能模块函数  #########

    def search_artificial_scene(self,question):
        """
            功能：########【人工场景判断】######
            输入：标准问题，人工场景字典列表artificial_scene_dict
            输出：标准答案，是否是人工场景
        """
        simi_question = {}
        # print("question传入：",question)
        for item in self.artificial_scene_dict:
            if set(set(self.artificial_scene_dict[item][0])).issubset(question):            #判断人工场景关键词是否在问题中
                simi_question['answer'] ={}
                simi_question['intentionCode']=str(self.artificial_scene_dict[item][1])
        # print("simi_question",simi_question)
        return simi_question

robot_artificial_scene = Artificial_Scene()

def main(text):
    while True:
        try:
            text=input("输入测试问题：")
            text_list=robot_jieba_cut.jieba_cut(text)
            print("text_list",text_list)
            question=robot_artificial_scene.search_artificial_scene(text_list)
        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

