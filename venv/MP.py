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

# 회원 정보 리스트
members = {}

# 회원 추가
def add_member():
    name = input("이름을 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    email = input("이메일을 입력하세요: ")
    if email in members:
        member = Member(name, password, email)
        members[email] = member
        print("회원이 추가되었습니다.")


add_member()
add_member()
find_member()
