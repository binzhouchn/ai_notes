#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

# 多进程压测
from sn_semantic.semantic_analysis import *
import pandas as pd
from multiprocessing import Process,Pool
QUESTION_PATH = './ori_data/aaa.xlsx'

df = pd.read_excel(QUESTION_PATH, sheet_name=0, ignore_index=False)
def run_test():
    # while True:
        for i in range(len(df['question'])):
            result=sn_robotbest_match(df['question'][i],2)
            print("question",df['question'][i])
            print("result",result)

if __name__=="__main__":
    for i in range(1):
        p=Process(target=run_test,args=())
        p.start()