def calibrate(state, sat, instrument, object):
    if (instrument, sat) in state.on_board and (instrument, object) in state.calibration_target and (sat, object) in state.pointing and instrument in state.power_on:
        state.calibrated.add(instrument)
        return state


def switch_off(state, instrument, sat):
    if (instrument, sat) in state.on_board and instrument in state.power_on:
        state.power_on.discard(instrument)
        state.power_avail.add(sat)
        return state


def switch_on(state, instrument, sat):
    if (instrument, sat) in state.on_board and sat in state.power_avail:
        state.power_on.add(instrument)
        state.calibrated.discard(instrument)
        state.power_avail.discard(sat)
        return state


def take_image(state, sat, object, instrument, type):
    if instrument in state.calibrated and (instrument, sat) in state.on_board and (instrument, type) in state.supports and instrument in state.power_on and (sat, object) in state.pointing and instrument in state.power_on:
        state.have_image.add((object, type))
        return state


def turn_to(state, sat, new_object, old_object):
    if (sat, old_object) in state.pointing and new_object != old_object:
        state.pointing.add((sat, new_object))
        state.pointing.discard((sat, old_object))
        return state