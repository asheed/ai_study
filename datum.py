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

def friends_of_friend_ids_bad(user):
	# foaf 는 친구의 친구를 의미
	return [foaf["id"]
	          for friend in user["friends"]   # user의 친구 개개인에 대해
	          for foaf in friend["friends"]]  # 그들의 친구들을 찾는다.

from collections import Counter

def not_the_same(user, other_user):
	"""만약 두 사용자의 id가 다르면 다른 사용자로 인식"""
	return user["id"] != other_user["id"]

def not_friends(user, other_user):
	"""만약 other_user가 user["friends"]에 포함되지 않으면
	친구가 아닌 것으로 간주함.
	즉, other_user를 not_the_same 함수를 사용해서
	user["friends"]에 포함된 사람과 다르다고 인식"""
	return all(not_the_same(friend, other_user)
	              for friend in user["friends"])

def friends_of_friend_ids(user):
	return Counter(foaf["id"]
	               for friend in user["friends"]    # 사용자의 친구 개개인에 대해
	               for foaf in friend["friends"]    # 그들의 친구들을 세어 보고
	               if not_the_same(user, foaf)      # 사용자 자신과
	               and not_friends(user, foaf))     # 사용자의 친구는 제외

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
	return [user_id
	        for user_id, user_interest in interests
	        if user_interest == target_interest]

from collections import defaultdict

# key가 관심사, value가 사용자 id
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
	user_ids_by_interest[interest].append(user_id)

# key가 사용자, value가 관심사
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
	interests_by_user_id[user_id].append(interest)

# 특정 사용자가 주어졌을  때, 사용자와 가장 유사한 관심사를 가진 사람을 출력
# 1. 해당 사용자의 관심사들을 본다.
# 2. 각 관심사를 가진 다른 사용자들이 누구인지 찾아본다.
# 3. 다른 사용자들이 몇 번이나 등장하는지 센다.
def most_common_interests_with(user_id):
	return Counter(interested_user_id
	               for interest in interests_by_user_id[user_id]
	               for interested_user_id in user_ids_by_interest[interest]
	               if interested_user_id != user_id)

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

	print()
	print("######################")
	print("#")
	print("# DATA SCIENTISTS YOU MAY KNOW")
	print("#")
	print("######################")
	print()

	print("friends of friends bad for user 0:", friends_of_friend_ids_bad(users[0]))
	print("friends of friends for user 3:", friends_of_friend_ids(users[3]))

	print()
	print("######################")
	print("#")
	print("# 나랑 관심사가 유사한 사람들")
	print("#")
	print("######################")
	print()

	print(most_common_interests_with(0))