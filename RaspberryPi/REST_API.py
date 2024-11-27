import requests

#URL
api_url = "http://i7a106.p.ssafy.io:8000/"
#설문 질문 받아오기
Get_survey = "kiosk/survey"
#설문 결과 받아오기
Get_survey_result="kiosk/result"
#추천 횟수 증가
count_up="kiosk/count/"
#얼굴감정분석 결과 받아오기
Get_face_result="kiosk/face/"

datas={
    '1':"sweet",
    '2':"alone",
    '3':"바보"
}
response = requests.get(api_url+Get_survey_result, json=datas)

#response = response.json()
#print(response)