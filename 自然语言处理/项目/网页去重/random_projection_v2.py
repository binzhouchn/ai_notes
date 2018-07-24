# coding: utf-8
__author__ = 'BinZHOU'
__version__ = '20180519'

# 网页去重
import os
import numpy as np
import re
import jieba
import jieba.posseg
# os.sys.path.append('/公共模块')
from bz_re import *

class RP(object):
	def __init__(self, user_dict_path, stop_words_path):
		# 加载外部词典
		jieba.initialize()
		jieba.load_userdict(user_dict_path)
		# 加载停用词
		f = open(stop_words_path,'r',encoding='utf-8')
		self.stop_words_list = [line.strip() for line in f.readlines()]
		self.dic = {}
	def ff(s):
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
        num_list = re_DATE_REG1.findall(s)+re_URL_REG.findall(s)+re_PHONE_REG.findall(s)+re_MAIL_REG.findall(s) +\
        re_IDCARD_REG.findall(s)+re_MONEY_REG1.findall(s)+re_MONEY_REG2.findall(s)+re_DATE_REG2.findall(s)+re_HYPER_REG.findall(s)
        return set(filter(lambda x : x != '',[x.strip() for x in jieba.lcut(s,HMM=True) if x not in stop_words_list])), set(num_list) # 这一步先变成set，后面不加判断会快很多  
    # 杰卡顿距离version2 目前距离阈值暂定0.8342
    @staticmethod
    def jaccard_dist(x, y):
		if len(x) == 0 or len(y) == 0:
		    return 0
		c = x.intersection(y)
		return len(c)*1.0 / (len(x)+len(y)-len(c))
	@classmethod
	def get_similarity(cls, x1, x2, y1, y2, type_dist = 'jaccard'):
	    if type_dist == 'jaccard':
	        dist1 = cls.jaccard_dist(x1,x2)
	        dist2 = cls.jaccard_dist(y1,y2)
	        # 构造PReLU函数
	        if dist2 <= 0.85:
	            dist2 = 2.0/17*dist2
	        else:
	            dist2 = 6.0*dist2-5.0
	        alpha = 0.60/(1+(len(y1)+len(y2))*1.0/(len(x1)+len(x2)))
	        # 调节数字比和数字量beta
	        beta = 1.10-(len(y1)+len(y2))/(len(x1)+len(x2))/2.35
	        return 0.51/alpha*beta*dist1+0.49*alpha/beta*dist2
    def get_hash(self, token, default_size):
		hash_20 = list(np.random.choice([-1,1],size=default_size))
		if token in self.dic.keys():
			return self.dic.get(token)
		elif hash_20 in self.dic.values():
			while True:
				hash_20 = list(np.random.choice([-1,1],size=default_size))
				if hash_20 not in self.dic.values():
					self.dic[token] = hash_20
					return hash_20
		else:
			self.dic[token] = hash_20
			return hash_20
	@classmethod
	def get_nonredundant(cls, df, thres):
		idx = 0
		idx_list = []
		content_list = []
		while idx < len(df):
		    word_cut1 = df.word_cut.iloc[idx]
		    if idx == len(df)-1:
		        idx_list.append(idx)
		        content_list.append(df.content.iloc[idx])
		        idx += 1
		        break
		    dist_list = df.word_cut.iloc[idx+1:].apply(lambda x : cls.get_similarity(x[0],word_cut1[0],x[1],word_cut1[1]))
		    if len(dist_list[dist_list.apply(lambda x : x > thres)]) == 0:
		        idx_list.append(idx)
		        content_list.append(df.content.iloc[idx])
		    idx += 1
		return idx_list, content_list
	def random_projection(self, s1, s2, default_size=20):
		l1 = np.where(np.sum([self.get_hash(x,default_size) for x in self.ff(s1)],axis=0) > 0,1,0)
		l2 = np.where(np.sum([self.get_hash(x,default_size) for x in self.ff(s2)],axis=0) > 0,1,0)
		return np.count_nonzero(np.subtract(l1, l2))
	def get_singleStr_hash(self, s, default_size=20):
		return np.where(np.sum([self.get_hash(x,default_size) for x in self.ff(s)],axis=0) > 0,1,0)
	def test(self, l, s,default_size=20):
		return np.count_nonzero(np.subtract(l, self.get_singleStr_hash(s)))

if __name__ == '__main__':
	user_dict_path = '../user_dict.txt'
	stop_words_path = '../stop_words.txt'
	rp = RP(user_dict_path,stop_words_path)
	s1 ='document1..'
	s2 = 'document2..'	
	print('distance: ' + str(rp.random_projection(s1,s2)))
