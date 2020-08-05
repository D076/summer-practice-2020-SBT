from datetime import datetime, timedelta
from threading import Thread, BoundedSemaphore
from time import sleep

# Token TTL (time to live)
TTL = timedelta(seconds=20)


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

        self.__tokens = list()
        self.__semaphore = BoundedSemaphore(2)
        self.__running = True

        self.daemon = True

    # Terminate TokenManager thread
    def terminate(self):
        self.__running = False

    # Main thread runner
    def run(self):
        while self.__running:
            self.__removeInactiveTokens()

            sleep(30)

        return

    # Add TokenInfo into query
    def addToken(self, TokenInfo):
        self.__semaphore.acquire()

        self.__tokens.append(TokenInfo)

        self.__semaphore.release()

    # Add token information directly into query
    def addTokenDirect(self, user_id, token, last_request_time):
        self.addToken(TokenInfo(user_id, token, last_request_time))

    # Update token TTL
    def updateToken(self, token):
        self.__semaphore.acquire()

        for i in range(len(self.__tokens)):
            if self.__tokens[i].token == token:
                self.__tokens[i].last_request_time = datetime.now()
                break

        self.__semaphore.release()

    def deleteToken(self, token):
        self.__semaphore.acquire()

        delete_index = None
        for i in range(len(self.__tokens)):
            if self.__tokens[i].token == token:
                delete_index = i
                break

        if delete_index is None:
            self.__semaphore.release()

            return False
        else:
            self.__tokens.pop(delete_index)

            self.__semaphore.release()

            return True

    def getUserIdByToken(self, token):
        self.__semaphore.acquire()
        
        index = None
        for i in range(len(self.__tokens)):
            if self.__tokens[i].token == token:
                index = i
                break
            
        self.__semaphore.release()

        return None if index is None else self.__tokens[index].user_id

    # Remove old tokens
    def __removeInactiveTokens(self):
        captured_time = datetime.now()

        self.__semaphore.acquire()

        indexes = list()
        for i in range(len(self.__tokens)):
            if self.__tokens[i].last_request_time + TTL < captured_time:
                indexes.append(i)

        for i in range(len(indexes) - 1, -1, -1):
            self.__tokens.pop(indexes[i])

        self.__semaphore.release()
