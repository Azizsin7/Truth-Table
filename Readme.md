[LogicCalculator](https://github.com/Azizsin7/Truth-Table/blob/main/logiccalculator.py)
----
Purpose:

This Python file implements a Boolean algebra calculator that generates truth tables for logical expressions.

* Module used:
    1. from itertools import product

        This imports the product function from Python's itertools module
        product is used to generate Cartesian products of input iterables
        In logic calculator context, it's likely used to generate all possible combinations of True/False values for variables
        Example: product([True, False], repeat=2) generates: (T,T), (T,F), (F,T), (F,F)
    2. import tkinter as tk

        Imports the standard GUI library Tkinter with alias 'tk'
        Tkinter provides tools to create desktop applications with buttons, windows, input fields etc.
        The alias tk is a common convention to make the code more concise
        Used to create the visual interface for the logic calculator
    3. from tkinter import messagebox

        Imports specifically the messagebox module from Tkinter
        Messagebox provides popup windows for:
        Showing errors
        Warnings
        Information messages
        OK/Cancel dialogues

Key Components

Class: LogicCalculator

Handles boolean expressions with variables (A, B, C, etc.)
* Supports operators:
  - NOT (!)
  - AND (*)
  - OR (+)
  - XOR (^)

* Main Features:
  - Expression parsing
  - Variable extraction
  - Truth table generation
  - Expression evaluation
  - Implementation Details

* Uses itertools.product for generating all possible combinations
Tkinter for GUI implementation
Dynamic column generation based on expression
Supports multiple variables and nested operations
Input/Output

- Input: Boolean expression (e.g., "A*!B+C")
- Output: a stand alone windows. Formatted truth table showing:
    - Variable columns
    - NOT operation results
    - Expression evaluation
    - Final results
    - Example Usage

```terminal
calculator = LogicCalculator("A*!B")
 Generates truth table:
 A | B | !B | A*!B
 0 | 0 | 1  | 0
 0 | 1 | 0  | 0
 1 | 0 | 1  | 1
 1 | 1 | 0  | 0
```