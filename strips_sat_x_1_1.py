from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star0'),('instrument1','star2'),('instrument2','star2')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite1'),('instrument2','satellite1')])
state.pointing = Oset([('satellite0','star6'),('satellite1','star0')])
state.power_avail = Oset(['satellite0','satellite1'])
state.supports = Oset([('instrument0','infrared0'),('instrument0','thermograph2'),('instrument1','infrared0'),('instrument1','infrared1'),('instrument1','thermograph2'),('instrument2','infrared1'),('instrument2','thermograph2')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon8','thermograph2'),('phenomenon9','infrared0'),('planet3','infrared1'),('planet5','thermograph2'),('star4','infrared1'),('star6','infrared1'),('star7','infrared0')])
goals.pointing = Oset([('satellite1','planet5')])

