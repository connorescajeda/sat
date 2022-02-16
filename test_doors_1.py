global state, goals
from pyhop_anytime import *

state = State('state')
state.key = Oset(['key1', 'key2','key3', 'key4','key5'])
state.keyloc = Oset([('A', 'key2'),('F', 'key3'),('E', 'key4')])
state.you = Oset(['main'])
state.pocket = Oset(['key1'])
state.room = Oset(['Main', 'A', 'B', 'C', 'D', 'E', 'F'])
state.key_room =  Oset([('key1', 'D' ), ('key2', 'F'),('key3', 'E'),('key4', 'C') ])
state.room_locked = Oset(['C', 'D', 'E', 'F'])
state.room_open = Oset(['main', 'A', 'B'])
state.connected = Oset([('main', 'A'), ('main', 'B'), ('main', 'C'),
                        ('A', 'main'), ('A', 'D'),
                        ('B', 'main'), ('B', 'E'), ('B', 'F'),
                        ('C', 'main'), ('C', 'E'),
                        ('D', 'A'), ('D', 'F'),
                        ('E', 'B'), ('E', 'C'),
                        ('F', 'B'), ('F', 'D')])
state.last = Oset([])

state.backpack = Oset([])
state.gold = Oset(['A', 'F', 'C'])

goals = State('goals')
goals.amount = Oset([3])
