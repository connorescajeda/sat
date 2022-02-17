from pyhop_anytime import *
global state, goals
state = State('state')
state.calibration_target = Oset([('instrument0','star4'),('instrument1','star0'),('instrument10','star3'),('instrument11','star1'),('instrument12','star3'),('instrument2','star4'),('instrument3','star1'),('instrument4','star1'),('instrument5','star3'),('instrument6','star0'),('instrument7','star3'),('instrument8','star3'),('instrument9','star1')])
state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument10','satellite3'),('instrument11','satellite3'),('instrument12','satellite4'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite1'),('instrument5','satellite1'),('instrument6','satellite1'),('instrument7','satellite2'),('instrument8','satellite2'),('instrument9','satellite2')])
state.pointing = Oset([('satellite0','star8'),('satellite1','phenomenon21'),('satellite2','star4'),('satellite3','phenomenon16'),('satellite4','phenomenon18')])
state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3','satellite4'])
state.supports = Oset([('instrument0','thermograph0'),('instrument0','thermograph2'),('instrument0','thermograph4'),('instrument1','thermograph3'),('instrument10','thermograph2'),('instrument11','thermograph0'),('instrument11','thermograph2'),('instrument11','thermograph4'),('instrument12','thermograph4'),('instrument2','image1'),('instrument3','thermograph3'),('instrument4','image1'),('instrument5','thermograph3'),('instrument6','image1'),('instrument6','thermograph0'),('instrument6','thermograph2'),('instrument7','thermograph0'),('instrument8','thermograph2'),('instrument8','thermograph3'),('instrument8','thermograph4'),('instrument9','thermograph2'),('instrument9','thermograph3')])
state.calibrated = Oset()
state.have_image = Oset()
state.power_on = Oset()

goals = State('goals')
goals.have_image = Oset([('phenomenon13','thermograph2'),('phenomenon17','thermograph4'),('phenomenon18','image1'),('phenomenon21','image1'),('phenomenon5','thermograph4'),('planet19','thermograph2'),('planet20','thermograph4'),('planet7','image1'),('star10','image1'),('star15','thermograph2'),('star22','thermograph3'),('star8','thermograph3'),('star9','image1')])

