from Lunch_Module import Lunch # Lunch_Module로부터 Lunch클래스의 메소드들을 호출한다.

if __name__ == '__main__': # 현재 스크립트 파일이 직접 실행될 때만 이 안의 코드를 실행한다.
    Lunch_instance = Lunch() # Lunch 클래스를 사용하여 새로운 객체를 생성하고 그 객체를 Lunch_instance 변수에 할당한다.

    restaurant_data = Lunch_instance.read_restaurants_from_file("list_restaurants.txt") # "list_restaurants.txt" 파일을 read_restaurants_from_file함수를 통해 불러온다.
    if not restaurant_data: # 만약 불러온 파일에 텍스트가 없다면 출력한다.
        print('식당 리스트가 없습니다.')

    selected_restaurant = Lunch_instance.select_restaurant(restaurant_data) # 파일의 문자를 리스트로 변환 후 저장된 restaurant_data에서 함수를 통해 사용자가 원하는 식당의 정보를 반환한다.
    print(f"선택한 식당: {selected_restaurant['name']} ({selected_restaurant['cuisine']})") # 딕셔너리로 저장된 식당 정보에서 식당의 이름과 요리 종류를 출력한다.

    selected_menu = Lunch_instance.select_random_menu(selected_restaurant) # 반환된 식당 정보에서 'menu' 안에 해당하는 식사 메뉴 중 하나를 무작위로 반환해 변수에 저장한다.
    print(f"사용자 추천 메뉴: {selected_menu['name']} (가격: {selected_menu['price']}원, 칼로리: {selected_menu['calories']}kcal)") # 무작위로 뽑힌 메뉴의 이름과 가격, 칼로리를 출력한다.

    selected_menu_by_budget = Lunch_instance.recommend_menu_in_budget(selected_restaurant) # 사용자의 예산에 맞춰 메뉴를 랜덤하게 하나 뽑아 반환되어 변수에 저장한다.
    # 무작위로 뽑힌 메뉴의 이름과 가격, 칼로리를 출력한다.
    print(f"예산 맞춤 추천 메뉴: {selected_menu_by_budget['name']} (가격: {selected_menu_by_budget['price']}원, 칼로리: {selected_menu_by_budget['calories']}kcal)")

    review = input("새로운 리뷰를 작성하시겠습니까? (Y/N): ").lower() # 사용자에게 리뷰 작성여부를 물어본다.
    if review == "y":
        new_review_text = input("리뷰를 작성해주세요: ")
        Lunch_instance.track_user_preferences('user_preferences.txt', new_review_text, selected_menu)
        recommended_menu = Lunch_instance.recommend_menu_based_on_preferences('user_preferences.txt')
        if recommended_menu is not None:
            print(f"과거 사용자 리뷰 기반 추천 메뉴: {recommended_menu}")
    else:
        print("사용자가 새로운 리뷰를 작성하지 않았습니다.")
    