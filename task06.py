raqam = input("Telefon raqamingizni kiriting (masalan: 90xxxxxxx): ")
kod = raqam[:2]

if kod == "90" or kod == "91":
    print("Operator: Ucell")

if kod == "93" or kod == "94":
    print("Operator: Beeline")

if kod == "95" or kod == "97":
    print("Operator: Uzmobile")

if kod == "88" or kod == "99":
    print("Operator: Mobiuz")
