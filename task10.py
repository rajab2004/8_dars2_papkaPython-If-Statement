ball = int(input("Imtihon ballini kiriting (0 dan 100 gacha): "))

if ball >= 90 and ball <= 100:
    print("Bahoyingiz: A")
else:
    if ball >= 80 and ball <= 89:
        print("Bahoyingiz: B")
    else:
        if ball >= 70 and ball <= 79:
            print("Bahoyingiz: C")
        else:
            if ball >= 60 and ball <= 69:
                print("Bahoyingiz: D")
            else:
                if ball >= 0 and ball <= 59:
                    print("Bahoyingiz: F")
                else:
                    print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak!")
