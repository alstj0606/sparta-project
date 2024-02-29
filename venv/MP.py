class Member:

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.password = password

    def display(self):
        print(f"이름: {self.name}, email(ID): {self.email}")

class Post:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

