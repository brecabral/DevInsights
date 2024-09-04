class Solution:
    def isHappy(self, n: int) -> bool: 
        while n >= 7:
            digitos = []
            digitosQuadrados = []
            numero = n
            
            while (numero > 0):
                digito = numero % 10
                numero //= 10
                digitos.append(digito)

            for digito in digitos:
                digitosQuadrados.append(digito * digito)

            n = sum(digitosQuadrados)

        if n == 1:
            return True
        return False


a = Solution()
print(a.isHappy(1111111))



class Solution:
    def isHappy(self, n: int) -> bool:
        hsh = set()
        def f(x):
            y = 0
            while x:
                y += (x % 10)**2
                x //= 10

            return y

        while True:
            if n == 1:
                return True
            if n in hsh:
                return False
            hsh.add(n)
            n = f(n)