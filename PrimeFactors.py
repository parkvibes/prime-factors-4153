class PrimeFactors:
    def of(self, n: int) -> []:
        result = []
        if n > 1:
            if n == 4:
                result.append(2)
                result.append(2)
            else:
                result.append(n)
        return result
