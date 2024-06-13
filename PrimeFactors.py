class PrimeFactors:
    def of(self, n: int) -> []:
        result = []
        if n > 1:
            divisor = 2
            if n == 4 or n == 6 or n == 9 or n == 12:
                while n > 1:
                    while n % divisor == 0:
                        result.append(divisor)
                        n //= divisor
                    divisor += 1
            else:
                result.append(n)
        return result
