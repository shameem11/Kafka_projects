from faker import Faker

fake=Faker()
def get_registration():
     return {
         'name':fake.name(),
         'address':fake.address(),
         'year':fake.year()
     }
if __name__ == "__main__":
    print(get_registration())