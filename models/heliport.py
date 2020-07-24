

class Heliport(object):

    def __init__(self, pad_count, signallers=4):
        self.pad_count = pad_count
        self.signallers = signallers
        self.pads = [Helipad() for p in range(pad_count)] 
    
    def request_land(self):
        for pad in self.pads:
            avaliable_id = pad.is_free()
            if avaliable_id:
                pad.occupied = True
                return avaliable_id
        return False 
    
    def land(self, pad_id, heli_id=1):
        for pad in self.pads:
            if pad.pad_id == pad_id:
                pad.inbound(heli_id)
                return True
        return False
    
    def leave(self, pad_id):
        for pad in self.pads:
            if pad.pad_id == pad_id:
                pad.outbound()
                return True 
        return False 



class Helipad(object):

    def __init(self, pad_id): 
        self.heli_id = None
        self.occupied = False 
        self.pad_id = pad_id
    
    def is_free(self):
        """Check if pad can accept inbound""" 
        if not (self.occupied):
            return self.pad_id
        return False
    
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
    

    
