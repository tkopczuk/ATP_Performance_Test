from datetime import datetime

class AskThePonyCursorWrapper(object):
    def __init__(self, cursor, atp_wrapper):
        self.cursor = cursor
        self.atp_wrapper = atp_wrapper

    def execute(self, sql, params=()):
        start = datetime.now()
        try:
            return self.cursor.execute(sql, params)
        finally:
            stop = datetime.now()
            duration = stop - start
            self.atp_wrapper.time_spent_in_db += duration.total_seconds()
#            print duration, self.atp_wrapper.time_spent_in_db

    def executemany(self, sql, param_list):
        start = datetime.now()
        try:
            return self.cursor.executemany(sql, param_list)
        finally:
            stop = datetime.now()
            duration = stop - start
            self.atp_wrapper.time_spent_in_db += duration.total_seconds()
 #           print duration, self.atp_wrapper.time_spent_in_db

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return getattr(self.cursor, attr)

    def __iter__(self):
        return iter(self.cursor)