from sys import maxsize


class Address:
    def __init__(self, firstname=None, lastname=None, mobile=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.mobile = mobile
        self.id = id

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id
                ) and self.firstname == other.firstname and (
                self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
