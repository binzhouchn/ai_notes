# word2vec详细笔记

## 1. Word2Vec

word2vec也叫word embeddings，中文名“词向量”<br>
word2vec本质上来说就是一个矩阵分解的模型，简单地说，矩阵刻画了每个词和其上下文的词的集合的相关情况。对这个矩阵进行分解，只取每个词对应在隐含空间的向量。<br>
https://blog.csdn.net/mylove0414/article/details/61616617

 -  skip-gram
 - cbow 连续词袋

对于CBOW和Skip-Gram两个模型，word2vec给出了两套框架，用Hierarchical Softmax和negative sampling来进行优化（使用的数据结构是霍夫曼树

参考网址：http://blog.csdn.net/a819825294/article/details/52438625<br>
参考网址2：http://www.cnblogs.com/pinard/p/7243513.html<br>

## 2. GolVe 

## 3. FastText