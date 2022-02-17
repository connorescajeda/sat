from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star3'),('instrument1','star2'),('instrument2','star4'),('instrument3','groundstation1'),('instrument4','star4'),('instrument5','star0'),('instrument6','star3'),('instrument7','star0'),('instrument8','star3'),('instrument9','star4')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite1'),('instrument5','satellite1'),('instrument6','satellite2'),('instrument7','satellite2'),('instrument8','satellite3'),('instrument9','satellite3')])
state.pointing = Oset([('satellite0','phenomenon14'),('satellite1','star4'),('satellite2','star6'),('satellite3','phenomenon5')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3'])
state.supports = Oset([('instrument0','image0'),('instrument0','thermograph1'),('instrument1','spectrograph3'),('instrument1','thermograph1'),('instrument1','thermograph2'),('instrument2','spectrograph3'),('instrument3','image0'),('instrument3','thermograph2'),('instrument4','thermograph1'),('instrument5','spectrograph3'),('instrument5','thermograph1'),('instrument5','thermograph2'),('instrument6','thermograph1'),('instrument6','thermograph2'),('instrument7','image0'),('instrument7','thermograph1'),('instrument7','thermograph2'),('instrument8','image0'),('instrument9','image0'),('instrument9','spectrograph3'),('instrument9','thermograph1')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon12','image0'),('phenomenon13','thermograph1'),('phenomenon14','thermograph2'),('phenomenon5','thermograph1'),('phenomenon8','image0'),('phenomenon9','image0'),('planet11','thermograph2'),('star10','spectrograph3'),('star6','thermograph1'),('star7','spectrograph3')])

