import numpy as np
import random

class AbstractSimulation:

    def __init__(self, number_steps):
        self.number_steps = number_steps
        self.show_intermediate_steps = True

    def initialize_sim(self):
        pass

    def run_one_step(self):
        raise NotImplementedError

    def print_sim_state(self):
        pass

    def run(self):
        self.initialize_sim()
        for a in range(self.number_steps):
            self.run_one_step()
            if self.show_intermediate_steps:
                self.print_sim_state()
        if not (self.show_intermediate_steps):
            self.print_sim_state()


class Rule90(AbstractSimulation):
    def __init__(self, number_steps, length, initial_density):
        super().__init__(number_steps)
        self.length = length
        self.initial_density = initial_density

        if initial_density <= 0:
            self.initial_density = 0
        elif initial_density >= 1:
            self.initial_density = 1

        self.current_state = np.zeros(self.length)
        self.next_state = np.zeros(self.length)

    def initialize_sim(self):
        self.time = 0

        random_indices = np.random.choice(
            range(self.length),
            size=int(round(self.initial_density * self.length)),
            replace=False)
        self.current_state.fill(0)
        self.current_state[random_indices] = 1

    def run_one_step(self):
        for i in range(self.length):
            if self.current_state[(i-1) % self.length] == self.current_state[(i+1) % self.length]:
                self.next_state[i] = 0
            else:
                self.next_state[i] = 1
        self.current_state, self.next_state = self.next_state, self.current_state
        self.time += 1

    def print_sim_state(self):
        print("At time {} the CA looks like: {}".format(
            self.time, ''.join(str(int(x)) for x in self.current_state)))
        #print(''.join('■' if x == 1 else ' ' for x in self.current_state))



ca = Rule90(20, 20, 0.4)
ca.run()
