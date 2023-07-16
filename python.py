print("rawr")
def create_youtube_video(title,description):
	meow={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{"username":""}}
	return meow

def dislike(dictionary):
	if "dislikes" in dictionary==True:
		dictionary["dislikes"]=dictionary["dislikes"]+1
	return dictionary
def like(dictionary):
	if "likes" in dictionary==True:
		dictionary["likes"]=dictionary["likes"]+1
	return dictionary