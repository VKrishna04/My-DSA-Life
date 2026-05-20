class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        resp = 0
        i = 0
        for element in s:

            current = roman[element]

            if i + 1 == len(s):
                resp = resp + current

            elif element == 'C' and (s[i+1] == 'M' or  s[i+1] == 'D'):
                resp = resp - 100

            elif element == 'X' and (s[i+1] == 'L' or  s[i+1] == 'C'):
                resp = resp - 10

            elif element == 'I' and (s[i+1] == 'V' or  s[i+1] == 'X'):
                resp = resp - 1

            else:
                resp = resp + current

            i += 1

        return resp