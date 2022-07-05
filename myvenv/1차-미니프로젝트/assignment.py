"""
(메뉴)
아래 메시지와 같이 1, 2, 3 를 프로그램 사용자에게 입력 받게 해주세요.
1 : 지출 내역 입력
2 : 지출 내역 확인
3 : 프로그램 종료
프로그램 사용자가 번호를 1~3번 외에 숫자를 입력하거나 문자가 출력되는 경우엔 다시 (메뉴) 가 표시되도록 구현해주세요.

그 외에 추가 요구 사항은 PDF 문서를 참고해주세요.
"""

spend = {}

def interface():
    print("""
    1 : 지출 내역 입력
    2 : 지출 내역 확인
    3 : 프로그램 종료""")
    menu = int(input("번호를 입력해주세요 : "))
    
    if menu == 1:
        menu_one()
    elif menu == 2:
        menu_two()
    elif menu == 3:
        exit()
    else:
        interface()

def menu_one():
    name = input("이름을 입력해주세요 : ")
    description = input("내역을 입력해주세요 : ")
    while True:
        try:
            amount = int(input("금액을 입력해주세요 : "))
            if amount <= 0:
                print("금액은 0보다 큰 정수이어야 합니다.")
                continue
            break
        except:
            print("금액은 정수이어야 합니다.")
    while True:
        try:
            year = int(input("연도를 입력해주세요 : "))
            if year <= 0:
                print("연도는 0보다 큰 정수이어야 합니다.")
                continue
            break
        except:
            print("연도는 정수이어야 합니다.")

    global spend
    spend = {
        "이름": name,
        "내역": description,
        "금액": amount,
        "연도": year
    }
    interface()

def menu_two():
    if spend == {}:
        print("입력된 건이 없습니다.")
    else:
        print(spend)
    interface()

interface()