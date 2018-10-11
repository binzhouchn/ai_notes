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

## 5. word2vec

 - CBOW模型
 - Skip-gram模型
 - Hierarchical Softmax 与 Negative Sampling
 - FastText
 - GolVe

GloVe 与 Word2Vec 的区别:
 - Word2Vec 本质上是一个神经网络；Glove 也利用了反向传播来更新词向量，但是结构要更简单，所以 GloVe 的速度更快
 - Glove 认为 Word2Vec 对高频词的处理还不够，导致速度慢；GloVe 认为共现矩阵可以解决这个问题
 - 从效果上看，虽然 GloVe 的训练速度更快，但是词向量的性能在通用性上要弱一些：

FastText 是从 Word2Vec 的 CBOW 模型演化而来的，不同点：
 - CBOW 的输入是中心词两侧skip_window内的上下文词；FastText 除了上下文词外，还包括这些词的字符级 N-gram 特征
 

[word2vec详细笔记](公共模块/word2vec.md)

# nlp开源工具

## 1. jieba，分词实现可以自己写代码（公共模块->WordSegment）

参考网址：http://blog.csdn.net/john_xyz/article/details/54645527

## 2. crf++工具(可用于分词，词性标注和实体识别等)

[实体识别训练](https://nbviewer.jupyter.org/github/binzhouchn/ai_notes/blob/master/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86/%E5%85%AC%E5%85%B1%E6%A8%A1%E5%9D%97/NER/%E5%AE%9E%E4%BD%93%E8%AF%86%E5%88%AB%E8%AE%AD%E7%BB%83%E8%BF%87%E7%A8%8B_V2.ipynb)

(公共模块->NER）

## 3. xx
