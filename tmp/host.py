#!/bin/env python36
# host.py


class Host():
  def __init__(self, hostname, *alias, **info):
    self.hostname = hostname
    self.alias = alias
    self.info = info
    for i in self.info.keys():
      setattr(self, i, self.info[i])
    



if __name__ == '__main__':
  h1 = Host('10.1.1.222','test-222', '1.222',hd='120GB',ipaddr='10.1.1.222')
  print(h1.ipaddr)
