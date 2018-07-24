nlp自我学习180515.xmind 思维脑图扩充中..

# nlp笔记

## 1. 文本相似度衡量距离
 - 余弦相似性（cosine similarity） 
 - 编辑距离（edit distance） 
 - WMD距离（word mover’s distance） 
 - 杰卡顿距离（Jaccard distance） 
 - Dice 距离（Dice distance）

[文本相似度详细笔记](公共模块/sim_text.md)

## 2. N-Gram:简单的马尔科夫链

bigram:一个词的出现仅依赖于它前面出现的一个词
P(w1,w2...wm) = 连乘P(wi|wi-1)
假设有一个很大的语料库，我们统计下面一些词出现的量，其中I出现了2533次，再给出基于bigram模型进行计数的结果，其中第一行，第二列表示给定前一个词是"I"时，当前词为"want"的情况一共出现了827次，所以P(want|I)=827/2533=0.33

ngram的应用：搜索，输入法联想，文本自动生成

http://blog.csdn.net/baimafujinji/article/details/51281816

## 3. 关键词提取主要算法

 - tfidf
 - topic-model(LDA)
 - textrank关键词提取

[关键词提取详细笔记](公共模块/keyword_extraction.md)

## 4. 信息熵

## 5. Word Vectors

 - Word2Vec
 - GolVe
 - FastText

[Word Vectors详细笔记](公共模块/wv.md)

# nlp开源工具

## 1. jieba，分词实现可以自己写代码（公共模块->WordSegment）

参考网址：http://blog.csdn.net/john_xyz/article/details/54645527

## 2. crf++工具(可用于分词，词性标注和实体识别等)

[实体识别训练](https://nbviewer.jupyter.org/github/binzhouchn/ai_notes/blob/master/nlp/%E9%A1%B9%E7%9B%AE/%E5%85%AC%E5%85%B1%E6%A8%A1%E5%9D%97/NER/%E5%AE%9E%E4%BD%93%E8%AF%86%E5%88%AB%E8%AE%AD%E7%BB%83%E8%BF%87%E7%A8%8B_V2.ipynb)

(公共模块->NER）

## 3. xx
