import numpy as np
import pandas as pd
import py2neo
from py2neo import Graph,Node,Relationship
import neo4j
from neo4j.v1 import GraphDatabase, basic_auth
# py2neo操作
test_graph = Graph(
    #"http://localhost:7474",
    "bolt://localhost:7687"
    username="neo4j",
    password="z123456789"
)
# 创建节点
node1 = Node('Customer', name='John',age=18,phone=2232)
node2 = Node('Customer', name='Lily',age=22,phone=9921)
node3 = Node('Customer', name='Cathy',age=52,phone=7100)
test_graph.create(node1)
test_graph.create(node2)
test_graph.create(node3)
# 创建节点2
arr = np.array([['John','Lily','Ben','Mark'],['189101','234220','019018','330682'],[11,23,56,28]])
df = pd.DataFrame(arr.transpose(),columns=['name','phone_no','age'])
for i, j, k in df.values:
    node1 = Node('Person',name=i,phone_no=j,age=k)
    graph.create(node1)
# neo4j.v1操作
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "z123456789"))
session = driver.session()
# 创建节点3
arr = np.array([['John','Lily','Ben','Mark'],['189101','234220','019018','330682'],[11,23,56,28]])
df = pd.DataFrame(arr.transpose(),columns=['name','phone_no','age'])
#    name   phone_no    age
# 0  John   189101      11
# 1  Lily   234220      23
# 2  Ben    019018      56
# 3  Mark   330682      28
# dataframe to dict操作
dic = {'events':df.to_dict('records')}
session.run("unwind {events} as event merge (n:Person{name:event.name,phone_no2:event.phone_no,age: event.age})",dic)
# 删除所有节点和边
test_graph.delete_all()