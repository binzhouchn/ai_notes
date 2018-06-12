#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

######################语义分析引擎配置文件################
base_path='/opt/anaconda3/lib/python3.5/site-packages/ChatterBot-0.8.7-py3.5.egg/chatterbot'

class Robot_Configure(object):
    ##########【公共数据】###################

    #【金融专用词典】jieba自定义字典路径
    finWordDict_path=base_path+'/sn_data/sn_ori_data/finWordDict.txt'
    # finWordDict_path='/opt/gongxf/python3_pj/Robot/word_correction/data/MY_DICT.dat'

    #【通用停用词字典】停用词文件路径--------
    stop_words_path =base_path+ '/sn_data/sn_ori_data/stop_words.txt'

    #【知识库标准问题字典】格式：{标准问：[标准问切词,标准答案,分类,ID]}
    Ques_Dict_path = base_path+'/sn_data/sn_knowledge_data/Ques_Dict.txt'

    # 【知识库标准问-答案】格式：{标准问：[pc端答案，微信端答案，app端答案]}
    Ques_Answer_path=base_path+ '/sn_data/sn_knowledge_data/Ques_Answer.txt'
    #【标准问题类别】标准问题{问题分类：[问题1，问题2，问题3]}
    Category_ques_path = base_path+'/sn_data/sn_knowledge_data/Category_ques.txt'

    ###########【算法模块数据】#########
    # 【0、Trie树】通用字典，直接使用Trie树匹配，完成简单相似度匹配 格式：{标准问：[标准答案,分类,ID]}
    Comques_Trie_path =base_path+ '/sn_data/sn_knowledge_data/Comques_Trie.txt'

    # 【1、转人工场景字典】格式：{标准问：[key,ID]}
    artifical_scene_dict_path = base_path+'/sn_data/sn_knowledge_data/artifical_scene_dict.txt'

    # 【4、问题纠错】问题纠错数据
    min_distance=3
    fre_dict_path =base_path+ '/sn_data/sn_function_data/sn_correct/fre_dict.txt'
    fre2_dict_path = base_path+'/sn_data/sn_function_data/sn_correct/fre2_dict.txt'
    fre3_dict_path = base_path+'/sn_data/sn_function_data/sn_correct/fre3_dict.txt'
    ott_dict_path =base_path+ '/sn_data/sn_function_data/sn_correct/ott_dict.txt'
    replace_dict_path =base_path+ '/sn_data/sn_function_data/sn_correct/replace_dict.txt'

    # 【6、问题分类】训练好的Glove词向量文件路径
    cate_topN=1
    glovevec_path = base_path+'/sn_data/sn_function_data/sn_cate/gloveVectors.txt'

    #【7、相似问模块】训练好的word2vec词向量文件路径
    simi_topN=4                                #相似问取前TOPN
    simi_threshold=0.5                          #相似性的阈值
    word2vec_path=base_path+'/sn_data/sn_function_data/sn_simi/word2vec_gensim'

    ###########【日志配置模块】#########
    robot_logging_conf_path=base_path+'/sn_config/robot_logging.conf'

    ######【闲聊、编辑距离控制长度】######
    Chatting_length=5
    EditDistance_length=40









