with open('notes.txt', 'w') as f:
    f.write('some todo...')
    
    
f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()
    
# example of context managers
'''
open and close files
open and close daatabases connections
acuire and release locks:
'''

from threading import Lock
lock = Lock()

# error-prone:
lock.acquire()
# do stuff
# lock should always be released!
lock.release()

# better:
# with lock:
    #do stuff
    
'''
Implementing a context manager as a class:
To support the with statement for our own classes, we have to implement the __enter__ and __exit__ methods. Python calls __enter__ when execution enters the context of the with statement. In here the resource should be acquired and returned. When execution leaves the context again, __exit__ is called and the resource is freed up.
'''

class ManagedField:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
            print('exit')
            
with ManagedField('notes.txt') as f:
    print('doing stuff...')
    print('some todo...')
    
    
'''
Handeling Exception
If an exception occurs, Python passes the type, value, and traceback to the __exit__ method. It can handle the exception here. If anything other than True is returned by the __exit__ method, then the exception is raised by the with statement.
'''

# no exception
with ManagedField('notes.txt') as f:
    print('soing stuff...')
    f.write('some todo...')
print('cotinuing...')

print()


# exception is raised , but the file can still be closed

with ManagedField('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_somethion()
    
print('countinuing...')


with ManagedField('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()

print('continuing...')

'''
Implementing a context manager as a generator¶
Instead of writing a class, we can also write a generator function and decorate it with the contextlib.contextmanager decorator. Then we can also call the function using a with statement. For this approach, the function must yield the resource in a try statement, and all the content of the __exit__ method to free up the resource goes now inside the corresponding finally statement.
'''

from contextlib import contextmanager

@ contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo...')
    
    
'''
The generator first acquires the resource. It then temporarily suspends its own execution and yields the resource so it can be used by the caller. When the caller leaves the with context, the generator continues to execute and frees up the resource in the finally statement.
'''