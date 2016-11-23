# -*- coding: utf-8 -*-

import threading
import time
import random
import collections
import numpy as np



class sensor(object):
    def __init__(self,freq):
        #self.name=name
        self.freq=freq
       
    def monitorar(self,sType,queue):
        if(sType=="H"):
           #print "batimento:" , random.randint(70, 130), "bpm"
           sensor=["batimento:",random.randint(70, 130),"bpm","H"]
        elif(sType=="P"):
           #print "pressão arterial:" , random.uniform(10,16)
           sensor= ["pressao arterial:" , round(random.uniform(10,16),2),"muG","P"]
        else:
            #print "ondas cerebrais:" , random.randint(220, 250),"Hertz"
            sensor=["ondas cerebrais:" , random.randint(220, 250),"Hertz","C"]


        #print sensor    
        queue.append(sensor)
        #print "adicionou na fila:",sensor




#generic thread to simulate sensors
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,sensorType,freq,queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.freq=freq
        self.sensorType=sensorType
        self.queue=queue
    def run(self):
        print "Starting " + self.name
        mySensor=sensor(self.freq) 
        while(True):
            # Get lock to synchronize threads
            time.sleep(self.freq)
            threadLock.acquire()
            #print_time(self.name, self.counter, 3)
            mySensor.monitorar(self.sensorType,self.queue)
            # Free lock to release next thread
            threadLock.release()

# thread used to consume data from sensor threads
class consumer (threading.Thread):
    def __init__(self, threadID, name, counter,queue,qPressao,qBat,qOnda):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue=queue
        self.qPressao=qPressao
        self.qBat=qBat
        self.qOnda=qOnda
        
    def run(self):
        typeS=3
        value=1
        print "Starting " + self.name
        while(True):
            if (len(self.queue)>0):
                #time.sleep(0.3)
                threadLock.acquire()
                q=self.queue.popleft()
                threadLock.release() 
                #print "retirou da fila>> ",q
                if(q[typeS]=="H"):
                    self.qBat.append(q[value])
                elif(q[typeS]=="P"):
                    self.qPressao.append(q[value])
                elif(q[typeS]=="C"):
                    self.qOnda.append(q[value])
                
##            else:
##                time.sleep(0.3)



    #main thread
threadLock = threading.Lock()
threads = []


    #Start my queue[BUFFER]
global queue
queue=collections.deque()
qPressao=collections.deque([],100)
qBat=collections.deque([],100)
qOnda=collections.deque([],100)

            # Create new threads
thread1 = myThread(1, "Thread- sensor coração", 1,"H",0.2,queue)
thread2 = myThread(2, "Thread-sensor pressao", 2,"P",0.5,queue)
thread3 = myThread(3, "Thread-sensor onda cerebral", 3,"C",1,queue)
thread4 = consumer(3, "Thread-Consumidora", 3,queue,qPressao,qBat,qOnda)



    # Start new Threads
thread1.start()
#time.sleep(0.3)
thread2.start()
#time.sleep(0.3)
thread3.start()
#time.sleep(0.3)
thread4.start()
    # Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)


#strings para montar cabeçalho da sumarização dos dados

    # Wait for all threads to complete
#for t in threads:
   # t.join()
#print "Exiting Main Thread"

#def main():
        #mostrar dados
def mostrarDados(nmSensor,v,d,m,amostra):
    txvariancia=">>variancia:",v
    txdesvio=">>desvio padrao:",d
    txmedia=">> media:",m
    txAmostra=">>amostragem:",amostra
    sp=" ---------- "
    print time.ctime(),sp,nmSensor,sp,"\n",txvariancia, "\n",txdesvio ,"\n", txmedia,"\n", txAmostra,"\n", sp, sp, "\n \n"




while (True):
        time.sleep(5)
        
        #variancia
        lista=qBat
        v = round(np.var(lista),2)
        #desvio padrão
        d = round(np.sqrt(v),2)
        #media
        m = round(np.mean(lista),2)
        amostra=len(lista)
        #print "tamanho lista heart:",len(lista)
        #qBat.clear()
        mostrarDados("Sensor de batimento cardiaco",v,d,m,amostra)

        time.sleep(5)
        
        #variancia
        lista=qPressao
        v = round(np.var(lista),2)
        #desvio padrão
        d = round(np.sqrt(v),2)
        #media
        m = round(np.mean(lista),2)
        amostra=len(lista)
        #print "tamanho lista heart:",len(lista)
        qPressao.clear()
        mostrarDados("Sensor de pressão arterial",v,d,m,amostra)

        time.sleep(5)
        time.clock
        #variancia
        lista=qOnda
        v = round(np.var(lista),2)
        #desvio padrão
        d = round(np.sqrt(v),2)
        #media
        m = round(np.mean(lista),2)
        amostra=len(lista)
        #print "tamanho lista heart:",len(lista)
        qOnda.clear()
        mostrarDados("Sensor de ondas cerebrais",v,d,m,amostra)


    
