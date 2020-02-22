class AlreadyCreatedError(Exception):
    def __init__(self, message):
        super(AlreadyCreatedError, self)


class CouldNotUpdateSMF(Exception):
    def __init__(self, message, data):
        super(CouldNotUpdateSMF, self)
        raise (message, "Was trying to update with the following Data", data)


class ErrorWillCreatingBucket(Exception):
    def __init__(self, message, data):
        message = "Message: {m}, Status of the Bucket Management: {bm} Status of the Bucket Creation: {bc}".format(
            m=message, bm=data[0], bc=data[1])
        raise Exception(message)
