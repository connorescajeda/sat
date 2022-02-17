from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star1'),('instrument1','star2'),('instrument2','star0'),('instrument3','star0')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite0'),('instrument3','satellite1')])
state.pointing = Oset([('satellite0','star4'),('satellite1','star0')])
state.power_avail = Oset(['satellite0','satellite1'])
state.supports = Oset([('instrument0','infrared0'),('instrument0','spectrograph2'),('instrument1','image1'),('instrument2','image1'),('instrument2','infrared0'),('instrument3','image1'),('instrument3','infrared0'),('instrument3','spectrograph2')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon5','spectrograph2'),('phenomenon7','spectrograph2'),('star3','infrared0'),('star4','spectrograph2')])
goals.pointing = Oset([('satellite0','phenomenon5')])

