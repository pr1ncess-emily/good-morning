import os
from time import time
from random import sample, randint
from dotenv import load_dotenv

load_dotenv()

DAY_IN_SECONDS = 86400

min_message_frequency = int(os.environ['MIN_MESSAGE_FREQUENCY'])
max_message_frequency = int(os.environ['MAX_MESSAGE_FREQUENCY'])

def get_num_messages():
    return randint(min_message_frequency, max_message_frequency)

def gen_message_send_times(num_messages, lower_time_bound, upper_time_bound):
    for n in range(num_messages):
            time_range = range(lower_time_bound, upper_time_bound)
            return sample(time_range, k=num_messages)

def create_daily_message_schedule():
    lower_time_bound = int(time())
    upper_time_bound = lower_time_bound + DAY_IN_SECONDS
    num_messages = get_num_messages()
    return gen_message_send_times(num_messages, lower_time_bound, upper_time_bound)

def is_message_send_time(schedule):
    current_time = int(time())
    for time in schedule:
        if time == current_time:
            return True
    return False
