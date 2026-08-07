class Logger:

    def __init__(self):
        self.logger_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logger_dict:
            self.logger_dict[message]= timestamp
            return True
        else:
            curr_timestamp = self.logger_dict[message]
            if timestamp - curr_timestamp <10:
                return False
            else: 
                self.logger_dict[message] = timestamp 
                return True




        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
