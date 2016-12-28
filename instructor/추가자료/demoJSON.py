#json문자열을 아래와 같이 만든다. 
jsonStr = '{"one":"1", "two":"2", "three":"3"}'
print(jsonStr)

#json데이터를 로딩해서 처리하기 
import json
j = json.loads('{"one":"1", "two":"2", "three":"3"}')
print(j['two'])

#url주소나 파일을 통해 받은 경우라면 아래와 같이 처리한다. 
import json
from pprint import pprint

#json_file='a.json' 
json_file='my_cube.json'
cube='1'

json_data=open(json_file)
data = json.load(json_data)
#pprint(data)
json_data.close()

print "Dimension: ", data['cubes'][cube]['dim']
print "Measures:  ", data['cubes'][cube]['meas']
