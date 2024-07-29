with open(r'C:\Users\9tyle\OneDrive\Documents\GitHub\ROAR-Academy\Week Two Exercise Solutions\motto.txt', 'r+') as f:
    
    content = f.read()
    print(content)
    f.write("Let there be light!")

