def add(a, b):
    return a + b

result = add(2,3)

with open("index.html", "w") as f:
    f.write(f"<h1>Result: {result}</h1>")
