class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            column_number = column_number * 26 + val
        return column_number
