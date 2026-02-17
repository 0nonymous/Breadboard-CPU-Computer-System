mode = "hex"

instructions = {
 'lda $': 0x00,
 'lda @': 0x01,
 'lda #': 0x02,
 'lda &': 0x03,
 'ldx $': 0x04,
 'ldx @': 0x05,
 'ldx #': 0x06,
 'ldx &': 0x07,
 'inx  ': 0x08,
 'dex  ': 0x09,
 'txa  ': 0x0a,
 'tax  ': 0x0b,
 'add $': 0x0c,
 'add @': 0x0d,
 'add #': 0x0e,
 'add &': 0x0f,
 'sub $': 0x10,
 'sub @': 0x11,
 'sub #': 0x12,
 'sub &': 0x13,
 'adc $': 0x14,
 'adc @': 0x15,
 'adc #': 0x16,
 'adc &': 0x17,
 'sbc $': 0x18,
 'sbc @': 0x19,
 'sbc #': 0x1a,
 'sbc &': 0x1b,
 'and $': 0x1c,
 'and @': 0x1d,
 'and #': 0x1e,
 'and &': 0x1f,
 'orr $': 0x20,
 'orr @': 0x21,
 'orr #': 0x22,
 'orr &': 0x23,
 'shr  ': 0x24,
 'shl  ': 0x25,
 'ror  ': 0x26,
 'rol  ': 0x27,
 'sta @': 0x28,
 'sta #': 0x29,
 'sta &': 0x2a,
 'stx @': 0x2b,
 'stx #': 0x2c,
 'stx &': 0x2d,
 'pla  ': 0x2e,
 'pha  ': 0x2f,
 'plx  ': 0x30,
 'phx  ': 0x31,
 'plf  ': 0x32,
 'phf  ': 0x33,
 'pla &': 0x34,
 'plx &': 0x35,
 'jsr @': 0x36,
 'rsr  ': 0x37,
 'clf  ': 0x38,
 'msk  ': 0x39,
 'umk  ': 0x3a,
 'jmp @': 0x3b,
 'beq @': 0x3c,
 'bne @': 0x3d,
 'bmi @': 0x3e,
 'bpl @': 0x3f,
 'bcs @': 0x40,
 'bcc @': 0x41
}

print("assembler v1.0")
x = input("path: ")
source = open(x, "r")
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
