#!/usr/bin/env python
import os
import sys
import time
from astron.object_repository import ClientRepository

if __name__ == '__main__':
    repo = ClientRepository('SimpleExample v0.2', 'simple_example.dc')

    def connected():
        print('Connection established.')

    def ejected(error_code, reason):
        print('Got ejected (%i): %s' % (error_code, reason))

    def failed():
        print('Connection attempt failed.')

    repo.connect(connected, failed, ejected)
    repo.poll_forever()

## Lets do some random things
#print mod.get_num_classes() # or GetNumClasses
#cls = mod.get_class_by_name('Foobar')  # or getClassByName
#print cls.get_name() # -> 'Foobar'
