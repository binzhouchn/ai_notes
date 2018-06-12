# coding: utf-8
__author__ = 'BinZHOU'
__version__ = '20180518'

# import CRFPP

# 将一个问题中的网址、邮箱、手机号、身份证、日期、价格提出来

# 日期 注：这里的{1,4}指的是匹配1到4位，问号指的是0个或1个
DATE_REG1 = "(?:[一二三四五六七八九零十0-9]{1,4}年[一二三四五六七八九零十0-9]{1,2}月[一二三四五六七八九零十0-9]{1,2}[日|号|天|分]?)|\
(?:[一二三四五六七八九零十0-9]+年[一二三四五六七八九零十0-9]+月)|\
(?:[一二三四五六七八九零十0-9]{1,2}月[一二三四五六七八九零十0-9]{1,2}[号|日|天]?)|\
(?:[一二三四五六七八九零十0-9]+年)|\
(?:[一二三四五六七八九零十0-9]+月)|\
(?:[一二三四五六七八九零十0-9]{1,3}[号|日|天])|\
(?:[一二三四五六七八九零十0-9]+小时[一二三四五六七八九零十0-9]+分钟)|\
(?:[一二三四五六七八九零十0-9]+小时)|\
(?:[一二三四五六七八九零十0-9]+分钟)\
"

# 网址
URL_REG = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
# 手机
PHONE_REG = "[+](?:86)[-\s+]*?1[3-8][0-9]{9}"
# 邮箱
MAIL_REG = "[0-9a-zA-Z_]{0,39}@(?:[A-Za-z0-9]+\.)+[A-Za-z]+"
# 身份证
IDCARD_REG = "\d{18}|\d{17}[Xx]"

# 价格
MONEY_REG1 = "(?:\d+[\.\d+]*万*亿*美*港*元/桶)|\
(?:\d+[\.\d+]*万*亿*美*港*元/吨)|\
(?:\d+[\.\d+]*万*亿*美*港*元/升)|\
(?:\d+[\.\d+]*万*亿*美*港*元/吨)|\
(?:\d+[\.\d+]*万*亿*美*港*元/赛季)|\
(?:\d+[\.\d+]*万*亿*美*港*平方米)|\
(?:\d+[\.\d+]*万*亿*美*港*平方千米)|\
(?:(?:[\d]{1,3},)*(?:[\d]{3})[万亿]*[美港]*元)|\
(?:\d+[\.\d+]*万*亿*美*港*[股|笔|户|辆|倍|桶|吨|升|个|手|点|元|亿|万])"

MONEY_REG2 = "([一二三四五六七八九零十百千万亿|\d|.]+[万|元|块|毛][一二三四五六七八九零十百千万亿|\d|.]*)+"


## add date reg
DATE_REG2 = "(?:[\d]*[-:\.]*\d+[-:\.点]\d+分)|(?:[\d+-]*\d+月份)|(?:\d+[-:\.]\d+[-:\.]\d+)"
# HYPER_REG 2017-09-20
HYPER_REG = "[0-9a-zA-Z]+[-:][0-9a-zA-Z]+[%]*"

