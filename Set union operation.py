# Enter your code here. Read input from STDIN. Print output to STDOUT
english_subscr_size = int(input())
english_subscription = set(input().split())
french_subscr_size = int(input())
french_subscription = set(input().split())

english_subscr_only = english_subscription.union(french_subscription)

print(len(english_subscr_only))
