import random
def generate_rand_code(lenght :int):
   """ 
     this function generate randome password contain 8 characters
     param: take lenght of Password from input user interface
     type param:int
     return: generated  password
     rtyp:str

   """
   characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
   passowrd = ""
   
   for _ in range(lenght):
      passowrd+=random.choice(characters)

   return passowrd