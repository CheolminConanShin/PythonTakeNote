import threading, time

# Thread 로 수행될 함수
# 이 함수에서 벗어나면 쓰레드로 종료된다.

def myThreadFunction(id):   # 쓰레드 함수
    for i in range(4):
        print ('id %s -> count : %s' % (id , i))
        time.sleep(0.5)

for i in range(5):
    # 5개의 Thread 를 독립적으로 생성
    threading._start_new_thread(myThreadFunction, (i,))                      # 쓰레드를 생성되는 부분 

time.sleep(3)
print ('Finish ')
