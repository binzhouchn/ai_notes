# coding: utf-8
__author__ = 'BinZHOU'
__version__ = '20180509'

import os
import re
from pprint import pprint
import time
import jieba
import jieba.analyse
import jieba.posseg as pseg
from bz_xx import *

# 加载外部词典
jieba.initialize()
jieba.load_userdict('user_dict.txt')


def merge_noun(a):
    idx1 = 0
    ll = []
    while idx1 < len(a):
        fg = False
        word = a[idx1].word
        flag = a[idx1].flag
        idx2 = idx1+1
        while idx2 < len(a):
            if a[idx1].flag in ("an","Ng","n","nr","ns","nt","nz","vn") and a[idx2].flag in ("an","Ng","n","nr","ns","nt","nz","vn"):
#             if a[idx1].flag[0] == a[idx2].flag[0] == 'n':
                word += a[idx2].word
                idx2 += 1
                fg = True
            else:
                break
        if fg:
            ll.append((word, 'n'))
        else:
            ll.append((word, flag))
        idx1 = idx2
    return ll


def tokenize2(b):
    ll2 = []
    for sen in b:
        word = sen[0]
        flag = sen[1]
        if len(word) == 1:
            ll2.append(word+' '+'S'+flag)
        else:
            ll2 += list(map(lambda x:x[0]+' '+x[1], zip([x for x in word], ['B'+flag]+['M'+flag]*(len(word)-2)+['E'+flag])))
    return ll2
def input_user_q(s):
    pseg_cut = pseg.lcut(s.strip().replace(' ','，').replace('\n',''))
    merge_noun_result = merge_noun(pseg_cut)
    return tokenize2(merge_noun_result)

def ner_f(st,tagger):
    l = []
    s = ''
    for i in range(tagger.size()):
        if tagger.y2(i) == 'B-N' or tagger.y2(i) == 'M-N':
            s += tagger.x(i,0)
        elif tagger.y2(i) == 'E-N':
            s += tagger.x(i,0)
            l.append(s)
            s = ''
    return l

def ner_run(tagger, s):
	tagger.clear()
	l = input_user_q(s)
	[tagger.add(x) for x in l]
	tagger.parse()

	return ner_f(s,tagger)

if __name__ == '__main__':

	# 读取stop_words.txt 默认启用
	stop_w = True
	f = open('stop_words.txt','r')
	stop_words_list = [line.strip() for line in f.readlines()]

	# 测试字符串列表
	user_file = open('user_file.txt','r')
	test_list = [line.strip() for line in user_file.readlines()]
	# 加入正则使分词细化
	for s in test_list:
		re_DATE_REG1 = re.compile(DATE_REG1)
		re_URL_REG = re.compile(URL_REG)
		re_PHONE_REG = re.compile(PHONE_REG)
		re_MAIL_REG = re.compile(MAIL_REG)
		re_IDCARD_REG = re.compile(IDCARD_REG)
		re_MONEY_REG1 = re.compile(MONEY_REG1)
		re_MONEY_REG2 = re.compile(MONEY_REG2)
		re_DATE_REG2 = re.compile(DATE_REG2)
		re_HYPER_REG = re.compile(HYPER_REG)
		[jieba.add_word(i,1,'date') for i in re_DATE_REG1.findall(s)]
		[jieba.add_word(i,1,'url') for i in re_URL_REG.findall(s)]
		[jieba.add_word(i,1,'phone') for i in re_PHONE_REG.findall(s)]
		[jieba.add_word(i,1,'mail') for i in re_MAIL_REG.findall(s)]
		[jieba.add_word(i,1,'idcard') for i in re_IDCARD_REG.findall(s)]
		[jieba.add_word(i,1,'money') for i in re_MONEY_REG1.findall(s)]
		[jieba.add_word(i,1,'money') for i in re_MONEY_REG2.findall(s)]
		[jieba.add_word(i,1,'date') for i in re_DATE_REG2.findall(s)]
		[jieba.add_word(i,1,'hyper') for i in re_HYPER_REG.findall(s)]

	# print('词性标注：\t')
	# for s in test_list:
	# 	if stop_w:
	# 		print([x for x in pseg.lcut(s) if x.word not in stop_words_list])
	# 	else:
	# 		print(pseg.lcut(s))

	# print('\n')
	# print('实体识别:\t')
	# # 加载模型
	# tagger = CRFPP.Tagger("-m model_c2_m256_e0003 -v 3 -n2")
	# for s in test_list:
	# 	print(ner_run(tagger,s))

	# print('\n')
	# print('动词提取：\t')
	# for s in l:
	# 	if stop_w:
	# 		print([x.word for x in pseg.lcut(s) if (x.word not in stop_words_list and x.flag == 'v')])
	# 	else:
	# 		print([x.word for x in pseg.lcut(s) if x.flag == 'v'])
    # 加载模型
	tagger = CRFPP.Tagger("-m model_c2_m256_e0003 -v 3 -n2")
	for s in test_list:
		print(ner_run(tagger,s) + [x.word for x in pseg.lcut(s) if (x.word not in stop_words_list and x.flag == 'v')])
