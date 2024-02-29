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

# 회원 정보 사전
members = {}

# 회원 추가
def add_member():
    while True:
        name = input("이름을 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        if email not in members:
            member = Member(name, password, email)
            members[email] = member
            print("회원이 추가되었습니다.")
        else:
            print("이미 존재하는 이메일입니다. 다른 이메일을 사용하세요.")

        추가요청 = input("회원을 추가하시겠습니까? (y/n): ").lower()
        if 추가요청 != 'y':
            break

    # 추가 요청이 끝나면 회원 목록을 표시
    display_members()

def display_members():
    print(f"총 회원 수: {len(members)}명")
    print("회원 정보:")
    for email in members:
        member = members[email]
        print(f"이름: {member.name}, 이메일: {member.email}")

# add_member 함수 호출
add_member()

