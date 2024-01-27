class RoseDictionary:
    def __init__(self):
        self.data = list()

    def __getitem__(self, key):
        for item in self.data:
            if item[0] == key:
                return item[1]

    def __setitem__(self, key, value):
        for item in self.data:
            if item[0] == key:
                item[1] = value
                return
        self.data.append([key, value])

    def pop_item(self, raise_error=False, default=None, error_msg=None):
        if not self.data:
            if raise_error:
                raise KeyError(error_msg if error_msg is not None else 'error_msg')
            elif default is not None:
                return default
            else:
                print (error_msg) if error_msg is not None else print ('Dictionary was empty and no default value/message was specified.')
        else:
            key, value = self.data[-1]
            self.data = self.data[:-1]
            return value

    def get_item(self, key, raise_error=False, default=None, error_msg=None):
        for item in self.data:
            if item[0] == key:
                return item[1]
        if raise_error:
            raise KeyError(error_msg if error_msg is not None else 'error_msg')
        else:
            if default is not None:
                return default
            else:
                print (error_msg) if error_msg is not None else print('Value was not found and no default value/message was specified.')
