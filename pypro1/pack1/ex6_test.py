print('1~100사이 정수 중 3의 배수이나 2의 배수가 아닌 수와 합')
i=1;hap=0
while i<100:
    if i%3==0 and i%2!=0:
        print(i, end=',')
        hap+=i
    i+=1
print('합은'+str(hap))
print('-----------------')
print('2~5 까지의 구구단 출력')
i=2
while i<=5:
    j=1
    while j<=9:
        print(str(i)+'*'+str(j)+'='+str(i*j), end=' ')
        j=j+1
    print()
    i+=1
print('--------------')
i=1
cnt=1
tot=0
while i<100:
    if cnt%2==0:    # 짝수 지점
        #print(i)
        tot+=i
    else:
        k= i*-1    # 홀수 지점
        #print(k)
        tot+=k
    cnt+=1
    i += 2
print('합:', tot)
print('-------------')
num=2;
count=0
while num<=1000:
    i=2
    while num%i:
        i+=1
    if i==num:
        count+=1
    num+=1
        
print(count)
