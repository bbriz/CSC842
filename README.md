#JOP dispatcher 

This program is intended to discover potential JOP dispatcher gadgets that could be 
utilized for Jump-oriented Programming for purposes of binary exploitation. JOP is 
similar to Return-oriented Programming (ROP) and works on similar ideas, but very different.

#JOP background
In JOP, one establishes a dispatcher gadget, that adds, subtracts, or dereferences in a
predictable way, such as the following:
add ebx, 0x10 
jmp dword ptr[ebx]. 
In this example, we have a value of 10 which is then added to the
program counter, which could be on the stack or in memory, and then goes to the
dispatcher table, which contains addresses of functional gadgets as well as necessary
padding. Each functional gadget terminates in a jmp to a reg, which links back to the
dispatcher gadget. Thus, all functional gadgets, must terminate in same jmp to [reg]. 
So unlike with ROP, where everything is connected and seemingly glued together by a ret,
we instead have everything connected to via a jmp to [reg]. So the dispatcher gadget
links to a dispatch table, which then links to the gadget catalog, which contains the 
functional gadgets. The purpose of the gadget dispatch table is that it might be necessary
to have data padding if you have an ugly value that is adding, subtracting, or dereferencing.
There are not a lot of valid JOP dispatcher gadgets, so you have to sometimes make do with
what is available. Please refer to image here to see this idea demonstrated visually:
 http://2.bp.blogspot.com/-yUFFwdM6oO0/Tuiw4OjNixI/AAAAAAAAK3E/tSw-A5H-O9o/s1600/Screen+Shot+2011-12-14+at+3.20.51+PM.png

There are many, many different possibilities for valid JOP dispatcher gadgets. What I 
intended to do was use Python and write a Python command for Immunity Debugger. This would 
reveal a large number of possible JOP dispatcher gadgets. Any of these dispatcher gadgets 
would work perfectly, although it should be pointed out that not everything else necessary
to get a JOP functional could be present in the binary. 

#Problems with JOP dispatcher gadgets
In actual practice, having additional lines of Assembly between the first and terminal part of 
the dispatcher gadget is acceptable. The problem with this is that it can induce side effects, 
which could make some registers unavailable for other purposes, or the side effects could 
even be desetructive to values that we wish to protect. In actual practice, finding "perfect"
dispatcher gadgets for JOP such as what this program is not commonplace. In my experience 
you can find *potential* dispatcher gadgets that may have other lines in between the first and
terminal lines. It is up to the attacker to determine if the dispatcher is still viable.

One shortcoming of this code is that it does not include "wild cards" between the first and
second lines for the dispatcher. I would love to be able to include this feature as it could 
give a lot more potential dispatcher gadgets. As it is, the program will only find the ideal
or perfect dispatcher gadgets, which are not common in binaries. I know how to implement wild
cards in Python, but as far as getting it to work with the searchFor and actually work for this
purpose, I am at a loss.

#How the program works
The program creates a large array of different values to search for in the binary. If it is
successful, it returns the starting location for the dispatcher. Because there are a substantial 
number of viable dispatchers to search for and there could be a lot of memory to search, this 
search could take a good while. Please be patient! The executable itself as well as any modules
or libraries are loaded into memory, and the memory for that process must be searched for those
sequences of Assembly.

#How to use this program
To use this code, you must have Immunity Debugger. Simply open any executable or attach to a 
currently running binary. If there are any problems, pick another. Avoid massive executables
or ones that link to tons of binaries, as it will take up a lot more time to search.

In the command line of Immunity Debugger towards the bottom of the screen, enter the command
!JOP-Dispatcher
It will run and say finished at the bottom. Hit Alt-L to view the log or go to View and select Log 
to view results. 

The program may seem to freeze. It is just taking a long time, and it will give
the results when it is done. It has a lot of memory to search for a substantial number of items.

You can add an unrelated search, that searches for Inc eax / Inc eax -- a very common sequence,
by uncommenting line 64. This just shows that it "works." There is a good chance the search
will not find any valid JOP dispatcher gadgets. This is expected, in the absence of wild card
lines between the first and terminal lines of the dispatcher gadget.

If results are found, they are displayed with the hexadecimal memory address in the log.







