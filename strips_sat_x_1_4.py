from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star0'),('instrument1','groundstation3'),('instrument2','star2'),('instrument3','star0'),('instrument4','star2'),('instrument5','star0'),('instrument6','groundstation3'),('instrument7','star2'),('instrument8','star2')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite1'),('instrument2','satellite1'),('instrument3','satellite1'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite2'),('instrument7','satellite3'),('instrument8','satellite4')])
state.pointing = Oset([('satellite0','star8'),('satellite1','groundstation3'),('satellite2','star4'),('satellite3','phenomenon9'),('satellite4','phenomenon9')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3','satellite4'])
state.supports = Oset([('instrument0','spectrograph4'),('instrument1','infrared0'),('instrument1','infrared1'),('instrument2','infrared0'),('instrument2','infrared1'),('instrument3','infrared1'),('instrument3','spectrograph4'),('instrument3','thermograph2'),('instrument4','image3'),('instrument4','infrared0'),('instrument4','infrared1'),('instrument5','spectrograph4'),('instrument5','thermograph2'),('instrument6','infrared0'),('instrument7','image3'),('instrument8','infrared0'),('instrument8','infrared1'),('instrument8','spectrograph4')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon15','infrared0'),('phenomenon7','infrared1'),('planet13','spectrograph4'),('planet14','thermograph2'),('planet16','image3'),('planet6','infrared1'),('star10','thermograph2'),('star11','infrared1'),('star17','infrared0'),('star5','image3'),('star8','image3')])
goals.pointing = Oset([('satellite0','phenomenon9'),('satellite1','star4'),('satellite4','star11')])

