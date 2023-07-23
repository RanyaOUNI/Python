class User:
    all_users = []
#!<---------------CONSTRUCTOR-------------------->
    
    def __init__(self,first_name,last_name,age,email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        User.all_users.append(self)

#!<------DISPLAY_INFO METHOD-------    
    def display_info(self):
        print(f"first name {self.first_name}\nlast name {self.last_name}")

#!<------ENROLL METHOD-------    

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(self.is_rewards_member)
        print(self.gold_card_points)


#!<------SPEND_POINTS METHOD-------    

    def spend_points(self,amount):
        self.gold_card_points -= amount
        print(self.gold_card_points)

@classmethod
def add_users(cls):
    for user in cls.all_users:
         user.display_info()

Sergio = User("Sergio","Ramos",37,"ranya.ouni.7@gmail.com")

Sergio.display_info()

Sergio.enroll()

Samar = User("Samar","Mahwechi",13,"ranya.ouni.7@gmail.com")
Tattou = User("Tattou","Ouni",4,"ranya.ouni.7@gmail.com")

Samar.spend_points(50)

Tattou.enroll()
Tattou.spend_points(80)


# all_users.add_users(cls)





    