from random import *
from copy import deepcopy
from math import exp

# switching times for all jobs 
job_matrix = [
    [0, 12, 10],
    [4, 0, 8],
    [6, 10, 0]
]

# corresponding job for machine
machine_matrix = [
    [10, 4, 8],
    [12, 9, 5]
]


#Initial temperature, cooling_rate and initial array for solution
temperature = 10000
cooling_rate = 0.005
initial_solution = [-1, 3, 2, 1]  


def create_neighbour_solution(current_solution):
    neighbour_solution = deepcopy(current_solution)

    r1 = randint(0, 3)
    r2 = randint(0, 3)

    while r1 == r2:
        r2 = randint(0, 3)

    neighbour_solution[r1], neighbour_solution[r2] = neighbour_solution[r2], neighbour_solution[r1]

    return neighbour_solution


def calculate_machine_cost(machine, machine_name):
    if machine_name == "machine1":
        m = 0
    elif machine_name == "machine2":
        m = 1

    length_machine = len(machine)
    cost_machine = 0

    if length_machine > 0:
        i = 0
        while i < length_machine:
            cost_machine += machine_matrix[m][machine[i] - 1]
            i += 1

    return cost_machine


def find_job_cost(machine):
    length_machine = len(machine)
    cost_job = 0

    if length_machine == 2:
        cost_job = job_matrix[machine[0] - 1][machine[1] - 1]
    elif length_machine == 3:
        cost_job = job_matrix[machine[0] - 1][machine[1] - 1] + job_matrix[machine[1] - 1][machine[2] - 1]

    return cost_job


def find_cost(solution):
    machine1 = []
    machine2 = []

    i = 0
    while i < len(solution):
        if solution[i] == -1:
            break
        machine1.append(solution[i])
        i += 1

    i += 1

    while i < len(solution):
        machine2.append(solution[i])
        i += 1
        
    cost_machine1 = calculate_machine_cost(machine1, "machine1")
    job_cost_machine1 = find_job_cost(machine1)
    total_cost_machine1 = cost_machine1 + job_cost_machine1

    cost_machine2 = calculate_machine_cost(machine2, "machine2")
    job_cost_machine2 = find_job_cost(machine2)
    total_cost_machine2 = cost_machine2 + job_cost_machine2

    if total_cost_machine1 < total_cost_machine2:
        max_cost_machine = total_cost_machine2
    else:
        max_cost_machine = total_cost_machine1

    return max_cost_machine

current_solution = deepcopy(initial_solution)
best_solution = deepcopy(current_solution)

while temperature > 1:

    new_solution = create_neighbour_solution(current_solution)
    current_solution_cost = find_cost(current_solution)
    
    print(current_solution, current_solution_cost)

    new_solution_cost = find_cost(new_solution);
    best_solution_cost = find_cost(best_solution)
    if new_solution_cost <= current_solution_cost:
        current_solution = new_solution
        if new_solution_cost <= best_solution_cost:
            best_solution = deepcopy(new_solution)
            
    elif exp( (current_solution_cost - new_solution_cost) / temperature) > uniform(0,1):
        current_solution = new_solution

    temperature *= 1 - cooling_rate

print(best_solution, find_cost(best_solution))
