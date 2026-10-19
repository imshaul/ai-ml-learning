lists = [10,20,30,40,50]
squared_list = []
squared_list = [n**2 for n in lists]
print(squared_list)

tv_shows = ["friends", "PARK AND RECREATION", "SUPERNATURAL", "the OFFice", "tHe bOys"]
tv_shows_cap = [new_shows.title() for new_shows in tv_shows if len(new_shows)<=8]
print(tv_shows_cap)

print([new**2 for new in range(1,11)])