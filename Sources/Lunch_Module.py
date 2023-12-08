import random

class Lunch: # Lunch라는 클래스를 만들고 각각의 메소드에 self를 넣어 해당 클래스의 인스턴스를 가르키는 역할을 한다.
   
    # 파일에서 식당 정보를 읽어오는 함수
    def read_restaurants_from_file(self, file_name): # file_name으로 파일을 불러온다.
        try:
            restaurant_list = open(file_name, 'r', encoding='utf8')
            restaurant_data = restaurant_list.read() # restaurant_list를 문자열로 읽어와 변수에 저장한다.
            # 파일에 저장된 텍스트를 문자열로 저장한 restaurant_data를 파이썬 코드로 실행하여 식당 정보를 담고 있는 리스트로 변환시킨다.
            restaurants = eval(restaurant_data) 
            return restaurants
        except FileNotFoundError: # 파일을 찾을 수 없을 때를 대비한 예외 처리이다.
            print("파일을 찾을 수 없습니다.")
            

    # 사용자에게 식당을 선택하도록 하는 함수
    def select_restaurant(self, restaurants):
        print("선택 가능한 식당 목록:")
        for i, restaurant in enumerate(restaurants): # enumerate 함수를 통해 restaurants 리스트를 반복하면서 각 식당의 인덱스와 식당 정보를 동시에 얻는다.
            print(f"{i + 1}. {restaurant['name']} ({restaurant['cuisine']})") # 반복문을 통해 딕셔너리 형태인 5개의 식당의 이름과 음식 종류를 보여준다.

        while True:
            try:
                choice = int(input(f"원하는 식당을 선택하세요 (1부터 {len(restaurants)}까지): ")) # 사용자에게 원하는 식당 번호를 입력받는다.
                if 1 <= choice <= len(restaurants): # 만약 사용자가 입력한 숫자가 1부터 마지막 식당까지의 숫자에 포함되면 
                    return restaurants[choice - 1] # 인덱스는 0부터 시작하므로 사용자가 입력한 숫자에 -1를 하면 해당 인덱스의 딕셔너리 형태인 원하는 식당의 정보가 반환된다.
                    break
                else: # 만약 1부터 마지막 식당까지의 숫자가 아니라면 다시 선택하도록 한다.
                    print(f"잘못된 선택입니다. 1부터 {len(restaurants)}까지의 번호 중 하나를 선택하세요.")
            except ValueError: # 숫자가 아닌 다른 문자를 입력했을 때를 대비한 예외 처리이다.
                print("올바른 숫자를 입력하세요.")


    # 메뉴를 랜덤하게 선택하는 함수
    def select_random_menu(self, restaurant):
        menu = restaurant['menu'] # restaurant에서 'menu'의 정보들을 변수에 저장한다.
        random_choice = random.choice(menu) # 저장된 'menu'의 식사 메뉴 중 하나를 무작위로 뽑는다.
        return random_choice # 무작위로 뽑힌 식사 메뉴를 반환한다.


    # 사용자가 자신의 예산을 입력하면 예산에 맞춰 랜덤하게 메뉴를 추천하는 함수
    def recommend_menu_in_budget(self, restaurant):
        while True:
            budget = int(input("예산을 입력하세요: ")) # 사용자에게 자신의 예산을 입력 받는다.
            if budget <= 0: # 만약 예산이 0보다 작다면 0 이상의 올바른 예산을 다시 입력받는다.
                print("올바른 예산을 입력하세요. (0보다 큰 숫자)")
            elif budget > 0: # 만약 예산이 0보다 크다면 
                menu_in_budget = []  # 사용자의 예산 내 메뉴를 저장하는 리스트를 만든다.
                for menu in restaurant['menu']: # 각 식당의 메뉴들을 반복문을 통해 menu에 저장한다.
                    if menu['price'] <= budget: # 만약 메뉴의 가격이 사용자의 예산 내라면
                        menu_in_budget.append(menu) # 메뉴를 리스트에 저장한다.
                if not menu_in_budget: # 만약 리스트에 사용자의 예산 내 메뉴가 아무것도 없다면 출력한다.
                    print("선택 가능한 메뉴가 없습니다. 더 높은 예산을 입력하세요.")
                else: # 리스트에 사용자의 예산 내 메뉴가 있다면 그 중에서 랜덤하게 메뉴 하나를 출력한다.
                    random_menu = random.choice(menu_in_budget) 
                    return random_menu 
                    break
            else: # 예산을 입력할 때 숫자가 아니라면 출력한다.
                print('숫자를 입력하세요.')
        

    # 사용자의 리뷰를 저장하고 분석하는 함수
    def track_user_preferences(self, file_name, review, selected_menu):
        fp_append = open(file_name, 'a', encoding='utf8') # 파일을 사용자가 작성한 리뷰와 메뉴를 추가할 수 있도록 한다.
        fp_append.write(f"Menu: {selected_menu['name']}, Review: {review}\n")
        return fp_append

    # 과거 선호도에 기반하여 메뉴를 추천하는 함수
    def recommend_menu_based_on_preferences(self, file_name):
        try:
            # 사용자의 이전 메뉴 선택과 리뷰를 읽어온다
            fp_read = open(file_name, 'r', encoding='utf8') # 파일을 읽기 모드로 불러온다.
            lines = fp_read.readlines()
            # 파일의 각 줄에서 'Menu' 부분에 해당하는 음식을 골라내 menu_preferences에 리스트 형태로 추가한다.
            menu_preference = [line.strip().split(': ')[1].split(', ')[0] for line in lines if line.startswith('Menu')] 

            if not menu_preference: # 만약 메뉴가 아무것도 없다면 출력한다.
                print('사용자의 이전 메뉴 선택 기록이 없습니다.')
                return None
            
            random_menu = random.choice(menu_preference) # menu_preference에 저장된 메뉴들 중 랜덤하게 하나를 불러온다.
            return random_menu
                
        except FileNotFoundError: 
            print('파일이 없습니다.')  # 파일이 없는 경우 예외처리이다.
        
            