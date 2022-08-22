try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")
website = "https://www.geeksforgeeks.org/"# need a exact site name including /
# to search
query = "geeksforgeeks" # keyword
rank, rank_list = 1, ""
squares = []
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
    squares.append(j)
print(squares)
# app.py

#streaming = ['netflix', 'hulu', 'disney+', 'appletv+']
streaming = squares
index = streaming.index(website)
print('The rank of your site is:', index+1)