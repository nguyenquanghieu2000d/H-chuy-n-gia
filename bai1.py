import numpy as np
import codecs
import sys
sys.stdin = codecs.getreader('utf_8')(sys.stdin)
from underthesea import word_tokenize
print('Phân tích từ tiếng Việt')
f=open('bai1.txt', 'rt',encoding='utf-8')
list_line = f.readlines()
f.close()
print(list_line)

mang_tu_VN=[]
print('Phân tích âm tiết tiếng Việt')
for i in range(len(list_line)):
    list_line[i]=list_line[i].replace('\n','')
    #list_w=list_line[i].split(' ')
    #print(list_w)
    list_w=word_tokenize(list_line[i])
    for j in range(len(list_w)):
       mang_tu_VN.append(list_w[j])
print('sau khi quét file mảng từ là:')
print(mang_tu_VN)