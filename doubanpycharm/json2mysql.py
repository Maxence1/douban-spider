#-*- coding: UTF-8 -*-
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


data = []
with open('data.json') as f:
    for line in f:

        data.append(json.loads(line))

#print json.dumps(data, ensure_ascii=False)

str = "\r\n"
for item in data:
    #print json.dumps(item)


    str = str + "insert into top250(title,star,movieInfo,quote) values "
    str = str + "('%s','%s','%s','%s');\r\n" % (item['title'],item['star'][0],item['movieInfo'],item['quote'])

import codecs
file_object = codecs.open('data.sql', 'w' ,"utf-8")
file_object.write(str)
file_object.close()
print "success"

