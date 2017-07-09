# JSNTLIB Manual



> `jsntlib` is an open sourse library for **number theory** written in Python, with compatibility in both 2.7.3 and 3.6.5 versions. The following is a manual for this library. Usage instructions and samples attached.






### Functions



  * `primelist(upper[, lower])`

    Returns `list` type containing **prime numbers** within integer `upper` and `lower` bound, if `lower` is given. When `lower` is omitted, all prime numbers **less than** (bound excluded) the `upper` bound.

    ```python
    >>> from jsntlib import primelist
    >>> primelist(17, 89)
    [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
    ```



  * `isdivisible(a, b)`

    Returns `bool` type if integers `a` and `b` are **divisible**, i.o.w. whether `b|a` or `b∤a`, when `b` is greater than `a`, and in other cases, vice versa.

    ```python
    >>> from jsntlib import isdivisible
    >>> isdivisible(983, 234)
    False
    ```



  * `isprime(N)`

    Returns `bool` type if integer `N` is a **prime number**.

    ```python
    >>> from jsntlib isprime
    >>> isprime(8563)
    True
    ```



  * `gcd(a, b)`

    Returns `int` type of the **greatest common divisor** between integers `a` and `b`.

    ```python
    >>> from jsntlib import gcd
    >>> gcd(657, 292)
    73
    ```



  * `lcm(a, b)`

    Returns `int` type of the **least common multiplier** between integers `a` and `b`.

    ```python
    >>> from jsntlib import lcm
    >>> lcm(146, 28)
    2044
    ```



  * `coprime(a, b)`

    Returns `bool` type if integers `a` and `b` are **coprime**, i.e. which greatest common divisor is one(1).

    ```python
    >>> from jsntlib import coprime
    >>> coprime(352, 76)
    False
    ```



  * `eealist(a, b)`

    Returns `list` type containing quotients for integers `a/b` with **extended Euclidean Algorithm**.

    ```python
    >>> from jsntlib import eealist
    >>> eealist(23, 984)
    [0, 42, 1, 3, 1, 1]
    ```



  * `bezout(a, b)`

    Returns `tuple` type containing parameters for **Bézout equition** of integers `a` and `b`.

    ```python
    # -20*-367 + -41*179 = (-367, 179)
    >>> from jsntlib import bezout
    >>> bezout(-367, 179)
    (-20, -41)
    ```



  * `factor(N[, wrap=False])`

    Returns `list` type containing **prime factors** of integers `N`, if keyword `wrap` is `False` or omitted. Once set `True`, `tuple` type of two lists will be offered, which implies the factors and their exponents.

    ```python
    >>> from jsntlib import factor
    >>> factor(72)
    [2, 2, 2, 3, 3]
    >>> factor(-345, wrap=True)
    ([-1, 3, 5, 23], [1, 1, 1, 1])
    ```



  * `decomposit(N)`

    Returns `tuple` type containing two(2) integers, which are the **decoposition** results of coposit number `N`, i.e. `(a, b)` where `N|a^2-b^2` but `N∤a+b` nor `N∤a-b`.

    ```python
    >>> from jsntlib import decomposit
    >>> decomposit(345)
    (1508, 608)
    ```



  * `binary(a, b, c)`

    Returns `tuple` type containing special solutions for an **indefinite binary equation**, i.e. `a*x + b*y = c`.

    ```python
    # 7*x + b*24 = -3
    # x = 6 + 24*t; y = -21 - 7*t (t∈Z)
    >>> from jsntlib import binary
    >>> binary(7,24,-3)
    (6, -21)
    ```



  * `modulo(b, e, m)`

    Returns `int` type for the result of `b^e (mod m)`.

    ```python
    # -765^264 = -291 (mod 597)
    >>> from jsntlib import modulo
    >>> modulo(-765, 264, 597)
    -291
    ```



  * `polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe)`

    Returns `tuple` type containing the lists of exponents and coefficients of **quotient** and **remainder** polynomials, which are the **division** results of **dividend** and **divisor** polynomials.

    ```python
    #   (x^34 + 4x^3 + 3x^2 - 2x) ÷ (x^7 - x)
    # = (x^27 + x^21 + x^15 + x^9 +x^3) •••••• (x^4 + 4x^3 + 3x^2 - 2x)
    >>> from jsntlib import polydiv
    >>> polydiv([1, 3, 2, 34], [-2, 4, 3, 1], [7,  1], [1, -1])
    ([27, 21, 15, 9, 3], [1, 1, 1, 1, 1], [4, 3, 2, 1], [1, 4, 3, -2])
    ```



   * `simplify(cgcExp, cgcCoe, modulo)`

     Returns `tuple` type containing the lists of exponents and coefficients of result congruence after **congruence simplification**.

     ```python
     #   (3x^14 + 4x^13 + 2x^11 + x^9 + x^6 + x^3 + 12x^2 + x) mod 5
     # ≡ (3x^3 + 16x^2 + 6x) mod 5
     >>> from jsntlib import simplify
     >>> simplify([14, 13, 11,  9,  6,  3,  2,  1], [ 3,  4,  2,  1,  1,  1, 12,  1], 5)
     ([3, 2, 1], [3, 16, 6])
     ```



  * `crt((mod, [x1, x2, …]), …)`

    Returns `list` type containing all solutions of a **naïve congruence set**.

    ```python
    # x = ±1 (mod 3); x = ±1 (mod 5); x = ±2 (mod 7)
    >>> from jsntlib import crt
    >>> crt(3, [1,-1]), (5, [1,-1]), (7, [2,-2])
    [16, 19, 26, 44, 61, 79, 86, 89]
    ```



  * `congsolve(cgcExp, cgcCoe, modulo)`

    Returns `list` type containing all solutions of an **polynomial congruence**.

    ```python
    # x^2 - 46 ≡ 0 (mod 105)
    from jsntlib import congsolve
    >>> congsolve([2, 0], [1, -46], 105)
    [16, 19, 26, 44, 61, 79, 86, 89]
    ```



  * `quadratic(p)`

    Returns `tuple` type containing the solutions of a **quadratic polynomial**, i.e. `x^2 + y^2 = p`.

    ```python
    # x^2 + y^2 = 2017
    # x = ±9; y = ±44
    from jsntlib import quadratic
    >>> quadratic(2017)
    (9, 44)
    ```



  * `ord(m, a)`

    Returns `int` type for the **order** of an integer `a` modulo `m`, i.e. `ord_m(a)`.

    ```python
    # ord_9(a) = 6
    >>> from jsntlib import ord
    >>> ord(9, 2)
    6
    ```



  * `euler(m)`

    Returns `int` type for the **Euler function** result of an integer `m`, i.e. `φ(m)`.

    ```python
    # φ(40) = 16
    >>> from jsntlib import euler
    >>> euler(40)
    16
    ```



  * `prc(m)`

    Returns `list` type for the **primitive residue class** of an integer`m`.

    ```python
    >>> from jsntlib import prc
    >>> prc(40)
    [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]
    ```



  * `root(m)`

    Returns `list` type for **primitive roots** of modulo `m`.

    ```python
    >>> from jsntlib import root
    >>> root(25)
    [2, 3, 8, 12, 13, 17, 22, 23]
    ```



  * `legendre(a, p)`

    Returns `int` type for the result of **Legendre symbol** `(a|p)`.

    ```python
    # (3|17) = -1
    >>> from jsntlib import legendre
    >>> legendre(3, 17)
    -1
    ```



  * `jacobi(a, m)`

    Returns `int` type for the result of **Jacobi symbol** `(a|m)`.

    ```python
    # (286|563) = -1
    >>> from jsntlib import jacobi
    >>> jacobi(286, 563)
    -1
    ```



  * `carmicheal(N)`

    Returns `bool` type if an integer `N` is a **Carmicheal number**.

    ```python
    >>> from jsntlib import carmicheal
    >>> carmicheal(3499)
    False
    ```



  * `pseudo([mode='Fermat'][, byte=16][, para=10000][, flag=False])`

    Returns `int` type for a **pseudo prime number**, which is `byte` long, using `mode` test with `para` times and (for `Fermat` test) Carmicheal number check set in`flag`.

    * `mode` can be set to the followings (`Fermat` in default)
    
      * `Fermat` —— using **Fermat test** for Fermat pseudo primes
      
      * `Euler` or `Solovay-Stassen` —— using **Solovay-Stassen test** for Euler pseudo primes
      
      * `Strong` or `Miller-Rabin` —— using **Miller-Rabin test** for strong pseudo primes
      
    * `byte` is the **binary length** of expected pseudo primes (`16` in default)
    
    * `para` is the **security parameter** for repetition in tests (`10000` in default)
    
    * `flag` is to decide if **Carmicheal numbers** will be checked in Fermat test (`False` in default)

    ```python
    >>> from jsntlib import pseudo
    >>> pseudo(mode='Fermat')
    56629
    >>> pseudo(mode='Euler')
    38231
    >>> pseudo(mode='Strong')
    42451
    ```



  * `fraction(n[, d])`

    Returns `list` type representing the continued fraction form of `n|d`.

    ```python
    # 7700/2145 = [3, 1, 1, 2, 3, 1, 1]
    >>> from jsntlib import fraction
    >>> fraction(7700, 2145)
    [3, 1, 1, 2, 3, 1, 1]
    ```






### Classes



  * `Fraction`

    An extended `Fraction` class with compability to **continued fraction** derived from system built-in class `fractions.Fraction`.

    * `Fraction(numerator=0, denominator=1)`

    * `Fraction(other_fraction)`

    * `Fraction(float)`

    * `Fraction(decimal)`

    * `Fraction(string)`

      > Above are same with the constructors in `fractions.Fraction`.

    * `Fraction(continued_fraction)`

      Construction from `list` type representing a **continued fraction**.

      ```python
      >>> from jsntlib import Fraction
      >>> Fraction(16, -10)
      Fraction(-8, 5)
      >>> Fraction(123)
      Fraction(123, 1)
      >>> Fraction()
      Fraction(0, 1)
      >>> Fraction('3/7')
      Fraction(3, 7)
      >>> Fraction(' -3/7 ')
      Fraction(-3, 7)
      >>> Fraction('1.414213 \t\n')
      Fraction(1414213, 1000000)
      >>> Fraction('-.125')
      Fraction(-1, 8)
      >>> Fraction('7e-6')
      Fraction(7, 1000000)
      >>> Fraction(2.25)
      Fraction(9, 4)
      >>> Fraction(1.1)
      Fraction(2476979795053773, 2251799813685248)
      >>> from decimal import Decimal
      >>> Fraction(Decimal('1.1'))
      Fraction(11, 10)
      >>> Fraction([-1, 1, 1, 3])
      Fraction(-3, 7)
      ```



    * `numerator`

      Numerator of the Fraction in lowest term.

    * `denominator`

      Denominator of the Fraction in lowest term.

    * `fraction`

      Continued fraction of the Fraction in `list` type.

    * `convergent`

      Convergents of the Fraction in `list` type, with elements (i.e. convergents) in `fractions.Fraction` type.

    * `number`

      Original fraction number of the Fraction in `fractions.Fraction`.



    * `__getitem__(level)`

      Returns the `level` of the Fraction in `convergent`. When `level` is overflowed, return `number` of the Fraction instead.

      ```python
      # -3/7 --> [-1, 0, -1/2, -3/7]
      >>> Fraction(-3, 7)[2]
      Fraction(-1, 2)
      ```

    * `__floor__()`

      Returns the greatest integer ` <= self`. This method can also be accessed through the `math.floor()` function:

      ```python
      >>> from math import floor
      >>> floor(Fraction(355, 113))
      3
      ```

    * `__ceil__()`

      Returns the least integer ` <= self`.  This method can also be accessed through the `math.ceil()` function.

    * `__round__()`

    * `__round__(ndigits)`

      The first version returns the nearest integer to `self`, rounding half to even. The second version rounds `self` to the nearest multiple of `Fraction(1, 10**ndigits^)` (logically, if `ndigits` is negative), again rounding half toward even. This method can also be accessed through the `round()` function.






  * `Index`

    The `Index` class provides support for integer **modulo index**.

    * `Index(int)`

      ```python
      >>> from jsntlib import Index
      >>> Index(41)
      Index(41)
      ```



    * `modulo`

      Modulo of the Index.

    * `root`

      Primitive root of the Index.

    * `phi`

      Euler function of modulo in the Index.

    * `index`

      Indexes to modulo of the Index in `list` type.

    * `table`

      Formatted table of indexes to modulo in the Index in `list` type.



    * `__call__([a, b, …])`

      Returns the product of multiplication with integers a, b, … after modulo of the Index. When omitted, returns `None`.

      ```python
      # 105 * 276 ≡ 34 (mod 41)
      >>> Index(41)(105, 276)
      34
      ```






  * `Legendre`

    The `Legendre` class implements **Legendre symbol**.

    * `Legendre(int, int)`

    * `Legendre(other_legendre)`

    * `Legendre(string)`

      ```python
      >>> from jsntlib import Legendre
      >>> Legendre(2, 3)
      Legendre(2, 3)
      >>> Legendre('4|7')
      Legendre(4, 7)
      >>> Legendre(' -4|7 ')
      Legendre(-4, 7)
      >>> Legendre('47|11 \t\n')
      Legendre(47, 11)
      >>> Legendre(' 8/23 ')
      Legendre(8, 23)
      >>> Legendre('-8/23')
      Legendre(-8, 23)
      ```



    * `numerator`

      Numerator of the Legendre symbol in lowest term.

    * `denominator`

      Denominator of the Legendre symbol.

    * `nickname`

      Returns `'Legendre'`.



    * `__call__()`

    * `eval()`

      Returns final result of the Legendre symbol, which equals to 1, -1 or 0.

    * `simplify()`

      Returns simplication of the Legendre symbol in lowest term, in which numerator equals to 0, ±1, or ±2 and denominator is prime.

    * `reciprocate()`

      Returns reciprocation of the Legendre symbol.

      ```python
      >>> Legendre(47, 5)()
      -1
      >>> Legendre(47, 5).eval()
      -1
      >>> Legendre(47, 5).simplify()
      Legendre(47, 5)
      >>> Legendre(47, 5).reciprocate()
      Legendre(42, 47)
      ```

    * `convert([kind])`

      Converts the Legendre symbol to another kind. When given `'Jacobi'`, returns Jacobi symbol with same numerator and denominator. When omitted or given `'Legendre'`, returns itself.

      ```python
      >>> Legendre(47, 5).convert()
      Legendre(47, 5)
      >>> Legendre(47, 5).convert('Legendre')
      Legendre(47, 5)
      >>> Legendre(47, 5).convert('Jacobi')
      Jacobi(47, 5)
      ```






  * `Jacobi`

    The `Jacobi` class implements **Jacobi symbol**.

    * `Jacobi(int, int)`

    * `Jacobi(other_jacobi)`

    * `Jacobi(string)`

      ```python
      >>> from jsntlib import Jacobi
      >>> Jacobi(2, 3)
      Jacobi(2, 3)
      >>> Jacobi('4|9')
      Jacobi(4, 9)
      >>> Jacobi(' -4|9 ')
      Jacobi(-4, 9)
      >>> Jacobi('47|18 \t\n')
      Jacobi(47, 18)
      >>> Jacobi(' 8/26 ')
      Jacobi(8, 26)
      >>> Jacobi('-8/26')
      Jacobi(-8, 26)
      ```



    * `numerator`

      Numerator of the Jacobie symbol in lowest term.

    * `denominator`

      Denominator of the Jacobi symbol.

    * `nickname`

      Returns `'Jacobi'`.



    * `__call__()`

    * `eval()`

      Returns final result of the Jacobi symbol, which equals to 1 or -1.

    * `simplify()`

      Returns simplication of the Jacobi symbol in lowest term, in which numerator equals to 0, ±1, or ±2 and denominator is prime.

    * `reciprocate()`

      Returns reciprocation of the Jacobi symbol.

      ```python
      >>> Jacobi(47, 6)()
      1
      >>> Jacobi(47, 6).eval()
      1
      >>> Jacobi(47, 6).simplify()
      Jacobi(1, 5)
      >>> Jacobi(47, 6).reciprocate()
      Jacobi(41, 47)
      ```

    * `convert([kind])`

      Converts the Jacobi symbol to another kind. When given `'Legendre'`, returns Legendre symbol with same numerator and denominator (if the latter is prime). When omitted or given `'Jacobi'`, returns itself.

      ```python
      >>> Jacobi(47, 6).convert()
      Jacobi(47, 6)
      >>> Jacobi(47, 6).convert('Jacobi')
      Jacobi(47, 6)
      >>> Jacobi(47, 5).convert('Legendre')
      Legendre(47, 5)
      ```






  * `Polynomial`

    A fully-functional **Polynomial** class with support for complex coefficients.

    * `Polynomial(dfvar='x')`

    * `default([var])`

      Default variable (used for common-number items) can be set when an instance is created. Also, it can be modified through `default([var])` later.


    * `Polynomial(number)`

      As long as `number` is an instance of a class derived `numbers.Number`.

    * `Polynomial(string)`

      > Default format of polynomial items:
      >
      > (+\\-) coeficient (\*) variable (^\\\*\*) exponent

    * `Polynomial(tuple_0, [tuple_1, …])`

      > Default format of polynomial item tuples:
      >
      > ( ' variable ' , ( exponent, coefficient ), … )

    * `Polynomial(dict)`

      > Default format of polynomial 'vec' dictionary:
      >
      > { ' variable ' : { exponent : coefficient, … } , … }

    * `Polynomial(other_polynomial)`

        ```python
        >>> from jsntlib import Polynomial
        >>> Polynomial(4.67, dfvar='var')
        Polynomial(var)
        >>> Polynomial(4+5j)
        Polynomial(x)
        >>> Polynomial(' a^34 + 4a^3+x + y^2 /t/n')
        Polynomial(a, x, y)
        >>> Polynomial(((1,0), (4,-4), (2,3), (0,1)))
        Polynomial(x)
        >>> Polynomial(('x', (1,1)), ('y', (1, 0), (2, 1)))
        Polynomial(x, y)
        >>> Polynomial({'y': {2: 1}, 'x': {1: 1}})
        Polynomial(x, y)
        ```



    * `iscomplex`

      If coefficients of the Polynomial are in **complex** field.

    * `isinteger`

      If coefficients of the Polynomial are in **integer** field.

    * `ismultivar`

      If there are multiple variables in the Polynomial.

    * `var`

      Name of variables in the Polynomial within `list` type.

    * `vector`

      Corespondence of variables, exponents and coefficeints in the Polynomial within `dict` type.

    * `dfvar`

      Default name of variables in the Polynomial.

    * `nickname`

      Returns `poly`.



    * `eval(dict)`

      > Default format for `dict` definition:
      >
      > { ' variable ' : value, … }

    * `eval(number)`

    * `eval(tuple_0[, tuple_1, …])`

      > Default format for `tuple` definition:
      >
      > ( ' variable ', value ), …

      Evaluate the Polynomial with the given values.

      ```python
      >>> Polynomial({'y': {2: 1}, 'x': {1: 1}}).eval({'y': 2, 'x': 3})
      7
      >>> Polynomial(((1,0), (4,-4), (2,3), (0,1))).eval(5)
      -2424
      >>> Polynomial(('x', (1,1)), ('y', (1, 0), (2, 1))).eval(('x', 2), ('y', 3))
      11
      ```

    * `mod(dict, mod=None)`

    * `mod(number, mod=None)`

    * `mod(tuple_0[, tuple_1, …], mod=None)`

      Evaluate the Polynomial with the given values after modulo. If `mod` omits or sets to None, returns `eval()`.

      ```python
      >>> Polynomial({'y': {2: 1}, 'x': {1: 1}}).mod({'y': 2, 'x': 3}, mod=3)
      1
      >>> Polynomial(((1,0), (4,-4), (2,3), (0,1))).mod(5, mod=75)
      51
      >>> Polynomial(('x', (1,1)), ('y', (1, 0), (2, 1))).mod(('x', 2), ('y', 3), mod=5)
      1
      ```



    * `__reduce__()`

    * `__copy__()`

    * `__deepcopy__()`

      Support for pickling, copy, and deepcopy.




    * Rich comparison is implemented.

    * Algebra calculation is implemented.

    * Slice and get, set, delete are also implemented.

      ```python
      >>> Polynomial(((7,1), (1,-1))) < Polynomial(((6,1), (3,4), (2,2)))
      False
      >>> Polynomial(((1,0), (4,-4), (2,3), (0,1))) / Polynomial(((2,-1), (0,1)))
      4x^2 + 1
      >>> Polynomial(('a', (1,3), (3,4), (2,2), (34,complex(1,3))))[1:3]
      2a^2 + 3a
      ```






  * `Congruence`

    The `Congruence` class, derived from `Polynomial` class, implements solution for mono-variable congruence in integer field.

    * `Congruence(dfvar='x')`

    * `default([var])`
    
    

    * `Congruence(number)`

      As long as `number` is an instance of a class derived `numbers.Number`.

    * `Congruence(string)`

    * `Congruence(tuple_0, [tuple_1, …])`

    * `Congruence(dict)`

    * `Congruence(other_congruence)`

        ```python
        >>> from jsntlib import Congruence
        >>> Congruence(4.67, mod=7, dfvar='var')
        Congruence(var, mod=7)
        >>> Congruence(4+5j, mod=9)
        Congruence(x, mod=9)
        >>> Congruence(' a^34 + 4a^3+x + y^2 /t/n', mod=87)
        Congruence(a, x, y, mod=87)
        >>> Congruence(((1,0), (4,-4), (2,3), (0,1)), mod=3)
        Congruence(x, mod=3)
        >>> Congruence(('x', (1,1)), ('y', (1, 0), (2, 1)), mod=67)
        Congruence(x, y, mod=67)
        >>> Congruence({'y': {2: 1}, 'x': {1: 1}}, mod=90)
        Congruence(x, y, mod=90)
        ```



    * `iscomplex`

      If coefficients of the Congruence are in **complex** field.

    * `isinteger`

      If coefficients of the Congruence are in **integer** field.

    * `ismultivar`

      If there are multiple variables in the Congruence.

    * `isprime`

      If `modulo` is prime.

    * `var`

      Name of variables in the Congruence within `list` type.

    * `vector`

      Corespondence of variables, exponents and coefficeints in the Congruence within `dict` type.

    * `dfvar`

      Default name of variables in the Congruence.

    * `modulo`

      Modulo of the Congruence.

    * `solution`

      Solution of the Congruence.

    * `nickname`

      Returns `cong`.



    * `simplify()`

      Returns the Congruence after simplification.

    * `solve()`

      Returns the `Solution` of the Congruence.

      > The `Solution` class implements solutions for the `Congruence` class.
      >
      > * `variables` : Name of variables in the Solution within `list` type.
      > * `modulo` : Modulo of the Solution.
      > * `solutions` : Ascending solutions of the Solution in `list` type.
      >
      > The Solution is callable which returns `solutions` within. Length (`len()` method) of the Solutions returns number of `solutions`. Slice and item can also be accessed with subscripts.

      ```python
      >>> Congruence(('z', (2014,2014), (8,8)), mod=7).simplify()
      2014z^4 + 8z^2 ≡ 0 (mod 7)
      >>> Congruence(('z', (2,1), (0,-46)), mod=105).solve()
      z ≡ 16, 19, 26, 44, 61, 79, 86, 89 (mod 105)
      ```



    * `eval(dict)`

    * `eval(number)`

    * `eval(tuple_0[, tuple_1, …])`

      Evaluate the Congruence with the given values.

      ```python
      >>> Congruence({'y': {2: 1}, 'x': {1: 1}}, mod=3).eval({'y': 2, 'x': 3})
      1
      >>> Congruence(((1,0), (4,-4), (2,3), (0,1)), mod=75).eval(5)
      51
      >>> Congruence(('x', (1,1)), ('y', (1, 0), (2, 1)), mod=5).eval(('x', 2), ('y', 3))
      1
      ```

    * `calc(dict)`

    * `calc(number)`

    * `calc(tuple_0[, tuple_1, …])`

      Evaluate the Congruence with the given values but without modulo.

      ```python
      >>> Congruence({'y': {2: 1}, 'x': {1: 1}}, mod=3).calc({'y': 2, 'x': 3})
      7
      >>> Congruence(((1,0), (4,-4), (2,3), (0,1)), mod=75).calc(5)
      -2424
      >>> Congruence(('x', (1,1)), ('y', (1, 0), (2, 1)), mod=5).calc(('x', 2), ('y', 3))
      11
      ```



    * `__reduce__()`

    * `__copy__()`

    * `__deepcopy__()`

      Support for pickling, copy, and deepcopy.






  * `Quadratic`

    The `Quadratic` class, derived from `Polynomial` class, implements solution for quadratic polynomials.

    * `Quadratic(number)`

    * `Quadratic(string)`

    * `Quadratic(tuple_0, [tuple_1, …])`

    * `Quadraticl(dict)`

    * `Quadratic(other_quadratic)`

        ```python
        >>> from jsntlib import Quadratic
        >>> Quadratic(4)
        Quadratic(x, y)
        >>> Quadratic(4, vars=('a', 'b'))
        Quadratic(a, b)
        >>> Quadratic(' p^2 +q^2- 9 /t/n')
        Quadratic(p, q)
        >>> Quadratic(('m', (2, 1)), ('n', (2, 1)))
        Quadratic(m, n)
        >>> Quadratic({'j': {2: 1}, 'k': {2: 1}})
        Quadratic(j, k)
        ```



    * `var`

      Name of variables in the Polynomial within `list` type.

    * `constant`

      Constant item in the Quadratic.

    * `isprime`

      If the `constant` is prime.

    * `solution`

      Solution of the Quadratic.

    * `nickname`

      Returns `quad`.



    * `solve()`

      Returns the `Solution` of the Quadratic.

      > The `Solution` class implements solutions for the `Quadratic` class.
      >
      > * `variables` : Name of variables in the Solution within `list` type.
      > * `modulo` : Modulo of the Solution.
      > * `solutions` : Ascending solutions of the Solution in `list` type.
      >
      > The Solution is callable which returns `solutions` within. Slice and item can also be accessed with subscripts.

      ```python
      >>> Quadratic(8068, vars=('p', 'q')).solve()
      p = ±9  q = ±44
      ```



    * `eval(dict)`

    * `eval(tuple_0, tuple_1)`

      Evaluate the Quadratic with the given values.

      ```python
      >>> Quadratic(4).eval({'y': 2, 'x': 3})
      13
      >>> Quadratic(4).eval(('x', 3), ('y', 2))
      13
      ```

    * `mod(dict, mod=None)`

    * `mod(tuple_0[, tuple_1, …], mod=None)`

      Evaluate the Quadratic with the given values after modulo. If `mod` omits or sets to None, returns `eval()`.

      ```python
      >>> Quadratic(4).mod({'y': 2, 'x': 3}, mod=3)
      1
      >>> Quadratic(4).mod(('x', 2), ('y', 3), mod=3)
      1
      ```
      


    * `__reduce__()`

    * `__copy__()`

    * `__deepcopy__()`

      Support for pickling, copy, and deepcopy.
