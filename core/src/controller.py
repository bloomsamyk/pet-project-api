from DB import DB


class Controller:
    db = DB()

    def __init__(self):
        print('Controller init')

    def get_data(self):
        print('validate form')
        # validate form
        return self.db.get_data()

