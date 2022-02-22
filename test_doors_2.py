global state, goals
from pyhop_anytime import *

state = State('state')
state.key = Oset(['key1', 'key2','key3'])
state.keyloc = Oset([('C', 'key1'),('E', 'key2'),('F', 'key3')])
state.you = Oset(['main'])
state.pocket = Oset(['empty'])
state.room = Oset(['Main', 'A', 'B', 'C', 'D', 'E', 'F', 'I'])
state.key_room =  Oset([('key1', 'G' ), ('key2', 'F'),('key3', 'I')])
state.room_locked = Oset(['G', 'H', 'I', 'F'])
state.room_open = Oset(['main', 'A', 'B', 'C', 'D', 'E'])
state.connected = Oset([('main', 'A'),
                        ('A', 'main'), ('A', 'B'), ('A', 'C'),
                        ('B', 'D'), ('B', 'A'),
                        ('C', 'A'), ('C', 'G'),
                        ('D', 'B'), ('D', 'G'), ('D', 'E'),
                        ('E', 'F'),
                        ('F', 'E'), ('F', 'H'), ('F', 'I'),
                        ('G', 'C'), ('G', 'D'), ('G', 'H'),
                        ('H', 'G'), ('H', 'F'), ('H', 'I'),
                        ('I', 'H'), ('I', 'F')])
state.last = Oset([])

state.backpack = Oset([])
state.gold = Oset(['B', 'E', 'F'])

goals = State('goals')
goals.amount = Oset([3])