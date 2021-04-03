import random
from collections import deque
from apscheduler.schedulers.blocking import BlockingScheduler
import pickle
from datetime import datetime as dt
from datetime import timedelta


# set time interval variable for apsceduler module
number_seconds = 1

# create lists with deque as sentdex showed
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

# make tuple of lists for storing in pickle file
data_X_Y = (X, Y)
print(data_X_Y)

# store tuple in pickle
pickle.dump(data_X_Y, open("data_X_Y.p", "wb"))

# function for getting data within Dash callback
def get_data():
    # initiate blockingscheduler
    sched = BlockingScheduler()

    # decorater in which you define the number of seconds see https://www.youtube.com/watch?v=FsAPt_9Bf3U&t=1s for good explanation decorators
    @sched.scheduled_job('interval', seconds=number_seconds, start_date=dt.now() - timedelta(seconds=(number_seconds - 1)))
    def update_data_4_graph():
        # these are the lines of codes that were in the function of the callback of Sentdex
        X.append(X[-1]+1)
        Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))
        # again make a tuple of lists and store the tuples in the a pickle file
        data_X_Y = (X, Y)
        print(data_X_Y)
        pickle.dump(data_X_Y, open("data_X_Y.p", "wb"))

    # start the apscheduler module
    sched.start()