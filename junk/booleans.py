#!/usr/bin/python
#coding:utf-8
import re

fp = open("currenttext", "r")

sentences = []

for line in fp.readlines():
	line = line.strip()
	if line == "": continue
	if line[0] in ["*", "="]: continue

	sen = [x.strip().lower() for x in line.split(". ")]
	sentences += sen

operands = [" skulu ", " skal ", " má ", " mega ", " á að ", " er ", " óskað ", " óska ", " skipar ", " getur "]
booleans = [" og ", " eða ", " en "]


def printtree(atoms, step):
	for i in atoms:
		if type(i) is list:
			printtree(i, step+1)
		elif type(i) is str:
			for m in range(step):
				print "    ",
			print " |--- '%s'" % i.strip()
		else:
			print type(i)



for a in sentences:

	print "*** '%s'" % a
	
	atoms = re.split("(%s)" % "|".join(operands), a)
	for i in range(len(atoms)):
		atoms[i] = re.split("(%s)" % "|".join(booleans), atoms[i])

	printtree(atoms, 0)
