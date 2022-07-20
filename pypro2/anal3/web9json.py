# JSON data <-> dict type 호환
import json

dict={'name':'tom','age':33,'score':['90','80','100']} # python의 dict
print('dict:%s'%dict)
print('dict type:%s'%type(dict))

print('---JSON encoding : dict,list,tuple 등을 JSON 모양의 문자열로 변경')
str_val=json.dumps(dict)
print('str_val:%s'%str_val)
print('str_val type:%s'%type(str_val))
print(str_val[0:20])    # 문자열 관련 슬라이싱 가능
# print(str_val['name'])  # dict 명령 X

print('---JSON decoding : JSON 모양의 문자열을 dict로 변경')
json_val=json.loads(str_val)
print('json_val:%s'%json_val)
print('json_val type:%s'%type(json_val))
# print(json_val[0:20])   # TypeError: unhashable type: 'slice'
print(json_val['name']) # dict 명령 o

print()
for k in json_val.keys():
    print(k)
    
print()
for k in json_val.keys():
    print(k)











