#!/usr/local/bin/python3
import os
import subprocess 
import sys
class xdb:
	def __init__(self,xdb="gdb",program=""):
		self.p = subprocess.Popen(xdb+" "+program, stdin = subprocess.PIPE,  stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True) 
		#p.stdin.write(bytes('1',"utf-8"))
		self.pin=self.p.stdin
		self.pout=self.p.stdout
		self.db=xdb
		print(self.readUntilnext(),end="")
	def readUntil(self,str0):#read untile str 
		tempstr=""
		while str0!=tempstr[-len(str0)-1:-1]:
			tempstr+= str( self.pout.read(1),encoding = "utf-8")  
		return tempstr
	def readUntilnext(self):
		return self.readUntil("("+self.db+")")
	def query(self,str0):
		self.pin.write(bytes(str0+'\n',"utf-8"))
		self.pin.flush()
		return gdb.readUntilnext()
	def db_run(self):
		return self.query("run")
	def db_continue(self):
		return self.query("continue")
	def db_break(self,no_line):
		return self.query("break"+" "+str(no_line))
gdb=xdb(program="test",xdb="lldb")
print(gdb.db_break(7),end="")
print(gdb.db_run(),end="")
