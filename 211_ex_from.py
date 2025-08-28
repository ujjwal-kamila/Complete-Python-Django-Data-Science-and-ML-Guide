# 211. Example - Creating Forum, User, and Post Classes

class User:
    """Represents a forum user with basic identity info."""
    def __init__(self, username: str, email: str):
        # store minimal profile; more fields can be added later (e.g., bio)
        self.username = username
        self.email = email


class Post:
    """Represents a post authored by a user."""
    def __init__(self, title: str, content: str, author: "User"):
        # title/content are plain strings for simplicity; could validate length
        self.title = title
        self.content = content
        # keep a reference to the User instance to link authorship
        self.author = author


class Forum:
    """In memory forum managing users and posts."""
    def __init__(self):
        # simple in-memory stores; a real app would use a database
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str) -> User:
        """Create a new User and add to the forum."""
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User) -> Post:
        """Create a new Post authored by an existing user."""
        # could check that `author` is in self.users before posting
        post = Post(title, content, author)
        self.posts.append(post)
        return post



