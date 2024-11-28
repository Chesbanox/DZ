from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.get("/greet/{name}")
def read_name(name: str):
    return {'Message': f'Greetings, traveler {name.capitalize()}'}

@app.get("/calc")
def calculator(a: int, b: int, operator: str):
    calculations = {
        '+': lambda op1, op2: op1 + op2,  # /calc?a=10&b=5&operator=%2B
        '-': lambda op1, op2: op1 - op2,  # /calc?a=10&b=5&operator=-
    }
    return {
        'result': f'{a} {operator} {b} = {calculations[operator](a, b)}'
    } if operator in calculations else (f'Unknown operator {operator}')
    