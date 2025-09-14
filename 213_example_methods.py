# 213. Example - Methods for Finding Users by Username 
# 214. Example - Method for Finding All Posts by a Specific User email
# 215. Example - Retrieving User Posts by Email
# 216. Example - Adding Parameter Types
# 217. Example - Wrapping up the Forum, Users, and Posts Example

class User:
    """Represents a forum user with basic identity info."""
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.username} ({self.email})"


class Post:
    """Represents a post authored by a user."""
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Post: '{self.title}' by {self.author.username}"


class Forum:
    """In-memory forum managing users and posts."""
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

    def find_user_by_username(self, username):
        """
        Returns the User object if found, otherwise returns None.
        """
        for user in self.users:
            if user.username == username:  # matched user
                return user
        return None
            
    def find_posts_by_email(self, email):
        """Return a list of posts authored by the user with the given email."""
        found_posts = []
        for post in self.posts:
            if post.author.email == email:
                #  Append the matched post to the list.
                found_posts.append(post)
        return found_posts


# --- Test ---

# Create a forum object
forum = Forum()

# Register 3 users
user1 = forum.register_user('user1', 'user123@gmail.com')
user2 = forum.register_user('user2', 'user234@gmail.com')
user3 = forum.register_user('user3', 'user345@gmail.com')

# Users create several posts
forum.create_post("User1 Post 1", "Hello, I am User1!", user1)
forum.create_post("User1 Post 2", "Another post by User1", user1)
forum.create_post("User2 Post 1", "This is User2's first post", user2)
forum.create_post("User2 Post 2", "User2 again!", user2)
forum.create_post("User3 Post 1", "Hey, this is User3", user3)

# Print all posts directly
print("\nAll Posts in Forum:")
for post in forum.posts:
    print(post)  # __str__ is called from Post
    print(f"  Content: {post.content}") 
print("-" * 30)

# 213...find user by username
print("\nTesting find_user_by_username:")
print(forum.find_user_by_username('user1'))  
print(forum.find_user_by_username('user3').email)
print(f"Searching for a non-existent user: {forum.find_user_by_username('nobody')}")
print("-" * 30)

# 214...find posts by email
print("\nTesting find_posts_by_email for 'user123@gmail.com':")
user1_posts = forum.find_posts_by_email('user123@gmail.com')
for post in user1_posts:
    print(post)
    
# 215.....Retrieving User Posts by Email
user_email = 'user345@gmail.com'
user_posts = forum.find_posts_by_email(user_email)
if user_posts:
    print(f"\nPosts by {user_email}:")
    for post in user_posts:
        print(post)
else:
    print(f"User with email {user_email} does not exist")
