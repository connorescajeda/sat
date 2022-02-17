from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star3'),('instrument1','star4'),('instrument10','star2'),('instrument2','star2'),('instrument3','star2'),('instrument4','star3'),('instrument5','star3'),('instrument6','star2'),('instrument7','star0'),('instrument8','groundstation1'),('instrument9','star0')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument10','satellite4'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite1'),('instrument5','satellite1'),('instrument6','satellite2'),('instrument7','satellite3'),('instrument8','satellite4'),('instrument9','satellite4')])
state.pointing = Oset([('satellite0','star0'),('satellite1','planet11'),('satellite2','phenomenon6'),('satellite3','planet10'),('satellite4','star9')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3','satellite4'])
state.supports = Oset([('instrument0','image4'),('instrument0','infrared1'),('instrument1','image2'),('instrument1','image4'),('instrument1','spectrograph0'),('instrument10','image2'),('instrument10','image4'),('instrument10','infrared1'),('instrument2','image2'),('instrument3','image2'),('instrument3','image3'),('instrument3','image4'),('instrument4','image2'),('instrument4','image3'),('instrument5','image4'),('instrument5','infrared1'),('instrument5','spectrograph0'),('instrument6','image2'),('instrument6','spectrograph0'),('instrument7','image3'),('instrument7','image4'),('instrument7','spectrograph0'),('instrument8','image3'),('instrument8','image4'),('instrument8','infrared1'),('instrument9','image4')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon12','image3'),('phenomenon13','spectrograph0'),('phenomenon6','image3'),('phenomenon7','infrared1'),('phenomenon8','image2'),('planet10','image4'),('planet11','spectrograph0'),('planet5','image2'),('star14','image4'),('star9','image3')])
goals.pointing = Oset([('satellite0','phenomenon7'),('satellite3','star9'),('satellite4','planet5')])

