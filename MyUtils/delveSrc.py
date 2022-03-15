import json


# path_read = "../Data/delve/test.json"
# path_write = "../Data/delve_processed_01/test.src"
# # [*] num of passage is : 3000
# path_read = "../Data/delve/train.json"
# path_write = "../Data/delve_processed_01/train.src"
# # [*] num of passage is : 72927
path_read = "../Data/delve/valid.json"
path_write = "../Data/delve_processed_01/val.src"
# [*] num of passage is : 3000

f_read = open(path_read)
f_write = open(path_write, 'w', encoding="utf-8")

line = f_read.readline()
index = 0
while line:
    doc = json.loads(line)
    # dict_keys(['multi_doc', 'abs'])
    passage = ""
    for i in range(len(doc["multi_doc"])):
        if i != len(doc["multi_doc"])-1:
            section = doc["multi_doc"][i][4:] + " NEWLINE_CHAR  NEWLINE_CHAR "
        else:
            section = doc["multi_doc"][i][4:] + "\n"
        passage += section
    line = f_read.readline()
    if not line:
        passage = passage[:-1]
    f_write.write(passage)
    index += 1
print("[*] num of passage is :", index)

f_read.close()
f_write.close()