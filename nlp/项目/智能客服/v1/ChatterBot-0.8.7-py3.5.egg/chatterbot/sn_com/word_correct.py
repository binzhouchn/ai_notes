#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from .robot_init import robotdata
from .jieba_cut import robot_jieba_cut
import re
import pandas as pd
import time
from pypinyin import lazy_pinyin
import Levenshtein


class Word_Correct(object):
    """
         功能：智能客服语义分析引擎-纠错
         输入：
         输出：
    """
    def __init__(self, **kwargs):
        #######    STEP1：公用数据部分  #########
       # 纠错数据
        self.fre_dict = robotdata.fre_dict
        self.fre2_dict = robotdata.fre2_dict
        self.fre3_dict = robotdata.fre3_dict
        self.ott_dict = robotdata.ott_dict
        self.replace_dict = robotdata.replace_dict

    ## 修改correct_step-----------------------------------------------------------------
    def correct_step(self,word_wrong, data, num, ott_dict):
        candidate = {'candidate_word': [], 'candidate_fre': []}
        pinyin_word = str(lazy_pinyin(word_wrong))
        # 查找word_wrong的同音词
        if pinyin_word in ott_dict.keys():
            c_set = ott_dict[pinyin_word]
            # 组装成candidate
            [(candidate['candidate_word'].append(w[0]), candidate['candidate_fre'].append(w[1])) for w in c_set]

        if len(candidate['candidate_word']) == 0:  # 如果还是没有找到, 查找拼音编辑距离最小的词
            return data
        sorted_candidate = pd.DataFrame(candidate).sort_values(by='candidate_fre', axis=0, ascending=False)  # 根据频率排序
        sorted_candidate.index = range(0, len(sorted_candidate['candidate_fre']))
        word_correct = sorted_candidate['candidate_word'][0]  # 用频率最高的词进行纠错
        data[num] = word_correct
        # print('纠正后的结果：',data)
        return data

    #-----------------------------------------------------------------------------------

    def replace_words(self,sentence_list):
        # 定义新的句子列表
        # print("sentence_list",sentence_list)
        new_sentence = []
        for word in sentence_list:
            for candidate_replacement in self.replace_dict:
                if candidate_replacement in word:
                    word = word.replace(candidate_replacement, self.replace_dict[candidate_replacement])
            new_sentence.append(word)
        return new_sentence

    def correct(self,sentence):
        """
            功能：########【问题纠错】##############
            输入：输入问题
            输出：纠错后问题
        """
        jieguo=[]
        data =robot_jieba_cut.jieba_cut(sentence)  # 分词
        jieba_len = len(data)
        if jieba_len <= 0:
            # print("词数太小，放弃纠错!",data)
            return sentence
        data = self.replace_words(data)
        jieba_key = []
        jieba_pro = []
        for i in range(0, jieba_len):
            if data[i] not in self.fre_dict['word']:
                pro = -1
            else:
                pro = self.fre_dict['frequency'][self.fre_dict['word'].index(data[i])]
            jieba_key.append(data[i])
            if pro:
                jieba_pro.append(pro)
            else:
                jieba_pro.append(0)
        wrong_count = []
        for i in range(0, len(jieba_pro)):
            if jieba_pro[i] < 0:
                wrong_count.append(i)
        if len(wrong_count) == 1:
            # self.correct_step(data[wrong_count[0]], data, wrong_count[0], self.fre_dict, self.fre2_dict, self.fre3_dict)
            self.correct_step(data[wrong_count[0]], data, wrong_count[0], self.ott_dict)
            return  ''.join(''.join(elems) for elems in data)
        elif len(wrong_count) >= 2:
            k = 0
            while k < len(wrong_count):
                if k < len(wrong_count) - 2 and wrong_count[k] + 1 == wrong_count[k + 1] and wrong_count[k + 1] + 1 == \
                        wrong_count[k + 2]:
                    wrong_word = data[wrong_count[k]] + data[wrong_count[k + 1]] + data[wrong_count[k + 2]]
                    data[wrong_count[k + 1]] = ""
                    data[wrong_count[k + 2]] = ""
                    # self.correct_step(wrong_word, data, wrong_count[k], self.fre_dict, self.fre2_dict, self.fre3_dict)
                    self.correct_step(wrong_word, data, wrong_count[k], self.ott_dict)
                    k += 3
                if k < len(wrong_count) - 1 and wrong_count[k] + 1 == wrong_count[k + 1]:
                    wrong_word = data[wrong_count[k]] + data[wrong_count[k + 1]]
                    data[wrong_count[k + 1]] = ""
                    # self.correct_step(wrong_word, data, wrong_count[k], self.fre_dict, self.fre2_dict, self.fre3_dict)
                    self.correct_step(wrong_word, data, wrong_count[k], self.ott_dict)
                    k += 2
                elif k < len(wrong_count):
                    # self.correct_step(data[wrong_count[k]], data, wrong_count[k], self.fre_dict, self.fre2_dict, self.fre3_dict)
                    self.correct_step(data[wrong_count[k]], data, wrong_count[k], self.ott_dict)
                    k += 1

            return ''.join(''.join(elems) for elems in data)
            # for i in data:
            #     jieguo.append(i)
            # print("jieguo_2",jieguo)
            # return jieguo
        else:
            return ''.join(''.join(elems) for elems in data)
            # jieguo=data
            # print("jieguo_0",jieguo)
            # return jieguo


#实例化语义分析模型

robot_word_correct=Word_Correct()

def main(text):
    while True:
        try:
            text=input("输入测试问题：")
            time_start = time.time()
            question=robot_word_correct.correct(text)
            print("question",question)
            print("use_time",time.time()-time_start)

        except Exception as e:
            raise e

if __name__=='__main__':
    main(text="")

