import threading
import time

g_count = 0

def threadCount(id, count):
    global g_count             # g_count 를 전역 변수로 참조
    for i in range(count):
        print ('id %s ====> count : %s, g_count : %s' % (id, i, g_count))
        threading.Lock.acquire()
        g_count = g_count + 1
        threading.Lock.release()
for i in range(5):
    threading._start_new_thread(threadCount, (i,5))         # 쓰레드 생성 

time.sleep(3)
print ('Final g_counter = ', g_count)
print ('Finish Thread TEST Process')
