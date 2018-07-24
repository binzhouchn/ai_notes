# coding: utf-8
__author__ = 'BinZHOU'
__version__ = '20180514'

# 网页去重
import os
import numpy as np
import re
import jieba
import jieba.posseg
os.sys.path.append('/公共模块文件地址')
from bz_re import *

class RP(object):
	def __init__(self, stop_words_path):
		# 加载停用词
		f = open(stop_words_path,'r')
		self.stop_words_list = [line.strip() for line in f.readlines()]
		self.dic = {}
	def ff(self, s):
		[jieba.add_word(i) for i in re.findall(DATE_REG,s)]
		[jieba.add_word(i) for i in re.findall(URL_REG,s)]
		[jieba.add_word(i) for i in re.findall(PHONE_REG,s)]
		[jieba.add_word(i) for i in re.findall(MAIL_REG,s)]
		[jieba.add_word(i) for i in re.findall(IDCARD_REG,s)]
		[jieba.add_word(i) for i in re.findall(MONEY_REG,s)]
		return list(filter(lambda x : x != '',[x.strip() for x in jieba.lcut(s,HMM=False) if x not in self.stop_words_list]))
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
	def random_projection(self, s1, s2, default_size=20):
		l1 = np.where(np.sum([self.get_hash(x,default_size) for x in self.ff(s1)],axis=0) > 0,1,0)
		l2 = np.where(np.sum([self.get_hash(x,default_size) for x in self.ff(s2)],axis=0) > 0,1,0)
		return np.count_nonzero(np.subtract(l1, l2))

if __name__ == '__main__':
	path = '../stop_words.txt'
	rp = RP(path)
	s1 ='我给了她一支笔。'
	s2 = '我把一支笔给了她。'	
	print(rp.random_projection(s1,s2))
