# 202. Practice - Inheriting Methods by the Instances

class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author
        self.total_likes = 0

    def like(self):
        self.total_likes += 1
    
my_post  = Post("My First Post","About Python",'Ujjwal')
print(my_post)
print(my_post.title)
print(my_post.total_likes)

my_post.like()   # recommnded 
my_post.like()
print(my_post.total_likes)

Post.like(my_post)  # not recommneted 

print(my_post.total_likes)


'''
Create another instances of this post class and call like method for it 
check total_likes for both instances 
'''

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.total_likes = 0 
        
    def like(self):
        self.total_likes += 1


# First post
my_post = Post("My First Post", "About Python", 'Ujjwal')
print(my_post.title, my_post.total_likes)

my_post.like()
my_post.like()
print("Likes on my_post:", my_post.total_likes)

Post.like(my_post)  # Not recommended 
print("Likes on my_post after direct call:", my_post.total_likes)

# Second post
second_post = Post("Second Post", "About AI", "John")
print(second_post.title, second_post.total_likes)

second_post.like()
print("Likes on second_post:", second_post.total_likes)

# Final check for both instances
print("\nFinal Likes:")
print(f"my_post: {my_post.total_likes} likes")
print(f"second_post: {second_post.total_likes} likes")