mode = "hex"
source = open("helloworld2.txt", "r")

instructions = {"lda #": 0x00, "lda @": 0x01, "sta @": 0x02, "add #": 0x03, "add @": 0x04, "sub #": 0x05, "sub @": 0x06, "xor #": 0x07, "xor @": 0x08, "and #": 0x09, "and @": 0x0a, "orr #": 0x0b, "orr @": 0x0c, "rol  ": 0x0d, "clf  ": 0x0e, "jmp @": 0x0f, "beq @": 0x10, "bcs @": 0x11, "nop  ": 0x12}
define = {"PORTA": 25}
labels = {"label1": 3}

address = 0
memory = [0x12] * 256

while True:
  line = source.readline()
  print(line)
  if line[0] == ";" or line[0] == "\n":  # this means that this line can be ignored
      pass
      #print("skip")
  elif line[:2] != "  ":  # this means that the instruction is a label
      #print("label")
      if line[0:len(line)-2] not in labels:
          labels.update({line[0:len(line)-2] : address})
      #print(labels)
  else:
      if line[2] == ".":  # this means that this is a directive
          if line[3]+line[4]+line[5] == "org":  # origin
              #print("origin")
              address = int(line[9] + line[10], 16)
              #print(address)
          else:  # declare byte
              #print("byte")
              memory[address] = int(line[10] + line[11], 16)
              #print(memory[address])
              address += 1
      elif line[2]+line[3]+line[4] == "end":
          #print("done")
          break
      elif line[2]+line[3]+line[4]+line[5]+line[6] not in instructions:
          #print("define")
          #print(line[2:len(line)-7])
          #print(int(line[len(line)-3:len(line)-1], 16))
          if line[2:len(line)-7] not in define:
              define.update({line[2:len(line)-7] : int(line[len(line)-3:len(line)-1], 16)})
      else:
          # store opcode
          #print(line[2:7])
          #print(instructions[line[2:7]])
          memory[address] = instructions[line[2:7]]
          address += 1
          # operand store
          if line[6] == "@" or line[6] == "#":
              #print("more stuff to store")
              if line[7] == "$":  # hexadecimal value
                  #print(int(line[8]+line[9], 16))
                  memory[address] = int(line[8]+line[9], 16)
                  address += 1
                  #print(memory)
              else:  # label or define
                  if memory[address-1] >= 15 and memory[address-1] <= 17:
                      #print("jump, so use label")
                      memory[address] = labels[line[7:len(line)-1]]
                      address += 1
                      #print(memory)
                  else:
                      #print("use define")
                      memory[address] = define[line[7:len(line)-1]]
                      address += 1
                      #print(memory)
                  #print(line[7:len(line)-1])

address = 0
while address != 256:
    if mode == "bin":
        print(bin(memory[address]))
    else:
        print(hex(memory[address]))
    address += 1
print("done")         
