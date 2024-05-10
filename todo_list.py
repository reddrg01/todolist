#Todo list
#James Wooldridge 
#This code will is for creating TO Do list and having the ability to create a list of To Do items & tasks.
#Each task can be modified and complete. Once complete it will be removed from the list. 

while True:
    user_action = input("Type... Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()
        
    match user_action:
        case'add':
            todo = input("Enter a ToDo: ") + '\n'
            
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
                        
            todos.append(todo.capitalize())
            
            
            file = open('files/todos.txt', 'w') 
            file.writelines(todos)
            file.close()
            
        case 'show'| "display":
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index + 1 }.{item}"
                print(row)
                
        case 'edit':
            number = int(input("Number of the todo to edit? "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo  
                           
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
             
            todos.pop(number - 1)  
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
               
        case 'exit':
            break
        #case _:
            print("Please enter a listed option")
    
print("Bye!!")    