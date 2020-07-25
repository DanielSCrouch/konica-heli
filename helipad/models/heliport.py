
class Heliport(object):

    def __init__(self, pad_count, signallers=4):
        self.pad_count = pad_count
        self.signallers = signallers
        self.pads = [Helipad(p) for p in range(1, pad_count + 1)]

    def request_land(self):
        for pad in self.pads:
            if pad.is_free():
                pad.occupied = True
                return pad.pad_id

    def land(self, pad_id, heli_id=1):

        for pad in self.pads:
            if pad.pad_id == int(pad_id):
                pad.inbound(heli_id)
                return True

    def leave(self, pad_id):
        for pad in self.pads:
            if pad.pad_id == int(pad_id):
                pad.outbound()
                return True


class Helipad(object):

    def __init__(self, pad_id):
        self.heli_id = None
        self.occupied = False
        self.pad_id = pad_id

    def is_free(self):
        """Check if pad can accept inbound"""
        return not self.occupied

    def inbound(self, heli_id):
        """Accept inbound helicopter"""
        self.heli_id = heli_id
        self.occupied = True

    def outbound(self):
        """Remove helictoper"""
        self.occupied = False
        self.heli_id = None


class SignalError(Exception):
    def __init__(self, msg):
        pass
