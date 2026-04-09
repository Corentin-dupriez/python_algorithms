class Solution:
    def intToRoman(self, num: int) -> str:
        romans ={1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        roman_keys = [key for key in romans.keys()]
        res = ''
        while num > 0:
            for i in range(len(roman_keys)):
                if num >= roman_keys[i]:
                    if int(str(num)[0]) not in (4,9):
                        res += romans[roman_keys[i]] * (num // roman_keys[i])
                        num = num % roman_keys[i]
                    else:
                        if roman_keys[i] in (1, 10, 100):
                            res += romans[roman_keys[i]] * ((roman_keys[i-1] - (roman_keys[i-1] - roman_keys[i])) // roman_keys[i])
                            res += romans[roman_keys[i-1]]
                            num = num % roman_keys[i]
                        else: 
                            res += romans[roman_keys[i+1]] * ((roman_keys[i-1] - (roman_keys[i-1] - roman_keys[i+1])) // roman_keys[i+1])
                            res += romans[roman_keys[i-1]]
                            num = int(str(num)[1:]) if str(num)[1:] != '' else 0

        return res

print(Solution().intToRoman(3749))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
print(Solution().intToRoman(1))
