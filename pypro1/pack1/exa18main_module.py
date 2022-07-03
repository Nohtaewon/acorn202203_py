# 사용자 정의 모듈 작성 후 읽기
print('현재 모듈에서 뭔가를 하다가 다른 모듈 호출하기')
a=10
print('a:', a)
print(dir())
print()
import pack1.exa18mymod1

list1=[1,3]
list2=[2,4]
pack1.exa18mymod1.list_hap(list1, list2)

def abc():
    if __name__=='__main__':
        print('여기가 최상위 모듈이라고 외칩니다')

abc()

pack1.exa18mymod1.kbs()

from pack1 import exa18mymod1
exa18mymod1.kbs()

from pack1.exa18mymod1 import kbs, mbc, name
kbs()
mbc()
print(name)

print()
# 다른 패키지의 모듈 읽기
from pack_other import exa18mymod2
exa18mymod2.hap(1, 2)

import pack_other.exa18mymod2
pack_other.exa18mymod2.cha(5, 3)

print()
# path가 설정된 지역의 모듈 호출
import exa18mymod3
exa18mymod3.gop(5, 3)

from exa18mymod3 import nanugi
nanugi(5, 3)











