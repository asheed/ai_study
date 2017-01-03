# -*- coding: utf-8 -*-
__author__ = 'woojin'

from math import sqrt

# 영화 비평과 영화 평가 정보를 담는 딕셔너리
critics={'Lisa Rose': {'Lady in the water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
         'Gene Seymour': {'Lady in the water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'The Night Listener': 3.0},
         'Michael Phillips': {'Lady in the water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0},
         'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5, 'The Night Listener': 4.5},
         'Mick LaSalle': {'Lady in the water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0, 'The Night Listener': 3.0},
         'Jack Matthews': {'Lady in the water': 3.0, 'Snakes on a Plane': 4.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'The Night Listener': 3.0},
         'Toby': {'Snakes on a Plane': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 1.0}
         }

# person1과 person2의 거리 기반 유사도 점수를 리턴
def sim_distance(prefs, person1, person2):
    # 공통항목 목록 추출
    si = {}     # 빈 딕셔너리
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # 공통 평가 항목이 없는 경우 0을 리턴
    if len(si)==0: return 0

    # 모든 차이 값의 제곱을 더함
    sum_of_squares = sum(
        [pow(prefs[person1][item] - prefs[person2][item],2)
         for item in prefs[person1] if item in prefs[person2]])

    return 1/(1 + sum_of_squares)

# person1과 person2에 대한 피어슨 상관계수를 리턴
def sim_peason(prefs, person1, person2):
    # 같이 평가한 항목들의 목록을 구함
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]: si[item] = 1

    # 요소들의 개수를 구함
    n = len(si)

    # 공통 요소가 없다면 0을 리턴
    if n==0: return 0

    # 모든 선호도를 계산함
    sum1 = sum([prefs[person1][it] for it in si])
    sum2 = sum([prefs[person2][it] for it in si])

    # 제곱의 합을 계산
    sum1sq = sum([pow(prefs[person1][it], 2) for it in si])
    sum2sq = sum([pow(prefs[person2][it], 2) for it in si])

    # 곱의 합을 계산
    pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])

    # 피어슨 점수 계산
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1sq-pow(sum1, 2)/n)*(sum2sq-pow(sum2, 2)/n))

    if den == 0: return 0

    r = num/den

    return r