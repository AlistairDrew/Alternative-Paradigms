#%%
def evaluate(code):
 cells = [0] # the memory space; 1 element; expands automaticall as required
 cellptr = 0 # pointer into the memory
 codeptr = 0 # pointer into the code provided as a string later
 stack = []
 while codeptr < len(code):

    command = code[codeptr]

 if command == ">":
    cellptr += 1
 if cellptr == len(cells): cells.append(0) # if memory too small, append a 0
 if command == "<":
    cellptr = 0 if cellptr <= 0 else cellptr - 1
 if command == "+":
    cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0
 if command == "-":
    cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

 # messing with Unicode to get the ' and . operators working
# if command == ".": sys.stdout.write(chr(cells[cellptr]))
# if command == ".": print( chr(cells[cellptr]))
# if command == ",": cells[cellptr] = ord(getch.getch())
 if command == ".": print(chr(cells[cellptr]), end='' ) # end='' overwrites '\n'
 if command == ",": cells[cellptr] = ord(input())

 if command == "[" and cells[cellptr] == 0: # skip or end the loop
    loop = 1
 while loop > 0: # there could be nested loops
    codeptr += 1 # which need to be skipped
    c = code[codeptr]
 if c == '[' :
    loop += 1
 elif c == ']' :
    loop -= 1 # if loop gets 0 we found the closing ]
 if command == "]": # and cells[cellptr] != 0: # end of loop but need to do more iterations
 # definitions of bf ] vary a bit
    loop = 1
 while loop > 0: # there could be nested loops
    codeptr -= 1 # which need to be skipped
 c = code[codeptr]
 if c == '[' :
    loop -= 1
 elif c == ']' :
    loop += 1 # if loop gets 0 we found the closing [
 codeptr -= 1 # one left becaus the main increments (as below)
 codeptr+=1
 return cells
# print "Hello World!"
s = """
 ++++++++++[>+++++++>++++++++++>+++>+<<<<-]
 >++.>+.+++++++..+++.>++.<<+++++++++++++++.
 >.+++.------.--------.>+.>.
"""
# s = """+++>++[<+>-]""" # add 3 to 2
# s = """,.""" # input, output
print(evaluate(s))
# %%
