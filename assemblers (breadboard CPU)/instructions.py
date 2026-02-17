instruction_set = [
  # load data a
  "lda $",
  "lda @",
  "lda #",
  "lda &",

  # load data x
  "ldx $",
  "ldx @",
  "ldx #",
  "ldx &",

  # x opperations
  "inx  ",
  "dex  ",

  # a,x opperations
  "txa  ",
  "tax  ",

  # addition
  "add $",
  "add @",
  "add #",
  "add &",

  # subtraction
  "sub $",
  "sub @",
  "sub #",
  "sub &",

  # addition with carry flag
  "adc $",
  "adc @",
  "adc #",
  "adc &",

  # subtract with borrow flag
  "sbc $",
  "sbc @",
  "sbc #",
  "sbc &",

  # and
  "and $",
  "and @",
  "and #",
  "and &",

  # or
  "orr $",
  "orr @",
  "orr #",
  "orr &",

  # shift
  "shr  ",
  "shl  ",

  # roll
  "ror  ",
  "rol  ",

  # store a register
  "sta @",
  "sta #",
  "sta &",

  # store x register
  "stx @",
  "stx #",
  "stx &",

  # stack
  "pla  ",
  "pha  ",
  "plx  ",
  "phx  ",
  "plf  ",
  "phf  ",
  "pla &",
  "plx &",

  # subroutine
  "jsr @",
  "rsr  ",

  # flags
  "clf  ",
  "msk  ",
  "umk  ",

  # jump
  "jmp @",
  "beq @",
  "bne @",
  "bmi @",
  "bpl @",
  "bcs @",
  "bcc @"
]