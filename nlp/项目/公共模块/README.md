## 1.jieba源码改写
jieba.add_word加入比如3423423@qq.com还是分不出来<br>
解决方案：源码里面把__init.py文件中的re_han_default和posseg中的re_han_internal增加一些要用到比如@

jieba \__init__.py
```python
re_han_default = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#@$\+{\s+}:=?\/\-&\._%]+)", re.U)
```
posseg \__init__.py
```python
re_han_internal = re.compile("([\u4E00-\u9FD5a-zA-Z0-9+#@$\+{\s+}:=?\/\-&\._%]+)")
```

## 2. 【正则轮子】将一个问题中的网址、邮箱、手机号、身份证、日期、价格提出来

[bz_re.py](bz_re.py)
