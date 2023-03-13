class Phone:
    def __init__(self, phone, cost):
        self.phone = phone
        self.cost = cost

    def call(self, phone_number):
        print(f"phone number {phone_number}")

    def __str__(self) -> str:
        return f"{self.phone} - {self.cost}"


iphone = Phone("iphone", 37000)
print(iphone)
