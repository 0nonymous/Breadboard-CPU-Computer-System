code = [
  [  # LDA IMMEDIATE 0
    ["PC OUT", "A SET", "OE", "PC INC"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # LDA ABSOLUTE 1 
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "A SET"],
    [],
    [],
    [],
    []
  ],
  [  # LDA INDIRECT 2
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "A SET"],
    []
  ],
  [  # LDA OFFSET ABSOLUTE 3
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "A SET", "X OFF"],
    [],
    [],
    [],
    []
  ],
  [  # LDX IMMEDIATE 4
    ["PC OUT", "X SET", "OE", "PC INC"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # LDX ABSOLUTE 5
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "X SET"],
    [],
    [],
    [],
    []
  ],
  [  # LDX INDIRECT 6
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "X SET"],
    []
  ],
  [  # LDX OFFSET ABSOLUTE 7
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "X SET", "X OFF"],
    [],
    [],
    [],
    []
  ],
    [  # INX 8
    ["X INC"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # DEX 9
    ["X DEC"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # TXA 10
    ["X OUT", "A SET"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # TAX 11
    ["A OUT", "X SET"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # ADD IMMEDIATE 12
    ["PC OUT", "OE", "PC INC", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # ADD ABSOLUTE 13
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET"],
    [],
    [],
    []
  ],
  [  # ADD INDIRECT 14
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET"]
  ],
  [  # ADD OFFSET ABSOLUTE 15
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET", "X OFF"],
    ["ADD", "A SET", "C SET", "SZ SET"],
    [],
    [],
    []
  ],
  [  # SUB IMMEDIATE 16
    ["PC OUT", "OE", "PC INC", "B SET"], 
    ["ADD", "A SET", "C SET", "SZ SET", "SUB"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # SUB ABSOLUTE 17
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB"],
    [],
    [],
    []
  ],
  [  # SUB INDIRECT 18
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB"]
  ],
  [  # SUB OFFSET ABSOLUTE 19
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET", "X OFF"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB"],
    [],
    [],
    []
  ],
  [  # ADC IMMEDIATE 20
    ["PC OUT", "OE", "PC INC", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "WC"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # ADC ABSOLUTE 21
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "WC"],
    [],
    [],
    []
  ],
  [  # ADC INDIRECT 22
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "WC"]
  ],
  [  # ADC OFFSET ABSOLUTE 23
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET", "X OFF"],
    ["ADD", "A SET", "C SET", "SZ SET", "WC"],
    [],
    [],
    []
  ],
  [  # SBC IMMEDIATE 24
    ["PC OUT", "OE", "PC INC", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB", "WC"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # SBC ABSOLUTE 25
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB", "WC"],
    [],
    [],
    []
  ],
  [  # SBC INDIRECT 26
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "B SET"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB", "WC"]
  ],
  [  # SBC OFFSET ABSOLUTE 27
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET", "X OFF"],
    ["ADD", "A SET", "C SET", "SZ SET", "SUB", "WC"],
    [],
    [],
    []
  ],
  [  # AND IMMEDIATE 28
    ["PC OUT", "OE", "PC INC", "B SET"],
    ["AND", "A SET", "SZ SET"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # AND ABSOLUTE 29
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["AND", "A SET", "SZ SET"],
    [],
    [],
    [],
    []
  ],
  [  # AND INDIRECT 30
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "B SET"],
    ["AND", "A SET", "SZ SET"]
  ],
  [  # AND OFFSET ABSOLUTE 31
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET", "X OFF"],
    ["AND", "A SET", "SZ SET"],
    [],
    [],
    []
  ],
  [  # ORR IMMEDIATE 32
    ["PC OUT", "OE", "PC INC", "B SET"],
    ["OR", "A SET", "SZ SET"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # ORR ABSOLUTE 33
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["OR", "A SET", "SZ SET"],
    [],
    [],
    [],
    []
  ],
  [  # ORR INDIRECT 34
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "OE", "B SET"],
    ["OR", "A SET", "SZ SET"]
  ],
  [  # ORR OFFSET ABSOLUTE 35
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "B SET", "X OFF"],
    ["OR", "A SET", "SZ SET"],
    [],
    [],
    []
  ],
  [  # SHR 36 CORRECTED
    ["A SET", "SZ SET", "C SET", "SHL"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # SHL 37 CORRECTED
    ["B SET", "A OUT"],
    ["A SET", "SZ SET", "C SET", "ADD"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # ROR 38 CORRECTED
    ["A SET", "SZ SET", "C SET", "SHL", "WC"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # ROL 39 CORRECTED
    ["B SET", "A OUT"],
    ["A SET", "SZ SET", "C SET", "ADD", "WC"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # STA ABSOLUTE 40
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "WE", "A OUT"],
    [],
    [],
    [],
    []
  ],
  [  # STA INDIRECT 41
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "WE", "A OUT"],
    []
  ],
  [  # STA OFFSET ABSOLUTE 42
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "WE", "A OUT", "X OFF"],
    [],
    [],
    [],
    []
  ],
  [  # STX ABSOLUTE 43
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "WE", "X OUT"],
    [],
    [],
    [],
    []
  ],
  [  # STX INDIRECT 44
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "OE", "MAR INC", "B SET"],
    ["MAR OUT", "OE", "MARH SET"],
    ["MARL SET", "B OUT"],
    ["MAR OUT", "WE", "X OUT"],
    []
  ],
  [  # STX OFFSET ABSOLUTE 45
    ["PC OUT", "OE", "PC INC", "MARL SET"],
    ["PC OUT", "OE", "PC INC", "MARH SET"],
    ["MAR OUT", "WE", "X OUT", "X OFF"],
    [],
    [],
    [],
    []
  ],
  [  # POP A 46
    ["SP INC"],
    ["A SET", "SP OUT", "OE"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # PSH A 47
    ["A OUT", "SP DEC", "SP OUT", "WE"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # POP X 48
    ["SP INC"],
    ["X SET", "SP OUT", "OE"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # PSH X 49
    ["X OUT", "SP DEC", "SP OUT", "WE"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # POP F 50
    ["SP INC"],
    ["F SET", "SP OUT", "OE"],
    [],
    [],
    [],
    [],
    []
  ],
  [  # PSH F 51
    ["F OUT", "SP DEC", "SP OUT", "WE"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # OFF A 52
    ["A SET", "SP OUT", "X OFF", "OE"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # OFF X 53
    ["X SET", "SP OUT", "X OFF", "OE"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # JSR 54
    ["SP DEC", "SP OUT", "PCL OUT", "WE"],
    ["SP DEC", "SP OUT", "PCH OUT", "WE"],
    ["B SET", "PC OUT", "PC INC", "OE"],
    ["PCH SET", "PC OUT", "PC INC", "U JMP", "OE"],
    ["PCL SET", "B OUT", "U JMP"],
    [],
    []
  ],
  [  # RSR 55
    ["SP INC"],
    ["SP OUT", "PCH SET", "OE", "U JMP"],
    ["SP INC"],
    ["SP OUT", "PCL SET", "OE", "U JMP"],
    ["PC INC"],
    ["PC INC"],
    [],
    [],
  ],
    [  # CLF 56
    ["F CLR"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # MSK 57
    ["M PRE"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # UMK 58
    ["M CLR"],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # JMP 59
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "U JMP", "OE"],
    ["B OUT", "PCL SET", "U JMP"],
    [],
    [],
    [],
    []
  ],
  [  # BEQ 60
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "Z JMP", "OE"],
    ["B OUT", "PCL SET", "Z JMP"],
    [],
    [],
    [],
    []
  ],
  [  # BNE 61
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "Z JMP", "N JMP", "OE"],
    ["B OUT", "PCL SET", "Z JMP", "N JMP"],
    [],
    [],
    [],
    []
  ],
  [  # BMI 62
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "S JMP", "OE"],
    ["B OUT", "PCL SET", "S JMP"],
    [],
    [],
    [],
    []
  ],
  [  # BPL 63
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "S JMP", "N JMP", "OE"],
    ["B OUT", "PCL SET", "S JMP", "N JMP"],
    [],
    [],
    [],
    []
  ],
  [  # BCS 64
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "C JMP", "OE"],
    ["B OUT", "PCL SET", "C JMP"],
    [],
    [],
    [],
    []
  ],
  [  # BCC 65
    ["PC INC", "PC OUT", "B SET", "OE"],
    ["PC INC", "PC OUT", "PCH SET", "C JMP", "N JMP", "OE"],
    ["B OUT", "PCL SET", "C JMP", "N JMP"],
    [],
    [],
    [],
    []
  ],
  [  # ILA INDIRECT STACK + X OFFSET 66
    ["SP INC"],
    ["MARH SET", "SP OUT", "OE", "X OFF"],
    ["SP INC"],
    ["MARL SET", "SP OUT", "OE", "X OFF"],
    ["SP DEC", "MAR OUT", "OE", "A SET"],
    ["SP DEC"],
    []
  ],
  [  # ILX INDIRECT STACK + X OFFSET 67
    ["SP INC"],
    ["MARH SET", "SP OUT", "OE", "X OFF"],
    ["SP INC"],
    ["MARL SET", "SP OUT", "OE", "X OFF"],
    ["SP DEC", "MAR OUT", "OE", "X SET"],
    ["SP DEC"],
    []
  ],
  [  # ISA INDIRECT STACK + X OFFSET 68
    ["SP INC"],
    ["MARH SET", "SP OUT", "OE", "X OFF"],
    ["SP INC"],
    ["MARL SET", "SP OUT", "OE", "X OFF"],
    ["SP DEC", "MAR OUT", "WE", "A OUT"],
    ["SP DEC"],
    []
  ],
  [  # ISX INDIRECT STACK + X OFFSET 69
    ["SP INC"],
    ["MARH SET", "SP OUT", "OE", "X OFF"],
    ["SP INC"],
    ["MARL SET", "SP OUT", "OE", "X OFF"],
    ["SP DEC", "MAR OUT", "WE", "X OUT"],
    ["SP DEC"],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
    [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
  [  # 
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ],
]