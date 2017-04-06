from matplotlib import pyplot as plt

users = [
	{"id": 0, "name": "Hero"},
	{"id": 1, "name": "Dunn"},
	{"id": 2, "name": "Sue"},
	{"id": 3, "name": "Chi"},
	{"id": 4, "name": "Thor"},
	{"id": 5, "name": "Clive"},
	{"id": 6, "name": "Hicks"},
	{"id": 7, "name": "Devin"},
	{"id": 8, "name": "Kate"},
	{"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# 각 사용자의 friends 속성에 빈 list를 할당
for user in users:
	user["friends"] = []

# friendships 데이터를 이용하여 각 list에 값을 할당
for i, j in friendships:
	# users[i]에서 i는 각 사용자의 id와 같으므로 이를 이용해서 친구를 추가함
	users[i]["friends"].append(users[j])
	users[j]["friends"].append(users[i])


def number_of_friends(user):
	""" user의 친구는 몇명일까?"""
	return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)  # 전체 친구 수

num_users = len(users)  # 사람 수
avg_connections = total_connections / num_users  # 평균 친구 수

if __name__ == "__main__":
	print()
	print("######################")
	print("#")
	print("# FINDING KEY CONNECTORS")
	print("#")
	print("######################")
	print()

	print("총 연결 수: ", total_connections)
	print("사용자 수: ", num_users)
	print("평균 연결 수: ", total_connections / num_users)
	print()

	# (user_id, number_of_friends) 로 구성된 list 생성
	num_friends_by_id = [(user["id"], number_of_friends(user))
	                     for user in users]

	print("친구 수를 기준으로 정렬된 사용자들")
	print(sorted(num_friends_by_id,
	             key=lambda pair: pair[1],  # num_friends 기준으로
	             reverse=True))  # 내림차순
