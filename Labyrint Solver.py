COZUM_3 = {"1":"3","6":"8","l":"x","m":"2","9":"y","z":"5","t":"7","0":"k","a":"a","b":"b"}
COZUM_5 = {"2":"5","7":"8","k":"y","l":"1","m":"z","x":"3","t":"6","0":"9","a":"a","b":"b"}
COZUM_6 = {"1":"6","k":"2","l":"t","9":"z","x":"7","y":"5","0":"m","a":"a","b":"b"}
COZUM_7 = {"2":"7","k":"x","9":"1","m":"t","y":"3","z":"6","0":"l","a":"a","b":"b"}
LABIRENT = [[cell for cell in line.split(" ")] for line in ([['y', '7', 'y', '7', '5', '2', '2', 'x', '3'], ['1', 'y', 'm', '2', '2', 'x', '3', '1', '1'], ['1', '6', 'y', '2', '7', '1', '9', 'm', 't'], ['9', '2', 'm', '2', '2', 't', '1', '3', '3'], ['9', '2', '2', '2', '2', 'k', 'm', 't', '1'], ['9', '2', '2', '2', 'x', 'z', '2', 'x', '1'], ['6', 'y', '2', '2', 'm', 'x', '3', '1', '1'], ['3', 'z', 'x', 'y', 'x', 'z', 't', 'z', 'l'], ['z', '2', 'a', 't', '6', 'b', '2', '2', 't']]
).split("\n")]
def COZUM():
    c = -1
    for SATIR in LABIRENT:
        c = c + 1
        for YASAK_SAYI in ["3","5","6","7"]:
            x = -1
            if YASAK_SAYI in SATIR:
                for TEST_SAYI in LABIRENT[c]:
                    x = x + 1
                    if TEST_SAYI == "3":
                        LABIRENT[c + 1][x] = COZUM_3[LABIRENT[c + 1][x]]
                        LABIRENT[c][x] = "8"
                    elif TEST_SAYI == "5":
                        LABIRENT[c][x + 1] = COZUM_5[LABIRENT[c][x + 1]]
                        LABIRENT[c][x] = "8"
                    elif TEST_SAYI == "6":
                        LABIRENT[c - 1][x] = COZUM_6[LABIRENT[c -1][x]]
                        LABIRENT[c][x] = "8"
                    elif TEST_SAYI == "7":
                        LABIRENT[c][x - 1] = COZUM_7[LABIRENT[c][x - 1]]
                        LABIRENT[c][x] = "8"
    for k in LABIRENT:
        for l in ["3","5","6","7"]:
            if l in k:
                COZUM()                        
COZUM()
print(LABIRENT)
