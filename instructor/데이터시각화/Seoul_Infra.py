# -*- coding: cp949 -*-
import csv
from bs4 import BeautifulSoup

#서울시 노인 여가복지시설 데이터 읽기 
reader = csv.reader(open('senior_lsf.csv', 'r'), delimiter=",")
#SVG 맵 읽기 
svg = open('seoul_map.svg', 'r').read()

senior_count={}
counts_only=[]
past_header=False
for row in reader:
    if not past_header:
        past_header=True
        continue

    try:
        unique = row[0]
        count=float(row[1].strip())
        senior_count[unique] = count
        counts_only.append(count)
    except:
        pass

#뷰티풀스프로 로드하기 
soup = BeautifulSoup(svg, "html5lib")
#구를 식별할 path데이터 찾기 
paths = soup.findAll('path')
#지도시각화에 사용할 색장 설정 
colors = ["white", "yellow", "green", "blue", "red", "black"]
#지도에 나타낼 스타일 설정 
path_style='font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

#노인여가시설의 수에 따른 구별 색상부여 
for p in paths:
    if p['id']:
        try:
            count=senior_count[p['id']]
        except:
            continue
        #색상을 부여할 값의 범위 
        if count>250:
            color_class=5
        elif count>200:
            color_class=4
        elif count>150:
            color_class=3
        elif count>100:
            color_class=2
        elif count>50:
            color_class=1
        else:
            color_class=0

        color=colors[color_class]
        p['style'] = path_style + color

print (soup.prettify())

