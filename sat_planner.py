from satellite import *
from pyhop_anytime import *

def start(state, goals):
    have = [(loc, supp) for loc, supp in state.have_image]
    needed = [supp for loc, supp in goals.have_image if (loc, supp) not in have]
    try:
        pointer_goal = [item for item in goals.pointing]
    except AttributeError:
        pointer_goal = []
    count = 0
    if len(pointer_goal) != 0:
        for item in goals.pointing:
            if item in state.pointing:
                count += 1

    if len(pointer_goal) == count and goals.have_image == state.have_image:
        return TaskList(completed=True)
    elif goals.have_image == state.have_image:
        return TaskList([('point_time', goals)])
    else:
        return TaskList([('activate', needed, goals), ('start', goals)])


def activate(state, needed, goals):
    i = ""
    sat = ""
    c_target = ""
    current = ""
    support = ""
    for inst, supp in state.supports:
        if supp in needed:
            i = inst
            support = supp
            break
    for inst, sate in state.on_board:
        if inst == i:
            sat = sate
            break
    for inst, calib in state.calibration_target:
        if inst == i:
            c_target = calib
            break
    for sate, loc in state.pointing:
        if sat == sate:
            current = loc
            break

    if (i, sat) in state.on_board and sat not in state.power_avail:
        inst = ""
        for i_t in state.power_on:
            inst = i_t
        return TaskList([('switch_off', inst, sat), ('switch_on', i, sat), ('turn_to', sat, c_target, current), ('calibrate', sat, i, c_target), ('action', sat, i, c_target, goals, support)])

    elif i not in state.power_on and current != c_target:
        return TaskList([('switch_on', i, sat), ('turn_to', sat, c_target, current), ('calibrate', sat, i, c_target), ('action', sat, i, c_target, goals, support)])
    elif current == c_target:
        return TaskList([('switch_on', i, sat), ('calibrate', sat, i, c_target), ('action', sat, i, c_target, goals, support)])
    else:
        return TaskList([('action', sat, i, current, goals, support)])

def action(state, sat, i, current, goals, support):
    supports = [(inst, supp) for inst, supp in state.supports if inst == i]
    location = [(loc, supp) for loc, supp in goals.have_image if (i, supp) in supports and (loc, supp) not in state.have_image]

    return TaskList([('turn_to', sat, location[0][0], current), ('take_image', sat, location[0][0], i, location[0][1])])

def point_time(state, goals):
    sats = [sat for sat,loc in goals.pointing]
    goal = [(sat, loc) for sat,loc in goals.pointing]
    current = [(sat, loc) for sat, loc in state.pointing if sat in sats]
    trip = []
    for sat, loc in current:
        for sat2, loc2 in goal:
            if sat == sat2:
                trip.append((sat, loc, loc2))
    return TaskList([[('turn_to', sat, new, old)]for sat,old, new in trip])


def make_satellite_planner():
    planner = Planner()
    planner.declare_operators(calibrate, switch_off, switch_on, take_image, turn_to)
    planner.declare_methods(start, activate, action, point_time)
    return planner


if __name__ == '__main__':
    anyhop_main(make_satellite_planner())