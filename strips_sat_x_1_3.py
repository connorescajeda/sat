from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star0'),('instrument1','groundstation2')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0')])
state.pointing = Oset([('satellite0','planet4')])
state.power_avail = Oset(['satellite0'])
state.supports = Oset([('instrument0','infrared0'),('instrument0','infrared1'),('instrument1','image2'),('instrument1','infrared0'),('instrument1','infrared1')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon5','image2'),('phenomenon6','infrared0'),('planet3','infrared0'),('planet4','infrared0'),('star7','infrared0')])

