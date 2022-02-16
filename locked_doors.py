from pyhop_anytime import *
def open_door(state, key, current, room):
    if key in state.key and key in state.pocket and room in state.room and (key, room) in state.key_room and room in state.room_locked and (current, room) in state.connected:
        state.pocket.discard(key)
        state.room_locked.discard(room)
        state.room_open.add(room)
        state.pocket.add("empty")
        return state

def move(state,you, start, end):
    if start in you and (start, end) in state.connected and end in state.room_open and end not in state.last:
        last = state.last.get_first()
        state.last.discard(last)
        state.last.add(start)
        state.you.discard(start)
        state.you.add(end)
        return state

def pickup(state, location, key):
    if "empty" in state.pocket and (location, key) in state.keyloc and location in state.you:
        state.pocket.discard("empty")
        state.pocket.add(key)
        state.keyloc.discard((location, key))
        return state

def acquire_gold(state, location):
    if location in state.gold:
        state.backpack.add(location)
        state.gold.discard(location)
    return state


