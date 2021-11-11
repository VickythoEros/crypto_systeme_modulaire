"""
==========================  DIVISER  =====================================
"""
def equation_1(a,b,c,r):
    """ verifie si 𝑎𝑟 + 𝑏𝑟 ≡ 𝑐𝑟 [33]
    ex: a= 27 ,b = 4, r = 1 alors c= 4
    """
    if((a**r + b**r)%(3**3) == c**r):
        return True
    else:
        return False

def equation_2(a,b,c):
    """ verifie si 𝑎 + 𝑐 𝑜𝑢 𝑏 + 𝑐 ≡ 3,6 [9] 𝑠𝑖 𝑎 ≡ 𝑏 [9]
    ex: a= 11 ,b = 2, C = 2
    """
    if (((a + c) % 9 == 3 or (a + c) % 9 == 6) or ((b + c) % 9 == 3 or (b + c) % 9 == 6)):
        return True
    else:
        return False




def equation_3(a,b,c):
    """ verifie si 𝑎 + 𝑐 𝑜𝑢 𝑏 + 𝑐 ≡ 3,6 [9] 𝑠𝑖 𝑎 ≡ 𝑏 [9]
    ex: a= 11 ,b = 2, C = 2
    """
    if ((a + c) % 9 == 0 or (b + c) % 9 == 0):
        return True
    else:
        return False


def equation_4(a,b,c):
    """ verifie si 1 + 𝑏𝑐 ≡ 0 [3] 𝑒𝑡 𝑎2 + 𝑏𝑐 ≢ 0 [9]
    ex: a= 1 ,b = 2, C = 1
    """
    if ((1 + b*c)%3 == 0 and (a**2 + b*c)%9 != 0):
        return True
    else:
        return False


def equation_5(a,b,c):
    """ verifie 𝑎2 + 𝑏𝑐 𝑒𝑡 𝑏2 + 𝑎𝑐 𝑒𝑡 𝑐2 − 𝑎𝑏 ≢ 0 [9]
    """
    if(a**2 + b*c)%9 == 0 and (b**2 + a*c)%9 == 0 and (c**2 - a*b)%9 ==0 :
        return True
    else:
        return False

def equation_6(a,b,c,r):
    """ verifie si 𝑎2𝑟 + (𝑏𝑐)𝑟 ≡ 3 [9]

    """
    if((a**(2*r) + (b*c)**r))%9 == 3:
        return True
    else:
        return False


def equation_7(a,b,c,r):
    """ verifie 𝑏2𝑟 + (𝑎𝑐)𝑟, 𝑐2𝑟 − (𝑎𝑏)𝑟 ≡ 0 𝑜𝑢 3 𝑜𝑢 6 [9]
    """
    if (((b**(2*r) + (a*c)**r))%9 == 0 or ((b**(2*r) + (a*c)**r))%9 == 3 or ((b**(2*r) + (a*c)**r))%9 == 6) or (((c**(2*r) - (a*b)**r))%9 == 0 or (c**(2*r) - (a*b)**r)%9 == 3 or (c**(2*r) - (a*b)**r)%9 == 6) :
        return True
    else:
        return False





def pgcd(a,b):
    """permet de calculer le PGCD(a,b)"""
    r =  a%b
    if r == 0:
        return b
    else:
        return pgcd(b,r)



def verify_1(a,b,c,r):
    "permet de verifier le systeme pour a congrus a b modulo 9"
    if( (a* b* c) %3 != 0):
        if (a % 9 == b):
            if(equation_1(a,b,c,r) and equation_2(a,b,c) and equation_4(a,b,c)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def verify_2(a,b,c,r):
    "permet de verifier le systeme pour a non congrus a b modulo 9"
    if ((a * b * c) % 3 != 0):
        if(a%9 != b):
            if(equation_1(a,b,c,r) and equation_3(a,b,c) and equation_4(a,b,c)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False



"""
=============================   FUSION  ================================================
"""

def ensemble_U(n):
    """ Permet de construire l'ensemble 𝑈3 avec 𝑈 = (ℤ ∕ 27ℤ)∗ ensemble des elements inversible de (ℤ ∕ 27ℤ)
        ++ ensemble des elements de (ℤ ∕ 27ℤ) premier avec 27 ++
    """
    tab = [i for i in range(n) if pgcd(i,n) == 1]
    return tab




def contrainte1(n,r,tab):
    tab_result = []
    U = []
    if tab:
        U = tab
    else:
        U = ensemble_U(n)

    for i in U:
        for j in U:
            for k in U:
                if equation_1(i,j,k,r) :
                    tab_result.append(i)
                    tab_result.append(j)
                    tab_result.append(k)
                
    return tab_result



def contrainte2(n,tab):
    tab_result = []
    U = []
    if tab:
        U = tab
    else:
        U = ensemble_U(n)

    for i in U:
        for j in U:
            for k in U:
                if equation_2(i,j,k) or equation_3(i,j,k) :
                    tab_result.append(i)
                    tab_result.append(j)
                    tab_result.append(k)
                
    return tab_result



def contrainte3(n,tab):
    tab_result = []
    U = []
    if tab:
        U = tab
    else:
        U = ensemble_U(n)

    for i in U:
        for j in U:
            for k in U:
                if equation_5(i,j,k):
                    tab_result.append(i)
                    tab_result.append(j)
                    tab_result.append(k)
                
    return tab_result





def contrainte4(n,r,tab):
    tab_result = []
    U = []
    if tab:
        U = tab
    else:
        U = ensemble_U(n)

    for i in U:
        for j in U:
            for k in U:
                if equation_6(i,j,k,r) and equation_7(i,j,k,r) :
                    tab_result.append(i)
                    tab_result.append(j)
                    tab_result.append(k)
                
    return tab_result





def algo_general_2(n,r):
    """
    permet de savoir si le systeme admet des solutions pour U
    :param n:
    :param r:
    :return: none
    """
    tab_result = []
    for i in ensemble_U(n):
        for j in ensemble_U(n):
            for k in ensemble_U(n):
                
                if equation_1(i,j,k,r) :
                    #print(f"Le triplé ( {i} , {j} , {k} ) est une solution de l'equation S pour r = {r}")
                    #v = "( "+ str(i) +" , " + str(j) +" , " + str(k) +" )"
                    tab_result.append(i)
                    tab_result.append(j)
                    tab_result.append(k)
                    #v = 1

    #if v == 0:
       # print(f"L'equation n'admet pas de solution pour r = {r} dans U ")
    return tab_result



def algo_general_1(n,r):
    """
    permet de savoir si le systeme admet des solutions pour U
    :param n:
    :param r:
    :return: none
    """
    tab_result = []
    for i in ensemble_U(n):
        for j in ensemble_U(n):
            for k in ensemble_U(n):
                if verify_1(i,j,k,r) or verify_2(i,j,k,r):
                    #print(f"Le triplé ( {i} , {j} , {k} ) est une solution de l'equation S pour r = {r}")
                    #v = "( "+ str(i) +" , " + str(j) +" , " + str(k) +" )"
                    tab_result.append(i)
                    tab_result.append(j)
                    tab_result.append(k)
                    #v = 1

    #if v == 0:
       # print(f"L'equation n'admet pas de solution pour r = {r} dans U ")
    return tab_result




def principal(n):
    """
    verifier pour tout element de r
    :param n:
    :return:
    """
    r = [1,5,7,11,13,17]
    for i in r:
        algo_general_1(n,i)
        print(" ")









""" == FONCTIONS TESTS =="""
def main_a_congrus_b(a,b,c,r):
    if verify_1(a,b,c,r) == True:
       print(f"Le triplé ( {a} , {b} , {c} ) est une solution de l'equation S pour r = {r}")

    else:
        print(f"L'equation S n'admet pas de solution pour les triplés ( {a} , {b} , {c} )  pour r = {r}")


def main_a_non_congrus_b(a,b,c,r):
    if verify_2(a,b,c,r) == True:
       print(f"Le triplé ( {a} , {b} , {c} ) est une solution de l'equation S pour r = {r}")

    else:
        print(f"L'equation S n'admet pas de solution pour les triplés ( {a} , {b} , {c} )  pour r = {r}")




def verify_a_b_c_r(a,b,c,r):
    if verify_2(a,b,c,r) or verify_1(a,b,c,r):
        return True
    else:
        return False


