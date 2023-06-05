text = ""
try:    
    text += 1
except TypeError:
    print("Eroare tip Type")
except ValueError:
    print("Eroare tip Value")
finally:
    print("Execut tot timpul")
