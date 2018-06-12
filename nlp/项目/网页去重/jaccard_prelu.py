# coding: utf-8
__author__ = 'BinZHOU'
__version__ = '20180522'

import pandas as pd
import numpy as np
import os
import jieba
import jieba.posseg as pseg
os.sys.path.append('**random_projection_v2所在的文件夹地址**')
from random_projection_v2 import *

THRESHOLD = 0.8342
user_dict_path = './user_dict.txt'
stop_words_path = './stop_words.txt'
file_path = './data1.csv'
# 初始化RP类
rp = RP(user_dict_path, stop_words_path)
# 读取要去重的文件
data = pd.read_csv(file_path, sep='\t')
data = data[['content']]
# 生成切词后的列 1w条数据大概9min
data['word_cut'] = data.content.apply(lambda x : rp.ff(x))
# 得到去重后的index list和content list
idx_list, content_list = rp.get_nonredundant(data, THRESHOLD)

# save
df = pd.DataFrame(list(zip(idx_list, content_list)),columns=['idx','content'])
df.to_csv('dup_keep.csv',index=True, encoding='utf-8',sep='\t')

