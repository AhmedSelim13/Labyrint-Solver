LABIRENT = [['y', '7', 'y', '7', '5', '2', '2', 'x', '3'], ['1', 'y', 'm', '2', '2', 'x', '3', '1', '1'],
            ['1', '6', 'y', '2', '7', '1', '9', 'm', 't'], ['9', '2', 'm', '2', '2', 't', '1', '3', '3'],
            ['9', '2', '2', '2', '2', 'k', 'm', 't', '1'], ['9', '2', '2', '2', 'x', 'z', '2', 'x', '1'],
            ['6', 'y', '2', '2', 'm', 'x', '3', '1', '1'], ['3', 'z', 'x', 'y', 'x', 'z', 't', 'z', 'l'],
            ['z', '2', 'a', 't', '6', 'b', '2', '2', 't']]
#
COZUM_3 = {"1": "3", "6": "8", "l": "x", "m": "2", "9": "y", "z": "5", "t": "7", "0": "k", "a": "a", "b": "b"}
COZUM_5 = {"2": "5", "7": "8", "k": "y", "l": "1", "m": "z", "x": "3", "t": "6", "0": "9", "a": "a", "b": "b"}
COZUM_6 = {"1": "6", "k": "2", "l": "t", "9": "z", "x": "7", "y": "5", "0": "m", "a": "a", "b": "b"}
COZUM_7 = {"2": "7", "k": "x", "9": "1", "m": "t", "y": "3", "z": "6", "0": "l", "a": "a", "b": "b"}


def COZUM():
    for satir_index in xrange(0, 9):
        for sutun_index in xrange(0, 9):
            hucre = LABIRENT[satir_index][sutun_index]
            if hucre == "3":
                LABIRENT[satir_index + 1][sutun_index] = COZUM_3[LABIRENT[satir_index + 1][sutun_index]]
                LABIRENT[satir_index][sutun_index] = "8"
            elif hucre == "5":
                LABIRENT[satir_index][sutun_index + 1] = COZUM_5[LABIRENT[satir_index][sutun_index + 1]]
                LABIRENT[satir_index][sutun_index] = "8"
            elif hucre == "6":
                LABIRENT[satir_index - 1][sutun_index] = COZUM_6[LABIRENT[satir_index - 1][sutun_index]]
                LABIRENT[satir_index][sutun_index] = "8"
            elif hucre == "7":
                LABIRENT[satir_index][sutun_index - 1] = COZUM_7[LABIRENT[satir_index][sutun_index - 1]]
                LABIRENT[satir_index][sutun_index] = "8"


def cozum_gerekli():
    for k in LABIRENT:
        for l in ["3", "5", "6", "7"]:
            if l in k:
                return True
    return False


x = 0
while (cozum_gerekli()):
    x += 1
    COZUM()

for k in LABIRENT:
    print(k)

print(x)
