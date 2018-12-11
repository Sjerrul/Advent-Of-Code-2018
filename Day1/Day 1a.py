with open("input.txt", "r") as f:
    content = f.readlines()
    
content = [x.strip() for x in content] 

frequencyChanges = []
for value in content:
    frequencyChanges.append(int(value))
    

frequency = 0
for change in frequencyChanges:
    frequency += change
    
print(frequency)
