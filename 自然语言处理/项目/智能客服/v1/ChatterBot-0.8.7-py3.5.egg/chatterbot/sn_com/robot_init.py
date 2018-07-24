#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

from chatterbot.sn_config.robot_config import *
from gensim.models import Word2Vec,KeyedVectors
from gensim.similarities import WmdSimilarity
import jieba
import pickle
import logging.config

config=Robot_Configure()

class Robot_Init(object):
    """
         功能：加载语义分析引擎-初始化数据
         输入：param1  config初始化数据存放目录配置文件
         输出：语义分词所需的模型
    """

    def __init__(self, config):
        self.config=config
        ###########################################################################################
        #############################################【公共数据加载】##############################
        ###########################################################################################

        #1、加载金融专用字典
        try:
            print("加载finance专用字典...")
            jieba.load_userdict(config.finWordDict_path)
        except Exception as e:
            print(e)

        #2、加载停用词
        try:
            print("加载停用词字典...")
            self.stopwords=[line.strip() for line in open(self.config.stop_words_path, 'r', encoding='utf-8').readlines()]
        except Exception as e:
            print(e)

        #3、加载知识库标准问题字典-----格式：{标准问：[标准问切词,标准答案,分类,ID]}
        try:
            print("加载知识库 标准问题列表...")
            self.Ques_Dict=pickle.load(open(self.config.Ques_Dict_path,'rb'))
        except Exception as e:
            print(e)

        # 3-1、加载知识库标准问-答案-----格式：{标准问：[pc端答案，微信端答案，app端答案]}
        try:
            print("加载知识库 标准问题-答案...")
            self.Ques_Answer = pickle.load(open(self.config.Ques_Answer_path, 'rb'))
        except Exception as e:
            print(e)

        ##加载问题类别：标准问题{问题分类：[问题1，问题2，问题3]}
        try:
            print("加载知识库问题分类列表...",)
            self.Category_ques=pickle.load(open(self.config.Category_ques_path,'rb'))
        except Exception as e:
            print(e)

        ###########################################################################################
        #############################################【算法模块数据加载】##########################
        ###########################################################################################
        # 4、通用知识库，构造的Trie树
        try:
            print("加载闲聊知识库...",)
            self.Comques_Trie = pickle.load(open(self.config.Comques_Trie_path, 'rb'))
        except Exception as e:
                print(e)

        # 4、转人工知识库字典：{标准问：(key,ID)}
        try:
            print("加载转人工知识库...", )
            self.artifical_scene_dict = pickle.load(open(self.config.artifical_scene_dict_path, 'rb'))
        except Exception as e:
            print(e)

        #4、纠错问题初始化数据
        try:
            print("加载纠错数据...")
            self.fre_dict=pickle.load(open(self.config.fre_dict_path,'rb'))
            self.fre2_dict = pickle.load(open(self.config.fre2_dict_path, 'rb'))
            self.fre3_dict = pickle.load(open(self.config.fre3_dict_path, 'rb'))
            self.ott_dict = pickle.load(open(self.config.ott_dict_path, 'rb'))
            self.replace_dict = pickle.load(open(self.config.replace_dict_path, 'rb'))
        except Exception as e:
            print(e)

        #6、问题分类：golve词向量模型
        try:
            print("加载glove词向量....",)
            self._glove = KeyedVectors.load_word2vec_format(self.config.glovevec_path)
        except Exception as e:
            print(e)

        #7、相似问：全量语料训练的word2vec词向量模型
        try:
            self.word2vec_model = Word2Vec.load(self.config.word2vec_path)
        except Exception as e:
            print(e)

    #5、分词函数：定义分词去停用词
    def jieba_cut(self,text):
        """
            功能：调用结巴分词函数,去停用词
            输入：标准问题
            输出：问题分词后的List
        """
        text_words=jieba.cut(text,cut_all=False)
        text_list=[word for word in text_words if word not in self.stopwords]
        return text_list

    # 7-1、按照分类加载对应分类的相似度模型：把对知识库 相似距离simmilar_model 转换成相似度模型
    def wmdsimilarity_model(self):
        """
            功能：按照问题类别，生成、加载对应的类别相似度模型
            输入：word2vec词向量模型、知识库字典、类别-问题字典
            输出：问题类别相似度模型
        """
        CateSimi_model={}
        cates=self.Category_ques.keys()
        for cate in cates:
            questions = self.Category_ques[cate]
            question_list = []
            for question in questions:
                question_list.append(self.Ques_Dict[question][0])
            print("加载 %s 类别相似度模型" % (cate))
            CateSimi_model[cate] = WmdSimilarity(question_list, self.word2vec_model, self.config.simi_topN)  # 把对知识库 相似距离simmilar_model 转换成相似度模型
        return CateSimi_model

#生成初始化数据实例
robotdata=Robot_Init(config)
logging.config.fileConfig(robotdata.config.robot_logging_conf_path)  # 采用配置文件
logger_robot = logging.getLogger("simpleExample")




