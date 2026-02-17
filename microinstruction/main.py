from code import *

instructions = [
    ["SHL", 1, "ADD", 1, "PCL OUT", 1, "PCH OUT", 1, "F OUT", 1, "X OUT", 1, "B OUT", 1, "A OUT", 1],
    ["C SET", 1, "X SET", 0, "A SET", 1, "B SET", 1, "MAR OUT", 1, "PC OUT", 1, "AND", 1, "OR", 1],
    ["OE", 1, "WE", 1, "F CLR", 0, "M CLR", 1, "M PRE", 1, "", 0, "M SET", 0, "SZ SET", 1],
    ["SP OUT", 1, "SP INC", 0, "SP DEC", 0, "X INC", 0, "X DEC", 0, "IR SET", 1, "MARH SET", 0, "MARL SET", 0],
    ["U JMP", 0, "C JMP", 0, "S JMP", 0, "Z JMP", 0, "WC", 0, "SUB", 0, "MAR INC", 0, "PC INC", 0],
    ["", 0, "", 0, "", 0, "", 0, "X OFF", 1, "PCH SET", 0, "PCL SET", 0, "N JMP", 0]
]

files = ["rom0.txt", "rom1.txt", "rom2.txt", "rom3.txt", "rom4.txt", "rom5.txt"]
fetch = ["PC INC", "PC OUT", "IR SET", "OE"]
for a in range(0, 6):
  f = open(files[a], "w")
  f.write("[")
  for x in range(0, 70):
    for y in range(0, 8):
      f.write("0b")
      for z in range(0, 8):
        if y != 0:
          if instructions[a][2*z] in code[x][y-1]:
            f.write(str(int(not instructions[a][2*z+1])))
          else:
            f.write(str(instructions[a][2*z+1]))
        else:
          if instructions[a][2*z] in fetch:
            f.write(str(int(not instructions[a][2*z+1])))
          else:
            f.write(str(instructions[a][2*z+1]))
      f.write(",")
  f.write("]")
  f.close()