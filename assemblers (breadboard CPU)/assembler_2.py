# this is the current instruction set for the cpu
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
 'xla  ': 0x34,
 'xlx  ': 0x35,
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

# parameters
path = "lcd.txt"
source = open(path, 'r')
min_address = 0  # when programming for rom
max_address = 2048
write_index = 0

# dictionaries
definitions = {}
labels = {}

machine_code = []
for x in range(0, 2048):
  machine_code.append(hex(0))

while True:
  # get instruction
  line = source.readline()
  print(line)
  if line == "\n":  # skip line
    pass
  elif line[0] == ";":  # comment
    pass
  else:
    mnemonic = line[2]+line[3]+line[4]+line[5]+line[6]
    value_type = line[6]
    if mnmonic == "end  ":
      break
    elif mnemonic == "org @":
      # gather the 16 bit value
      value = line[7]+line[8]+line[9]+line[10]
      # convert into integer
      value = int(value, 16)
      write_index = value
    elif mnemonic in instructions:
      machine_code[write_index] = hex(instructions[mnemonic])
      write_index += 1

      # if the instruction specifies a value
      if value_type == "$":  # 8 bit
        value = line[7]+line[8]
        machine_code[write_index] = hex(int(value, 16))
        write_index += 1
      elif value_type == "@" or value_type == "#" or value_type == "&":  # 16 bit
        value = line[9]+line[10]
        machine_code[write_index] = hex(int(value, 16))
        write_index += 1

        value = line[7]+line[8]
        machine_code[write_index] = hex(int(value, 16))
        write_index += 1

source.close()
print("assembler_2 mk 1.0")
print("compiled")
output = "assembled_" + path
source_2 = open(output, 'w')
source_2.write("[")
for x in range(0, 2048):
  source_2.write(str(machine_code[x]))
  source_2.write(",")
source_2.write("]")
source_2.close()
print(output)
