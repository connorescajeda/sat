import copy
import sys


class State:
    def __init__(self, name):
        self.__name__ = name


class Planner:
    def __init__(self, verbose=0):
        self.opeartors = {}
        self.methods = {}
        self.verbose = verbose

    def declare_operators(self, *op_list):
        self.opeartors.update({op.__name__:op for op in op_list})

    def declare_methods(self, task_name, *method_list):
        self.methods.update({task_name: list(method_list)})

    def print_operators(self):
        print(f'OPERATORS: {", ".join(self.opeartors)}')

    def print_methods(self):
        print('{:<14}{}'.format('TASK:','METHODS:'))
        for task in self.methods:
            print('{:<14}'.format(task) + ', '.join([f.__name__ for f in self.methods[task]]))

    def log(self, min_verbose, msg):
        if self.verbose >= min_verbose:
            print(msg)

    def log_state(self, min_verbose, msg, state):
        if self.verbose >= min_verbose:
            print(msg)
            print_state(state)

    def anyhop(self, state, tasks):
        self.log(1, f"** pyhop, verbose={self.verbose}: **\n   state = {state.__name__}\n   tasks = {tasks}")
        options = [PlanStep([], tasks, state)]
        while len(options) > 0:
            candidate = options.pop()
            self.log(2, f"depth {candidate.depth()} tasks {candidate.tasks}")
            if candidate.complete():
                self.log(3, f"depth {candidate.depth()} returns plan {candidate.plan}")
                self.log(1, f"** result = {candidate.plan}\n")
                return candidate.plan
            else:
                options.extend(candidate.successors(self))


def print_state(state, indent=4):
    if state is not None:
        for (name,val) in vars(state).items():
            if name != '__name__':
                for x in range(indent): sys.stdout.write(' ')
                sys.stdout.write(state.__name__ + '.' + name)
                print(' =', val)
    else:
        print('False')


class PlanStep:
    def __init__(self, plan, tasks, state):
        self.plan = plan
        self.tasks = tasks
        self.state = state

    def depth(self):
        return len(self.plan)

    def complete(self):
        return len(self.tasks) == 0

    def successors(self, planner):
        options = []
        task1 = self.tasks[0]
        if task1[0] in planner.opeartors:
            planner.log(3, f"depth {self.depth()} action {task1}")
            operator = planner.opeartors[task1[0]]
            newstate = operator(copy.deepcopy(self.state), *task1[1:])
            planner.log_state(3, f"depth {self.depth()} new state:", newstate)
            if newstate:
                options.append(PlanStep(self.plan + [task1], self.tasks[1:], newstate))
        if task1[0] in planner.methods:
            planner.log(3, f"depth {self.depth()} method instance {task1}")
            relevant = planner.methods[task1[0]]
            for method in relevant:
                subtask_options = method(self.state, *task1[1:])
                if subtask_options is not None:
                    for subtasks in subtask_options:
                        planner.log(3, f"depth {self.depth()} new tasks: {subtasks}")
                        options.append(PlanStep(self.plan, subtasks + self.tasks[1:], self.state))
        if len(options) > 0:
            planner.log(3, f"depth {self.depth()} returns failure")
        return options
