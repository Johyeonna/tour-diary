from django.conf import settings
from pymongo import MongoClient

# MongoDB 클라이언트 설정
client = MongoClient('mongodb://localhost:27017/', 27017)
db = client.diaryData
# 컬렉션
user_collection = db['users_usermodel']



# 사용자 정보
def get_user(request, user_email=None):
    # 사용자 정보 조회
    if user_email :
        #user = user_collection.find_one({'email': user_email})
        # 다른 사용자 예시 db
        user = user_collection.find_one({'email': 'dobi@nate.com'})
    else:
        # user = user_collection.find_one({'email': request.user.email})
        # 로그인 사용자 예시 이메일
        user = {
            'email': 'neweeee@gmail.com',
            'name': '로그인 사용자'
        }

    # 로그인 사용자 확인
    #is_own_page = user and (user['email'] == request.user.email)

    return {
        'user': user,
        #'is_own_page': is_own_page,
        'is_own_page': True,
        # 로그인 사용자 테스트 : True
        # 다른 사용자 테스트 : 주소에 'view/<str:user_email>/' 넣기, urls 설정, False
    }