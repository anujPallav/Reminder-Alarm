import time import pyttsx3

print('\n')

print(' WARNING:THIS ALARM ONLY SUPPORT 24:00 HOUR FORMAT') print('\n') print(' IF YOU SELECT N ON SET REMINDER THEN YOU WILL START A ALARM ') print('\n')

REMINDER_LIST = []

def set_alarm_off(): print(' ALARM IS OFF: ')

def get_reminder_entity(): reminder_label = input('SET REMINDER LABEL: ') reminder_hour = input('SET HOUR: ') reminder_minute = input('SET MINUTE: ') reminder_container = reminder_label,reminder_hour,reminder_minute

def set_reminder_entity():
    total_reminder_count = len(REMINDER_LIST)
    set_loop_bool = True
    print(' ')
    get_user_input = input('Do you want to set this reminder? y/n: ')
    if get_user_input == 'y':
        REMINDER_LIST.append(reminder_container)
        print(f'REMINDER SET')
        print('')
        get_reminder_entity()
    elif get_user_input == 'n':
        print('')
        print(REMINDER_LIST)
        get_reminder_status = input('Do you want to start alarm? y/n: ')
        if get_reminder_status == 'y':
            print('ok ALARM IS ON...')
            INDEX = 0
            while set_loop_bool:
                engine = pyttsx3.init()
                TIME = (time.localtime())
                if f'{TIME[3]}' in REMINDER_LIST[INDEX][1] and f'{TIME[4]}' in REMINDER_LIST[INDEX][2]:
                    engine.say(REMINDER_LIST[INDEX][0])
                    engine.runAndWait()
                    INDEX = INDEX + 1    
                    if INDEX >= total_reminder_count:
                        set_loop_bool = False
                        set_alarm_off() 

        elif get_reminder_status == 'n':
            get_reminder_entity()
        else:
            print('Invalid Input')
    else:
        print('wrong input')
        set_reminder_entity()
set_reminder_entity()
get_reminder_entity()
