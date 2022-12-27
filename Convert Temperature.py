class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:

        #answer list
        answer = []
        
        #calculate the temperature conversion
        kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32
        
        #append result to list
        answer.append(kelvin)
        answer.append(Fahrenheit)
        
        #return the result
        return answer
