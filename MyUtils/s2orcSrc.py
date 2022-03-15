import json


# path_read = "../Data/s2orc/test.json"
# path_write = "../Data/s2orc_processed_01/test.src"
# # [*] num of passage is : 5000
# path_read = "../Data/s2orc/train.json"
# path_write = "../Data/s2orc_processed_01/train.src"
# # [*] num of passage is : 126655
path_read = "../Data/s2orc/valid.json"
path_write = "../Data/s2orc_processed_01/val.src"
# [*] num of passage is : 5000

f_read = open(path_read)
f_write = open(path_write, 'w', encoding="utf-8")

line = f_read.readline()
index = 0
while line:
    doc = json.loads(line)
    # dict_keys(['abs', 'multi_doc'])
    passage = ""
    for i in range(len(doc["multi_doc"])):
        if i != len(doc["multi_doc"])-1:
            section = doc["multi_doc"][i][4:] + " NEWLINE_CHAR  NEWLINE_CHAR "
            if section[:2] == ". ":
                section = section[2:]
        else:
            section = doc["multi_doc"][i][4:] + "\n"
            if section[:2] == ". ":
                section = section[2:]
        passage += section
    line = f_read.readline()
    if not line:
        passage = passage[:-1]
    f_write.write(passage)
    index += 1
print("[*] num of passage is :", index)

f_read.close()
f_write.close()