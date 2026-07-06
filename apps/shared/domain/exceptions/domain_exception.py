class AppErrorException(Exception):
    default_message = "Something went wrong"

    def __init__(self, message=None):

        if message is None:
            message = self.default_message

        super().__init__(message)
