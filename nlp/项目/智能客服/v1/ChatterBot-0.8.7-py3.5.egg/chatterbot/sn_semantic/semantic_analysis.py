#encoding:utf-8

__author__ = 'binzhou'
__version__ = '20180612'

import time
from sn_com.encoding import robot_encoding
from sn_com.string_filter import robot_string_filter
from sn_com.jieba_cut import robot_jieba_cut
from sn_com.word_correct import robot_word_correct
from sn_com.question_category import robot_question_category
from sn_com.search_trie import robot_search_trie
from sn_com.word2vec_wmddistance import robot_word2vec_wmddistance
from sn_com.artificial_scene import robot_artificial_scene
from sn_com.precise_search import robot_precise_search
from sn_com.word_editdistance import robot_word_editdistance_sort
from sn_com.robot_init import *

def sn_robotbest_match(question,source=0):
    """
        功能：########【语义引擎分析】进行闲聊，人工场景匹配，问题相似度匹配
        输入：问题、问题来源
        输出：相似问、相似置信度、ID、答案
    """
    try:
        # question = input("输入测试问题：")
        logger_robot.info('算法模块输入： {}'.format(question))
        time_start = time.time()
        question = robot_encoding.encoding(question)
        logger_robot.debug('标准化编码： {}'.format(question))
        question = robot_string_filter.string_filter(question)
        logger_robot.debug('字符纯化： {}'.format(question))
        if len(question) < robotdata.config.Chatting_length:  # 闲聊匹配判断
            simi_question = robot_search_trie.search_trie(question)
            # logger_robot.debug('闲聊判断： {}'.format(simi_question))
            # print("闲聊返回：",simi_question,type(simi_question))
            if simi_question['type'] == 0:  # 闲聊直接返回答案，否则转人工场景判断
                logger_robot.info('闲聊输出： {}'.format(simi_question))
                # print("闲聊：", simi_question)
                # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                logger_robot.info('闲聊输出耗时： {}'.format(time.time() - time_start))
                return simi_question
            else:
                simi_question = robot_precise_search.precise_search(question,source=source)
                # logger_robot.info('精确匹配输出： {}'.format(simi_question))
                if simi_question['type'] == 0:  # 闲聊直接返回答案，否则转人工场景判断
                    logger_robot.info('精确匹配输出： {}'.format(simi_question))
                    # print("闲聊：", simi_question)
                    # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                    logger_robot.info('精确匹配耗时： {}'.format(time.time() - time_start))
                    return simi_question
                else:
                    question = robot_word_correct.correct(question)
                    logger_robot.debug('问题纠错： {}'.format(question))
                    # print("纠错结果：",question)
                    question_cut = robot_jieba_cut.jieba_cut(question)
                    logger_robot.debug('问题分词： {}'.format(question_cut))
                    # print("question_cut", question_cut)
                    simi_question = robot_artificial_scene.search_artificial_scene(question_cut)  # 人工场景转换判断
                    # logger_robot.debug('人工场景判断： {}'.format(simi_question))
                    # print("人工场景返回1：",simi_question)
                    if len(simi_question) > 0:
                        logger_robot.info('人工场景输出： {}'.format(simi_question))
                        # print("人工场景1：", simi_question)
                        # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                        logger_robot.info('人工场景耗时： {}'.format(time.time() - time_start))
                        return simi_question
                    else:
                        cate = robot_question_category.question_category(question_cut)
                        logger_robot.debug('问题分类： {}'.format(cate))
                        simi_question = robot_word2vec_wmddistance.word2vec_wmddistance(text_list=question_cut,
                                                                                       cate=cate,source=source)
                        logger_robot.info('词向量相似问输出： {}'.format(simi_question))
                        # print("相似:1：", simi_question)
                        # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                        logger_robot.info('词向量相似问耗时： {}'.format(time.time() - time_start))
                        return simi_question
        else:
            simi_question = robot_precise_search.precise_search(question,source=source)
            # logger_robot.info('精确匹配输出： {}'.format(simi_question))
            if simi_question['type'] == 0:  # 闲聊直接返回答案，否则转人工场景判断
                logger_robot.info('精确匹配输出： {}'.format(simi_question))
                # print("闲聊：", simi_question)
                # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                logger_robot.info('精确匹配耗时： {}'.format(time.time() - time_start))
                return simi_question
            else:
                question = robot_word_correct.correct(question)
                logger_robot.debug('问题纠错： {}'.format(question))
                # print("纠错结果：",question)
                question_cut = robot_jieba_cut.jieba_cut(question)
                logger_robot.debug('问题分词： {}'.format(question_cut))
                # print("question_cut", question_cut)
                simi_question = robot_artificial_scene.search_artificial_scene(question_cut)  # 人工场景转换判断
                # logger_robot.debug('人工场景判断： {}'.format(simi_question))
                # print("人工场景返回2：", simi_question)
                if len(simi_question) > 0:
                    # print("人工场景2：", simi_question)
                    logger_robot.info('人工场景输出： {}'.format(simi_question))
                    # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                    logger_robot.info('人工场景耗时： {}'.format(time.time() - time_start))
                    return simi_question
                else:
                    cate = robot_question_category.question_category(question_cut)
                    logger_robot.debug('问题分类： {}'.format(cate))
                    if len(question) > robotdata.config.EditDistance_length:
                        simi_question = robot_word_editdistance_sort.word_editdistance_sort(text_list=question_cut,
                                                                                             cate=cate,source=source)
                        logger_robot.info('编辑距离相似问输出： {}'.format(simi_question))
                        # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                        logger_robot.info('编辑距离相似问耗时： {}'.format(time.time() - time_start))
                        # print("相似度2：", simi_question)
                        return simi_question
                    else:
                        simi_question = robot_word2vec_wmddistance.word2vec_wmddistance(text_list=question_cut,
                                                                                       cate=cate,source=source)
                        logger_robot.info('词向量相似问输出： {}'.format(simi_question))
                        # print("SemanticAnalysis_UseTime:", time.time() - time_start)
                        logger_robot.info('词向量相似问耗时： {}'.format(time.time() - time_start))
                        # print("相似度2：", simi_question)
                        return simi_question
    except Exception as e:
        logger_robot.exception(e)
        err={}
        err['err_code'] = e
        return err


if __name__=='__main__':
    pass

