class MaximoDivisorComum:

    def mdc(self, num1, num2):
        a = max(num1, num2)
        b = min(num1, num2)

        if a == b:
            return a
        
        if a == 0 or b == 0:
            return -1
        
        c = a - ((a // b) * b)

        if c == 0:
            return b

        return self.mdc(b, c)


a = MaximoDivisorComum()
print(a.mdc(1680, 641))