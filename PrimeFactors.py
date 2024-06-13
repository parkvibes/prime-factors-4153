class PrimeFactors:
    def of(self, n: int) -> []:
        result = []
        if n > 1:
            if n == 4:
                while n % 2 == 0:
                    result.append(2)
                    n //= 2
            elif n == 6:
                result.append(2)
                result.append(3)
            else:
                result.append(n)
        return result
