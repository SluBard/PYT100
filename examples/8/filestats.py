#!/usr/bin/env python3
import sys, os, time
tag = ["\tmode", "\tinode#", "\tdevice#",
       "\t#links", "\tuser", "\tgroup", "\tbytes",
       "\tlast access", "\tlast modified",
       "\tchange/creation time"]

def printstats01(file, stat):
    print("File Stats for:", file)
    print(tag[0], ":", oct(stat.st_mode))
    print(tag[1], ":", stat.st_ino)
    print(tag[2], ":", stat.st_dev)
    print(tag[3], ":", stat.st_nlink)
    print(tag[4], ":", stat.st_uid)
    print(tag[5], ":", stat.st_gid)
    print(tag[6], ":", stat.st_size)
    print(tag[7], ":", time.ctime(stat.st_atime))
    print(tag[8], ":", time.ctime(stat.st_mtime))
    print(tag[9], ":", time.ctime(stat.st_ctime))
    print("\n")


def printstats02(file, stats):
    print("File Stats for:", file)
    for i, a_stat in enumerate(stats):
        print(tag[i], ":", a_stat)
    print("\n")


for file in sys.argv[1:]:
    info = os.stat(file)
    if os.path.isfile(file):
        print("*" * 30)
        printstats01(file, info)
        printstats02(file, info)
