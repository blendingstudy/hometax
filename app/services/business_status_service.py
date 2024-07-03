from app.models.business_status_model import BusinessStatus
from app import db


class BusinessStatusService:
    @staticmethod
    def check_business_status(business_id):
        # 여기에 실제 API 호출 코드 삽입
        # 예를 들어:
        # response = requests.get(f'https://api.hometax.go.kr/business_status/{business_id}')
        # status = response.json().get('status')

        # 가상의 응답 데이터 사용
        status = 'Active'  # 또는 'Closed'

        # 상태를 데이터베이스에 저장
        business_status = BusinessStatus(
            business_id=business_id,
            status=status
        )
        db.session.add(business_status)
        db.session.commit()

        return status

    @staticmethod
    def fetch_business_status_history(business_id):
        return BusinessStatus.query.filter_by(business_id=business_id).all()
