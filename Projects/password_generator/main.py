import random
import string
class PasswordGenerator:
    def __init__(self) -> None:
        self.UppercaseLetter1 = chr(random.randint(65,90))
        
        self.UppercaseLetter2 = chr(random.randint(65,90))
        
        self.LowercaseLetter1 = chr(random.randint(97,122))
        
        self.LowercaseLetter2 = chr(random.randint(97,122))
        
        self.Digit1 = str(random.randrange(0,9))
        
        self.Digit2 = str(random.randrange(0,9))
        
        self.PunctualtionSign1 =random.choice(string.punctuation)
        
        self.PunctualtionSign2 =random.choice(string.punctuation)

            
    def PasswordCreation(self):

        password = self.UppercaseLetter1 + self.UppercaseLetter2 + self.LowercaseLetter1 + self.LowercaseLetter2 + self.PunctualtionSign1 + self.PunctualtionSign2 + self.Digit1 + self.Digit2
        password_list = [password]
        
        # Shuffle the list
        random.shuffle(password_list)
        
        # Convert the shuffled list back to a string
        shuffled_password = ' '.join(password_list)

        return shuffled_password
  

generator = PasswordGenerator()
generator.PasswordCreation()