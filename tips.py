import random
import pyjokes

Q = "question"

while True:
    print("HI I'm tip's ")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print('''I AM NOT VERY SMART . but i con do all this, like ''')
    print('''#I con calculate for calculate type 'c'.
       #I can play game with you for game type 'game'.
      #to know who created me?? type 'sommay'. 
      #have you heard a joke for type 'joke'. 
      #if I have told you ABCD for ABCD type 'ABCD'.
      #and I can count to billions and trillions.
      #If you ever forget your IDs or passwords, I can keep your data 100% safe without any servers! 
          type (RR) ''')
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    
    Q_1 = input("what do you want to do? ")
    print("you choose to " + Q_1 + " ok let's do it")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    
    # 1. Calculator
    if Q_1 == "c":
       print("you have a maths " + Q + " ok I can solve it")
       print("for add type it ' + '")
       print("for sudtraction  type it ' - '")
       print("for multipliction type it ' * ' ")
       print("for division type it ' / ' ")
       print("for remainder type it ' % ' ")
       s = input("you choose it wow! type your operator ")
       num_1 = int(input("what is you fist number for " + s + " "))
       num_2 = int(input("what is your second number for " + s + " "))
       if s == "+":
          s_1 = num_1 + num_2
       elif s == "-":
          s_1 = num_1 - num_2
       elif s == "*":
          s_1 = num_1 * num_2
       elif s == "/":
          s_1 = num_1 / num_2
       elif s == "%":
          s_1 = num_1 % num_2
       else:
          s_1 = "Invalid Operator!"
       print("ans is")
       print(s_1)
       
    # 2. Game
    elif Q_1 == "game":
       print("you choose to play a game")
       print("let's play a random number guessing game") 
       print("I will think of a number between 1 and 100, and you have to guess it.")
       number_to_guess = random.randint(1, 100)
       attempts = 0
       while True:
         user_guess = input("Enter your guess (or type 'exit' to quit): ")
         if user_guess.lower() == 'exit':
               print("Thanks for playing! Goodbye!")
               break
         try:
               user_guess = int(user_guess)
               attempts += 1
               if user_guess < number_to_guess:
                  print("Too low! Try again.")
               elif user_guess > number_to_guess:
                  print("Too high! Try again.")
               else:
                  print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                  break
         except ValueError:
               print("Invalid input! Please enter a valid number or 'exit' to quit.")
               
    # 3. Creator Info
    elif Q_1 == "sommay":
     print('''You choose to know who created me!
          I was created by Sommay. He is a 13-year-old boy, very smart, and the best programmer in 
           the world! He is the 
           leader of this team.
           He studies in 7th grade at Kendriya Vidyalaya. He has two more teammates, 
           Tarun and Prashant, who are also 13 years old and study in the same class.
           This team of three KV kids worked together and made this project in just 30 days!
            Sommay is the main mind who created me, and all three friends are working hard 
           every day to make me better, smarter, and more useful.''')
           
    # 4. Joke
    elif Q_1 == "joke":
     print("you choose to hear a joke")
     joke = pyjokes.get_joke()
     print(joke)
     
    # 5. ABCD
    elif Q_1 == "ABCD":
     print("you choose to hear ABCD")
     print('''A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
     a b c d e f g h i j l m n o p q r s t u v w x y z''')
     
    # 6. Counter
    elif Q_1 == "count":
     s = input("how much do you want to count to? ")
     try:
        s = int(s)
        for i in range(1, s + 1):
            print(i)
     except ValueError:
        print("Invalid input! Please enter a valid number.")
        
    # 7. Secret RR Feature (Serverless Secure Memory)
    elif Q_1 == "RR":
      print("=== The Tips AI Offline Secure Memory ===")
      print("You can save data, IDs, or Passwords locally.")
      print("Example: 'my email = Sommaysingh0@gmail.com'")
      print("To delete a saved entry, type: 'your word = delete'")
      print("Data is stored 100% locally on your machine. No external servers connected!")
      print("-----------------------------------------------------------------------")
      knowledge = {}

      try:
         with open("memory.txt", "r") as f:
            for line in f:
                if "|" in line:
                    q, a = line.strip().split("|", 1)
                    knowledge[q] = a
      except FileNotFoundError:
         pass

      while True:
          user = input("You : ").strip().lower()

          if user == "exit":
              print("The Tips AI : Exiting Secure Memory Mode...")
              break

          elif "=" in user:
              question, answer = user.split("=", 1)
              question = question.strip().lower()
              answer = answer.strip()

              if answer.lower() == "delete":
                  if question in knowledge:
                      del knowledge[question]
                      print("The Tips AI : Deleted!")
                  else:
                      print("The Tips AI : Not found!")
              else:
                  knowledge[question] = answer
                  print("The Tips AI : Saved safely offline!")

              with open("memory.txt", "w") as f:
                  for q, a in knowledge.items():
                      f.write(q + "|" + a + "\n")

          elif user in knowledge:
              print("The Tips AI :", knowledge[user])

          else:
              print("The tips AI : I don't remember that. Can you teach me?")
              answer = input("Teach me : ")
              knowledge[user] = answer

              with open("memory.txt", "w") as f:
                  for q, a in knowledge.items():
                      f.write(q + "|" + a + "\n")
              print("The Tips AI : Thanks, I learned something new!")
              
    else:
        print("Invalid Option! Please select from the menu.")
        
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")