# 去重算法

jaccard_prelu.py杰卡顿距离+prelu调数字权重的方法，simhash和random projection没有考虑到数字的影响

## simhash算法

补充..

## random_projection算法

shingling关注了文档顺序，但是忽略了文档单词出现的频率，random projection说我要讨论文档的频率。

Random Projection也是很有意思的一种算法，它是一种随机算法。简单描述为： <br>
1. 将每一个token映射到b位的空间。每一个维度是由{-1,1}组成。对所有页面投影函数是一样的<br> 
2. 每一个页面的b维度向量，是所有token的投影的简单加和 <br>
3. 最后把b维向量中的正数表示为1，负数和0都写成0 <br>
4. 比较两个page的b维向量一致的个数

Charikar最牛的地方是，证明，两个b位变量一致的位数的比率就是文档向量的consine相似性。这里的数学基础还是很有意思的，如果感兴趣，可以参考M.S. Charikar. Similarity Estimation Techniques for Rounding Algorithm(May 2002)<br>
[rp基础代码](random_projection_basic.py)

