# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
        result = 0
        prev_value = 0
    
        for char in s[::-1]:  # Итерируемся по строке справа налево
            value = roman_dict[char]
        
        # Если значение текущего символа меньше предыдущего,
        # вычитаем его из результата, иначе прибавляем
            if value < prev_value:
                result -= value
            else:
                result += value
        
            prev_value = value
    
        return result