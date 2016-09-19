#!/usr/bin/env python

from os import path
import immlib
import getopt
import sys
import immutils
import struct


from immutils import *
imm = immlib.Debugger()

dispatcher =[" "]
term =""


def searchForDis():
	for expr in dispatcher:
			searchFor=expr
			term = searchFor
			results=imm.search( imm.assemble (searchFor) )
			for result in results:
				opC = imm.disasm(result)
				OpCStr = opC.getDisasm()
				opRegInQuestion = OpCStr[4:7]				
				#imm.log("Target Reg  %s    " % opRegInQuestion)
				
				newop=imm.disasm(result+1)
				newoppystring=newop.getDisasm()
				#imm.log("                %s    " % newoppystring)
				if str(newoppystring).find("JMP") > -1:
					if str(newoppystring).find(opRegInQuestion) > -1:
						
						
						imm.log("0 lines of filler:")   
						imm.log("Possible Dispatcher found for query %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
						imm.log("         JMP %s" % newoppystring, address = (result+1))
						imm.log("         Address: 0x%08x" %  (result+1), address = (result+1))
						imm.log("  ")
						
				#	imm.log(" val  %s    " % val1)
				newop=imm.disasm(result+2)
				newoppystring=newop.getDisasm()
				#imm.log("                %s    " % newoppystring)
				if str(newoppystring).find("JMP") > -1:
					if str(newoppystring).find(opRegInQuestion) > -1:
						#imm.log("      JMP          %s    " % newoppystring)
												#imm.log("Possible at at 0x%08x " % result)
						imm.log("1 line of filler:")   												
						imm.log("Possible Dispatcher found for query %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
						imm.log("Start:        %s" % searchFor, (result))
						newop=imm.disasm(result+1)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+1))
						imm.log("JMP:          %s" % newoppystring, address = (result+2))
						imm.log("         Address: 0x%08x" %  (result+2), address = (result+2))
						imm.log("  ")
						
				newop=imm.disasm(result+3)
				newoppystring=newop.getDisasm()
				#imm.log("                %s   " % newoppystring)
				if str(newoppystring).find("JMP") > -1:
					if str(newoppystring).find(opRegInQuestion) > -1:
						#imm.log("      JMP          %s    " % newoppystring)
					
						#imm.log("Possible at at 0x%08x " % result)   
						imm.log("2 lines of filler:") 
						imm.log("Possible Dispatcher found for query %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
						imm.log("Start:        %s" % searchFor, (result))
						newop=imm.disasm(result+1)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+1))
						newop=imm.disasm(result+2)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+2))
						imm.log("JMP:          %s" % newoppystring, address = (result+3))
						imm.log("         Address: 0x%08x" %  (result+3), address = (result+3))
						imm.log("  ")
				
				newop=imm.disasm(result+4)
				newoppystring=newop.getDisasm()
				#imm.log("                %s    " % newoppystring)
				if str(newoppystring).find("JMP") > -1:
					if str(newoppystring).find(opRegInQuestion) > -1:
						#imm.log("Possible at at 0x%08x " % result)   
						imm.log("3 lines of filler:") 
						imm.log("Possible Dispatcher found for query %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
						imm.log("Start:        %s" % searchFor, (result))
						newop=imm.disasm(result+1)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+1))
						newop=imm.disasm(result+2)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+2))
						newop=imm.disasm(result+3)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+3))
						imm.log("JMP:          %s" % newoppystring, address = (result+4))
						imm.log("         Address: 0x%08x" %  (result+3), address = (result+4))
						imm.log("  ")		
				newop=imm.disasm(result+5)
				newoppystring=newop.getDisasm()
				#imm.log("                %s   " % newoppystring)
				if str(newoppystring).find("JMP") > -1:
					if str(newoppystring).find(opRegInQuestion) > -1:
						#imm.log("Possible at at 0x%08x " % result)   
						imm.log("4 lines of filler:") 
						imm.log("Possible Dispatcher found for query %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
						imm.log("Start:        %s" % searchFor, (result))
						newop=imm.disasm(result+1)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+1))
						newop=imm.disasm(result+2)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+2))
						newop=imm.disasm(result+3)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+3))
						newop=imm.disasm(result+4)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+4))
						imm.log("JMP:          %s" % newoppystring, address = (result+5))
						imm.log("         Address: 0x%08x" %  (result+3), address = (result+5))
						imm.log("  ")	
				
				newop=imm.disasm(result+6)
				newoppystring=newop.getDisasm()
				#imm.log("                %s    " % newoppystring)
				if str(newoppystring).find("JMP") > -1:
					if str(newoppystring).find(opRegInQuestion) > -1:
						#imm.log("      JMP          %s    " % newoppystring)
						imm.log("5 lines of filler:") 
						imm.log("Possible Dispatcher found for query %s at 0x%08x " % (searchFor.replace('\n',' - '), result), address = result)
						imm.log("Start:        %s" % searchFor, (result))
						newop=imm.disasm(result+1)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+1))
						newop=imm.disasm(result+2)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+2))
						newop=imm.disasm(result+3)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+3))
						newop=imm.disasm(result+4)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+4))
						newop=imm.disasm(result+5)
						optempString=newop.getDisasm()
						imm.log("Other:        %s" % optempString, (result+5))
						imm.log("JMP:          %s" % newoppystring, address = (result+6))
						imm.log("         Address: 0x%08x" %  (result+3), address = (result+6))
						imm.log("  ")	
						

						
def wildcard(term):
		dispatcherVal = ["4", "6", "8", "A", "C", "E", "10", "12", "14", "16", "18", "1A","1C", "1E", "20", "22", "24", "26", "28", "2A", "2C", "2E", "30","32", "34","36", "38","3A", "3C","3E", "40","42", "44","46", "48"]	
		
	  	for r in dispatcherVal:
			termTemp = term
			termTemp += " "
			termTemp += r
			imm.log("add to dispatcher  %s  " % termTemp) 
			dispatcher.insert(0, termTemp)
			termTemp="" 	
			
def main(args):

	if not args:
		
		#imm.updateLog()
		#Arrays of values
		regs = ["EAX","EBX","ECX","EDX","EBP","ESI","EDI"]
		dispatcherVal = ["4", "6", "8", "A", "C", "E", "10", "12", "14", "16", "18", "1A","1C", "1E", "20", "22", "24", "26", "28", "2A", "2C", "2E", "30","32", "34","36", "38","3A", "3C","3E", "40","42", "44","46", "48"]
		dispatcherVal2 = ["4", "8", "C", "10", "14", "18", "1C", "20", "24", "28", "2C", "30", "34"]
		dispatcherMov = ["ADD", "SUB", "ADC"] 
		dispatcherJmp = ["jmp dword ptr ss:[", "jmp dword ptr ds:["]
		#dispatcher =[" "]
		dispatcher2 = ""
	
	  	for r in dispatcherMov:
			for r2 in regs:
				for r3 in dispatcherVal:
							dispatcher2 += r
							dispatcher2 += " "
							dispatcher2 += r2
							dispatcher2 += ", "
							dispatcher2 += r3
							dispatcher2 += "\n"
							imm.log("add to dispatcher  %s  " % dispatcher2) 
							dispatcher.insert(0, dispatcher2)
							dispatcher2="" 
		
		""" If you are getting no results and want to verify it works, just uncomment the next line, and you will seekm
		many results. You often do not get perfect JOP dispatcher gadgets.
		"""
		#dispatcher.insert(0, "inc eax")
		imm.log("Array  %s  " % dispatcher) 
		
		#i do my searches here
		searchForDis()
		
	else:
		if (args[0]=="-i"):
			if (args[1]=="help"):
				imm.log("")
				imm.log("HELP:    ")
				imm.log("Enter a line of instruction to begin your dispatcher gadget with.    ")
				imm.log("E.g., !dis2 -i add eax, 4 or !dis2 -i sub edx, 5")
				imm.log("You may add a * as a wild card--e.g. dis2 -i add eax, *")
				imm.log("It will search only for that particular instruction.")
				imm.log("")
			if not (args[1]=="help"):
				imm.log("")

			dispatcher2 = ""
			try:
				dispatcher2 += args[1]
			except IndexError:
				imm.log("")
			dispatcher2 += " "
			try:
				dispatcher2 += args[2]
			except IndexError:
				imm.log("")
			try:
				if args[3]=="*":
					term = dispatcher2
					imm.log("%s" % term)
					imm.log("Wild card")
					wildcard(term)
				else:
					dispatcher2 += args[3]
			except IndexError:
				imm.log("")
			dispatcher2 += "\n"
			if not (args[1]=="help"):
				imm.log("add to dispatcher  %s  " % dispatcher2) 
			dispatcher.insert(0, dispatcher2)
			searchForDis()
			
		if (args[0]=="-r"):
			if (args[1]=="help"):
				imm.log("")
				imm.log("HELP:    ")
				imm.log("Enter a register to search for!    ")
				imm.log("Example usage:    !dis2 -r eax    ")
				imm.log("")
			
			try:
				term = ""
				regs = []
				
				dispatcherVal = ["4", "6", "8", "A", "C", "E", "10", "12", "14", "16", "18", "1A","1C", "1E", "20", "22", "24", "26", "28", "2A", "2C", "2E", "30","32", "34","36", "38","3A", "3C","3E", "40","42", "44","46", "48"]
				dispatcherMov = ["ADD", "SUB", "ADC"] 
				dispatcher2 = ""
				if not (args[1]=="help"):
					imm.log("")
					term = args[1]
					regs.insert(0, term)
					for r in dispatcherMov:
						for r2 in regs:
							for r3 in dispatcherVal:
								dispatcher2 += r
								dispatcher2 += " "
								dispatcher2 += r2
								dispatcher2 += ", "
								dispatcher2 += r3
								dispatcher2 += "\n"
								imm.log("add to dispatcher  %s  " % dispatcher2) 
								dispatcher.insert(0, dispatcher2)
								dispatcher2="" 
					searchForDis()
			except IndexError:
				imm.log("Oh no!")
		
		
			
	
			
			
	return "FINSIHED!!!"
	
	"""
	I learned how to program with Immunity via https://www.corelan.be/index.php/2010/01/26/starting-to-write-immunity-debugger-pycommands-my-cheatsheet/
	I also checked out sample codes from Grey Hat Python (book), the source repository of which is online. 
	I have little previous experience with Python and took a while to learn the mechanics of how to do things.
	
	
	
	"""