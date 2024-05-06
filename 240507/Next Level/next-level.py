class User:
    def __init__(self, user_id = "john doe", level = "1" ):
        self.user_id = user_id
        self.level   = level
    
    def __repr__(self):
        return(
            f"user {self.user_id} lv {self.level}"
        )


user1 = User("codetree", "10")
user2 = User(*list(map(str, input().split())))

print(user1)
print(user2)