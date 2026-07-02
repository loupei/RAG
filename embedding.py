# coding:utf-8
import pandas as pd
from FlagEmbedding import BGEM3FlagModel
import numpy as np
import ast
# 读txt中embedding，llm计算q，计算q-p相似度top n

list = []
with open("D:\RAG\shunbo.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        try:
            float_value = ast.literal_eval(line)
            # print(f"转换后的浮点数为: {float_value}")
        except (ValueError, SyntaxError):
            print("无法将字符串转换为浮点数")
        list.append(float_value)
        arr1 = np.array(list)
p_embeddings=arr1.reshape(481,1024)
# print(p_embeddings)35，7615
model = BGEM3FlagModel('BAAI/bge-m3',
                  use_fp16=True) # Setting use_fp16 to True speeds up computation with a slight performance degradation
queries = ["哪些药物不能和顺铂同时服用"]
q_embeddings = model.encode(queries)['dense_vecs']
# print(p_embeddings.type)numpy.ndarray
# print(q_embeddings)
scores = q_embeddings @ p_embeddings.T
print(scores)
n = 10
print(scores[0].argsort()[-n:][::-1])

