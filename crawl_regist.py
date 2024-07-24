import pandas as pd

# 자동차 등록 현황

# 자동차 등록 현황 엑셀파일 불러오기, 파일 경로와 파일명을 정확히 입력합니다.
cars = pd.read_excel(io='./car_enrollment.xlsx', engine="openpyxl")

# 데이터 확인
print(cars)

# 자동차 등록 현황

# 자동차 등록 현황 엑셀파일 불러오기, 파일 경로와 파일명을 정확히 입력합니다.
cars = pd.read_excel(io='./car_enrollment.xlsx', engine="openpyxl")

# 데이터 확인
print(cars)
# 자동차 지역별 등록 현황

# 자동차 지역별 등록 현황파일 불러오기
cars2 = pd.read_excel(io='./city_enrollment.xlsx', engine='openpyxl')


# 데이터 확인
print(cars2)

xlsx = pd.read_excel("C:\dev\Crawling\car_enrollment.xlsx") # 데이터 프레임을 위한 CSV파일 변경
xlsx.to_csv("C:\dev\Crawling\car_enrollment.csv")


xlsx = pd.read_excel("C:\dev\Crawling\city_enrollment.xlsx") # 데이터 프레임을 위한 CSV파일 변경
xlsx.to_csv("C:\dev\Crawling\city_enrollment.csv")


# 변경된 CSV파일 불러오기
df1 = pd.read_csv('car_enrollment.csv', encoding='utf-8')
df1

df1.info() # 불필요한 값 삭제를위해 type확인

df1 = df1.drop(df1.columns[0], axis=1) # 불필요한 값 삭제

df1 # 정리된 데이터 확인

df1.to_csv('./car.csv') # 변경된 값 저장


# 변경된 CSV파일 불러오기
df2 = pd.read_csv('city_enrollment.csv', encoding='utf-8')
df2

df2.info() # 불필요한 값 삭제를위해 type확인

df2 = df2.drop(df2.columns[0], axis=1) # 불필요한 값 삭제

df2 # 정리된 데이터 확인

df2.to_csv('./city.csv') # 변경된 값 저장