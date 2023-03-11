import math
import time
import os
import plotly.graph_objects as go
import numpy as np
import sympy as sp
import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def start_up():
    output = """
                       Where would you like to go?

                        1 --> 1st Order Differential Solver
                        2 --> 2nd Order Differential Solver
                        3 --> Laplace Transform Solver
    """
    return output

@app.route("/second-order-solver")
def second_order_solver():
    output = """
    <h3>Available Operations:</h3>
    <ul>
        <li>Homogenoues Solution Calculator</li>
        <li>Complete/Particular Solution Calculator</li>
        <li>Root Calculator</li>
        <li>Guess Table</li>
        <li>Graphing</li>
        <li>Measurement System</li>
        <li>Basic Parallel RLC Circuit</li>
    </ul>
    """
    return output

@app.route("/unsupported-input")
def unsupported_input():
    output = """
                Unsupported Input...
                Available options:
                1) Main Menu
                2) Exit
    """
    return output

if __name__ == "__main__":
    app.run()
