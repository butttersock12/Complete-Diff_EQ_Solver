import math
import time
import os
import plotly.graph_objects as go
import numpy as np
import sympy as sp
import sys

#   START TITLES

def differential_equation_calculator_title():
    print("""
#########################################################################################    
██████╗ ██╗███████╗███████╗███████╗██████╗ ███████╗███╗   ██╗████████╗██╗ █████╗ ██╗     
██╔══██╗██║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██║██╔══██╗██║     
██║  ██║██║█████╗  █████╗  █████╗  ██████╔╝█████╗  ██╔██╗ ██║   ██║   ██║███████║██║     
██║  ██║██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗██╔══╝  ██║╚██╗██║   ██║   ██║██╔══██║██║     
██████╔╝██║██║     ██║     ███████╗██║  ██║███████╗██║ ╚████║   ██║   ██║██║  ██║███████╗
╚═════╝ ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝
                                                                                         
        ███████╗ ██████╗ ██╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗                
        ██╔════╝██╔═══██╗██║   ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║                
        █████╗  ██║   ██║██║   ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║                
        ██╔══╝  ██║▄▄ ██║██║   ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║                
        ███████╗╚██████╔╝╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║                
        ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝                
                                                                                         
                ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗                         
                ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗                        
                ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝                        
                ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗                        
                ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║                        
                ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝                        
#########################################################################################""")
    return

def author_title():
    print("""                                                                                                                              
   ___         _       ___           __  _        ____             __    __  __  _ 
  / _ )__ __  (_)     / _ \__ _____ / /_(_)__    / __/__ ____  ___/ /__ / /_/ /_(_)
 / _  / // / _       / // / // (_-</ __/ / _ \  / _// _ `/ _ \/ _  / -_) __/ __/ / 
/____/\_, / (_)     /____/\_,_/___/\__/_/_//_/ /_/  \_,_/_//_/\_,_/\__/\__/\__/_/  
     /___/                                                                          """)
    return

def first_order_solver_title():
    print("""                                                                                                                              
______      _____     _______       _________                ________     ______                   
__<  /________  /_    __  __ \____________  /____________    __  ___/________  /__   ______________
__  /__  ___/  __/    _  / / /_  ___/  __  /_  _ \_  ___/    _____ \_  __ \_  /__ | / /  _ \_  ___/
_  / _(__  )/ /_      / /_/ /_  /   / /_/ / /  __/  /        ____/ // /_/ /  / __ |/ //  __/  /    
/_/  /____/ \__/      \____/ /_/    \__,_/  \___//_/         /____/ \____//_/  _____/ \___//_/     
                                                                                                   """)
    return

def separable_first_order_title():
    print('''
 __                            _     _        __       _                
/ _\ ___ _ __   __ _ _ __ __ _| |__ | | ___  / _\ ___ | |_   _____ _ __ 
\ \ / _ \ '_ \ / _` | '__/ _` | '_ \| |/ _ \ \ \ / _ \| \ \ / / _ \ '__|
_\ \  __/ |_) | (_| | | | (_| | |_) | |  __/ _\ \ (_) | |\ V /  __/ |   
\__/\___| .__/ \__,_|_|  \__,_|_.__/|_|\___| \__/\___/|_| \_/ \___|_|   
        |_|                                                             ''')
    return

def second_order_solver_title():
    print(""" 
 ___         _   ___         _             ___       _                
<_  >._ _  _| | | . | _ _  _| | ___  _ _  / __> ___ | | _ _  ___  _ _ 
 / / | ' |/ . | | | || '_>/ . |/ ._>| '_> \__ \/ . \| || | |/ ._>| '_>
<___>|_|_|\___| `___'|_|  \___|\___.|_|   <___/\___/|_||__/ \___.|_|  
                                                                     """)
    return

def homogenoues_solution_calculator_title():
    print("""    
    __  __                                                            
   / / / /___  ____ ___  ____  ____ ____  ____  ___  ____  __  _______
  / /_/ / __ \/ __ `__ \/ __ \/ __ `/ _ \/ __ \/ _ \/ __ \/ / / / ___/
 / __  / /_/ / / / / / / /_/ / /_/ /  __/ / / /  __/ /_/ / /_/ (__  ) 
/_/ /_/\____/_/ /_/ /_/\____/\__, /\___/_/ /_/\___/\____/\__,_/____/  
       _____       __      _/____/                                    
      / ___/____  / /_  __/ /_(_)___  ____                            
      \__ \/ __ \/ / / / / __/ / __ \/ __ \                           
     ___/ / /_/ / / /_/ / /_/ / /_/ / / / /                           
    /____/\____/_/\__,_/\__/_/\____/_/ /_/                            
         ______      __           __      __                          
        / ____/___ _/ /______  __/ /___ _/ /_____  _____              
       / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/              
      / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /                  
      \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/                   
                                                                     """)
    return

def complete_and_particular_solution_calculator_title():
    print("""    
                                                                                                                                
             ,-----.                        ,--.         ,--.                                ,--.                               
            '  .--./ ,---. ,--,--,--. ,---. |  | ,---. ,-'  '-. ,---.      ,--,--.,--,--,  ,-|  |                               
            |  |    | .-. ||        || .-. ||  || .-. :'-.  .-'| .-. :    ' ,-.  ||      \' .-. |                               
            '  '--'\' '-' '|  |  |  || '-' '|  |\   --.  |  |  \   --.    \ '-'  ||  ||  |\ `-' |                               
             `-----' `---' `--`--`--'|  |-' `--' `----'  `--'   `----'     `--`--'`--''--' `---'                                
,------.                  ,--.  ,--. `--'         ,--.                    ,---.         ,--.          ,--.  ,--.                
|  .--. ' ,--,--.,--.--.,-'  '-.`--' ,---.,--.,--.|  | ,--,--.,--.--.    '   .-'  ,---. |  |,--.,--.,-'  '-.`--' ,---. ,--,--,  
|  '--' |' ,-.  ||  .--''-.  .-',--.| .--'|  ||  ||  |' ,-.  ||  .--'    `.  `-. | .-. ||  ||  ||  |'-.  .-',--.| .-. ||      \ 
|  | --' \ '-'  ||  |     |  |  |  |\ `--.'  ''  '|  |\ '-'  ||  |       .-'    |' '-' '|  |'  ''  '  |  |  |  |' '-' '|  ||  | 
`--'      `--`--'`--'     `--'  `--' `---' `----' `--' `--`--'`--'       `-----'  `---' `--' `----'   `--'  `--' `---' `--''--' 
                         ,-----.        ,--.              ,--.          ,--.                                                    
                        '  .--./ ,--,--.|  | ,---.,--.,--.|  | ,--,--.,-'  '-. ,---. ,--.--.                                    
                        |  |    ' ,-.  ||  || .--'|  ||  ||  |' ,-.  |'-.  .-'| .-. ||  .--'                                    
                        '  '--'\| '-'  ||  |\ `--.'  ''  '|  |\ '-'  |  |  |  ' '-' '|  |                                       
                         `-----' `--`--'`--' `---' `----' `--' `--`--'  `--'   `---' `--'                                       
                                                                                                                               """)
    print("\033[1;31;40m    **Note: Any errors that arise indicate that the guess has failed and as such calculator will not work for that system**\033[0m")
    return

def root_calculator_title():
    print("""    
                                                                                                                                
8888888b.                   888          .d8888b.           888                   888          888                    
888   Y88b                  888         d88P  Y88b          888                   888          888                    
888    888                  888         888    888          888                   888          888                    
888   d88P .d88b.   .d88b.  888888      888         8888b.  888  .d8888b 888  888 888  8888b.  888888 .d88b.  888d888 
8888888P" d88""88b d88""88b 888         888            "88b 888 d88P"    888  888 888     "88b 888   d88""88b 888P"   
888 T88b  888  888 888  888 888         888    888 .d888888 888 888      888  888 888 .d888888 888   888  888 888     
888  T88b Y88..88P Y88..88P Y88b.       Y88b  d88P 888  888 888 Y88b.    Y88b 888 888 888  888 Y88b. Y88..88P 888     
888   T88b "Y88P"   "Y88P"   "Y888       "Y8888P"  "Y888888 888  "Y8888P  "Y88888 888 "Y888888  "Y888 "Y88P"  888     
                                                                                                                     """)
    return

def guess_table_title():
    print("""                                                                                                                              
   ___                  _____     _    _      
  / __|_  _ ___ ______ |_   _|_ _| |__| |___  
 | (_ | || / -_|_-<_-<   | |/ _` | '_ \ / -_) 
  \___|\_,_\___/__/__/   |_|\__,_|_.__/_\___| 
                                              """)
    return

def graphing_title():
    print("""                                                                                                                              
   ____                 _     _             
  / ___|_ __ __ _ _ __ | |__ (_)_ __   __ _ 
 | |  _| '__/ _` | '_ \| '_ \| | '_ \ / _` |
 | |_| | | | (_| | |_) | | | | | | | | (_| |
  \____|_|  \__,_| .__/|_| |_|_|_| |_|\__, |
                 |_|                  |___/  """)
    return

def homogenoues_input_title():
    print("""    
 _     _                                                           
| |   | |                                                          
| |__ | | ___  ____   ___   ____  ____ ____   ____ ___  _   _  ___ 
|  __)| |/ _ \|    \ / _ \ / _  |/ _  )  _ \ / _  ) _ \| | | |/___)
| |   | | |_| | | | | |_| ( ( | ( (/ /| | | ( (/ / |_| | |_| |___ |
|_|   |_|\___/|_|_|_|\___/ \_|| |\____)_| |_|\____)___/ \____(___/ 
                          (_____|                                  
                 _____                                             
                (_____)                  _                         
                   _   ____  ____  _   _| |_                       
                  | | |  _ \|  _ \| | | |  _)                      
                 _| |_| | | | | | | |_| | |__                      
                (_____)_| |_| ||_/ \____|\___)                     
                            |_|                                    """)
    return

# END TITLES

def solve_separable_first_order():
    print("In the form: da/db = AB")
    #getting user info
    resp_to1 = input("da = d")
    resp_to2 = input("db = d")
    function1 = input("Function for A = ")
    function2 = input("Function for B = ")
    
    #moving A to lhs 
    sep_left = ["1/(", function1, ")"]
    left = "".join(sep_left)

    #integrating
    int_left = find_integral(left, resp_to1)
    int_right = find_integral(function2, resp_to2)
    total_integral = [str(int_left), str(int_right)]
    eqn = "=".join(total_integral)
    simplifed = simplify_equation(eqn, function1)
    print(str(simplifed))
    insert1 = [resp_to1, "=", str(simplifed[1, 1])]
    insert2 = "".join(insert1)
    print(insert2)


def solve_integrating_factor_first_order():
    print("Not finished")
    request_executed()

def solve_integral_first_order():
    print("Not finished")
    request_executed()

def find_integral(function, respect_to):
    x = sp.Symbol(respect_to)
    f = sp.sympify(function)
    result = sp.integrate(f, x)
    return result

def simplify_equation(eqn, respect_to):
    lhs, rhs = eqn.split("=")
    x = sp.Symbol(respect_to)
    lhs = sp.sympify(lhs)
    rhs = sp.sympify(rhs)
    eqn = sp.Eq(lhs, rhs)
    solved_eqn = sp.solve(eqn, x)
    simplified_eqn = [sp.simplify(sol) for sol in solved_eqn]
    return simplified_eqn

def solve_homo_second_order_diff_eq(m, c, k):
 
    r1, r2, alpha, beta, discriminant = calculate_roots(m, c, k)
    print(" ")
    # Check if the system is overdamped, critically damped, or underdamped
    if discriminant > 0: # overdamped
        
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            print(" ")
            print("~ Overdamped ~")
            print("Homogeneous Solution:")
            print("\033[1;36;40mx_h(t) = c1 *e^(", round(r1, 3), "*t) + c2 *e^(", round(r2, 3), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            # Get the initial conditions from the user
            x0, xdot0, t01, t02 = get_initial_conditions()
            print(" ")
            print("~ Overdamped ~")
            # Define A and b for overdamped
            A = [[math.exp(r1*t01), math.exp(r2*t01)], [r1 * math.exp(r1*t02), r2 * math.exp(r2*t02)]]
            b = [x0, xdot0]
    
            # Calculate matrix of c1 and c2, by solving SOE
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            print("Homogeneous Solution:")
            if c1 ==0 and c2 == 0:
                print("\033[1;36;40mx_h(t) = 0\033[0m")
            else:
                print("\033[1;36;40mx_h(t) =", round(c1, 3), "*e^(", round(r1, 3), "*t) +", round(c2, 3), "*e^(", round(r2, 3), "*t)\033[0m")
        else:
            unsupported_input()
    elif discriminant == 0: # critically damped
        r3 = r1
        
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            print(" ")
            print("~ Critically Damped ~")
            print("Homogeneous Solution:")
            print("\033[1;36;40mx_h(t) = c1 *e^(", round(r3, 3), "*t) + c2 *t*e^(", round(r3, 3), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            # Get the initial conditions from the user
            x0, xdot0, t01, t02 = get_initial_conditions()
            print(" ")
            print("~ Critically Damped ~")
                # Define A and b for critically damped
            A = [[math.exp(r3*t01), t01 * math.exp(r3*t01)], [r3 * math.exp(r3*t02), math.exp(r3*t02) + (r3 * t02 * math.exp(r3*t02))]]
            b = [x0, xdot0]

            # Calculate matrix of c1, by solving SOE
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            print("Homogeneous Solution:")
            if c1 ==0 and c2 == 0:
                print("\033[1;36;40mx_h(t) = 0\033[0m")
            else:
                print("\033[1;36;40mx_h(t) =", round(c1, 3), "*e^(", round(r3, 3), "*t) +", round(c2, 3), "*t*e^(", round(r3, 3), "*t)\033[0m")
        else:
            unsupported_input()
    else: # underdamped
        
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            print(" ")
            print("~ Underdamped ~")
            print("Homogeneous Solution:")
            print("\033[1;36;40mx_h(t) = c1 *e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) + c2 *e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            print(" ")
            print("~ Underdamped ~")
            # Define A and b for underdamped
            A = [[math.exp(alpha*t01) * math.cos(beta*t01*0.017453293), math.exp(alpha*t01) * math.sin(beta*t01*0.017453293)], [((-beta * math.exp(alpha*t02) * math.sin(beta*t02*0.017453293)) + (alpha * math.exp(alpha * t02) * math.cos(beta *t02*0.017453293))), ((beta * math.exp(alpha*t02) * math.cos(beta*t02*0.017453293)) + (alpha * math.exp (alpha*t02) * math.sin(beta*t02*0.017453293)))]]
            b = [x0, xdot0]

            # Calculate matrix of c1 and c2, by solving SOE
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            print("Homogeneous Solution:")
            if c1 ==0 and c2 == 0:
                print("\033[1;36;40mx_h(t) = 0\033[0m")
            else:
                print("\033[1;36;40mx_h(t) =", round(c1, 3), "*e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) +", round(c2, 3), "*e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t)\033[0m")
        else:
            unsupported_input()        
    if ask_inital_conditions == "Y":
        print(" ")
        time.sleep(1)
        ask_for_graph = input("Would you like me to graph this for you? Y / N: ")
        if ask_for_graph == "Y":
            graphing_homogenous(r1, r2, discriminant, alpha, beta, c1, c2)
        elif ask_for_graph == "N":
            request_executed()
        else:
            unsupported_input()
    elif ask_inital_conditions == "N":
        request_executed()
    else:
        unsupported_input()
      
def solve_algebraic_particular(m, c, k, A_part): # particular solution for 'At'
    r1, r2, alpha, beta, discriminant = calculate_roots(m, c, k)   
    if discriminant > 0: # overdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            p1, p2 = find_algrbraic_particular_solution(m, c, k, A_part)
            print("~ Overdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r1, 3), "*t) + c2 *e^(", round(r2, 3), "*t) +", round(p1, 2), " +", round(p2, 2), "*t\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            p1, p2 = find_algrbraic_particular_solution(m, c, k, A_part)
            A = [[math.exp(r1*t01), math.exp(r2*t01)], [r1 * math.exp(r1*t02), r2 * math.exp(r2*t02)]]
            b = [x0 - p1 - (p2 * t01), xdot0 - p2]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Overdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "e^(", round(r1, 3), "*t) +", round(c2, 3), "*e^(", round(r2, 3), "*t) +", round(p1, 2), " +", round(p2, 2), "*t\033[0m")
        else:
            unsupported_input()
    elif discriminant == 0: # critically damped
        r3 = r1
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            p1, p2 = find_algrbraic_particular_solution(m, c, k, A_part)
            print("~ Critically Damped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r3, 3), "*t) + c2 *t*e^(", round(r3, 3), "*t) +", round(p1, 2), " +", round(p2, 2), "*t\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            p1, p2 = find_algrbraic_particular_solution(m, c, k, A_part)
            A = [[math.exp(r3*t01), t01 * math.exp(r3*t01)], [r3 * math.exp(r3*t02), math.exp(r3*t02) + (r3 * t02 * math.exp(r3*t02))]]
            b = [x0 - p1 - (p2 * t01), xdot0 - p2]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Critically Damped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r3, 3), "*t) +", round(c2, 3), "*t*e^(", round(r3, 3), "*t) +", round(p1, 2), " +", round(p2, 2), "*t\033[0m")
        else:
            unsupported_input()
    else: # underdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            p1, p2 = find_algrbraic_particular_solution(m, c, k, A_part)
            print("~ Underdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) + c2 *e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(p1, 2), " +", round(p2, 2), "*t\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            p1, p2 = find_algrbraic_particular_solution(m, c, k, A_part)
            A = [[math.exp(alpha*t01) * math.cos(beta*t01*0.017453293), math.exp(alpha*t01) * math.sin(beta*t01*0.017453293)], [((-beta * math.exp(alpha*t02) * math.sin(beta*t02*0.017453293)) + (alpha * math.exp(alpha * t02) * math.cos(beta *t02*0.017453293))), ((beta * math.exp(alpha*t02) * math.cos(beta*t02*0.017453293)) + (alpha * math.exp (alpha*t02) * math.sin(beta*t02*0.017453293)))]]
            b = [x0 - p1 - (p2 * t01), xdot0 - p2]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Underdamped ~")
                print("Complete Soltuion:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) +", round(c2, 3), "*e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(p1, 2), " +", round(p2, 2), "*t\033[0m")
        else:
            unsupported_input()
    if ask_inital_conditions == "Y":
        print(" ")
        time.sleep(1)
        ask_for_graph = input("Would you like me to graph this for you? Y / N: ")
        if ask_for_graph == "Y":
            graphing_forced_algebraic(r1, r2, discriminant, alpha, beta, c1, c2, p1, p2)
        elif ask_for_graph == "N":
            request_executed()
        else:
            unsupported_input()
    elif ask_inital_conditions == "N":
        request_executed()
    else:
        unsupported_input()
    
def solve_exponential_particular(m, c, k, A_part, B):
    r1, r2, alpha, beta, discriminant = calculate_roots(m, c, k)
    if discriminant > 0: # overdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            C = find_exponential_particular_solution(m, c, k, A_part, B)
            print("~ Overdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r1, 3), "*t) + c2 *e^(", round(r2, 3), "*t) +", round(C, 3), "*e^(", round(B, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            C = find_exponential_particular_solution(m, c, k, A_part, B)
            A = [[math.exp(r1*t01), math.exp(r2*t01)], [r1 * math.exp(r1*t02), r2 * math.exp(r2*t02)]]
            b = [x0 - (C * math.exp(B*t01)), xdot0 - (B * C * math.exp(B*t02))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Overdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r1, 3), "*t) +", round(c2, 3), "*e^(", round(r2, 3), "*t) +", round(C, 3), "*e^(", round(B, 2), "*t)\033[0m")
        else:
            unsupported_input()
    elif discriminant == 0: # critically damped
        r3 = r1
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            C = find_exponential_particular_solution(m, c, k, A_part, B)
            print("~ Critcally Damped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r3, 3), "*t) + c2 *t*e^(", round(r3, 3), "*t) +", round(C, 3), "*e^(", round(B, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            C = find_exponential_particular_solution(m, c, k, A_part, B)
            A = [[math.exp(r3*t01), t01 * math.exp(r3*t01)], [r3 * math.exp(r3*t02), math.exp(r3*t02) + (r3 * t02 * math.exp(r3*t02))]]
            b = [x0 - (C * math.exp(B*t01)), xdot0 - (B * C * math.exp(B*t02))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Critcally Damped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r3, 3), "*t) +", round(c2, 3), "*t*e^(", round(r3, 3), "*t) +", round(C, 3), "*e^(", round(B, 2), "*t)\033[0m")
        else:
            unsupported_input()
    else: # underdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            C = find_exponential_particular_solution(m, c, k, A_part, B)
            print("~ Underdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) + c2 *e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(C, 3), "*e^(", round(B, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            C = find_exponential_particular_solution(m, c, k, A_part, B)
            A = [[math.exp(alpha*t01) * math.cos(beta*t01*0.017453293), math.exp(alpha*t01) * math.sin(beta*t01*0.017453293)], [((-beta * math.exp(alpha*t02) * math.sin(beta*t02*0.017453293)) + (alpha * math.exp(alpha * t02) * math.cos(beta *t02*0.017453293))), ((beta * math.exp(alpha*t02) * math.cos(beta*t02*0.017453293)) + (alpha * math.exp (alpha*t02) * math.sin(beta*t02*0.017453293)))]]
            b = [x0 - (C * math.exp(B*t01)), xdot0 - (B * C * math.exp(B*t02))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Underdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) +", round(c2, 3), "*e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(C, 3), "*e^(", round(B, 2), "*t)\033[0m")
        else:
            unsupported_input()
    if ask_inital_conditions == "Y":
        print(" ")
        time.sleep(1)
        ask_for_graph = input("Would you like me to graph this for you? Y / N: ")
        if ask_for_graph == "Y":
            graphing_forced_exponential(r1, r2, discriminant, alpha, beta, c1, c2, C, B)
        elif ask_for_graph == "N":
            request_executed()
        else:
            unsupported_input()
    elif ask_inital_conditions == "N":
        request_executed()
    else:
        unsupported_input()
    
def solve_trigonometric_particular(m, c, k, A_part, B_part, C_part):
    r1, r2, alpha, beta, discriminant = calculate_roots(m, c, k)
    if discriminant > 0: # overdamped        
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            d1, d2 = find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part)
            print("~ Overdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r1, 3), "*t) + c2 *e^(", round(r2, 3), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            d1, d2 = find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part)
            A = [[math.exp(r1*t01), math.exp(r2*t01)], [r1 * math.exp(r1*t02), r2 * math.exp(r2*t02)]]
            b = [x0 - (d1 * math.cos(B_part*t01*0.017453293)) - (d2 * math.sin(B_part*t01*0.017453293)), xdot0 + (B_part * d1 *math.sin(B_part*t02*0.017453293)) - (B_part  * d2 * math.cos(B_part*t02*0.017453293))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Overdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r1, 3), "*t) +", round(c2, 3), "*e^(", round(r2, 3), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        else:
            unsupported_input()
    elif discriminant == 0: # critcally damped
        r3 = r1
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            d1, d2 = find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part)
            print("~ Critically Damped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r3, 3), "*t) + c2 *t*e^(", round(r3, 3), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            d1, d2 = find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part)
            A = [[math.exp(r3*t01), t01 * math.exp(r3*t01)], [r3 * math.exp(r3*t02), math.exp(r3*t02) + (r3 * t02 * math.exp(r3*t02))]]
            b = [x0 - (d1 * math.cos(B_part*t01*0.017453293)) - (d2 * math.sin(B_part*t01*0.017453293)), xdot0 + (B_part * d1 *math.sin(B_part*t02*0.017453293)) - (B_part  * d2 * math.cos(B_part*t02*0.017453293))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Critcally Damped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r3, 3), "*t) +", round(c2, 3), "*t*e^(", round(r3, 3), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        else:
            unsupported_input()
    else: # underdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            d1, d2 = find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part)
            print("~ Underdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) + c2 *e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            d1, d2 = find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part)
            A = [[math.exp(alpha*t01) * math.cos(beta*t01*0.017453293), math.exp(alpha*t01) * math.sin(beta*t01*0.017453293)], [((-beta * math.exp(alpha*t02) * math.sin(beta*t02*0.017453293)) + (alpha * math.exp(alpha * t02) * math.cos(beta *t02*0.017453293))), ((beta * math.exp(alpha*t02) * math.cos(beta*t02*0.017453293)) + (alpha * math.exp (alpha*t02) * math.sin(beta*t02*0.017453293)))]]
            b = [x0 - (d1 * math.cos(B_part*t01*0.017453293)) - (d2 * math.sin(B_part*t01*0.017453293)), xdot0 + (B_part * d1 *math.sin(B_part*t02*0.017453293)) - (B_part  * d2 * math.cos(B_part*t02*0.017453293))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Underdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) +", round(c2, 3), "*e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        else:
            unsupported_input()
    if ask_inital_conditions == "Y":
        print(" ")
        time.sleep(1)
        ask_for_graph = input("Would you like me to graph this for you? Y / N: ")
        if ask_for_graph == "Y":
            graphing_forced_trigonometric(r1, r2, discriminant, alpha, beta, c1, c2, d1, d2, B_part)
        elif ask_for_graph == "N":
            request_executed()
        else:
            unsupported_input()
    elif ask_inital_conditions == "N":
        request_executed()
    else:
        unsupported_input()
    
def solve_exponential_and_trigonometric_particular(m, c, k, A_part, B_part, C_part, D_part):
    r1, r2, alpha, beta, discriminant = calculate_roots(m, c, k)
    if discriminant > 0: # overdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            d1, d2 = find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part)
            print("~ Overdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r1, 3), "*t) + c2 *e^(", round(r2, 3), "*t) + ", round(d1, 3), "*e^(", round(B_part, 2), "*t) * cos(", round(C_part, 2), "*t) +", round(d2, 3), "*e^(", round(B_part, 2), "*t) * sin(", round(C_part, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            d1, d2 = find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part)
            A = [[math.exp(r1*t01), math.exp(r2*t01)], [r1 * math.exp(r1*t02), r2 * math.exp(r2*t02)]]
            b = [x0 - (d1 * math.exp(B_part*t01) * math.cos(C_part*t01*0.017453293)) - (d2 * math.exp(B_part*t01) * math.sin(C_part*t01*0.017453293)), xdot0 - (d1 * B_part * math.exp(B_part*t02) * math.cos(C_part*t02*0.017453293)) + (d1 * C_part * math.exp(B_part*t02) * math.sin(C_part*t02*0.017453293)) - (d2 * B_part * math.exp(B_part*t02) * math.sin(C_part*t02*0.017453293)) - (d2 * C_part * math.exp(B_part*t02) * math.cos(C_part*t02*0.017453293))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Overdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r1, 3), "*t) +", round(c2, 3), "*e^(", round(r2, 3), "*t) +", round(d1, 3), "*e^(", round(B_part, 2), "*t) * cos(", round(C_part, 2), "*t) +", round(d2, 3), "*e^(", round(B_part, 2), "*t) * sin(", round(C_part, 2), "*t)\033[0m")
        else:
            unsupported_input()
    elif discriminant == 0: # critically damped
        r3 = r1
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            d1, d2 = find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part)
            print("~ Critically Damped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(r3, 3), "*t) + c2 *t*e^(", round(r3, 3), "*t) +", round(d1, 3), "*e^(", round(B_part, 2), "*t) * cos(", round(C_part, 2), "*t) +", round(d2, 3), "*e^(", round(B_part, 2), "*t) * sin(", round(C_part, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            d1, d2 = find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part)
            A = [[math.exp(r3*t01), t01 * math.exp(r3*t01)], [r3 * math.exp(r3*t02), math.exp(r3*t02) + (r3 * t02 * math.exp(r3*t02))]]
            b = [x0 - (d1 * math.exp(B_part*t01) * math.cos(C_part*t01*0.017453293)) - (d2 * math.exp(B_part*t01) * math.sin(C_part*t01*0.017453293)), xdot0 - (d1 * B_part * math.exp(B_part*t02) * math.cos(C_part*t02*0.017453293)) + (d1 * C_part * math.exp(B_part*t02) * math.sin(C_part*t02*0.017453293)) - (d2 * B_part * math.exp(B_part*t02) * math.sin(C_part*t02*0.017453293)) - (d2 * C_part * math.exp(B_part*t02) * math.cos(C_part*t02*0.017453293))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Critically Damped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(r3, 3), "*t) +", round(c2, 3), "*t*e^(", round(r3, 3), "*t) +", round(d1, 3), "*e^(", round(B_part, 2), "*t) * cos(", round(C_part, 2), "*t) +", round(d2, 3), "*e^(", round(B_part, 2), "*t) * sin(", round(C_part, 2), "*t)\033[0m")
        else:
            unsupported_input()
    else: # underdamped
        ask_inital_conditions = input("Do you have inital conditions?? Y / N: ")
        if ask_inital_conditions == "N":
            d1, d2 = find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part)
            print("~ Underdamped ~")
            print("Complete Solution:")
            print("\033[1;36;40mx(t) = c1 *e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) + c2 *e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)\033[0m")
        elif ask_inital_conditions == "Y":
            x0, xdot0, t01, t02 = get_initial_conditions()
            d1, d2 = find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part)
            A = [[math.exp(alpha*t01) * math.cos(beta*t01*0.017453293), math.exp(alpha*t01) * math.sin(beta*t01*0.017453293)], [((-beta * math.exp(alpha*t02) * math.sin(beta*t02*0.017453293)) + (alpha * math.exp(alpha * t02) * math.cos(beta *t02*0.017453293))), ((beta * math.exp(alpha*t02) * math.cos(beta*t02*0.017453293)) + (alpha * math.exp (alpha*t02) * math.sin(beta*t02*0.017453293)))]]
            b = [x0 - (d1 * math.exp(B_part*t01) * math.cos(C_part*t01*0.017453293)) - (d2 * math.exp(B_part*t01) * math.sin(C_part*t01*0.017453293)), xdot0 - (d1 * B_part * math.exp(B_part*t02) * math.cos(C_part*t02*0.017453293)) + (d1 * C_part * math.exp(B_part*t02) * math.sin(C_part*t02*0.017453293)) - (d2 * B_part * math.exp(B_part*t02) * math.sin(C_part*t02*0.017453293)) - (d2 * C_part * math.exp(B_part*t02) * math.cos(C_part*t02*0.017453293))]
            x = matrix_solver(A, b)
            c1 = x[0]
            c2 = x[1]
            if c1 == 0 and c2 ==0:
                print("Computation Failed...")
                print("Error 01")
            else:
                print("~ Underdamped ~")
                print("Complete Solution:")
                print("\033[1;36;40mx(t) =", round(c1, 3), "*e^(", round(alpha, 2), "*t) * cos(", round(beta, 2), "*t) +", round(c2, 3), "*e^(", round(alpha, 2), "*t) * sin(", round(beta, 2), "*t) +", round(d1, 3), "*e^(", round(B_part, 2), "*t) * cos(", round(C_part, 2), "*t) +", round(d2, 3), "*e^(", round(B_part, 2), "*t) * sin(", round(C_part, 2), "*t)\033[0m")
        else:
            unsupported_input()
    if ask_inital_conditions == "Y":
        print(" ")
        time.sleep(1)
        ask_for_graph = input("Would you like me to graph this for you? Y / N: ")
        if ask_for_graph == "Y":
            graphing_forced_exponential_and_trigonometric(r1, r2, discriminant, alpha, beta, c1, c2, d1, d2, B_part, C_part)
        elif ask_for_graph == "N":
            request_executed()
        else:
            unsupported_input()
    elif ask_inital_conditions == "N":
        request_executed()
    else:
        unsupported_input()
    request_executed()

def graphing_homogenous(r1, r2, discriminant, alpha, beta, c1, c2):
    print(" ")
    print("What range would you liked this graphed in?")
    low, high = map(float, input("Enter range separated by a comma (ex. 0, 10): ").split(", "))
    print(" ")
    x_values = np.arange(low, high, 0.1)
    if discriminant > 0: 
        y = [(c1 * math.exp(r1*x)) + (c2 * math.exp(r2*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40moverdamped\033[0m system")
    elif discriminant == 0:
        r3 = r1
        y = [(c1 * math.exp(r3*x)) + (c2 * x* math.exp(r3*x)) for x in x_values]
        print("Graph will reflect a \033[1;31;40mcrtically damped\033[0m system")
    else:
        y = [(c1 * math.exp(alpha*x) * math.cos(beta*x)) + (c2 * math.exp(alpha*x) * math.sin(beta*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40munderdamped\033[0m system")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y))    
    fig.show()
    request_executed()

def graphing_forced_algebraic(r1, r2, discriminant, alpha, beta, c1, c2, p1, p2):
    print(" ")
    print("What range would you liked this graphed in?")
    low, high = map(float, input("Enter range separated by a comma (ex. 0, 10): ").split(", "))
    print(" ")
    x_values = np.arange(low, high, 0.1)
    if discriminant > 0:
        y = [(c1 * math.exp(r1*x)) + (c2 * math.exp(r2*x)) + p1 + (p2*x) for x in x_values]
        print("Graph will reflect an \033[1;31;40moverdamped\033[0m system")
    elif discriminant == 0:
        r3 = r1
        y = [(c1 * math.exp(r3*x)) + (c2 * x* math.exp(r3*x)) + p1 + (p2*x) for x in x_values]
        print("Graph will reflect a \033[1;31;40mcrtically damped\033[0m system")
    else:
        y = [(c1 * math.exp(alpha*x) * math.cos(beta*x)) + (c2 * math.exp(alpha*x) * math.sin(beta*x)) + p1 + (p2*x) for x in x_values]
        print("Graph will reflect an \033[1;31;40munderdamped\033[0m system")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y))    
    fig.show()
    request_executed()

def graphing_forced_exponential(r1, r2, discriminant, alpha, beta, c1, c2, C, B):
    print(" ")
    print("What range would you liked this graphed in?")
    low, high = map(float, input("Enter range separated by a comma (ex. 0, 10): ").split(", "))
    print(" ")
    x_values = np.arange(low, high, 0.1)
    if discriminant > 0:
        y = [(c1 * math.exp(r1*x)) + (c2 * math.exp(r2*x)) + (C*math.exp(B*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40moverdamped\033[0m system")
    elif discriminant == 0:
        r3 = r1
        y = [(c1 * math.exp(r3*x)) + (c2 * x* math.exp(r3*x)) + (C*math.exp(B*x)) for x in x_values]
        print("Graph will reflect a \033[1;31;40mcrtically damped\033[0m system")
    else:
        y = [(c1 * math.exp(alpha*x) * math.cos(beta*x)) + (c2 * math.exp(alpha*x) * math.sin(beta*x)) + (C*math.exp(B*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40munderdamped\033[0m system")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y))    
    fig.show()
    request_executed()

def graphing_forced_trigonometric(r1, r2, discriminant, alpha, beta, c1, c2, d1, d2, B_part):
    print(" ")
    print("What range would you liked this graphed in?")
    low, high = map(float, input("Enter range separated by a comma (ex. 0, 10): ").split(", "))
    print(" ")
    x_values = np.arange(low, high, 0.1)
    if discriminant > 0:
        y = [(c1 * math.exp(r1*x)) + (c2 * math.exp(r2*x)) + (d1 * math.cos(B_part*x)) + (d2 * math.sin(B_part*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40moverdamped\033[0m system")
    elif discriminant == 0:
        r3 = r1
        y = [(c1 * math.exp(r3*x)) + (c2 * x* math.exp(r3*x)) + (d1 * math.cos(B_part*x)) + (d2 * math.sin(B_part*x)) for x in x_values]
        print("Graph will reflect a \033[1;31;40mcrtically damped\033[0m system")
    else:
        y = [(c1 * math.exp(alpha*x) * math.cos(beta*x)) + (c2 * math.exp(alpha*x) * math.sin(beta*x)) + (d1 * math.cos(B_part*x)) + (d2 * math.sin(B_part*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40munderdamped\033[0m system")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y))    
    fig.show()
    request_executed()

def graphing_forced_exponential_and_trigonometric(r1, r2, discriminant, alpha, beta, c1, c2, d1, d2, B_part, C_part):
    print(" ")
    print("What range would you liked this graphed in?")
    low, high = map(float, input("Enter range separated by a comma (ex. 0, 10): ").split(", "))
    print(" ")
    x_values = np.arange(low, high, 0.1)
    if discriminant > 0:
        y = [(c1 * math.exp(r1*x)) + (c2 * math.exp(r2*x)) + (d1 * math.exp(B_part*x) * math.cos(C_part*x)) + (d2 * math.exp(B_part*x) * math.sin(C_part*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40moverdamped\033[0m system")
    elif discriminant == 0:
        r3 = r1
        y = [(c1 * math.exp(r3*x)) + (c2 * x* math.exp(r3*x)) + (d1 * math.exp(B_part*x) * math.cos(C_part*x)) + (d2 * math.exp(B_part*x) * math.sin(C_part*x)) for x in x_values]
        print("Graph will reflect a \033[1;31;40mcrtically damped\033[0m system")
    else:
        y = [(c1 * math.exp(alpha*x) * math.cos(beta*x)) + (c2 * math.exp(alpha*x) * math.sin(beta*x)) + (d1 * math.exp(B_part*x) * math.cos(C_part*x)) + (d2 * math.exp(B_part*x) * math.sin(C_part*x)) for x in x_values]
        print("Graph will reflect an \033[1;31;40munderdamped\033[0m system")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_values, y=y))    
    fig.show()
    request_executed()

def find_algrbraic_particular_solution(m, c, k, A_part):
    p2 = A_part/k
    p1 = (-p2 * c)/k
    print(" ")
    print("Particular Soltuion: ")
    print("x_p(t) =", round(p1, 2), "+", round(p2, 2), "*t")
    return p1, p2

def find_exponential_particular_solution(m, c, k, A_part, B):
    # calculate C
    C = A_part/(m*(B**2) + c*B + k)
    print(" ")
    print("Particular Solution:")
    print("x_p(t) =", round(C, 3), "*e^(", round(B, 3), "*t)")
    return C

def find_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part):
    A = [[(-m * B_part**2) + k, c * B_part], [-c * B_part, (-m * B_part**2) + k]]
    b = [A_part, C_part]
    x = matrix_solver(A, b)
    d1 = x[0]
    d2 = x[1]
    print(" ")
    print("Particular Solution:")
    print("x_p(t) =", round(d1, 3), "*cos(", round(B_part, 2), "*t) +", round(d2, 3), "*sin(", round(B_part, 2), "*t)" )
    return d1, d2
    
def find_exponential_and_trigonometric_particular_solution(m, c, k, A_part, B_part, C_part, D_part):
    A = [[(m * (B_part**2)) - (m * (C_part**2)) + (c * B_part) + k, (2 * m * C_part * B_part) + (c * C_part)], [(-2 * m * C_part * B_part) - (c * C_part), (m * (B_part**2)) - m * ((C_part**2)) + (c * B_part) + k]]
    b = [A_part, D_part]
    x = matrix_solver(A, b)
    d1 = x[0]
    d2 = x[1]
    print(" ")
    print("Particular Solution:")
    print("x_p(t) =", round(d1, 3), "*e^(", round(B_part, 2), "*t) * cos(", round(C_part, 2), "*t) +", round(d2, 3), "*e^(", round(B_part, 2), "*t) * sin(", round(C_part, 2), "*t)")
    return d1, d2
    
def calculate_roots(m, c, k):
    discriminant = c**2 - 4*m*k
    if discriminant > 0:
        # Real roots
        r1 = ((-c) + (math.sqrt(discriminant))) / (2*m)
        r2 = ((-c) - (math.sqrt(discriminant))) / (2*m)
        alpha = 0
        beta = 0
    elif discriminant == 0:
        # Complex roots
        r1 = -c / (2*m)
        r2 = 0
        alpha = 0
        beta = 0
    else:
        alpha = -c / (2*m)
        beta = math.sqrt(4*m*k - c**2) / (2*m)
        r1 = 0
        r2 = 0
    return r1, r2, alpha, beta, discriminant

def root_solver():
    print("Please input your coefficients, in the form: mx'' + cx' + kx = 0")
    m = float(input("Value for m: "))
    c = float(input("Value for c: "))
    k = float(input("Value for k: "))
    r1, r2, alpha, beta, discriminant = calculate_roots(m, c, k)
    if discriminant > 0:
        print(" ")
        print("From these coefficients, there are 2 real roots:")
        print("r_1 =", round(r1, 3))
        print("r_2 =", round(r2, 3))
    elif discriminant == 0:
        print(" ")
        print("From these coefficients, there is only 1 real root:")
        print("r =", round(r1, 3))
    else:
        print(" ")
        print("From these coefficients, there are 2 complex roots:")
        print("alpha =", round(alpha, 3))
        print("beta =", round(beta, 3))
    time.sleep(1)
    print(" ")
    ask_for_solution = input("Would you like me to solve for a soltuion using the root(s)? Y / N: ")
    if ask_for_solution == "Y":
        print(" ")
        print("Which solution would you like me to provide?")
        print("(1) Homogeneous Solution")
        print("(2) Complete Solution")
        ask_for_forced = input("Choose: ")
        if ask_for_forced == "1":
            solve_homo_second_order_diff_eq(m, c, k)
        elif ask_for_forced == "2":
            print(" ")
            print("Chose which function looks like yours: f(t) = ")
            print("(1) At")
            print("(2) Ae^Bt")
            print("(3) Acos(Bt)+Csin(Bt)")
            print("(4) Ae^(Bt)cos(Ct) + De^(Bt)sin(Ct)")
            ask_type = input("Choose: ")
            if ask_type == "1":
                    solve_algebraic_particular(m, c, k)
            elif ask_type == "2":
                    solve_exponential_particular(m, c, k)
            elif ask_type == "3":
                    solve_trigonometric_particular(m, c, k)
            elif ask_type == "4":
                    solve_exponential_and_trigonometric_particular(m, c, k)
            else:
                    unsupported_input()
        else:
            unsupported_input()
    elif ask_for_solution == "N":
        request_executed()
    else:
        unsupported_input()
        
def guess_table():
    print(" ")
    print('What does your forced function "f(t)" look like?')
    print("(1) At")
    print("(2) Ae^Bt")
    print("(3) Acos(Bt)+Csin(Bt)")
    print("(4) Ae^(Bt)cos(Ct) + De^(Bt)sin(Ct)")
    print("(5) Back")
    f_t_looks_like = input("Choose: ")
    if f_t_looks_like == "1":
        print(" ")
        print("Your guess should resemble:")
        print('"p1 + p2*t"') 
    elif f_t_looks_like == "2":
        coeff1 = float(input("Value for B: "))
        print(" ")
        print("Your guess should resemble:")
        print('"A*e^(', coeff1, '*t)"')
    elif f_t_looks_like == "3":
        coeff1 = float(input("Value for A: "))
        coeff2 = float(input("Value for B: "))
        coeff3 = float(input("Value for C: "))
        print(" ")
        print("Your guess should resemble:")
        if coeff1 == 0:
            print('"D*sin(', coeff2, '*t)"')
        elif coeff3 == 0:
            print('"D*cos(', coeff2, '*t)"')
        else:
            print('"D*cos(', coeff1, '*t)+E*sin(', coeff1, '*t)"')
    elif f_t_looks_like == "4":
        coeff1 = float(input("Value for A: "))
        coeff2 = float(input("Value for B: "))
        coeff3 = float(input("Value for C: "))
        coeff4 = float(input("Value for D: "))
        print(" ")
        print("Your guess should resemble:")
        if coeff1 == 0:
            print('"E*e^(', coeff2, '*t) * sin(', coeff3, '*t)"')
        elif coeff4 == 0:
            print('"E*e^(', coeff2, '*t) * cos(', coeff3, '*t)"')
        else:
            print('"E*e^(', coeff2, '*t) * cos(', coeff3, '*t) + F*e^(', coeff2, '*t) * sin(', coeff3, '*t)"')
    elif f_t_looks_like == "5":
        os.system('cls')
        aviodance()
    else:
        unsupported_input()
    time.sleep(1)
    print(" ")
    ask_for_solution = input("Would you like me to provide a solution for this guess? Y / N: ")
    if ask_for_solution == "Y":
        print(" ")
        print("To do this please input your coefficients, in the form: mx'' + cx' + kx = f(t)")
        m = float(input("Value for m: "))
        c = float(input("Value for c: "))
        k = float(input("Value for k: "))
        if f_t_looks_like == "1":
            A_part = float(input('I also need the coefficient "A": '))
            print(" ")
            solve_algebraic_particular(m, c, k, A_part)
        elif f_t_looks_like == "2":
            A_part = float(input('I also need the coefficient "A": '))
            print(" ")
            solve_exponential_particular(m, c, k, A_part, coeff1)
        elif f_t_looks_like == "3":
            print(" ")
            solve_trigonometric_particular(m, c, k, coeff1, coeff2, coeff3)
        elif  f_t_looks_like == "4":
            print(" ")
            solve_exponential_and_trigonometric_particular(m, c, k, coeff1, coeff2, coeff3, coeff4)
    elif ask_for_solution == "N":
            request_executed()
    else:
            unsupported_input()

def measurement_system_second_order(measurement_operation_type):
    if measurement_operation_type == "a" or measurement_operation_type == "A":
        os.system('cls')
        homogenoues_input_title()
        print(" ")
        print("To help you, I will need some additional information about your system: ")
        print(" ")
        time.sleep(1)
        print("What form are you given")
        time.sleep(1)
        print("Form (1): mx'' + cx' + kx = 0")
        print("Form (2): ω_n = #  /  ζ = #  /  K = #")
        form_type = input("Form ")
        if form_type == "1":
            print('\033[1A', end='')
            m = float(input("Form 1 --> Value for m: "))
            c = float(input("           Value for c: "))
            k = float(input("           Value for k: "))
        elif form_type == "2":
            print('\033[1A', end='')
            ω_n = float(input("Form 2 --> Value for ω_n: "))
            while True:
                ζ = float(input("           Value for ζ: "))
                if ζ >= 0:
                    break
                print("           This value is \033[1;31;40moutside\033[0m ζ's domain, \033[1;31;40mplease try again\033[0m")
                time.sleep(1)
                sys.stdout.write("\033[F")  # Move the cursor up one line
                sys.stdout.write("\033[K")  # Clear the line
                sys.stdout.write("\033[F")  # Move the cursor up one line
                sys.stdout.write("\033[K")  # Clear the line
            K = float(input("           Value for K: "))
        else:
            unsupported_input()
        print(" ")
        print("From this form, what information would you like: ")
        time.sleep(1)
        print("(1) System Soltuion Type")
        print("(2) Homogeneous Solution")
        print("(3) Characteristic Equation")
        print("(4) Properties of the System")
        information_type = input("Choose: ")
        if form_type == "1":
            if information_type == "1":
                gen_soltution_table(form_type, m, c, k)
            elif information_type == "2":
                os.system('cls')
                homogenoues_solution_calculator_title()
                time.sleep(1)
                print("Brought over data: ")
                print("m = ", m)
                print("c = ", c)
                print("k = ", k)
                time.sleep(1)
                solve_homo_second_order_diff_eq(m, c, k)
            elif information_type == "3":
                charactersitic_equation(form_type, m, c, k)
            elif information_type == "4":
                properties_of_second_order_system(form_type, m, c, k)
            else:
                unsupported_input()
        else:
            if information_type == "1":
                gen_soltution_table(form_type, ω_n, ζ, K)
            elif information_type == "2":
                m = 1/((ω_n**2)*K)
                c = (2*ζ)/(ω_n*K)
                k = 1/K
                solve_homo_second_order_diff_eq(m, c, k) # NOT A SET SOLUTION AS solve_homo_second_order_diff_eq DOES NOT CORRECTLY SOLVE FOR UNDERDAMPED CASES
            elif information_type == "3":
                charactersitic_equation(form_type, ω_n, ζ, K)
            elif information_type == "4":
                properties_of_second_order_system(form_type, ω_n, ζ, K)
            else:
                unsupported_input()
    elif measurement_operation_type == "b" or measurement_operation_type == "B":
        print("Not Finished")
    else:
        unsupported_input()
        
def gen_soltution_table(form_type, num1, num2, num3):
    print(" ")
    int1 = '''Overdamped System Soltuion:
x(t) = C_1*e^(r_1*t) + C_2*e^(r_2*t)      -->      IMPORTANT: Soltuion has \033[1;31;40m2 unique\033[0m roots '''
    int2 = '''Critcally Damped System Solution: 
x(t) = C_1*e^(r*t) + C_2*t*e^(r*t)      -->      IMPORTANT: Solution only has \033[1;31;40m1 unique\033[0m root '''
    int3 = '''Underdamped System Soltuion: 
x(t) = C_1*e^(α*t)*cos(β*t) + C_2*e^(α*t)*sin(β*t)      -->      IMPORTANT: α = \033[1;31;40mreal root\033[0m   /   β = \033[1;31;40mimaginary root\033[0m'''
    int4 = '''Overdamped System Soltuion:
x(t) = C_1*e^(λ_1*t) + C_2*e^(λ_2*t)      -->      IMPORTANT: Soltuion has \033[1;31;40m2 unique\033[0m roots '''
    int5 = '''Critcally Damped System Solution: 
x(t) = C_1*e^(λ*t) + C_2*t*e^(λ*t)      -->      IMPORTANT: Solution only has \033[1;31;40m1 unique\033[0m root '''
    int6 = '''Underdamped System Soltuion: 
x(t) = C*e^(-ζ*ω_n*t)*sin(ω_n*sqrt(1 - ζ^2)*t + Θ)      -->      IMPORTANT: Solution requires some "\033[1;31;40mΘ\033[0m" function'''
    print("From the information you've provided, your solution should ressemble: ")
    if form_type == "1":
        discrimiant = (num2**2) - (4*num1*num3)
        if discrimiant > 0:
            print(int1)
        elif discrimiant == 0:
            print(int2)
        else:
            print(int3)
    elif form_type == "2":
        if num2 > 1:
            print(int4)
        elif num2 == 1:
            print(int5)
        else:
            print(int6)
    request_executed()

def charactersitic_equation(form_type, num1, num2, num3):
    print(" ")
    print("The charactersitic equation from the values you've given me is: ")
    if form_type == "1":
        print(num1, "*r^2 +", num2, "*r +", num3, "= 0")
    else:
        print(round(1/(num1**2), 2), "*λ^2 +", round((2*num2)/(num1), 2), "*λ + 1 = 0")
    time.sleep(1)
    print(" ")
    decision = input("Would you like me to solve this quadratic for the roots? Y/N: ")
    if decision == "Y":
        root_existence = get_roots_for_advanced_measurement(form_type,num1, num2, num3)
        print(" ")
        time.sleep(1)
        if root_existence == "1":
            print("Would you like a solution using these roots?")
            solution_ask = input("Choose: ")
            if solution_ask == "Y":
                if form_type == "1":
                    solve_homo_second_order_diff_eq(num1, num2, num3)
                else:
                    m = 1/((num1**2)*num3)
                    c = (2*num2)/(num1*num3)
                    k = 1/num3
                    solve_homo_second_order_diff_eq(m, c, k)  # NOT A SET SOLUTION AS solve_homo_second_order_diff_eq DOES NOT CORRECTLY SOLVE FOR UNDERDAMPED CASES
            elif solution_ask == "N":
                request_executed()
            else:
                unsupported_input()
        else:
            request_executed()
    elif decision == "N":
        request_executed()
    else:
        unsupported_input()

def get_roots_for_advanced_measurement(form_type, x, y, z):
    print(" ")
    if form_type == "1":
        r1, r2, alpha, beta, discriminant = calculate_roots(x, y, z)
        if discriminant > 0:
            print("There are 2 real roots: ")
            print("r_1 =", round(r1, 3))
            print("r_2 =", round(r2, 3))
        elif discriminant == 0:
            print("There is only 1 real root: ")
            print("r =", round(r1, 3))
        else:
            print("There are 2 complex roots: ")
            print("alpha =", round(alpha, 3))
            print("beta =", round(beta, 3))
        return "1"
    else:
        if y > 1:
            λ1 = (-y*x) + (x*math.sqrt((y**2)-1))
            λ2 = (-y*x) - (x*math.sqrt((y**2)-1))
            print("There are 2 real roots: ")
            print("λ_1 =", round(λ1, 3))
            print("λ_2 =", round(λ2, 3))
        elif y == 1:
            λ3 = -y*x
            print("There is only 1 real root: ")
            print("λ =", round(λ3, 3))
        else:
            print("Because 0 ≤ ζ < 1   -->   There are \033[1;31;40mno\033[0m roots for this particular quadratic")
            return "0"
        return "1"

def properties_of_second_order_system(form_type, num1, num2, num3):
    print(" ")
    if form_type == "1":
        if num1 < 0 or num3 <0:
            sys.stdout.write("Because ")
            if num1 < 0 and num3 < 0:
                sys.stdout.write("m and k are")
            elif num1 < 0:
                sys.stdout.write("m is")
            else:
                sys.stdout.write("k is =")
            sys.stdout.write(" negative...")
            sys.stdout.write("\n")
            print("There is \033[1;31;40mno\033[0m Natural Frequency (ω_n)")
            print("There is \033[1;31;40mno\033[0m Damping Ratio (ζ)")
            time.sleep(1)
            print("This then leads to: ")
            time.sleep(1)
            print("\033[1;31;40mNo\033[0m Ringing Frequency (ω_d)")
            print("\033[1;31;40mNo\033[0m Period (T_d)")
            print("\033[1;31;40mNo\033[0m Resonance Frequency (ω_R)")
        else:
            ω_n = math.sqrt(num3/num1)
            ζ = num2/(2*math.sqrt(num3*num1))
            '''ω_d = ω_n*math.sqrt(1-(ζ**2))
            T_d = (2*math.pi)/ω_d
            ω_R = ω_n*math.sqrt(1-(2*(ζ**2)))'''
            print("Natural Frequency: ω_n =", round(ω_n, 3))
            print("Damping Ratio: ζ =", round(ζ, 3))
            '''print("Ringing Frequency: ω_d =", round(ω_d, 3))
            print("Period: T_d =", round(T_d, 3))
            print("Resonance Frequency: ω_R =", round(ω_R, 3))'''
    else:
        m = 1/((num1**2)*num3)
        c = (2*num2)/(num1*num3)
        k = 1/num3
        '''ω_d = num1*math.sqrt(1-(num2**2))
        T_d = (2*math.pi)/ω_d
        ω_R = num1*math.sqrt(1-(2*(num2**2)))'''
        print("Mass: m =", round(m, 3))
        print("Dampening Constant: c =", round(c, 3))
        print("Spring Constant: k =", round(k, 3))
        '''print("Ringing Frequency: ω_d =", round(ω_d, 3))
        print("Period: T_d =", round(T_d, 3))
        print("Resonance Frequency: ω_R =", round(ω_R, 3))'''
    request_executed()

def parallel_RLC_circuit_second_order():
    print("Not finsihed)")

def matrix_solver(A, b):
    n = len(A)
    M = A
    
    for i in range(n):
        M[i].append(b[i])
    
    for i in range(n):
        # Divide the pivot row by the pivot element
        div = M[i][i]
        for j in range(n + 1):
            M[i][j] /= div
        
        # Eliminate the pivot column for all rows except the pivot row
        for j in range(n):
            if j == i or M[j][i] == 0:
                continue
            factor = M[j][i]
            for k in range(n + 1):
                M[j][k] -= factor * M[i][k]
    
    x = [0 for i in range(n)]
    for i in range(n):
        x[i] = M[i][n]
    return x

def get_initial_conditions():
    # Get the initial conditions from the user
    # One initial position and one initial velocity
    print(" ")
    print("PLease inout your inital conditions:")
    x0 = float(input("Inital Postion (x_0): "))
    t01 = float(input("Inital time at inital position (t_01): "))
    xdot0 = float(input("Inital velocity (x'_0): "))
    t02 = float(input("Inital time at inital velocity (t_02): "))
    return x0, xdot0, t01, t02
    
def unsupported_input():
    print("""
                Unsupported Input...""")
    print("Availbale options:")
    print("(1) Main Menu")
    print("(2) Exit")
    unsupported_input = input("")
    if unsupported_input == "1":
        os.system('cls')
        aviodance()
    else:
        os.system('cls')
        raise SystemExit
        
def request_executed():
    time.sleep(1)
    print("""
                Request has been executed""")
    print("What would you like to do now?")
    print("(1) Main Menu")
    print("(2) Exit")
    main_menu = input("Choose: ")
    if main_menu == "1":
        os.system('cls')
        aviodance()
    else:
        os.system('cls')
        raise SystemExit

def first_order_solver():
    os.system('cls')
    first_order_solver_title()
    print("Avaliable Operations:")
    print("(1) Separable Solver")
    print("(2) Integrating Factor Solver")
    print("(3) Unknown Type")
    ask_first_order_type = input("Choose: ")
    if ask_first_order_type == "1":
        os.system('cls')
        separable_first_order_title()
        solve_separable_first_order()
    elif ask_first_order_type == "2":
        os.system('cls')
        solve_integrating_factor_first_order()
    elif ask_first_order_type == "3":
        print(" ")
        print("Does you function look like:")
        print("(a) Ax' + Bx = 0")
        print("(b) Ax' + Bx = f(t)")
        print("(c) Ax' = Bx")
        print("(d) None of these")
        ask_unknown_first_order_type = input("Choose: ")
        if ask_unknown_first_order_type == "a":
            os.system('cls')
            solve_integral_first_order()
        elif ask_unknown_first_order_type == "b":
            os.system('cls')
            solve_integrating_factor_first_order()
        elif ask_unknown_first_order_type == "c":
            os.system('cls')
            solve_separable_first_order()
        elif ask_unknown_first_order_type == "d":
            print(" ")
            print("This calculator is \033[1;31;40munable\033[0m to successfully solve your 1st order ODE...")
        else:
            unsupported_input()
    else:
        unsupported_input()
        
def second_order_solver():
    os.system('cls')
    second_order_solver_title()
    print("Avaliable Operations:")
    print(" ")
    print("- Conventional -")
    print("(1) Homogenoues Solution Calculator")
    print("(2) Complete/Particular Solution Calculator")
    print("(3) Root Calculator")
    print("(4) Guess Table")
    print("(5) Graphing")
    print(" ")
    print("- Advanced - ")
    print("(6) Measurement System")
    print("(7) Basic Parallel RLC Circuit")
    operation_type = input("Choose: ")
    if operation_type == "1":
        os.system('cls')
        homogenoues_solution_calculator_title()
        print("Please input your coefficients, in the form: mx'' + cx' + kx = 0")
        m = float(input("Value for m: "))
        c = float(input("Value for c: "))
        k = float(input("Value for k: "))                                                               
        solve_homo_second_order_diff_eq(m, c, k)
    elif operation_type == "2":
        os.system('cls')
        complete_and_particular_solution_calculator_title()
        print(" ")
        print("Please input your coefficients, in the form: mx'' + cx' + kx = f(t)")
        m = float(input("Value for m: "))
        c = float(input("Value for c: "))
        k = float(input("Value for k: "))
        print(" ")
        print("Chose which function looks like yours: f(t) = ")
        print("(1) At")
        print("(2) Ae^Bt")
        print("(3) Acos(Bt)+Csin(Bt)")
        print("(4) Ae^(Bt)cos(Ct) + De^(Bt)sin(Ct)")
        ask_type = input("Choose: ")
        if ask_type == "1":
            A_part = float(input("Value for A: "))
            print(" ")
            solve_algebraic_particular(m, c, k, A_part)
        elif ask_type == "2":
            A_part = float(input("Value for A: "))
            B = float(input("Value for B: "))
            print(" ")
            solve_exponential_particular(m, c, k, A_part, B)
        elif ask_type == "3":
            A_part = float(input("Value for A: "))
            B_part = float(input("Value for B: "))
            C_part = float(input("Value for C: "))
            print(" ")
            solve_trigonometric_particular(m, c, k, A_part, B_part, C_part)
        elif ask_type == "4":
            A_part = float(input("Value for A: "))
            B_part = float(input("Value for B: "))
            C_part = float(input("Value for C: "))
            D_part = float(input("Value for D: "))
            print(" ")
            solve_exponential_and_trigonometric_particular(m, c, k, A_part, B_part, C_part, D_part)
        else:
            unsupported_input()
    elif operation_type == "3":
        os.system('cls')
        root_calculator_title()
        root_solver()
    elif operation_type == "4":
        os.system('cls')
        guess_table_title()
        guess_table()
    elif operation_type == "5":
        os.system('cls')
        graphing_title()
        ask_have_roots = input("Do you know the roots? Y / N: ")
        if ask_have_roots == "N":
            print('You will first need to find the roots... I will divert you to "Homogenoues Solver"')
            time.sleep(1.5)
            print("To do this please input your coefficients, in the form: mx'' + cx' + kx = 0")
            m = float(input("Value for m: "))
            c = float(input("Value for c: "))
            k = float(input("Value for k: "))
            sys.stdout.write("Diverting in ")
            for i in range(3):
                h = 3 - i
                sys.stdout.write(str(h))
                if i < 2:
                    sys.stdout.write(", ")
                time.sleep(1)
            # Output a newline after the countdown
            sys.stdout.write("\n")
            os.system('cls')
            homogenoues_solution_calculator_title()
            solve_homo_second_order_diff_eq(m, c, k)
        elif ask_have_roots == "Y":
            print("Which system do you have?")
            print("(1) Overdamped (2 real roots)")
            print("(2) Critcally Damped (1 real root)")
            print("(3) Underdamped (2 complex roots)")
            ask_type_roots = float(input("Choose: "))
            if ask_type_roots == 1:
                r1 = float(input("Value for r1: "))
                r2 = float(input("Value for r2: "))
                alpha = 0
                beta = 0
                discriminant = 1
            elif ask_type_roots == 2:
                r1 = float(input("Value for r: "))
                r2 = 0
                alpha = 0
                beta = 0
                discriminant = 0
            elif ask_type_roots == 3:
                alpha = float(input("Value for alpha: "))
                beta = float(input("Value for beta: "))
                r1 = 0
                r2 = 0
                discriminant = -1
            else:
                unsupported_input()
            print(" ")  
            print("Please input your outer coefficients (c1, c2):")
            c1 = float(input("Value for c1: "))
            c2 = float(input("Value for c2: "))
            graphing_homogenous(r1, r2, discriminant, alpha, beta, c1, c2)
        else:
            unsupported_input()
        print(" ")  
        print("Please input your outer coefficients (c1, c2):")
        c1 = float(input("Value for c1: "))
        c2 = float(input("Value for c2: "))
        print(" ")
        graphing_homogenous(r1, r2, discriminant, alpha, beta, c1, c2)
    elif operation_type == "6":
        os.system('cls')
        second_order_solver_title()
        print("Avaliable Operations:")
        print(" ")
        print("- Conventional -")
        print("(1) Homogenoues Solution Calculator")
        print("(2) Complete/Particular Solution Calculator")
        print("(3) Root Calculator")
        print("(4) Guess Table")
        print("(5) Graphing")
        print(" ")
        print("- Advanced - ")
        print("(6) Measurement System")
        print("     --> What would you like me to do?")
        print("         (a) Homogenous Input")
        print("         (b) Step Input")
        measurement_operation_type = input("         Choose: ")  
        measurement_system_second_order(measurement_operation_type)
    elif operation_type == "7":
        parallel_RLC_circuit_second_order()
    else:
        unsupported_input()

def laplace_tranform_solver():
    os.system('cls')
    print("Haven't finished")

def aviodance():
    differential_equation_calculator_title()
    print("\033[1;31;40m                      **Note: ALL DATA HAS BEEN ERASED** \033[0m")
    start_up()

def start_up():
    print("""  
                       Where would you like to go?
    """)
    
    print("                    1 --> 1st Order Differential Solver")
    print("                    2 --> 2nd Order Differential Solver")
    print("""                    3 --> Laplace Transform Solver
    """)
    main_selection = input("                      Choose: ")
    if main_selection == "1":
        first_order_solver()
    elif main_selection == "2":
        second_order_solver()
    elif main_selection == "3":
        laplace_tranform_solver()
    else: 
        unsupported_input()    

os.system('cls')

differential_equation_calculator_title()
time.sleep(1)
author_title()
time.sleep(1)
start_up()

'''
- Finish first order systems
- Add Advanced section in second order systems
- Add abaility to straight up graph solved second order systems equations
- Add memory
- Start laplace solver'''
        
        
