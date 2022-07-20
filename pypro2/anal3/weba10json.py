# JSON 문서읽기
import json

json_file="./제이슨.json"
json_data = {}



def readData(fname):
    f=open(fname,'r',encoding='utf-8')
    lines=f.read()
    f.close()
    return json.loads(lines)    # JSON decoding     str -> dict

def main():
    global json_data
    json_data=readData(json_file)
    print(json_data)
    print(type(json_data))
    d1=json_data['직원']['이름']
    d2=json_data['직원']['직급']
    d3=json_data['웹사이트']['사이트명']
    d4=json_data['웹사이트']['user']
    print(d1, d2, d3, d4)

if __name__ == "__main__":
    main()