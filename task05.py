omonat = float(input("Qanch pul omonatga qo'yayapsiz:  "))
if omonat < 100_000 :
    
    print(omonat,"* 5% ")

if omonat > 100_000 and omonat <= 500_000:
    
    print(omonat,"* 7% ")
    
if omonat > 500_000 :
    
    print(omonat,"* 10% ")