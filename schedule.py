import os
from time import time, sleep
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
            return sorted(sample(time_range, k=num_messages))

def create_daily_message_schedule():
    lower_time_bound = int(time())
    upper_time_bound = lower_time_bound + DAY_IN_SECONDS
    num_messages = get_num_messages()
    return gen_message_send_times(num_messages, lower_time_bound, upper_time_bound)

def sleep_until(stop_time):
    current_time = int(time())
    sleep_duration = stop_time - time()
    sleep(sleep_duration)