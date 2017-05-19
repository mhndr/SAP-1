"""
	This is a Simple as Possible Assembler
	to go with the Simple as possible Computer
	The idea is to grow both of them together
	by adding new instructions together

	Syntax:
		<Label> <DATA> instruction/literal
		instruction : opcode+addr
	Eg:
		A DATA 444
		B DATA 555
			LDA A
			ADD B
			OUT
			LDA A
			SUB 34 
			HLT

	Breakdown of the two passes
		 1. run through the code and count the number of instuction
			this count becomes the offset for all the symbol addresses.
			which means that all the literals that the symbols point to
			are kept at addresses after this count.
			In this pass we can also populate the symbol table and addr-
			-ess table
				Eg:
				addr = count + instr_count + 1
				symbol_table["A"] = addr
				address_table[addr] = symbol_val
				sym_count++
		2. decode instruction
			first the opcode 
				op = opcode_table[field[0]]
			then the symbol/literal
				if digit(field[1])
					addr = field[1]
				else
					addr = symbol_table[field[1]]	  						
			join
				instr = op*100 + addr

			after all instructions are done, dump the address_table contents at the end


"""
import sys


opcode_table = {"NOP":'0',
				"LDA":'1',
				"ADD":'2',
				"SUB":'3',
				"OUT":'4',
				"HLT":'5'}
symbol_table = {} # symbol:address
address_table ={} # address:value
instruction_count = 0
symbol_count = 0

with open("code.sap","r") as f:
	lines= f.readlines()
for i,line in enumerate(lines):
	if "DATA" in line:
		fields = line.split()
		if len(fields) != 3:
			print "Error, Unrecognised Data definition, Line:",i
	else:
		if line.strip():
			instruction_count += 1
	

for i,line in enumerate(lines):
	if "DATA" in line:
		fields = line.split()
		if len(fields) == 3:
			addr = symbol_count + instruction_count 
			symbol = fields[0]
			val    = fields[2]
			symbol_table[symbol] = addr
			address_table[addr] = val
			symbol_count += 1
		else:
			print "Error, Unrecognised Data definition, Line:",i
	else:
		if line.strip():
			field = line.split()
			addr = 0
			if len(field)==2:
				addr   = symbol_table[field[1]]	
			if addr < 10:
				addr = '0' + str(addr)
			opcode = opcode_table[field[0]]
			print opcode+addr

for addr in address_table:
	print address_table[addr]

