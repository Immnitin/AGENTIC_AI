from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp=FastMCP('math')

@mcp.tool()
def add(a:int, b:int)->str:
    return f"The sum of {a} and {b} is {a+b}"

@mcp.tool()
def sub(a:int,b:int)->str:
    return f"The difference of {a} and {b} is {a-b}"

@mcp.tool()
def multiply(a:int, b:int)->str:
    return f"The product of {a} and {b} is {a*b}"

@mcp.tool()
def divide(a:int,b:int)->str:
    try:
        return f"The division of {a} and {b} is {a/b}"
    except Exception:
        return f"{Exception.__context__}"
    
    
@mcp.resource("math://formulas")
def formulas():
    return """
Arithmetic:
Addition: a + b
Subtraction: a - b
Multiplication: a * b
Division: a / b

Algebra:
(a+b)^2 = a^2 + 2ab + b^2
(a-b)^2 = a^2 - 2ab + b^2
a^2 - b^2 = (a-b)(a+b)

Geometry:
Area of Circle = πr²
Circumference = 2πr
Area of Rectangle = l × b
"""
    
@mcp.prompt()
def step_by_step_solver():
    return """
IMPORTANT:

Every response MUST start with:

PROMPT ACTIVATED

Show every step.
"""

if __name__ == "__main__":
    mcp.run()