class Alarm_Clock:
    def __init__(self, current_time, alarm_time):

        self.current_time = current_time
        self.alarm_status = False
        self.alarm_time = alarm_time

    def set_clock_time(self):
        self.current_time = input('Input the current time: ')
        print(f' the current time is: {self.current_time}')
    
    def turn_alarm_on_off(self):
        self.alarm_status = not self.alarm_status
        if self.alarm_status:
            print( f'The alarm is on and set to go off at: {self.alarm_time}')
        else:
            print( f'The alarm is off.')

    def set_alarm_time(self):
        self.alarm_time = input('Input the desired alarm time: ')
        print(f' the alarm is set to go off at: {self.alarm_time}')



