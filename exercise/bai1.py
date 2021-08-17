"""
Đọc từng dòng bai1.txt và danh sách câu list_line.\n
3a.Tách các dòng thành các từ đơn, đôi và từ 3, mỗi từ thành danh sách list_w. Hiển thị list_w \n
3b.Xác định danh sách tất cả các từ xuất hiện trong file được biến list_tu. Hiển thị list_tu \n
3c. Xác định danh sách các từ không lặp lại được biến list_tu_khonglap. Hiển thị list_tu_khonglap.\n
3d. Xác định các từ xuất hiện trong file và số lần xuất hiện. Hiển thị kết quả.\n

Giải thích: ví dụ câu "Phú Xuân Phú Tân An Giang" được tách thành 3 tên riêng có nghĩa
"Phú Xuân"; "Phú Tân" và "An Giang"
"""

import codecs
import sys
from underthesea import word_tokenize
from collections import Counter

sys.stdin = codecs.getreader('utf_8')(sys.stdin)

f = open('../data/bai1.txt', 'rt', encoding='utf-8')
list_line = f.readlines()
f.close()


def tachThanhTu(listLineParams):
    mang_tu_VN = []
    # Quét từng dòng
    for i in range(len(listLineParams)):
        listLineParams[i] = listLineParams[i].replace('\n', '')
        # Tách thành từng từ
        list_w = word_tokenize(listLineParams[i])
        # add vào mảng kết quả
        for j in range(len(list_w)):
            mang_tu_VN.append(list_w[j])
    return mang_tu_VN


# Câu 1
list_w = tachThanhTu(list_line)
print("Đáp án câu 1: ", list_w)
# Câu 2
list_tu = list_w
print("Đáp án câu 2: ", list_tu)
# Câu 3
list_tu_khonglap = list(set(list_tu))
print("Đáp án câu 3: ", list_tu_khonglap)
# Câu 4
dict_counter = dict(Counter(list_tu))
print("Đáp án câu 4: ", dict_counter)
