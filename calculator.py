class calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b): 
        return a*b
    def divide(self,a,b):
        if b == 0:
            return "Error: Division by zero"
        return a/b 
    
obj = calculator()
print(obj.add(10,5))          # Output: 15