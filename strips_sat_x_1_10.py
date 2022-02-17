from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star1'),('instrument1','groundstation3'),('instrument10','star0'),('instrument2','groundstation3'),('instrument3','star4'),('instrument4','star2'),('instrument5','star0'),('instrument6','groundstation3'),('instrument7','star4'),('instrument8','star4'),('instrument9','star2')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument10','satellite4'),('instrument2','satellite1'),('instrument3','satellite1'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite3'),('instrument7','satellite3'),('instrument8','satellite4'),('instrument9','satellite4')])
state.pointing = Oset([('satellite0','star0'),('satellite1','star4'),('satellite2','star1'),('satellite3','groundstation3'),('satellite4','planet10')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3','satellite4'])
state.supports = Oset([('instrument0','image4'),('instrument1','infrared0'),('instrument1','spectrograph1'),('instrument10','image2'),('instrument10','image4'),('instrument2','image2'),('instrument2','infrared0'),('instrument3','infrared0'),('instrument3','infrared3'),('instrument4','image4'),('instrument4','infrared0'),('instrument4','spectrograph1'),('instrument5','image2'),('instrument5','infrared0'),('instrument5','infrared3'),('instrument6','infrared0'),('instrument6','infrared3'),('instrument7','image4'),('instrument7','infrared3'),('instrument7','spectrograph1'),('instrument8','image4'),('instrument8','spectrograph1'),('instrument9','infrared3')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon13','image4'),('phenomenon14','spectrograph1'),('phenomenon8','image4'),('planet10','infrared3'),('planet5','image4'),('planet9','infrared0'),('star12','image4'),('star15','spectrograph1'),('star16','image2'),('star6','infrared3'),('star7','image4')])
goals.pointing = Oset([('satellite4','planet9')])

