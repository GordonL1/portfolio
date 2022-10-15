# This simulates a Think-A-Dot (https://en.wikipedia.org/wiki/Think-a-Dot)
# Given a starting position and an ending position, this can determine the quickest series of moves to get between the two

# for n in range(2**8):
#   print('{0:08b}'.format(n))

# new_list = []
# string = ""
# new_list = [int(i)>0 for i in string]
def string_to_bool(string):
  return [int(i)>0 for i in string]


class ThinkADot:
  def __init__(self, state = [0,0,0,0,0,0,0,0]): # Initial state of Think A Dot
      self.state = state
      self.new_state = self.state[::]
    

  def s(self, pos):
    if self.state[pos] == 1:
        self.new_state[pos] = 0
    elif self.state[pos] == 0:
        self.new_state[pos] = 1
          
  def state3(self):
      if self.state[3] == 0:
          self.s(6)
      else:
          self.s(5)
      self.s(3)
          
  def state4(self):
      if self.state[4] == 0:
          self.s(7)
      else:
          self.s(6)
      self.s(4)
      
  def state0(self):
      if self.state[0] == 0:
          self.s(5)
      else:
          self.state3()
      self.s(0)
      
  def state1(self):
      if self.state[1] == 0:
          self.state4()
      else:
          self.state3()
      self.s(1)
      
  def state2(self):
      if self.state[2] == 0:
          self.state4()
      else:
          self.s(7)
      self.s(2)
  
  def transition(self, column): #Columns 1-3
      self.new_state = self.state[::]
      if column == 0:
          self.state0()
      elif column == 1:
          self.state1()
      elif column == 2:
          self.state2()
      else:
          print("Invalid column number. Please try a column between 1 and 3.")
      
      return self.new_state
    
  def __repr__(self, mode = 0):
          a = str(self.state[0])
          b = str(self.state[1])
          c = str(self.state[2])
          d = str(self.state[3])
          e = str(self.state[4])
          f = str(self.state[5])
          g = str(self.state[6])
          h = str(self.state[7])
          return a+" "+b+" "+c+"\n "+d+" "+e+" \n"+f+" "+g+" "+h

def state_to_idx(state):
  return sum(val*(2**idx) for (idx, val) in enumerate(state[::-1]))

STATES = [ThinkADot(string_to_bool('{0:08b}'.format(n))) for n in range(2**8)]

def shortest_path(starting_state): # <- ThinkADot

  candidate_distance = {s: (256, []) for s in STATES}
  candidate_distance[starting_state] = (0, [])

  cur_states = [starting_state]

  # for each of the states in cur_states, find all its neighbors, check if there is a better solution, if so, update distance and add the neighbor to a new list (new_states?), repeat the process for the new_states 
  while len(cur_states) != 0:
    new_states = []

    for state in cur_states:
      # state.transition
      neighbors = [STATES[state_to_idx(state.transition(x))] for x in range(3)]

      for (drop_pos, neighbor) in enumerate(neighbors):

        if candidate_distance[state][0] + 1 < candidate_distance[neighbor][0]:
          new_states.append(neighbor)
          candidate_distance[neighbor] = (candidate_distance[state][0] + 1, candidate_distance[state][1] + [drop_pos])
    
    # repeat with new_states
    cur_states = new_states

  return candidate_distance


start_position =  string_to_bool("00000000")
target_position = string_to_bool("00011000")
start_state = STATES[state_to_idx(start_position)]
target_state = STATES[state_to_idx(target_position)]
distances = shortest_path(start_state)
print(distances[target_state])
