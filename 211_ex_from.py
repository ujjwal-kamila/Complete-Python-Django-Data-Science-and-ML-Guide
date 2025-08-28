# 211. Example - Creating Forum, User, and Post Classes

class User:
    """Represents a forum user with basic identity info."""
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Post:
    """Represents a post authored by a user."""
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    """In memory forum managing users and posts."""
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username, email):
        """Create a new User and add to the forum."""
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title, content, author):
        """Create a new Post authored by an existing user."""
        post = Post(title, content, author)
        self.posts.append(post)
        return post

# 212. Example - Creating Instances of the Forum, User, and Post Classes

# Create a forum object
forum = Forum()

# register users
ujjwal = forum.register_user('ujjwal123', 'ujjwal@gmail.com')
other = forum.register_user('xyz643', 'xyz@gmail.com')

# Print all registered users
print(forum.users)

# Create a post by 'ujjwal'
forum.create_post("My first post", "Post content", ujjwal)

# Print all posts
print(forum.posts)

# Print details of post
print(forum.posts[0].title)     
print(forum.posts[0].content)   
print(forum.posts[0].author)


