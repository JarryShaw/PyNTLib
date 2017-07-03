# JSNTLIB Manual



> `jsntlib` is an open sourse library for **number theory** written in Python, with compatibility in both 2.7.3 and 3.6.5 versions. The following is a manual for this library. Usage instructions and samples attached.



### Functions



*  `primelist(upper[, lower])`

  Return `list` type containing **prime numbers** within integer `upper` and `lower` bound, if `lower` is given. When `lower` is omitted, all prime numbers **less than** (bound excluded) the `upper` bound.

  ```python
  >>> primelist(17, 89)
  >>> [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
  ```





* `isdivisible(a, b)`

  Return `bool` type if integers `a` and `b` are **divisible**, i.o.w. whether `b|a` or `b∤a`, when `b` is greater than `a`, and in other cases, vice versa.

  ```python
  >>> isdivisible(983, 234)
  >>> False
  ```





* `isprime(N)`

  Return `bool` type if integer `N` is a **prime number**.

  ```python
  >>> isprime(8563)
  >>> True
  ```

  ​

* `gcd(a, b)`

  Return `int` type of the **greatest common divisor** between integers `a` and `b`.

  ```python
  >>> gcd(657, 292)
  >>> 73
  ```

  ​

* `lcm(a, b)`

  Return `int` type of the **least common multiplier** between integers `a` and `b`.

  ```python
  >>> lcm(146, 28)
  >>> 2044
  ```





* `coprime(a, b)`

  Return `bool` type if integers `a` and `b` are **coprime**, i.e. which greatest common divisor is one(1).

  ```python
  >>> coprime(352, 76)
  >>> False
  ```





* `eealist(a, b)`

  Return `list` type containing quotients for integers `a/b` with **extended Euclidean Algorithm**.

  ```python
  >>> eealist(23, 984)
  >>> [0, 42, 1, 3, 1, 1]
  ```





* `bezout(a, b)`

  Return `tuple` type containing parameters for **Bézout equition** of integers `a` and `b`.

  ```python
  >>> bezout(-367, 179)
  >>> (-20, -41)        # -20*-367 + -41*179 = (-367, 179)
  ```





* `factor(N[, wrap=False])`

  Return `list` type containing **prime factors** of integers `N`, if keyword `wrap` is `False` or omitted. Once set `True`, `tuple` type of two lists will be offered, which implies the factors and their exponents.

  ```python
  >>> factor(72)
  >>> [2, 2, 2, 3, 3]
  >>> factor(-345, wrap=True)
  >>> ([-1, 3, 5, 23], [1, 1, 1, 1])
  ```





* `decomposit(N)`

  Return `tuple` type containing two(2) integers, which are the **decoposition** results of coposit number `N`, i.e. `(a, b)` where `N|a^2-b^2` but `N∤a+b` nor `N∤a-b`.

  ```python
  >>> decomposit(345)
  >>> (1508, 608)
  ```





* `binary(a, b, c)`

  Return `tuple` type containing special solutions for an **indefinite binary equation**, i.e. `a*x + b*y = c`.

  ```python
  >>> binary(7,24,-3) # 7*x + b*24 = -3
  >>> (6, -21)        # x = 6 + 24*t; y = -21 - 7*t (t∈Z)
  ```





* `modulo(b, e, m)`

  Return `int` type for the result of `b^e (mod m)`.

  ```python
  >>> modulo(-765, 264, 597)
  >>> -291                   # -765^264 = -291 (mod 597)
  ```





* `polydiv(dvdExp, dvdCoe, dvsExp, dvsCoe)`

  Return `tuple` type containing the lists of exponents and coefficients of **quotient** and **remainder** polynomials, which are the **division** results of **dividend** and **divisor** polynomials.

  ```python
  >>> polydiv([1, 3, 2, 34], [-2, 4, 3, 1], [7,  1], [1, -1])           # (x^34 + 4x^3 + 3x^2 - 2x) ÷ (x^7 - x)
  >>> ([27, 21, 15, 9, 3], [1, 1, 1, 1, 1], [4, 3, 2, 1], [1, 4, 3, -2]) # = (x^27 + x^21 + x^15 + x^9 +x^3) •••••• (x^4 + 4x^3 + 3x^2 - 2x)
  ```





* `simplify(cgcExp, cgcCoe, modulo)`

  Return `tuple` type containing the lists of exponents and coefficients of result congruence after **congruence simplification**.

  ```python
  >>> simplify([14, 13, 11,  9,  6,  3,  2,  1], [ 3,  4,  2,  1,  1,  1, 12,  1], 5) # (3x^14 + 4x^13 + 2x^11 + x^9 + x^6 + x^3 + 12x^2 + x) mod 5
  >>> ([3, 2, 1], [3, 16, 6])                                                         # ≡ (3x^3 + 16x^2 + 6x) mod 5
  ```





* `crt((mod, [x1, x2, …]), …)`

  Return `list` type containing all solutions of a **naïve congruence set**.

  ```python
  >>> crt(3, [1,-1]), (5, [1,-1]), (7, [2,-2]) # x = ±1 (mod 3); x = ±1 (mod 5); x = ±2 (mod 7)
  >>> [16, 19, 26, 44, 61, 79, 86, 89]
  ```





* `congsolve(cgcExp, cgcCoe, modulo)`

  Return `list` type containing all solutions of an **polynomial congruence**.

  ```python
  >>> congsolve([2, 0], [1, -46], 105) # x^2 - 46 ≡ 0 (mod 105)
  >>> [16, 19, 26, 44, 61, 79, 86, 89]
  ```





* `quadratic(p)`

  Return `tuple` type containing the solutions of a **quadratic polynomial**, i.e. `x^2 + y^2 = p`.

  ```python
  >>> quadratic(2017) # x^2 + y^2 = 2017
  >>> (9, 44)         # x = ±9; y = ±44
  ```





* `ord(m, a)`

  Return `int` type for the **order** of an integer `a` modulo `m`, i.e. `ord_m(a)`.

  ```python
  >>> ord(9, 2) # ord_9(a) = 6
  >>> 6
  ```





* `euler(m)`

  Return `int` type for the **Euler function** result of an integer `m`, i.e. `φ(m)`.

  ```python
  >>> euler(40) # φ(40) = 16
  >>> 16
  ```





* `prc(m)`

  Return `list` type for the **primitive residue class** of an integer`m`.

  ```python
  >>> prc(40)
  >>> [1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39]
  ```





* `root(m)`

  Return `list` type for **primitive roots** of modulo `m`.

  ```python
  >>> root(25)
  >>> [2, 3, 8, 12, 13, 17, 22, 23]
  ```





* `legendre(a, p)`

  Return `int` type for the result of **Legendre symbol** `(a|p)`.

  ```python
  >>> legendre(3, 17) # (3|17) = -1
  >>> -1
  ```





* `jacobi(a, m)`

  Return `int` type for the result of **Jacobi symbol** `(a|m)`.

  ```python
  >>> jacobi(286, 563) # (286|563) = -1
  >>> -1
  ```





* `carmicheal(N)`

  Return `bool` type if an integer `N` is a **Carmicheal number**.

  ```python
  >>> carmicheal(3499)
  >>> False
  ```





* `pseudo([mode='Fermat'][, byte=16][, para=10000][, flag=False])`

  Return `int` type for a **pseudo prime number**, which is `byte` long, using `mode` test with `para` times and (for `Fermat` test) Carmicheal number check set in`flag`.

  * `mode` can be set to the followings (`Fermat` in default)
    * `Fermat` —— using **Fermat test** for Fermat pseudo primes
    * `Euler` or `Solovay-Stassen` —— using **Solovay-Stassen test** for Euler pseudo primes
    * `Strong` or `Miller-Rabin` —— using **Miller-Rabin test** for strong pseudo primes
  * `byte` is the **binary length** of expected pseudo primes (`16` in default)
  * `para` is the **security parameter** for repetition in tests (`10000` in default)
  * `flag` is to decide if **Carmicheal numbers** will be checked in Fermat test (`False` in default)

  ```python
  >>> pseudo(mode='Fermat')
  >>> 56629
  >>> pseudo(mode='Euler')
  >>> 38231
  >>> pseudo(mode='Strong')
  >>> 42451
  ```





* `fraction(n[, d])`

  Return `list` type representing the continued fraction form of `n|d`.

  ```python
  >>> fraction(7700, 2145)
  >>> [3, 1, 1, 2, 3, 1, 1]
  ```




### Classes



* `Fraction`

  > An extended `Fraction` class derived from system internal class `fractions.Fraction`.

  * Properties of `Fraction` are described as followed:
    * `numerator` —— 
    * `denominator` —— 
    * `fraction` —— 
    * `convergent` —— 
    * `number` —— 
  * `