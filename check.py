#! /usr/bin/env python3

import os, sys

TEAMS_DIR = "."

alls = [x.strip() for x in open(os.path.join(TEAMS_DIR, "students.txt")).readlines()]
allocd = set()
err = False
for tl in os.listdir(TEAMS_DIR):
    if tl in [".git"]:
        continue
    if not os.path.isdir(tl):
        continue
    mems = [x.strip() for x in open(os.path.join(TEAMS_DIR, tl, "members.txt")).readlines()]
    for m in mems:
        if m == "":
            continue
        if m in allocd:
            print("Error: %s appears in multiple teams" % m)
            err = True
        if m not in alls:
            print("Error: %s not in student records" % m)
            err = True
        allocd.add(m)

if err:
    sys.exit(1)
