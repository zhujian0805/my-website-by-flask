#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='mysql://root:123456@localhost:3306/test', debug='False', repository='db_repository')
