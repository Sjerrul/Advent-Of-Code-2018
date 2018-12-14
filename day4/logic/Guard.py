class Guard(object):
    id = None
    minutes = [60]

    def __init__(self, id_):
        self.id = id_
        self.minutes = [0]*60

    def __repr__(self):
        return "<Guard #%s - %s>" % (self.id, self.minutes)

    def get_minutes_sleeping(self):
        return sum(self.minutes)
