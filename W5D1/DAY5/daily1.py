import urllib.request as urllib2
import requests
from time import time


def timePage():
    x = urllib2.urlopen('https://www.google.fr/')
    
    start_time = time()
    output =x.read()
    print (output)
    endtime = time()
    x.close()
    print(f'endtime:{endtime},start time :{start_time}')
    timeload = endtime - start_time
    print(f' The load time of the page is {timeload}')


timePage()