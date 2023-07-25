print("meow")
print("rawr")
def create_youtube_video(title,description):
	meow={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":""}}
	return meow
meow=create_youtube_video("onwan","wasf")
def dislike(dictionary):
	if "dislikes" in dictionary:
		dictionary["dislikes"]=dictionary["dislikes"]+1
	return dictionary
def like(dictionary):
	if "likes" in dictionary:
		dictionary["likes"]=dictionary["likes"]+1
	return dictionary
def add_comment(dictionary,username,comment_text):
	dictionary["comments"]["CharlesD"]=comment_text
	return dictionary
print("now for some fun hehehe")
for i in range(500):
	meow=like(meow)
print(meow["likes"])
print(add_comment(meow,"wawa","skibidi toilet"))