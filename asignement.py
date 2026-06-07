class DynamicMass:
    def __init__(self):
        self.sizeForUser = 0
        self.sizeForPost = 0
        self.capacityForPost = 1
        self.capacityForUser = 1
        self.hatags = dict()
        self.massForUser = self.newCapasity(self.capacityForUser)
        self.massForPost = self.newCapasity(self.capacityForPost)
 
    def newCapasity(self, cap):
        return [None] * cap
 
    # ------------------------- RESIZE -------------------------
    def resize_users(self):
        new_cap = self.capacityForUser * 2
        new_arr = self.newCapasity(new_cap)
        for i in range(self.sizeForUser):
            new_arr[i] = self.massForUser[i]
        self.massForUser = new_arr
        self.capacityForUser = new_cap
 
    def resize_posts(self):
        new_cap = self.capacityForPost * 2
        new_arr = self.newCapasity(new_cap)
        for i in range(self.sizeForPost):
            new_arr[i] = self.massForPost[i]
        self.massForPost = new_arr
        self.capacityForPost = new_cap
 
    # ------------------------- USERS -------------------------
    def add_user(self, username):
        if self.sizeForUser == self.capacityForUser:
            self.resize_users()
 
        # [username, user_id, follows[], posts[]]
        self.massForUser[self.sizeForUser] = [username, self.sizeForUser, [], []]
        self.sizeForUser += 1
 
    # ------------------------- POSTS -------------------------
    def add_post(self, user_id, content, hashtags):
        if user_id >= self.sizeForUser or user_id < 0:
            return
        if self.sizeForPost == self.capacityForPost:
            self.resize_posts()
        self.massForUser[user_id][3].append(self.sizeForPost)
 
        # [user_id, content, post_id, likes]
        self.massForPost[self.sizeForPost] = [user_id, content, self.sizeForPost, []]
 
        # add hashtags
        for h in hashtags:
            h = h.lower()
            if h not in self.hatags:
                self.hatags[h] = []
            self.hatags[h].append(self.sizeForPost)
 
        self.sizeForPost += 1
 
    def getSizeForPost(self):
        return self.sizeForPost
 
    # ------------------------- FOLLOW -------------------------
    def follow(self, follower_id, followed_id):
        if (follower_id >= self.sizeForUser or follower_id < 0 or followed_id >= self.sizeForUser or followed_id < 0):
            return
        follows = self.massForUser[follower_id][2]
        if followed_id not in follows:
            follows.append(followed_id)
 
    # ------------------------- LIKE -------------------------
    def like(self, user_id, post_id):
        if (user_id >= self.sizeForUser or user_id < 0 or post_id >= self.sizeForPost or post_id < 0):
            return
        likes = self.massForPost[post_id][3]
        if user_id not in likes:
            likes.append(user_id)
 
    # ------------------------- SEARCH -------------------------
    def search_hashtag(self, hashtag):
        hashtag = hashtag.lower()
        if hashtag not in self.hatags:
            print("")
            return
 
        posts = self.hatags[hashtag]
        if not posts:
            print("")
            return
 
        print(" ".join(str(pid + 1) for pid in posts))
 
    # ------------------------- TOP_HASHTAGS -------------------------
    def top_hashtags(self, k):
        if not self.hatags:
            print("")
            return
        # сортировка по числу постов + по алфавиту
        sorted_tags = sorted(
            self.hatags.items(),
            key=lambda x: (-len(x[1]), x[0])
        )[:k]
 
        if not sorted_tags:
            print("")
            return
 
        print(" ".join(tag for tag, _ in sorted_tags))
 
    # ------------------------- FEED -------------------------
    def FEED(self, user_id, k):
        if user_id >= self.sizeForUser or user_id < 0:
            print("")
            return
        follows = self.massForUser[user_id][2]
        posts = []
        # собираем посты всех, на кого подписан
        for u in follows:
            if u < self.sizeForUser and u >= 0:
                posts.extend(self.massForUser[u][3])
 
        if not posts:
            print("")
            return
 
        # сортируем по убыванию времени → post_id
        posts.sort(reverse=True)
 
        print(" ".join(str(pid + 1) for pid in posts[:k]))
 
 
# ========================= MAIN =========================
 
dynamicMass = DynamicMass()
Q = int(input())
 
for _ in range(Q):
    data = input().split()
 
    if data[0] == "ADD_USER":
        dynamicMass.add_user(data[1])
 
    elif data[0] == "ADD_POST":
        user_id = int(data[1]) - 1
        content_words = []
        tags = []
 
        for word in data[2:]:
            if word.startswith("#"):
                tags.append(word[1:])
            else:
                content_words.append(word)
 
        content = " ".join(content_words)
        dynamicMass.add_post(user_id, content, tags)
 
    elif data[0] == "FOLLOW":
        follower = int(data[1]) - 1
        followed = int(data[2]) - 1
        if follower != followed:
            dynamicMass.follow(follower, followed)
 
    elif data[0] == "LIKE":
        dynamicMass.like(int(data[1]) - 1, int(data[2]) - 1)
 
    elif data[0] == "SEARCH":
        dynamicMass.search_hashtag(data[1][1:])
 
    elif data[0] == "TOP_HASHTAGS":
        dynamicMass.top_hashtags(int(data[1]))
 
    elif data[0] == "FEED":
        dynamicMass.FEED(int(data[1]) - 1, int(data[2]))