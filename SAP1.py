"""
	SAP-1 computer

	This is a simulator for the simple as possible computer
	described in Digital Computer Electronics.
	
	Registers: 
	A - Accumulator  - 2 decimal digits 

	Instruction set:
	NOP 
	LDA addr - load the contents(1 byte) at addr to the accumulator
	ADD addr - add contents of addr with contents of accumulator
	SUB addr - subtract contents of addr with contents of accumulator
	OUT addr - move contents of accumulator to the output register
	HLT	     - stop execution

"""
import sys 

ram_size = 32
ram = []
A = 0

def init_ram():
	for i in range(ram_size):
		ram.append(0)

def load_hex_program(progfile):
	with open(progfile, "r") as f:
		code = f.readlines()
	if len(code) >= ram_size:
		print "Program too large"
		exit()
	for i in range(0,len(code)):
		ram[i] = int(code[i])
	print ram

def run():
	for i in range(len(ram)):
		instr = ram[i]
		opcode = (instr/100)%10
		addr = instr%100
		execute(opcode,addr)

def execute(opcode, addr):
	global A
	if opcode == 0:
		print "NOP"
		pass
	elif opcode == 1:
		print "LDA",addr
		A = ram[addr]
	elif opcode == 2:
		print "ADD",addr
		A = A + ram[addr]
	elif opcode == 3:
		print "SUB",addr
		A = A - ram[addr]
	elif opcode == 4:
		print "OUT",A 
	elif opcode == 5:
		print "HLT"
		sys.exit(0)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "No file given to execute"
		sys.exit(-1)
	init_ram()
	load_hex_program(sys.argv[1])
	run()
