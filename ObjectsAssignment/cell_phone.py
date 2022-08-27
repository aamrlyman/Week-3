class Cell_Phone:

    def __init__(self, model, phone_number, name):    
        self.user_name = name
        self.model = model
        self.phone_number = phone_number
        self.contacts = {}
        self.messages = []
        self.vibrate_mode = False

    def receive_text_message(self):
        message = [input("enter your name: "), input('Type your message here: ')]
        self.messages += message[1]
        print(f'New message from {message[0]}: {message[1]}')

    def send_text_message(self, contact):
        message = [input('Enter message here: ')]
        contact.messages += f'New message received from {self.user_name}: {message[0]}'.split(' ,') 
        print(f'Message sent to {contact.user_name}: {message[0]}')


    def toggle_vibrate_mode(self):
        self.vibrate_mode = not self.vibrate_mode
        if self.vibrate_mode:
            print('Vibrate mode is on')
        else: 
            print("Vibrate mode is off")