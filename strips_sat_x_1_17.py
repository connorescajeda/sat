from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star0'),('instrument1','star2'),('instrument2','star3'),('instrument3','star4'),('instrument4','star4'),('instrument5','groundstation1'),('instrument6','star4'),('instrument7','star2'),('instrument8','star2'),('instrument9','star4')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite1'),('instrument5','satellite2'),('instrument6','satellite3'),('instrument7','satellite4'),('instrument8','satellite4'),('instrument9','satellite4')])
state.pointing = Oset([('satellite0','planet16'),('satellite1','star4'),('satellite2','star15'),('satellite3','phenomenon6'),('satellite4','star14')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3','satellite4'])
state.supports = Oset([('instrument0','infrared1'),('instrument0','spectrograph4'),('instrument1','infrared0'),('instrument1','infrared1'),('instrument2','infrared0'),('instrument2','infrared1'),('instrument3','infrared0'),('instrument3','spectrograph4'),('instrument4','infrared0'),('instrument4','infrared3'),('instrument4','thermograph2'),('instrument5','infrared1'),('instrument6','infrared1'),('instrument7','infrared1'),('instrument7','infrared3'),('instrument8','infrared0'),('instrument8','infrared3'),('instrument8','spectrograph4'),('instrument9','infrared1'),('instrument9','infrared3'),('instrument9','spectrograph4')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon13','spectrograph4'),('phenomenon17','spectrograph4'),('phenomenon21','thermograph2'),('phenomenon24','infrared0'),('phenomenon6','spectrograph4'),('planet10','thermograph2'),('planet11','infrared3'),('planet16','infrared1'),('planet20','thermograph2'),('planet5','infrared0'),('planet8','infrared1'),('star14','thermograph2'),('star15','infrared3'),('star18','spectrograph4'),('star19','thermograph2'),('star22','infrared1'),('star23','spectrograph4'),('star7','infrared0'),('star9','spectrograph4')])

