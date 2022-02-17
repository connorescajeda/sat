from satellite import *
from pyhop_anytime import *
# To install pyhop_anytime: pip3 install git+https://github.com/gjf2a/pyhop_anytime


# Every pyhop planner should have a method named start which sets up the initial task list from the goals
def start(state, goals):
    supports = set([item[1] for item in goals.have_image])
    insts = set()
    sats = set()
    i_sat = set()
    for (inst, supp) in state.supports:
        if supp in supports:
            supports.remove(supp)
            insts.add(inst)
    for (inst, sat) in state.on_board:
        if inst in insts:
            sats.add(sat)
            i_sat.add((inst, sat))
    if state.have_image == goals.have_image:
        return TaskList(completed=True)
    else:
        return TaskList([('activate', insts, sats, i_sat, goals), ('start', goals)])


def activate(state, insts, sats, i_sat, goals):
    total_pics = [support for loc, support in goals.have_image]
    total = [pic for pic in state.have_image]
    insts_on = [inst for inst in state.power_on]
    used = set()
    calib = [inst for inst in state.calibrated]
    inst_t = [inst for inst in state.power_on]
    amount = 0
    pair = []
    for inst in inst_t:
        for (inst2, sat) in state.on_board:
            if inst2 == inst and sat in sats:
                pair.append((inst, sat))
    for (inst, support) in state.supports:
        if inst in calib:
            used.add(inst)
            for support2 in total_pics:
                if support == support2:
                    amount += 1
                    total_pics.remove(support2)
    for inst in insts:
        if inst in state.power_on:
            used.add(inst)

    if len(sats) != len(insts_on):
        return TaskList([[('switch_on', inst, sat)] for (inst, sat) in i_sat if inst not in used])
    elif len(total) != amount or amount == 0:
        return TaskList([[('turn_cal', inst, sat, calib, goals, len(sats)), ('activate', insts, sats, i_sat, goals)] for (inst, sat) in pair])
    else:
        return TaskList([[('reset', inst, calib, sat, i_sat, goals)] for inst, sat in i_sat if inst in state.power_on])




def turn_cal(state, inst, sat, calib, goals, check):
    calibration = [location for inst_t, location in state.calibration_target if inst_t == inst]
    pointing = [location for (sat_t, location) in state.pointing if sat == sat_t]
    if len(calib) != check:
        return TaskList([('turn_to', sat, calibration[0], pointing[0]), ('calibrate', sat, inst, calibration[0])])
    else:
        supports = [support for inst, support in state.supports if inst in calib]
        goal = [(location, support) for location, support in goals.have_image if support in supports]
        uses = []
        for (location, support) in goal:
            for (inst, support_t) in state.supports:
                if support == support_t and inst in calib and (location, support) not in state.have_image:
                    uses.append((inst, location, support))
        return TaskList([[('turn_to', sat, location , pointing[0]), ('take_image', sat, location, inst, support), ] for (inst, location, support) in uses])


def reset(state, inst, calib ,sat, i_sat, goals):
    insts = [insts for insts, sat in i_sat]
    sats = [sat for insts, sat in i_sat]
    if inst in calib:
        return TaskList([('switch_off', inst, sat), ('activate', insts, sats, i_sat, goals)])





##SOMETHING WITH POWERING UP DIFFERENT INSTRUMENTS, AND CALIBRATING THEM


## WRITE ADDITIONAL METHODS HERE ##


def make_satellite_planner():
    planner = Planner()
    planner.declare_operators(calibrate, switch_off, switch_on, take_image, turn_to)
    planner.declare_methods(start, activate, turn_cal, reset)
    return planner


if __name__ == '__main__':
    anyhop_main(make_satellite_planner())