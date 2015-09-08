#Level 1 solution:
import string

alphabet_list = list(string.ascii_lowercase)
numericMap_list = list(range(1,27))
zipped_map = zip(alphabet_list,numericMap_list)
dict_mapping = dict(zipped_map)

zipped_map = zip(numericMap_list,alphabet_list)
reverseMap = dict(zipped_map)

def convertMessage(msg):
    retStr = ""
    msg.lower()
    for index in msg:
        if (index.isalpha()):
            retStr = retStr + reverseMap[((dict_mapping[index]+2)%26)]
        else:
            retStr = retStr + str(index)
    return retStr
            

msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \nbmgle gr gl zw fylb gq glcddgagclr "\
        "ylb rfyr'q ufw rfgq rcvr gq qm jmle. \nsqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
msg1 = "http://www.pythonchallenge.com/pc/def/map.html"
print convertMessage(msg1)
