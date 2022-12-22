class Solution:
    def interpret(self, command: str) -> str:
        #
        result = []
        bracketCounter = 0
        for char in command:
            if char == 'G':
                result.append(char)
            elif char == '(':
                bracketCounter += 1
            elif char == ')' and bracketCounter > 0:
                result.append('o')
                bracketCounter = 0
            elif char == 'a' and bracketCounter > 0:
                result.append('al')
                bracketCounter = 0


        return "".join(result)
