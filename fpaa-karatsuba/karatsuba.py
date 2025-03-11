class Karatsuba:
    
    @staticmethod
    def multiply(x, y):

        if x < 10 or y < 10:
            return x * y

        n = max(len(str(x)), len(str(y)))
        half = n // 2

        a = x // (10 ** half)
        b = x % (10 ** half)
        c = y // (10 ** half)
        d = y % (10 ** half)

        ac = Karatsuba.multiply(a, c)
        bd = Karatsuba.multiply(b, d)
        ad_plus_bc = Karatsuba.multiply(a + b, c + d) - ac - bd

        return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd
