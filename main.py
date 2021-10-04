#5.Determină dacă un număr dat este palindrom.

def is_palindrome(n):
    '''
    Determina daca un nr dat este palindrom
    Input:
    -n : int
    Output:
    -True, daca n e palindrom, False in caz contrar : bool
    '''
    inverse = 0
    copie=n
    while copie>0:
        inverse=inverse*10+copie%10
        copie=copie//10

    if n == inverse:
        return True
    else:
        return False


def test_is_palidnrome():

    assert is_palindrome(1234321) == True
    assert is_palindrome(52525) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True

test_is_palidnrome()


def is_prime(n):
    """
    Verifica daca un numar este prim
    Input:
    -n : int
    Output
    -True, daca n e palindrom, False in caz contrar
    """
    if n < 2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False

        return True


def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(1) == False
    assert is_prime(29) == True
test_is_prime()

#1.Găsește ultimul număr prim mai mic decât un număr dat.

def get_largest_prime_below(n):
    """
    Returneaza ultimul număr prim mai mic decât un număr dat.
    Input:
    -n (int)
    Output:
    - numarul prim cautat
    """
    for i in range(n-1, 0, -1):
        if is_prime(i)==True:
            return i

def test_get_largest_prime_below():
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(2498) == 2477
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(50) == 47
test_get_largest_prime_below()

#7.Determină dacă un număr este antipalindrom: un număr este antipalindrom dacă oricare două cifre egal depărtate de extremități sunt diferite (excepție făcând cifra din mijloc dacă avem un număr impar de cifre).
def is_antipalindrome(n):
    """
    Verifica daca un numar este antipalindrom
    Input:
    -n: int
    Output:
    -True, daca n e antipalindrom, False in caz contrar : bool
    """

    invers = 0
    copie = n
    while copie > 0:
        invers = invers * 10 + copie % 10
        copie = copie // 10

    for i in range(len(str(n)) // 2):
        if n%10==invers%10:
            return False

        n=n//10
        invers=invers//10

    return True

def test_is_antipalindrome():

    assert is_antipalindrome(2794) == True
    assert is_antipalindrome(4775) == False
    assert is_antipalindrome(834597) == True
    assert is_antipalindrome(22) == False
    assert is_antipalindrome(3) == True

test_is_antipalindrome()
def main():
    while True:
        print('1. Verificare numar palindrom')
        print('2. Ultimul număr prim mai mic decât un număr dat')
        print('3. Verificare numar antipalindrom')
        print('x. Iesire din program')

        optiune=input('Alege optiunea: ')

        if optiune=='1':
            n=int(input('Dati numarul n: '))
            if is_palindrome(n)==True:
                print('Numarul este palindrom')
            elif is_palindrome(n)==False:
                print('Numarul nu este palindrom')
        elif optiune=='2':
            n=int(input('Dati numarul n: '))
            valoare=get_largest_prime_below(n)
            print(f'Numarul prim cautat este {valoare}')
        elif optiune=='3':
            n = int(input('Dati numarul n: '))
            if is_antipalindrome(n) == True:
                print('Numarul este antipalindrom')
            elif is_antipalindrome(n) == False:
                print('Numarul nu este antipalindrom')

        elif optiune=='x':
            break
        else:
            print('Optiune invalida.')


main()

