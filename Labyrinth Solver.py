www = 0
son = []
def f():
	www= 0
    for i in ko:
        for k in [3,5,6,7]:
            try:
                x = i.index(str(k))
                c = ko.index(i)
                i[x] = 8
                if x >= 0:
                    if k == 3:
                        alt = ko[c + 1]
                        if alt[x] == "1":
                            alt[x] = "3"
                        elif alt[x] == "6":
                            alt[x] = 8
                        elif alt[x] == "l":
                            alt[x] = "x"
                        elif alt[x] == "m":
                             alt[x] = "2"
                        elif alt[x] == "9":
                            alt[x] ="y"
                        elif alt[x] == "z":
                             alt[x] = "5"
                        elif alt[x] == "t":
                            alt[x] = "7"
                        elif alt[x] == "0":
                            alt[x] = "k"
                    elif k == 5:
                        sag = ko[c]
                        y = x + 1
                        if sag[y]== "2":
                            sag[y] = "5"
                        elif sag[y]== "7":
                            sag[y] = 8
                        elif sag[y]== "k":
                            sag[y] = "y"
                        elif sag[y]== "l":
                            sag[y] = "1"
                        elif sag[y]== "m":
                            sag[y] = "z"
                        elif sag[y]== "x":
                            sag[y] = "3"
                        elif sag[y]== "t":
                            sag[y] = "6"
                        elif sag[y]== "0":
                            sag[y] = "9"
                        
                    elif k == 6:
                        ust = ko[c - 1]
                        if ust[x]== "1":
                            ust[x] = "6"
                        elif ust[x]== "k":
                            ust[x] = "2"
                        elif ust[x]== "l":
                            ust[x] = "t"
                        elif ust[x]== "9":
                            ust[x] = "z"
                        elif ust[x]== "x":
                            ust[x] = "7"
                        elif ust[x]=="y":
                            ust[x] = "5"
                        elif ust[x]== "0":
                            ust[x] = "m"
                        
                    elif k == 7:
                        sol = ko[c]
                        o = x - 1
                        if sol[o]== "2":
                            sol[o] = "7"
                        elif sol[o]== "k":
                            sol[o] = "x"
                        elif sol[o]== "9":
                            sol[o] = "1"
                        elif sol[o]== "m":
                            sol[o] = "t"
                        elif sol[o]== "y":
                            sol[o] ="3"
                        elif sol[o]== "z":
                            sol[o] ="6"
                        elif sol[o]== "0":
                            sol[o] = "l"

            except:
                w = 0
            finally:
                for v in son:
                    for q in [3,5,6,7]:
                        if str(q) not in v:
                        		www = 1
                        else:
                            f()
        		if www == 1:
        			break
        son.append(i)
ko = [['y', '7', 'y', '7', '5', '2', '2', 'x', '3'], ['1', 'y', 'm', '2', '2', 'x', '3', '1', '1'], ['1', '6', 'y', '2', '7', '1', '9', 'm'], ['9', '2', 'm', '2', '2', 't', '1', '3', '3'], ['9', '2', '2', '2', '2', 'k', 'm', 't', '1'], ['9', '2', '2', '2', 'x', 'z', '2', 'x', '1'], ['6', 'y', '2', '2', 'm', 'x', '3', '1', '1'], ['3', 'z', 'x', 'y', 'x', 'z', 't', 'z', 'l'], ['z', '2', 'a', 't', '6', 'b', '2', '2', 't']]
print(ko)
f()
print(son)

