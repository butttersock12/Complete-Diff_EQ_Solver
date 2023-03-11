import math
import time
import os
import plotly.graph_objects as go
import numpy as np
import sympy as sp
import sys

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
def second_order_solver_title():
    print(""" 
 ___         _   ___         _             ___       _                
<_  >._ _  _| | | . | _ _  _| | ___  _ _  / __> ___ | | _ _  ___  _ _ 
 / / | ' |/ . | | | || '_>/ . |/ ._>| '_> \__ \/ . \| || | |/ ._>| '_>
<___>|_|_|\___| `___'|_|  \___|\___.|_|   <___/\___/|_||__/ \___.|_|  
                                                                     """)
    return
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
def unsupported_input():
    print("""
                Unsupported Input...""")
    print("Availbale options:")
    print("(1) Main Menu")
    print("(2) Exit")
    unsupported_input = input("")
    if unsupported_input == "1":
        os.system('cls')
    else:
        os.system('cls')
        raise SystemExit
def start_up():
    print("""  
                       Where would you like to go?
    """)
    
    print("                    1 --> 1st Order Differential Solver")
    print("                    2 --> 2nd Order Differential Solver")
    print("""                    3 --> Laplace Transform Solver
    """)
    main_selection = input("                      Choose: ")
    if main_selection == "2":
        second_order_solver()
    else: 
        unsupported_input() 

os.system('clc')
differential_equation_calculator_title()
time.sleep(1)
time.sleep(1)
start_up()