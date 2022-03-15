import json


path_read = "../Data/delve/test.json"
path_write = "../Data/delve_processed_01/test.tgt"
# [*] num of passage is : 3000
# path_read = "../Data/delve/train.json"
# path_write = "../Data/delve_processed_01/train.tgt"
# # [*] num of passage is : 72927
# path_read = "../Data/delve/valid.json"
# path_write = "../Data/delve_processed_01/val.tgt"
# # [*] num of passage is : 3000

f_read = open(path_read)
f_write = open(path_write, 'w', encoding="utf-8")
line = f_read.readline()
index = 0
while line:
    doc = json.loads(line)
    # dict_keys(['multi_doc', 'abs'])
    abs = "– " + doc["abs"] + "\n"
    line = f_read.readline()
    f_write.write(abs)
    index += 1
print("[*] num of passage is :", index)
f_read.close()
f_write.close()