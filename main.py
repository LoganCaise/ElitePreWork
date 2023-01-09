# Bank Chatbot
def chatbot():
  
  print("Welcome to our online bank! How can I help you today? Enter balance, payment, or exit")
  
  
  while True:
    
    message = input("Enter your message: ")
    
    
    if "balance" in message:
      print("Your current balance is $150.")
      

    elif "payment" in message:
      print("How much would you like to pay?")
      amount = float(input("Enter the amount: "))
      print("Your payment of $" + str(amount) + " has been made.")
      
    
    elif "exit" in message:
      print("Thank you for using our online bank. Have a great day!")
      break
      
    
    else:
      print("I'm sorry, I didn't understand your message. Could you please rephrase it?")


chatbot()