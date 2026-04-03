import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# 1. 기초 데이터 설정
DEPARTMENTS = ['테스트1팀', '테스트2팀', '개발1팀', '개발2팀', '인프라팀', '인사팀', '서비스기획팀', '디자인팀']
JOB_TITLES = ['사원', '대리', '과장', '차장', '부장']
TECH_STACKS = ['Python, Pytest', 'Java, Spring', 'Node.js, AWS', 'React, Next.js', 'Go, Docker']
CERTIFICATIONS = ['정보처리기사', 'ISTQB', 'SQLD', 'AWS-SAA', 'ADsP', '-']
LANG_SCORES = ['AL', 'IH', 'IM3', 'IM2', 'IM1', 'NH']

# 2. Faker 설정 (한글/영어 혼용)
fake_ko = Faker('ko_KR')
fake_en = Faker('en_US') 
Faker.seed(2026)

def generate_hr_txt(count=1000):
    data = []
    
    for i in range(1, count + 1):
        emp_id = f"2025{i:03d}"
        is_male = random.choice([True, False])
        
        # 날짜 및 보상 데이터
        birth_date = fake_ko.date_of_birth(minimum_age=26, maximum_age=48)
        hire_date = fake_ko.date_between(start_date='-4y', end_date='today')
        salary = random.randint(4800, 12000) * 10000
        
        row = {
            "사번": emp_id,
            "이름(한)": fake_ko.name_male() if is_male else fake_ko.name_female(),
            "이름(영)": fake_en.name(),
            "성별": "남" if is_male else "여",
            "생년월일": birth_date.strftime('%Y-%m-%d'),
            "주소": f"{fake_ko.province()} {fake_ko.city()}",
            "국적": "대한민국",
            "핸드폰": f"010-{random.randint(1000,9999)}-{random.randint(1000,9999)}",
            "개인메일": fake_ko.free_email(),
            "회사메일": f"emp_{emp_id}@testaccount.com",
            "부서": random.choice(DEPARTMENTS),
            "직위": random.choice(JOB_TITLES),
            "입사일": hire_date.strftime('%Y-%m-%d'),
            "연봉": salary,
            "성과급": int(salary * random.uniform(0.05, 0.15)),
            "직전고과": random.choice(['S', 'A', 'B', 'C']),
            "기술스택": random.choice(TECH_STACKS)
        }
        data.append(row)
    
    # 3. 데이터프레임 생성 및 파일 저장
    df = pd.DataFrame(data)
    file_name = "HR_Test_Dataset.txt"
    
    # 구글 스프레드시트 복사 시 가장 깔끔한 탭(Tab) 구분자 사용
    # index=False로 행 번호 제외, sep='\t'로 탭 구분
    df.to_csv(file_name, index=False, sep='\t', encoding='utf-8-sig')
    print(f"성공: {count}명의 데이터가 '{file_name}' 파일로 저장")

if __name__ == "__main__":
    generate_hr_txt()