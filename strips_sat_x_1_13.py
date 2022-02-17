from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','groundstation2')])
state.on_board = Oset([('instrument0','satellite0')])
state.pointing = Oset([('satellite0','phenomenon6')])
state.power_avail = Oset(['satellite0'])
state.supports = Oset([('instrument0','thermograph0')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon4','thermograph0'),('phenomenon6','thermograph0'),('star5','thermograph0')])

