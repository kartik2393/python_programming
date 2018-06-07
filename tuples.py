# a=b=c=d=12
# print(a)
#
# a,b=12,13
# print(a,b)
# a,b=b,a
# print("a is {}".format(a))
# print("b is {}".format(b))

# znmd="hrithik", "katrina", "farhan", 2014
# sarkar="amithab","aishwarya","abhiskek", 2009
# sarkar2="amithab","aishwarya","abhishek",2011

mth="varun","iliena","nargis",2015, (
    (1, "title song"),(2, "promo"),(3,"journey"))
print(mth)


title, artist, artist2, year, track = mth
print(title)
print(artist)
print(artist2)
print(year)
for song in track:
    track, title=song
    print("\t {} track number, {} title:".format(track,title))


