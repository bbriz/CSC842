#!/usr/bin/env python

import immlib
import getopt
import immutils
import struct
from immutils import *
imm = immlib.Debugger()

def mes():
    imm.log("No arguments are needed! ")
    imm.log("Try again without an arg.")
	
def main(args):
	if not args:
		
		#imm.updateLog()
		#Arrays of values
		regs = ["EAX","EBX","ECX","EDX","EBP","ESI","EDI"]
		dispatcherVal = ["4", "6", "8", "A", "C", "E", "10", "12", "14", "16", "18", "1A","1C", "1E", "20", "22", "24", "26", "28", "2A"]
		dispatcherVal2 = ["4", "8", "C", "10", "14", "18", "1C", "20", "24", "28", "2C", "30", "34"]
		dispatcherMov = ["ADD", "SUB", "ADC"] 
		dispatcherJmp = ["jmp dword ptr ss:[", "jmp dword ptr ds:["]
		dispatcher =[" "]
		dispatcher2 = ""
	
	  	for r in dispatcherMov:
			for r2 in regs:
				for r3 in dispatcherVal:
					for r4 in dispatcherJmp:
						for r5 in dispatcherVal2:
							dispatcher2 += r
							dispatcher2 += " "
							dispatcher2 += r2
							dispatcher2 += ", "
							dispatcher2 += r3
							dispatcher2 += "\n"
							dispatcher2 +=r4
							dispatcher2 +=r2
							dispatcher2 += "+"
							dispatcher2 += r5
							dispatcher2 += "]"
							imm.log("final  %s  " % dispatcher2)
							dispatcher.insert(0, dispatcher2)
							dispatcher2=""   
						
		for r in dispatcherMov:		
			for r2 in regs:
				for r3 in dispatcherVal:
					dispatcher2 += r
					dispatcher2 += " "
					dispatcher2 += r2
					dispatcher2 += ", "
					dispatcher2 += r3
					dispatcher2 +="\njmp "
					dispatcher2 +=r2
					imm.log("final3f  %s  " % dispatcher2)
					dispatcher.insert(0, dispatcher2)
					dispatcher2=""		
		
		dispatcher.insert(0, "inc eax\ninc eax")
		imm.log("test  %s  " % dispatcher)
		
		#i do my searches here
		
		for expr in dispatcher:
			searchFor=expr
			results=imm.search( imm.assemble (searchFor) )
			for result in results:
				imm.log("Found %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
	else:
		mes()
	return "FINSIHED!!!"