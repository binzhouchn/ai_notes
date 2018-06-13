思维脑图扩充中..

# nlp笔记

1. N-Gram:简单的马尔科夫链

bigram:一个词的出现仅依赖于它前面出现的一个词
P(w1,w2...wm) = 连乘P(wi|wi-1)
假设有一个很大的语料库，我们统计下面一些词出现的量，其中I出现了2533次，再给出基于bigram模型进行计数的结果，其中第一行，第二列表示给定前一个词是"I"时，当前词为"want"的情况一共出现了827次，所以P(want|I)=827/2533=0.33

ngram的应用：搜索，输入法联想，文本自动生成

http://blog.csdn.net/baimafujinji/article/details/51281816

2. TF-IDF

根据词频来确定词的重要性不是很科学，比如你，她，好的等这种词频在每篇文章中肯定较高，通过tf-idf算法,idf相当于对词频进行了一个权重调整，过滤掉常见的词语，保留重要的词语。

http://blog.csdn.net/sangyongjia/article/details/52440063

3. MI 互信息


4. word2vec， gensim（蚂蚁笔记），
对于CBOW和Skip-Gram两个模型，word2vec给出了两套框架，用Hierarchical Softmax和negative sampling来进行优化（使用的数据结构是霍夫曼树）

参考网址：http://blog.csdn.net/a819825294/article/details/52438625
参考网址2：http://www.cnblogs.com/pinard/p/7243513.html

# nlp开源工具

1. jieba，分词实现可以自己写代码（项目->公共模块->WordSegment）

参考网址：http://blog.csdn.net/john_xyz/article/details/54645527

2. crf++工具(可用于分词，词性标注和实体识别等)

[实体识别训练](https://nbviewer.jupyter.org/github/binzhouchn/ai_notes/blob/master/nlp/%E9%A1%B9%E7%9B%AE/%E5%85%AC%E5%85%B1%E6%A8%A1%E5%9D%97/NER/%E5%AE%9E%E4%BD%93%E8%AF%86%E5%88%AB%E8%AE%AD%E7%BB%83%E8%BF%87%E7%A8%8B_V2.ipynb)

(项目->公共模块->NER）

3. xx
