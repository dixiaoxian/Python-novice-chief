import threading

class myThread(threading.Thread):
    def __init__(self,ID,name,counter):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始执行:"+self.name)

        print("退出任务:"+self.name)

def print_time(threadName,delay,counter):
    while counter:
        print()