#!/bin/env python
#*coding=utf8*#
import time
import sys

print 'hello,world'

a = 'abc'
b = a
a = 'zxc'
print b

print u'中文'.encode('utf-8')

print len('abc')
print len(u'abc')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

print 'growth rate:%d %%' % 7

classmates = ['a','a','b']
print classmates
print len(classmates)
print classmates[-1]
classmates.append('c')
print classmates
classmates.insert(1,'b')
print classmates
classmates.pop()
print classmates
arr = ['a','b',['c','d']]
print arr
print len(arr)

arr1 = ['1','2','3']
arr2 = ['a','b','c']

t = ('z','x',arr1)
print t
arr1 = arr2
print t
print arr1
#t = ()
print t

if t:
    print 'true'
else:
    print 'false'

for item in t:
    print item


sum = 0
for item in range(101):
    sum = sum + item
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print sum

# birth = int(raw_input('birth:'))
# if birth < 2000:
#     print '00前'
# else:
#     print '00后'

d = {'Michael':95,'Bob':75,'Tracy':85}
print d['Bob']
d['Kevin'] = [1,2,3]
d.pop('Michael')
print d
print 'Bob' in d

s = set([1,2,3])

print type(time.localtime(time.time()))

abcb='1'
if abcb in locals().keys():
    print 'yes'
