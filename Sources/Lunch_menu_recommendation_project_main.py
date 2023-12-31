from Lunch_Module import Lunch # Lunch_Module로부터 Lunch클래스의 메소드들을 호출한다.

if __name__ == '__main__': # 현재 스크립트 파일이 직접 실행될 때만 이 안의 코드를 실행한다.
    Lunch_instance = Lunch() # Lunch 클래스를 사용하여 새로운 객체를 생성하고 그 객체를 Lunch_instance 변수에 할당한다.

    restaurant_data = Lunch_instance.read_restaurants_from_file("list_restaurants.txt") # "list_restaurants.txt" 파일을 read_restaurants_from_file함수를 통해 불러온다.
    if not restaurant_data: # 만약 불러온 파일에 텍스트가 없다면 출력한다.
        print('식당 리스트가 없습니다.')

    selected_restaurant = Lunch_instance.select_restaurant(restaurant_data) # 파일의 문자를 리스트로 변환 후 저장된 restaurant_data에서 함수를 통해 사용자가 원하는 식당의 정보를 반환한다.
    print(f"사용자님이 선택한 식당: {selected_restaurant['name']} ({selected_restaurant['cuisine']})") # 딕셔너리로 저장된 식당 정보에서 식당의 이름과 요리 종류를 출력한다.

    selected_menu = Lunch_instance.select_random_menu(selected_restaurant) # 반환된 식당 정보에서 'menu' 안에 해당하는 식사 메뉴 중 하나를 무작위로 반환해 변수에 저장한다.
    print('<메뉴 추천>')
    print(f"사용자님에게 메뉴를 추천했어요. 오늘은 {selected_menu['name']} (가격: {selected_menu['price']}원, 칼로리: {selected_menu['calories']}kcal) 어떠세요?") # 무작위로 뽑힌 메뉴의 이름과 가격, 칼로리를 출력한다.

    selected_menu_by_budget = Lunch_instance.recommend_menu_in_budget(selected_restaurant) # 사용자의 예산에 맞춰 메뉴를 랜덤하게 하나 뽑아 반환되어 변수에 저장한다.
    # 무작위로 뽑힌 메뉴의 이름과 가격, 칼로리를 출력한다.
    print('<예산 기반 메뉴 추천>')
    print(f"사용자님의 예산을 기반으로 메뉴를 추천했어요. 오늘은 {selected_menu_by_budget['name']} (가격: {selected_menu_by_budget['price']}원, 칼로리: {selected_menu_by_budget['calories']}kcal) 어떠세요?")

    recommended_menu = Lunch_instance.recommend_menu_based_on_preferences('user_preferences.txt')
    if recommended_menu is not None: # 과거 사용자의 리뷰를 기반해서 메뉴를 랜덤하게 하나 추천한다.
            print('<리뷰 기반 메뉴 추천>')
            print(f"사용자님의 리뷰를 기반으로 메뉴를 추천했어요. 오늘은 {recommended_menu} 어떠세요? ")
    
    
    user_choice = input('추천받은 음식 중 어느 것을 드시겠어요? > ')
    review = input("식당과 음식에 대한 리뷰를 작성하시겠어요? (Y/N): ").lower() # 사용자에게 리뷰 작성여부를 물어본다.
    if review == "y":
        new_review_text = input("해당 식당에 대한 리뷰를 작성해주세요: ")
        Lunch_instance.track_user_preferences('user_preferences.txt', new_review_text, user_choice) # 리뷰와 메뉴를 저장한다.
    else:
        print("사용자님이 리뷰를 작성하지 않았어요.")

    menu_count_df = Lunch_instance.count_menu_preferences('user_preferences.txt')
    if menu_count_df is not None:
        # 상위 5개의 메뉴를 보여줍니다.
        print("가장 많이 먹은 메뉴 (상위 5개):\n", menu_count_df.head()) # pandas로 만든 데이터프레임 중 상위 5개 항목만 출력한다.

    else:
        print("메뉴 빈도 데이터가 없습니다.")

    