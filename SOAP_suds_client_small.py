#!/usr/bin/env python

'''
Created on Oct 5, 2015

@author: chazarey
'''

from suds.client import Client

def main():

    print 'In main now...'
    
    client = Client('http://ladonize.org/python-demos/Calculator/soap/description')

    print client
    
    result = client.service.add(34,56)
    
    print result
    
if __name__ == '__main__':
    
    print 'Going to call main now...'
    
    main()
    
