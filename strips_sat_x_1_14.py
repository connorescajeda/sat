from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star1'),('instrument1','star2'),('instrument2','star2'),('instrument3','star2'),('instrument4','star0')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite1'),('instrument2','satellite1'),('instrument3','satellite1'),('instrument4','satellite2')])
state.pointing = Oset([('satellite0','phenomenon8'),('satellite1','star6'),('satellite2','star6')])
state.power_avail = Oset(['satellite0','satellite1','satellite2'])
state.supports = Oset([('instrument0','infrared1'),('instrument0','spectrograph0'),('instrument1','infrared3'),('instrument2','infrared1'),('instrument2','infrared3'),('instrument2','thermograph2'),('instrument3','infrared1'),('instrument3','infrared3'),('instrument3','spectrograph0'),('instrument4','infrared3')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon8','spectrograph0'),('planet4','thermograph2'),('planet5','spectrograph0'),('star10','infrared3'),('star6','thermograph2'),('star7','infrared3'),('star9','infrared1')])

