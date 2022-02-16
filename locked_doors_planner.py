from pyhop_anytime import *
from locked_doors import *

def start(state, goals):
    neighbors = [(room1, room2) for room1,room2 in state.connected if room1 in state.you]
    backpack = [gold for gold in state.backpack]
    goal_amount = goals.amount.get_first()
    if len(backpack) == goal_amount:
        return TaskList(completed=True)
    else:
        return TaskList([('go', neighbors), ('start', goals)])

def go(state, neighbors):
    current = state.you.get_first()
    pocket = state.pocket.get_first()
    if current in state.gold:
        return TaskList([('acquire_gold', current)])
    if pocket == 'empty':
        for (room, key) in state.keyloc:
            if room in state.you:
                return TaskList([('pickup', room, key)])

    if "empty" != pocket:
        for (key, room) in state.key_room:
            for (you, neighbor) in neighbors:
                if room == neighbor and key == pocket:
                    return TaskList([('door', pocket, current, room)], [('go', neighbors)])

    return TaskList([[('move', current, neighbor[0], neighbor[1])] for neighbor in neighbors])

def door(state, key, current, room):
    return TaskList([('open_door', key, current, room)])


def make_door_planner():
    planner = Planner()
    planner.declare_operators(open_door, move, pickup, acquire_gold)
    planner.declare_methods(start, go, door)
    return planner

if __name__ == '__main__':
    anyhop_main(make_door_planner())