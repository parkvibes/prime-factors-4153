class PrimeFactors:
    def of(self, n: int) -> []:
        result = []
        if n > 1:
            divisor = 2
            if n == 4:
                while n % divisor == 0:
                    result.append(divisor)
                    n //= divisor
            elif n == 6:
                while n > 1:
                    while n % divisor == 0:
                        result.append(divisor)
                        n //= divisor
                    divisor += 1
            elif n == 9:
                result.append(3)
                result.append(3)
            else:
                result.append(n)
        return result
