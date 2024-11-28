import requests

API_KEY = "b9f5e18bfa23cf1f9f5f5e9aa84b2667"
BASE_URL = "https://api.themoviedb.org/3"

CATEGORIES = {
    1: ("인기 영화", "popular"),
    2: ("현재 상영작", "now_playing"),
    3: ("평점 높은 영화", "top_rated"),
    4: ("개봉 예정작", "upcoming")
}

def get_movies_by_category(category_type):
    url = f"{BASE_URL}/movie/{category_type}"
    params = {
        "api_key": API_KEY,
        "language": "ko-KR",
        "page": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])[:5]
    return []

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "ko-KR",
        "append_to_response": "credits,reviews"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def display_movie_details(movie):
    print("\n🎞️ 영화 상세 정보 📽️")
    print(f"제목: {movie.get('title')}")
    print(f"개봉일: {movie.get('release_date')}")
    print(f"평점: {movie.get('vote_average'):.1f}/10")
    print(f"러닝타임: {movie.get('runtime')}분")
    print(f"\n줄거리: {movie.get('overview')}")
    
    credits = movie.get('credits', {})
    directors = [person['name'] for person in credits.get('crew', []) if person['job'] == 'Director']
    if directors:
        print(f"\n감독: {', '.join(directors)}")
    
    cast = credits.get('cast', [])[:3]
    if cast:
        print(f"주요 출연: {', '.join(person['name'] for person in cast)}")

def main():
    while True:
        print("\n🎬 영화 카테고리 🎬")
        for num, (name, _) in CATEGORIES.items():
            print(f"{num}. {name}")
        print("0. 종료")

        try:
            choice = int(input("\n카테고리 번호를 선택하세요: "))
            if choice == 0:
                print("프로그램을 종료합니다.")
                break
            if choice not in CATEGORIES:
                print("❗ 올바른 카테고리 번호를 선택해주세요.")
                continue

            category_name, category_type = CATEGORIES[choice]
            movies = get_movies_by_category(category_type)
            
            print(f"\n🎯 {category_name} TOP 5 🎯")
            for idx, movie in enumerate(movies, 1):
                print(f"{idx}. {movie['title']} (평점: {movie['vote_average']:.1f})")
            
            movie_choice = int(input("\n상세 정보를 볼 영화 번호를 선택하세요 (0: 뒤로가기): "))
            if movie_choice == 0:
                continue
            if 1 <= movie_choice <= len(movies):
                movie_details = get_movie_details(movies[movie_choice-1]['id'])
                if movie_details:
                    display_movie_details(movie_details)
                else:
                    print("❗ 영화 정보를 가져오는데 실패했습니다.")
            else:
                print("❗ 올바른 영화 번호를 선택해주세요.")

        except ValueError:
            print("❗ 숫자를 입력해주세요.")
        except Exception as e:
            print(f"❗ 오류가 발생했습니다: {str(e)}")
        
        input("\n계속하려면 Enter를 누르세요...")

if __name__ == "__main__":
    main()