mode = "bin"
source = open("hello_world.txt", "r")

instructions = {"lda #": 0x00, "lda @": 0x01, "sta @": 0x02, "add #": 0x03, "add @": 0x04, "sub #": 0x05, "sub @": 0x06, "xor #": 0x07, "xor @": 0x08, "and #": 0x09, "and @": 0x0a, "orr #": 0x0b, "orr @": 0x0c, "rol  ": 0x0d, "clf  ": 0x0e, "jmp @": 0x0f, "beq @": 0x10, "bcs @": 11, "nop  ": 0x12}

counter = 0
while True:
  line = source.readline()
  opcode = line[:5]

  if opcode != "res #" and opcode != "end  " and opcode[0] != ";":
    if mode == "hex":
      print(hex(instructions[opcode]))
    else:
      print(bin(instructions[opcode] & 0xFF)[2:].zfill(8))
    counter += 1
  elif opcode == "end  ":
    break

  if opcode[4] == "#" or opcode[4] == "@":
    if mode == "hex":
      print(hex(int((line[5] + line[6]), 16)))
    else:
      print(bin(int((line[5] + line[6]), 16) & 0xFF)[2:].zfill(8))
    counter += 1

print("your program took", counter, "bytes")
