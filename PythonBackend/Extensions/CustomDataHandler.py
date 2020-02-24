class CustomDataHandler:
    def __init__(self, data_link, get_data, custom_function=None):
        self.data_link = data_link
        self.old_data = get_data
        if custom_function is None:
            self.custom_func = self.pass_func
        else:
            self.custom_func = custom_function

    def custom_runner(self, new_data):
        old_data = self.old_data()
        self.data_link(self.custom_func(old_data, new_data))

    @staticmethod
    def pass_func(data):
        return data
