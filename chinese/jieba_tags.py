# coding=utf-8
import jieba.analyse

file_name = 'article.txt'
text = open(file_name, 'rb').read()

tags = jieba.analyse.extract_tags(text, 10)

for tag in tags:
    print tag

