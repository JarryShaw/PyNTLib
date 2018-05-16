# JSNTLIB Manual


 > &emsp; `jsntlib` is an open sourse library for __number theory__ written in Python, with compatibility in both 2.7 and 3.6 versions. The following is a manual for this library. Usage instructions and samples attached.


 - [Functions](#functions)
    * [`prime`](#prime)
    * [`primelist`](#primelist)
    * [`isdivisible`](#isdivisible)
    * [`isprime`](#isprime)
    * [`gcd`](#gcd)
    * [`lcm`](#lcm)
    * [`coprime`](#coprime)
    * [`eealist`](#eealist)
    * [`bezout`](#bezout)
    * [`factor`](#factor)
    * [`decomposit`](#decomposit)
    * [`binary`](#binary)
    * [`modulo`](#modulo)
    * [`polydiv`](#polydiv)
    * [`simplify`](#simplify)
    * [`crt`](#crt)
    * [`congsolve`](#congsolve)
    * [`quadratic`](#quadratic)
    * [`ord`](#ord)
    * [`euler`](#euler)
    * [`prc`](#prc)
    * [`root`](#root)
    * [`legendre`](#legendre)
    * [`jacobi`](#jacobi)
    * [`carmicheal`](#carmicheal)
    * [`pseudo`](#pseudo)
    * [`fraction`](#fraction)

 - [Classes](#classes)
    * [`Fraction`](#class_fraction)
        - [Properties](#fraction_properties)
        - [Data models](#fraction_datamodels)
    * [`Index`](#class_index)
        - [Properties](#index_properties)
        - [Data models](#index_datamodels)
    * [`Legendre`](#class_legendre)
        - [Properties](#legendre_properties)
        - [Data models](#legendre_datamodels)
        - [Methods](#legendre_methods)
    * [`Jacobi`](#class_jacobi)
        - [Properties](#jacobi_properties)
        - [Data models](#jacobi_datamodels)
        - [Methods](#jacobi_methods)
    * [`Polynomial`](#class_polynomial)
        - [Properties](#polynomial_properties)
        - [Methods](#polynomial_methods)
        - [Data models](#polynomial_datamodels)
        - [Notes](#polynomial_notes)
    * [`Congruence`](#class_congruence)
        - [Properties](#congruence_properties)
        - [Methods](#congruence_methods)
        - [Data models](#congruence_datamodels)
    * [`Quadratic`](#class_quadratic)
        - [Properties](#quadratic_properties)
        - [Methods](#quadratic_methods)
        - [Data models](#quadratic_datamodels)


---


```python
# some preparations :)
>>> from jsntlib import *
```


&nbsp;


<a name="function"> </a>

### Functions

<a name="prime"> </a>

 * `prime(stop)`
 * `prime(start, end[, step])`

    &emsp; Returns an `iterator` type generating prime numbers in an array range with `start`, `end` and `step`.

    ```python
    >>> prime(17, 89)
    <generator object primerange at 0x10fef7fc0>
    ```

&nbsp;

<a name="primelist"> </a>

 * `primelist(upper[, lower])`

    &emsp; Returns `list` type containing **prime numbers** within integer `upper` and `lower` bound, if `lower` is given. When `lower` is omitted, all prime numbers **less than** (bound excluded) the `upper` bound.

    ```python
    >>> primelist(17, 89)
    [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
    ```

&nbsp;

<a name="isdivisible"> </a>

 * `isdivisible(a, b)`

    &emsp; Returns `bool` type if integers `a` and `b` are **divisible**, i.o.w. whether $b \mid a$ or $b \nmid a$, when `b` is greater than `a`, and in other cases, vice versa.

    ```python
    >>> isdivisible(983, 234)
    False
    ```

&nbsp;

<a name="isprime"> </a>

 * `isprime(N)`

    &emsp; Returns `bool` type if integer `N` is a **prime number**.

    ```python
    >>> isprime(8563)
    True
    ```

&nbsp;

<a name="gcd"> </a>

 * `gcd(a, b)`

    &emsp; Returns `int` type of the **greatest common divisor** between integers `a` and `b`.

    ```python
    >>> gcd(657, 292)
    73
    ```

&nbsp;

<a name="lcm"> </a>

 * `lcm(a, b)`

    &emsp; Returns `int` type of the **least common multiplier** between integers `a` and `b`.

    ```python
    >>> lcm(146, 28)
    2044
    ```

&nbsp;

<a name="coprime"> </a>

 * `coprime(a, b)`

    &emsp; Returns `bool` type if integers `a` and `b` are **coprime**, i.e. which greatest common divisor is $one$.

    ```python
    >>> coprime(352, 76)
    False
    ```

&nbsp;

<a name="eealist"> </a>

 * `eealist(a, b)`

    &emsp; Returns `list` type containing quotients for integers $a \div b$ with **extended Euclidean Algorithm**.

    ```python
    >>> eealist(23, 984)
    [0, 42, 1, 3, 1, 1]
    ```

&nbsp;

<a name="bezout"> </a>

 * `bezout(a, b)`

    &emsp; Returns `tuple` type containing parameters for **Bézout equition** of integers `a` and `b`.

    ```python
    # -20*-367 + -41*179 = (-367, 179)
    >>> bezout(-367, 179)
    (-20, -41)
    ```

&nbsp;

<a name="factor"> </a>

 * `factor(N[, wrap=False])`

    &emsp; Returns `list` type containing **prime factors** of integers `N`, if keyword `wrap` is `False` or omitted. Once set `True`, `tuple` type of two lists will be offered, which implies the factors and their exponents.

    ```python
    # 72 = 2 * 2 * 2 * 3 * 3
    >>> factor(72)
    [2, 2, 2, 3, 3]
    # -72 = -1 * 2^3 * 3^2
    >>> factor(-72, wrap=True)
    ([-1, 2, 3], [1, 3, 2])
    ```

&nbsp;

<a name="decomposit"> </a>

 * `decomposit(N)`

    &emsp; Returns `tuple` type containing two(2) integers, which are the **decoposition** results of coposit number `N`, i.e. `(a, b)` where $N \mid a^2-b^2$ but $N \nmid a+b$ nor $N \nmid a-b$.

    ```python
    # 1508^2 - 608^2 = 345 * 5520   // 345 | 1508^2 - 608^2
    # 1508 + 608 = 345 * 6 + 46     // 345 ∤ 1508 + 608
    # 1508 - 608 = 345 * 2 + 210    // 345 ∤ 1508 - 608
    >>> decomposit(345)
    (1508, 608)
    ```

&nbsp;

<a name="binary"> </a>

 * `binary(a, b, c)`

    &emsp; Returns `tuple` type containing special solutions for an **indefinite binary equation**, i.e. $ax + by = c$.

    ```python
    # 7*x + b*24 = -3
    #   x = 6 + 24*t (t∈Z)
    #   y = -21 - 7*t (t∈Z)
    >>> binary(7,24,-3)
    (6, -21)
    ```

&nbsp;

<a name="modulo"> </a>

 * `modulo(b, e, m)`

    &emsp; Returns `int` type for the result of $b^e \mod m$.

    ```python
    # -765^264 = -291 (mod 597)
    >>> modulo(-765, 264, 597)
    -291
    ```

&nbsp;

<a name="polydiv"> </a>

 * `polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe)`

    &emsp; Returns `tuple` type containing the lists of exponents and coefficients of **quotient** and **remainder** polynomials, which are the **division** results of **dividend** and **divisor** polynomials.

    ```python
    # (x^34 + 4x^3 + 3x^2 - 2x) = (x^27 + x^21 + x^15 + x^9 +x^3)(x^7 - x) + (x^4 + 4x^3 + 3x^2 - 2x)
    >>> polydiv([1, 3, 2, 34], [-2, 4, 3, 1], [7,  1], [1, -1])
    ([27, 21, 15, 9, 3], [1, 1, 1, 1, 1], [4, 3, 2, 1], [1, 4, 3, -2])
    ```

&nbsp;

<a name="simplify"> </a>

 * `simplify(cgcExp, cgcCoe, modulo)`

     &emsp; Returns `tuple` type containing the lists of exponents and coefficients of result congruence after **congruence simplification**.

     ```python
     # 3x^14 + 4x^13 + 2x^11 + x^9 + x^6 + x^3 + 12x^2 + x ≡ 3x^3 + 16x^2 + 6x (mod 5)
     >>> simplify([14, 13, 11,  9,  6,  3,  2,  1], [ 3,  4,  2,  1,  1,  1, 12,  1], 5)
     ([3, 2, 1], [3, 16, 6])
     ```

&nbsp;

<a name="crt"> </a>

 * `crt((mod, [x1, x2, …]), …)`

    &emsp; Returns `list` type containing all solutions of a **naïve congruence set**.

    ```python
    # x = ±1 (mod 3)
    # x = ±1 (mod 5)
    # x = ±2 (mod 7)
    #   x = 16, 19, 26, 44, 61, 79, 86, 89
    >>> crt(3, [1,-1]), (5, [1,-1]), (7, [2,-2])
    [16, 19, 26, 44, 61, 79, 86, 89]
    ```

&nbsp;

<a name="congsolve"> </a>

 * `congsolve(cgcExp, cgcCoe, modulo)`

    &emsp; Returns `list` type containing all solutions of an **polynomial congruence**.

    ```python
    # x^2 - 46 ≡ 0 (mod 105)
    #   x = 16, 19, 26, 44, 61, 79, 86, 89
    >>> congsolve([2, 0], [1, -46], 105)
    [16, 19, 26, 44, 61, 79, 86, 89]
    ```

&nbsp;

<a name="quadratic"> </a>

 * `quadratic(p)`

    &emsp; Returns `tuple` type containing the solutions of a **quadratic polynomial**, i.e. $x^2 + y^2 = p$.

    ```python
    # x^2 + y^2 = 2017
    #   x = ±9
    #   y = ±44
    >>> quadratic(2017)
    (9, 44)
    ```

&nbsp;

<a name="ord"> </a>

 * `ord(m, a)`

    &emsp; Returns `int` type for the **order** of an integer `a` modulo `m`, i.e. $ord_m(a)$.

    ```python
    # ord_9(a) = 6
    >>> ord(9, 2)
    6
    ```

&nbsp;

<a name="euler"> </a>

 * `euler(m)`

    &emsp; Returns `int` type for the **Euler function** result of an integer `m`, i.e. $\varphi (m)$.

    ```python
    # φ(40) = 16
    >>> euler(40)
    16
    ```

&nbsp;

<a name="prc"> </a>

 * `prc(m)`

    &emsp; Returns `list` type for the **primitive residue class** of an integer`m`.

    ```python
    >>> prc(40)
    [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]
    ```

&nbsp;

<a name="root"> </a>

 * `root(m)`

    &emsp; Returns `list` type for **primitive roots** of modulo `m`.

    ```python
    >>> root(25)
    [2, 3, 8, 12, 13, 17, 22, 23]
    ```

&emsp;

<a name="legendre"> </a>

 * `legendre(a, p)`

    &emsp; Returns `int` type for the result of **Legendre symbol** $\left(\dfrac{a}{p}\right)$.

    ```python
    # (3|17) = -1
    >>> legendre(3, 17)
    -1
    ```

&nbsp;

<a name="jacobi"> </a>

 * `jacobi(a, m)`

    &emsp; Returns `int` type for the result of **Jacobi symbol** $\left(\dfrac{a}{m}\right)$.

    ```python
    # (286|563) = -1
    >>> jacobi(286, 563)
    -1
    ```

&nbsp;

<a name="carmicheal"> </a>

 * `carmicheal(N)`

    &emsp; Returns `bool` type if an integer `N` is a **Carmicheal number**.

    ```python
    >>> carmicheal(3499)
    False
    ```

&nbsp;

<a name="pseudo"> </a>

 * `pseudo([mode='Fermat'][, byte=16][, para=10000][, flag=False])`

    &emsp; Returns `int` type for a **pseudo prime number**, which is `byte` long, using `mode` test with `para` times and (for `Fermat` test) Carmicheal number check set in`flag`.

    - `mode` can be set to the followings (`Fermat` in default)

        * `Fermat` —— using **Fermat test** for Fermat pseudo primes

        * `Euler` or `Solovay-Stassen` —— using **Solovay-Stassen test** for Euler pseudo primes

        * `Strong` or `Miller-Rabin` —— using **Miller-Rabin test** for strong pseudo primes

    - `byte` is the **binary length** of expected pseudo primes (`16` in default)

    - `para` is the **security parameter** for repetition in tests (`10000` in default)

    - `flag` is to decide if **Carmicheal numbers** will be checked in Fermat test (`False` in default)

    ```python
    >>> pseudo(mode='Fermat')
    56629
    >>> pseudo(mode='Euler')
    38231
    >>> pseudo(mode='Strong')
    42451
    ```

&nbsp;

<a name="fraction"> </a>

 * `fraction(n[, d])`

    &emsp; Returns `list` type representing the **continued fraction** form of $\frac a d$.

    ```python
    # 7700/2145 = [3, 1, 1, 2, 3, 1, 1]
    >>> fraction(7700, 2145)
    [3, 1, 1, 2, 3, 1, 1]
    ```

&nbsp;

<a name="classes"> </a>

### Classes

<a name="class_fraction"> </a>

 * `Fraction`

    &emsp; An extended `Fraction` class with compability to **continued fraction** derived from system built-in class `fractions.Fraction`.

    - `Fraction(numerator=0, denominator=1)`

    - `Fraction(other_fraction)`

    - `Fraction(float)`

    - `Fraction(decimal)`

    - `Fraction(string)`

      > Above are same with the constructors in `fractions.Fraction`.

    - `Fraction(continued_fraction)`

        &emsp; Construction from `list` type representing a **continued fraction**.

        ```python
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

    <a name="fraction_properties"> </a>

    - Properties

        * `numerator`

          &emsp; Numerator of the Fraction in lowest term.

        * `denominator`

          &emsp; Denominator of the Fraction in lowest term.

        * `fraction`

          &emsp; Continued fraction of the Fraction in `list` type.

        * `convergent`

          &emsp; Convergents of the Fraction in `list` type, with elements (i.e. convergents) in `fractions.Fraction` type.

        * `number`

          &emsp; Original fraction number of the Fraction in `fractions.Fraction`.

    <a name="fraction_datamodels"> </a>

    - Data models

        * `__getitem__(level)`

            &emsp; Returns the `level` of the Fraction in `convergent`. When `level` is overflowed, return `number` of the Fraction instead.

            ```python
            # -3/7 --> [-1, 0, -1/2, -3/7]
            >>> Fraction(-3, 7)[2]
            Fraction(-1, 2)
            ```

        * `__floor__()`

            &emsp; Returns the greatest integer ` <= self`. This method can also be accessed through the `math.floor()` function:

            ```python
            >>> from math import floor
            >>> floor(Fraction(355, 113))
            3
            ```

        * `__ceil__()`

            &emsp; Returns the least integer ` <= self`.  This method can also be accessed through the `math.ceil()` function.

        * `__round__()`

        * `__round__(ndigits)`

            &emsp; The first version returns the nearest integer to `self`, rounding half to even. The second version rounds `self` to the nearest multiple of `Fraction(1, 10**ndigits)` (logically, if `ndigits` is negative), again rounding half toward even. This method can also be accessed through the `round()` function.

&nbsp;

<a name="class_index"> </a>

 * `Index`

    &emsp; The `Index` class provides support for integer **modulo index**.

    - `Index(int)`

        ```python
        >>> Index(41)
        Index(41)
        ```

    <a name="index_properties"> </a>

    - Properties

        * `modulo`

            &emsp; Modulo of the Index.

        * `root`

            &emsp; Primitive root of the Index.

        * `phi`

            &emsp; Euler function of modulo in the Index.

        * `index`

            &emsp; Indexes to modulo of the Index in `list` type.

        * `table`

            &emsp; Formatted table of indexes to modulo in the Index in `list` type.

    <a name="index_datamodels"> </a>

    - Data models

        * `__call__([a, b, …])`

            &emsp; Returns the product of multiplication with integers `a, b, ...` after modulo of the Index. When omitted, returns `None`.

            ```python
            # 105 * 276 ≡ 34 (mod 41)
            >>> Index(41)(105, 276)
            34
            ```

&nbsp;

<a name="class_legendre"> </a>

 * `Legendre`

    &emsp; The `Legendre` class implements **Legendre symbol**.

    - `Legendre(int, int)`

    - `Legendre(other_legendre)`

    - `Legendre(string)`

        ```python
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

    <a name="legendre_properties"> </a>

    - Properties

        * `numerator`

            &emsp; Numerator of the Legendre symbol in lowest term.

        * `denominator`

          &emsp; Denominator of the Legendre symbol.

        * `nickname`

          &emsp; Returns `'Legendre'`.

    <a name="legendre_datamodels"> </a>

    - Data models

        * `__call__()`

            &emsp; Returns final result of the Legendre symbol, which equals to $1$, $-1$ or $0$.

    <a name="legendre_methods"> </a>

    - Methods

        * `eval()`

            &emsp; Returns final result of the Legendre symbol, which equals to $1$, $-1$ or $0$.

        * `simplify()`

            &emsp; Returns simplication of the Legendre symbol in lowest term, in which numerator equals to $0$, $\pm 1$, or $\pm 2$ and denominator is prime.

        * `reciprocate()`

            &emsp; Returns reciprocation of the Legendre symbol.

            ```python
            >>> l = Legendre(47, 5)
            >>> l()
            -1
            >>> l.eval()
            -1
            >>> l.simplify()
            Legendre(2, 5)
            >>> l.reciprocate()
            Legendre(42, 47)
            ```

        * `convert([kind])`

            &emsp; Converts the Legendre symbol to another kind. When given `'Jacobi'`, returns Jacobi symbol with same numerator and denominator. When omitted or given `'Legendre'`, returns itself.

        ```python
        >>> l.convert()
        Legendre(47, 5)
        >>> l.convert('Legendre')
        Legendre(47, 5)
        >>> l.convert('Jacobi')
        Jacobi(47, 5)
        ```

&nbsp;

<a name="class_jacobi"> </a>

 * `Jacobi`

    &emsp; The `Jacobi` class implements **Jacobi symbol**.

    - `Jacobi(int, int)`

    - `Jacobi(other_jacobi)`

    - `Jacobi(string)`

        ```python
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

    <a name="jacobi_properties"> </a>

    - Properties

        * `numerator`

            &emsp; Numerator of the Jacobie symbol in lowest term.

        * `denominator`

            &emsp; Denominator of the Jacobi symbol.

        * `nickname`

            &emsp; Returns `'Jacobi'`.

    <a name="jacobi_datamodels"> </a>

    - Data models

        * `__call__()`

            &emsp; Returns final result of the Jacobi symbol, which equals to $1$ or $-1$.

    <a name="jacobi_methods"> </a>

    - Methods

        * `eval()`

            &emsp; Returns final result of the Jacobi symbol, which equals to $1$ or $-1$.

        * `simplify()`

            &emsp; Returns simplication of the Jacobi symbol in lowest term, in which numerator equals to $0$, $\pm 1$, or $\pm 2$ and denominator is prime.

        * `reciprocate()`

            &emsp; Returns reciprocation of the Jacobi symbol.

            ```python
            >>> j = Jacobi(47, 6)
            >>> j()
            1
            >>> j.eval()
            1
            >>> j.simplify()
            Jacobi(1, 5)
            >>> j.reciprocate()
            Jacobi(41, 47)
            ```

        * `convert([kind])`

            &emsp; Converts the Jacobi symbol to another kind. When given `'Legendre'`, returns Legendre symbol with same numerator and denominator (if the latter is prime). When omitted or given `'Jacobi'`, returns itself.

            ```python
            >>> j.convert()
            Jacobi(47, 6)
            >>> j.convert('Jacobi')
            Jacobi(47, 6)
            >>> j.convert('Legendre')
            Legendre(47, 5)
            ```

&nbsp;

<a name="class_polynomial"> </a>

 * `Polynomial`

    &emsp; A fully-functioned **Polynomial** class with support for complex coefficients.

    - `Polynomial(dfvar='x')`

        * `default([var])`

            &emsp; Default variable (used for common-number items) can be set when an instance is created. Also, it can be modified through `default([var])` later.

    - `Polynomial(number)`

        &emsp; As long as `number` is an instance of a class derived `numbers.Number`.

    - `Polynomial(string)`

      > Default format of polynomial items:
      >
      > &emsp; $\pm \ coeficient \ (\ast) \ variable \ (\hat{} \mid \ast \ast ) \ exponent$

    - `Polynomial(tuple_0, [tuple_1, …])`

      > Default format of polynomial item tuples:
      >
      > &emsp; $( 'variable',\ (exponent,\ coefficient),\ \dots )$

    - `Polynomial(dict)`

      > Default format of polynomial "vec" dictionary:
      >
      > &emsp; $\{ 'variable':\ \{exponent:\ coefficient,\ \dots \},\ \dots \}$

    - `Polynomial(other_polynomial)`

        ```python
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

    <a name="polynomial_properties"> </a>

    - Properties

        * `iscomplex`

            &emsp; If coefficients of the Polynomial are in **complex** field.

        * `isinteger`

            &emsp; If coefficients of the Polynomial are in **integer** field.

        * `ismultivar`

            &emsp; If there are multiple variables in the Polynomial.

        * `var`

            &emsp; Name of variables in the Polynomial within `list` type.

        * `vector`

            &emsp; Corespondence of variables, exponents and coefficeints in the Polynomial within `dict` type.

        * `dfvar`

            &emsp; Default name of variables in the Polynomial.

        * `nickname`

            &emsp; Returns `poly`.

    <a name="polynomial_methods"> </a>

    - Methods

        * `eval(dict)`

            > Default format for `dict` definition:
            >
            > &emsp; $\{ 'variable':\ value,\ \dots \}$

        * `eval(number)`

        * `eval(tuple_0[, tuple_1, …])`

            > Default format for `tuple` definition:
            >
            > &emsp; $( 'variable',\ value ),\ \dots$

            &emsp; Evaluate the Polynomial with the given values.

            ```python
            >>> p1 = Polynomial({'y': {2: 1}, 'x': {1: 1}})
            >>> p1.eval({'y': 2, 'x': 3})
            7
            >>> p2 = Polynomial(((1,0), (4,-4), (2,3), (0,1)))
            >>> p2.eval(5)
            -2424
            >>> p3 = Polynomial(('x', (1,1)), ('y', (1, 0), (2, 1)))
            >>> p3.eval(('x', 2), ('y', 3))
            11
            ```

        * `mod(dict, mod=None)`

        * `mod(number, mod=None)`

        * `mod(tuple_0[, tuple_1, …], mod=None)`

            &emsp; Evaluate the Polynomial with the given values after modulo. If `mod` omits or sets to None, returns `eval()`.

            ```python
            >>> p4 = Polynomial({'y': {2: 1}, 'x': {1: 1}})
            >>> p4.mod({'y': 2, 'x': 3}, mod=3)
            1
            >>> p5 = Polynomial(((1,0), (4,-4), (2,3), (0,1)))
            >>> p5.mod(5, mod=75)
            51
            >>> p6 = Polynomial(('x', (1,1)), ('y', (1, 0), (2, 1)))
            >>> p6.mod(('x', 2), ('y', 3), mod=5)
            1
            ```

    <a name="polynomial_datamodels"> </a>

    - Data models

        * `__reduce__()`

        * `__copy__()`

        * `__deepcopy__()`

            &emsp; Support for pickling, copy, and deepcopy.

    <a name="polynomial_notes"> </a>

    - Notes

        * Rich comparison is implemented.

        * Algebra calculation is implemented.

        * Slice and get, set, delete are also implemented.

            ```python
            >>> p7 = Polynomial(((7,1), (1,-1)))
            >>> p8 = Polynomial(((6,1), (3,4), (2,2)))
            >>> p7 < p8
            False
            >>> p9 = Polynomial(((1,0), (4,-4), (2,3), (0,1)))
            >>> p10 = Polynomial(((2,-1), (0,1)))
            >>> p9 / p10
            4x^2 + 1
            >>> p11 = Polynomial(('a', (1,3), (3,4), (2,2), (34,complex(1,3))))
            >>> p11[1:3]
            2a^2 + 3a
            ```

&nbsp;

<a name="class_congruence"> </a>

 * `Congruence`

    &emsp; The `Congruence` class, derived from `Polynomial` class, implements solution for mono-variable congruence in integer field.

    - `Congruence(dfvar='x')`

        * `default([var])`

            &emsp; Default variable (used for common-number items) can be set when an instance is created. Also, it can be modified through `default([var])` later.

    - `Congruence(number)`

        &emsp; As long as `number` is an instance of a class derived `numbers.Number`.

    - `Congruence(string)`

    - `Congruence(tuple_0, [tuple_1, …])`

    - `Congruence(dict)`

    - `Congruence(other_congruence)`

        ```python
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

    <a name="congruence_properties"> </a>

    - Properties

        * `iscomplex`

            &emsp; If coefficients of the Congruence are in **complex** field.

        * `isinteger`

            &emsp; If coefficients of the Congruence are in **integer** field.

        * `ismultivar`

            &emsp; If there are multiple variables in the Congruence.

        * `isprime`

            &emsp; If `modulo` is prime.

        * `var`

            &emsp; Name of variables in the Congruence within `list` type.

        * `vector`

            &emsp; Corespondence of variables, exponents and coefficeints in the Congruence within `dict` type.

        * `dfvar`

            &emsp; Default name of variables in the Congruence.

        * `modulo`

            &emsp; Modulo of the Congruence.

        * `solution`

            &emsp; Solution of the Congruence.

        * `nickname`

            &emsp; Returns `cong`.

    <a name="congruence_methods"> </a>

    - Methods

        * `simplify()`

            &emsp; Returns the Congruence after simplification.

        * `solve()`

            &emsp; Returns the `Solution` of the Congruence.

            > &emsp; The `Solution` class implements solutions for the `Congruence` class.
            >
            >  - `variables` —— Name of variables in the Solution within `list` type.
            >  - `modulo` —— Modulo of the Solution.
            >  - `solutions` —— Ascending solutions of the Solution in `list` type.
            >
            > The Solution is callable which returns `solutions` within. Length (`len()` method) of the Solutions returns number of `solutions`. Slice and item can also be accessed with subscripts.

            ```python
            >>> c1 = Congruence(('z', (2014,2014), (8,8)), mod=7)
            >>> c1.simplify()
            2014z^4 + 8z^2 ≡ 0 (mod 7)
            >>> c2 = Congruence(('z', (2,1), (0,-46)), mod=105)
            >>> c2.solve()
            z ≡ 16, 19, 26, 44, 61, 79, 86, 89 (mod 105)
            ```

        * `eval(dict)`

        * `eval(number)`

        * `eval(tuple_0[, tuple_1, …])`

            &emsp; Evaluate the Congruence with the given values.

            ```python
            >>> c3 = Congruence({'y': {2: 1}, 'x': {1: 1}}, mod=3)
            >>> c3.eval({'y': 2, 'x': 3})
            1
            >>> c4 = Congruence(((1,0), (4,-4), (2,3), (0,1)), mod=75)
            >>> c4.eval(5)
            51
            >>> c5 = Congruence(('x', (1,1)), ('y', (1, 0), (2, 1)), mod=5)
            >>> c5.eval(('x', 2), ('y', 3))
            1
            ```

        * `calc(dict)`

        * `calc(number)`

        * `calc(tuple_0[, tuple_1, …])`

            &emsp; Evaluate the Congruence with the given values but without modulo.

            ```python
            >>> c6 = Congruence({'y': {2: 1}, 'x': {1: 1}}, mod=3)
            >>> c6.calc({'y': 2, 'x': 3})
            7
            >>> c7 = Congruence(((1,0), (4,-4), (2,3), (0,1)), mod=75)
            >>> c7.calc(5)
            -2424
            >>> c8 = Congruence(('x', (1,1)), ('y', (1, 0), (2, 1)), mod=5)
            >>> c8.calc(('x', 2), ('y', 3))
            11
            ```

    <a name="congruence_datamodels"> </a>

    - Data models

        * `__reduce__()`

        * `__copy__()`

        * `__deepcopy__()`

            &emsp; Support for pickling, copy, and deepcopy.

&nbsp;

<a name="class_quadratic"> </a>

 * `Quadratic`

    &emsp; The `Quadratic` class, derived from `Polynomial` class, implements solution for quadratic polynomials.

    - `Quadratic(number)`

    - `Quadratic(string)`

    - `Quadratic(tuple_0, [tuple_1, …])`

    - `Quadraticl(dict)`

    - `Quadratic(other_quadratic)`

        ```python
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

    <a name="quadratic_properties"> </a>

    - Properties

        * `var`

            &emsp; Name of variables in the Polynomial within `list` type.

        * `constant`

            &emsp; Constant item in the Quadratic.

        * `isprime`

            &emsp; If the `constant` is prime.

        * `solution`

            &emsp; Solution of the Quadratic.

        * `nickname`

            &emsp; Returns `quad`.

    <a name="quadratic_methods"> </a>

    - Methods

        * `solve()`

            &emsp; Returns the `Solution` of the Quadratic.

            > &emsp; The `Solution` class implements solutions for the `Quadratic` class.
            >
            >  - `variables` —— Name of variables in the Solution within `list` type.
            >  - `modulo` —— Modulo of the Solution.
            >  - `solutions` —— Ascending solutions of the Solution in `list` type.
            >
            > The Solution is callable which returns `solutions` within. Slice and item can also be accessed with subscripts.

            ```python
            >>> Quadratic(8068, vars=('p', 'q')).solve()
            p = ±9  q = ±44
            ```

        * `eval(dict)`

        * `eval(tuple_0, tuple_1)`

            &emsp; Evaluate the Quadratic with the given values.

            ```python
            >>> q = Quadratic(4
            >>> q.eval({'y': 2, 'x': 3})
            13
            >>> q.eval(('x', 3), ('y', 2))
            13
            ```

        * `mod(dict, mod=None)`

        * `mod(tuple_0[, tuple_1, …], mod=None)`

            &emsp; Evaluate the Quadratic with the given values after modulo. If `mod` omits or sets to None, returns `eval()`.

            ```python
            >>> q.mod({'y': 2, 'x': 3}, mod=3)
            1
            >>> q.mod(('x', 2), ('y', 3), mod=3)
            1
            ```

    <a name="quadratic_datamodels"> </a>

    - Data models

        * `__reduce__()`

        * `__copy__()`

        * `__deepcopy__()`

          &emsp; Support for pickling, copy, and deepcopy.
