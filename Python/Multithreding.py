import threading

import time

def func(seconds):
    time.sleep(seconds)
    print(f"slept for {seconds} ")
    
    
    
    
func(3)
func(6)
func(3)


time1 
t1 = threding.Thread(target= func, args=[1])
t2 = threding.Thread(target= func, args=[2])
t3 = threding.Thread(target= func, args=[3])
t4 = threding.Thread(target= func, args=[4])
