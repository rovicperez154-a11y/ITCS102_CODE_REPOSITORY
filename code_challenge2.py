money=62672

thou= money // 1000
thou_change= money % 1000

five= thou_change // 500
five_change= thou_change % 500

dos= five_change // 200
dos_change= five_change % 200

uno= dos_change // 100
uno_change= dos_change % 100

sek= uno_change // 50
sek_change= uno_change % 50

twen= sek_change // 20
twen_change= sek_change % 20

ten= twen_change // 10
ten_change= twen_change % 10

cin= ten_change // 5
cin_change= ten_change % 5

one= cin_change // 1
one_change= cin_change % 1



print("CURRENT MONEY IS -->",money,"php")
print("1000 -->",thou)
print(" 500 -->",five)
print(" 200 -->",dos)
print(" 100 -->",uno)
print("  50 -->",sek)
print("  20 -->",twen)
print("  10 -->",ten)
print("   5 -->",cin)
print("   1 -->",one)





