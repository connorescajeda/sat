from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star1'),('instrument1','groundstation0'),('instrument2','groundstation2'),('instrument3','groundstation4'),('instrument4','star1'),('instrument5','star1'),('instrument6','groundstation4'),('instrument7','groundstation0')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite3'),('instrument7','satellite3')])
state.pointing = Oset([('satellite0','star6'),('satellite1','groundstation0'),('satellite2','star6'),('satellite3','groundstation2')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3'])
state.supports = Oset([('instrument0','image1'),('instrument0','image3'),('instrument1','image3'),('instrument2','image0'),('instrument3','image0'),('instrument3','image2'),('instrument4','image0'),('instrument4','image1'),('instrument5','image0'),('instrument5','image1'),('instrument5','image2'),('instrument6','image0'),('instrument6','image1'),('instrument6','image2'),('instrument7','image0'),('instrument7','image1'),('instrument7','image3')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon5','image0'),('planet10','image0'),('planet11','image2'),('planet8','image0'),('planet9','image3'),('star6','image1'),('star7','image0')])
goals.pointing = Oset([('satellite1','star1'),('satellite2','phenomenon5')])

