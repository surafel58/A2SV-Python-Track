# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
list_of_words = []
freq_of_words = {}

for i in range(n):
  word = input()
  if word in freq_of_words:
    freq_of_words[word] = freq_of_words[word] + 1
  else:
    freq_of_words[word] = 1
    list_of_words.append(word)
  
# print(freq_of_words)  
print(len(freq_of_words))  
for value in list_of_words:
  print(freq_of_words[value], end=" ")
  
