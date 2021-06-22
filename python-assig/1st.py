#WAP to input number of seconds and print it in form HH:MM:SS. Like for 4000 seconds it will be 01:06:40.  
import time
  
def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(n))
      
# Driver program
n = 4000
print(convert(n))
