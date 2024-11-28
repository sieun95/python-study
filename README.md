# 🎬 Movie Information System (영화 정보 조회 시스템)

TMDB API를 활용한 영화 정보 조회 시스템입니다. 인기 영화, 현재 상영작, 평점 높은 영화, 개봉 예정작 등 다양한 카테고리의 영화 정보를 간편하게 확인할 수 있습니다.

## 📋 주요 기능

- **카테고리별 영화 조회**

  - 인기 영화 TOP 5
  - 현재 상영작 TOP 5
  - 평점 높은 영화 TOP 5
  - 개봉 예정작 TOP 5

- **영화 상세 정보 제공**
  - 제목 및 개봉일
  - 평점 및 러닝타임
  - 줄거리
  - 감독 및 주요 출연진

## 🔧 설치 방법

1. Python 설치 (3.6 이상)
2. 필요한 라이브러리 설치

```bash
pip install requests
```

## 🔑 API 키 설정

1. TMDB 웹사이트에서 계정 생성
2. API 키 발급
3. API_KEY 변수에 발급받은 키 입력

## 💻 사용 방법

1. 프로그램 실행

```bash
python3 movie_recommendation.py
```

2. 메뉴에서 원하는 카테고리 선택 (1-4)
3. 표시된 영화 목록에서 상세 정보를 볼 영화 선택
4. 영화 상세 정보 확인
5. Enter 키를 눌러 계속 진행

## ⚙️ 주요 구성 요소

- get_movies_by_category(): 카테고리별 영화 목록 조회
- get_movie_details(): 영화 상세 정보 조회
- display_movie_details(): 영화 정보 출력
- main(): 메인 프로그램 실행

## 📞 문의사항

문의사항이나 버그 리포트는 GitHub Issues를 통해 제출해 주세요.

## 🙏 감사의 글

이 프로젝트는 TMDB API를 사용하여 제작되었습니다.
