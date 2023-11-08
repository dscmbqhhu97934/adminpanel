import time

data = {
    "realtime": 0
}

data["realtime"] = 0

def sync_realtime():
    data["realtime"] = data["realtime"] + 1
    

def get_realtime():
    sync_realtime()
    return data["realtime"]


def lerp(start, end, t):
    sync_realtime()
    return start + (end - start) * t


def lerp_vec2(start, end, t):
    sync_realtime()
    return (lerp(start[0], end[0], t), lerp(start[1], end[1], t))

def easeInOutCubic(t):
    sync_realtime()
    return t * t * t * (t * (t * 6 - 15) + 10)