from commands import *
from trace import *
import acorn

load(0x8000, "NFS-3.34.rom", "6502")
move(0x0400, 0x934c, 0x300)
set_output_filename("nfs334.6502")

comment(0x8000, '''*****************************************************
If patching for Master 128, set the following:
econet_station_id = &2000 (or any address you choose)
econet_INTOFF     = &fe38
econet_INTON      = &fe3c
*****************************************************''')
blank(0x8000)

acorn.bbc()
acorn.is_sideways_rom()

string(0x8BD7,n=None)
string(0x8BDA,n=None)
stringcr(0x8BE5)
stringcr(0x8BEA)
string(0x8BEF,n=None)
string(0x8CE7,n=None)

byte(0x8015,n=11)
byte(0x824d,n=14)
byte(0x84BB,n=1)
byte(0x84C6,n=1)
byte(0x84D5,n=1)
byte(0x84DF,n=1)
byte(0x84E9,n=1)
byte(0x84F1,n=1)
byte(0x84FD,n=1)
byte(0x918e,n=26)
for i in range(9):
    byte(0x964c+i*2,n=2)
byte(0x9F4B,n=8)

label(0xfe18,"econet_station_id")
label(0xfe18,"econet_INTOFF")
label(0xfe20,"econet_INTON")
label(0xfea0,"econet_adlc_address_0")
label(0xfea1,"econet_adlc_address_1")
label(0xfea2,"econet_adlc_address_2")
label(0xfea3,"econet_adlc_address_3")
hook_subroutine(0x853b,"print_message_and_fall_through", stringhi_hook)

label(0x9d94,"l9d94")
expr(0x9d8e, make_lo("l9d94"))
expr(0x9d90, make_hi("l9d94"))

label(0x9db2,"l9db2")
expr(0x9dac, make_lo("l9db2"))
expr(0x9dae, make_hi("l9db2"))

label(0x9dc8,"l9dc8")
expr(0x9dc2, make_lo("l9dc8"))
expr(0x9dc4, make_hi("l9dc8"))

label(0x9de3,"l9de3")
expr(0x9dd3, make_lo("l9de3"))
expr(0x9dd5, make_hi("l9de3"))

label(0x9edd,"l9edd")
expr(0x9e0a, make_lo("l9edd"))
expr(0x9e0c, make_hi("l9edd"))

label(0x9e2b,"l9e2b")
expr(0x9e25, make_lo("l9e2b"))
expr(0x9e27, make_hi("l9e2b"))

label(0x9e50,"l9e50")
expr(0x9e43, make_lo("l9e50"))
expr(0x9e45, make_hi("l9e50"))

label(0x9ea4,"l9ea4")
expr(0x9e4a, make_lo("l9ea4"))
expr(0x9e4c, make_hi("l9ea4"))

label(0x9a34,"l9a34")
expr(0x9e88, make_lo("l9a34"))
expr(0x9e8a, make_hi("l9a34"))

label(0x9ee9,"l9ee9")
expr(0x9ee3, make_lo("l9ee9"))
expr(0x9ee5, make_hi("l9ee9"))

label(0x9eff,"l9eff")
expr(0x9ef9, make_lo("l9eff"))
expr(0x9efb, make_hi("l9eff"))

label(0x9f15,"l9f15")
expr(0x9f0a, make_lo("l9f15"))
expr(0x9f0c, make_hi("l9f15"))

label(0x9d4c,"l9d4c")
expr(0x9cab, make_lo("l9d4c"))
expr(0x9cad, make_hi("l9d4c"))

label(0x96f6,"l96f6")
expr(0x9a44, make_lo("l96f6"))
expr(0x9a46, make_hi("l96f6"))

label(0x9715,"l9715")
expr(0x970f, make_lo("l9715"))
expr(0x9711, make_hi("l9715"))

label(0x9747,"l9747")
expr(0x9731, make_lo("l9747"))
expr(0x9733, make_hi("l9747"))

label(0x982d,"l982d")
expr(0x9827, make_lo("l982d"))
expr(0x9829, make_hi("l982d"))

label(0x9839,"l9839")
expr(0x9833, make_lo("l9839"))
expr(0x9835, make_hi("l9839"))

label(0x984f,"l984f")
expr(0x9849, make_lo("l984f"))
expr(0x984b, make_hi("l984f"))

label(0x9865,"l9865")
expr(0x985a, make_lo("l9865"))
expr(0x985c, make_hi("l9865"))

label(0x989a,"l989a")
expr(0x9878, make_lo("l989a"))
expr(0x987a, make_hi("l989a"))

label(0x98f7,"l98f7")
expr(0x9884, make_lo("l98f7"))
expr(0x9886, make_hi("l98f7"))

label(0x99bb,"l99bb")
expr(0x9971, make_lo("l99bb"))
expr(0x9973, make_hi("l99bb"))

label(0x9992,"l9992")
expr(0x998c, make_lo("l9992"))
expr(0x998e, make_hi("l9992"))

label(0x9bdd,"l9bdd")
expr(0x9b9c, make_hi(make_subtract("l9bdd",1)))
expr(0x9b9f, make_lo(make_subtract("l9bdd",1)))

expr(0x82c4, "econet_station_id")
expr(0x968f, "econet_station_id")
expr(0x9701, "econet_station_id")
expr(0x9844, "econet_station_id")
expr(0x9993, "econet_station_id")
expr(0x9d7e, "econet_station_id")
expr(0x9dbd, "econet_station_id")
expr(0x9e2c, "econet_station_id")
expr(0x9ef4, "econet_station_id")
expr(0x9670, "econet_INTOFF")
expr(0x969e, "econet_INTOFF")
expr(0x96b5, "econet_INTOFF")
expr(0x9c54, "econet_INTOFF")
expr(0x9c57, "econet_INTOFF")
expr(0x9fcc, "econet_INTOFF")

for i in range(36):
    rts_code_ptr(0x8020+1+i, 0x8044+1+i)

for i in range(5):
    rts_code_ptr(0x8e18+i, 0x8e1d+i)
    #Does .c9b88 reference this table???
    rts_code_ptr(0x9B91+i, 0x9B96+i)

for i in range(8):
    #Does .c9a80 reference this table???
    rts_code_ptr(0x9A8F+i, 0x9A97+i)
    #Does .c9ca2 reference this table???
    rts_code_ptr(0x9CD4+i, 0x9CDC+i)

for i in range(9):
    rts_code_ptr(0x902B+i, 0x9034+i)

for i in range(14):
    code_ptr(0x0500+2*i)

entry(0x81F8) #RTS to here via stack manipulation
entry(0x8211) #RTS to here via stack manipulation
entry(0x8217) #RTS to here via stack manipulation
entry(0x8694) #Orphaned code? No caller?
entry(0x89EA) #Orphaned code? No caller?
entry(0x8BF2) #Orphaned code? No caller?
entry(0x8C24) #RTS to here via stack manipulation
entry(0x8C2E) #RTS to here via stack manipulation
entry(0x8C41) #RTS to here via stack manipulation
entry(0x8C67) #RTS to here via stack manipulation
entry(0x8C73) #RTS to here via stack manipulation
entry(0x8C8B) #RTS to here via stack manipulation
entry(0x8C9D) #RTS to here via stack manipulation
entry(0x8CA7) #RTS to here via stack manipulation
entry(0x8D06) #Orphaned code? No caller?
entry(0x9007) #Orphaned code? No caller?
entry(0x9307) #Relocated to &16. Orphaned code? No caller?
entry(0x934C) #Relocated to &400 Orphaned code? No caller?
entry(0x934F) #Relocated to &403. Orphaned code? No caller?
entry(0x9433) #Relocated to 0x4e9. Orphaned code? No caller?
entry(0x943B) #Relocated to 0x4ef. Orphaned code? No caller?
entry(0x9468) #Relocated to 0x51d. Orphaned code? No caller?

entry(0x9715) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9747) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x982D) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9839) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x984F) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x98F7) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9992) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x99BB) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9D4C) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9D94) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9DB2) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9DC8) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9E2B) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9E50) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9EA4) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9EE9) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9EFF) #Called by setting A=Lo, Y=Hi and jumping to &0d0e
entry(0x9FCB) #Orphaned code? No caller?
entry(0x9FD9) #Orphaned code? No caller?
entry(0x9FEB) #Orphaned code? No caller?

go()