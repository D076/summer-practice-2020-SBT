from datetime import datetime, timedelta
from threading import Thread, BoundedSemaphore
from time import sleep
from functools import lru_cache

# Token TTL (time to live)
TTL = timedelta(seconds=10)

class TokenInfo(object):
    def __init__(self, user_id, token, last_request_time):
        self.__user_id = user_id
        self.__token = token
        self.__last_request_time = last_request_time

    @property
    def user_id(self):
        return self.__user_id

    @property
    def token(self):
        return self.__token

    @property
    def last_request_time(self):
        return self.__last_request_time

    @last_request_time.setter
    def last_request_time(self, new_time):
        self.__last_request_time = new_time

    def __str__(self):
        return 'user_id = {0}, token = {1}, last_request_time = {2}' \
            .format(self.__user_id, self.__token, self.__last_request_time)

# Token managment class
class TokenManager(Thread):
    def __init__(self):
        super().__init__()

        self.tokens = list()
        self.semaphore = BoundedSemaphore(2)

    # Main thread runner
    def run(self):
        while True:
            print('CURRENT TOKENS')
            for token in self.tokens:
                print(token)
            self.__removeInactiveTokens()
            sleep(1)

    # Add TokenInfo into query
    def addToken(self, TokenInfo):
        self.semaphore.acquire()

        self.tokens.append(TokenInfo)

        self.semaphore.release()

    # Add token information directly into query
    def addTokenDirect(self, user_id, token, last_request_time):
        self.addToken(TokenInfo(user_id, token, last_request_time))

    # Update token TTL
    def updateToken(self, token):
        self.semaphore.acquire()

        for i in range(len(self.tokens)):
            if self.tokens[i].token == token:
                self.tokens[i].last_request_time = datetime.now()

        self.semaphore.release()

    @lru_cache(maxsize=32)
    def getUserIdByToken(self, token):
        self.semaphore.acquire()
        
        for i in range(len(self.tokens)):
            if self.tokens[i].token == token:
                return self.tokens[i].user_id

        self.semaphore.release()

        return None

    # Remove old tokens
    def __removeInactiveTokens(self):
        captured_time = datetime.now()

        self.semaphore.acquire()

        indexes = list()
        for i in range(len(self.tokens)):
            if self.tokens[i].last_request_time + TTL < captured_time:
                indexes.append(i)

        for i in range(len(indexes) - 1, -1, -1):
            self.tokens.pop(indexes[i])

        self.semaphore.release()

        