import os
import subprocess

class ProcessNotFoundError(Exception):
    pass

def wmic_command(process_name):
    print(f"Getting creation date of the process: {process_name}")
    command = f"wmic process where name='{process_name}.exe' get creationdate"
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
    result = result.stdout[29:43] # 29:43 is the range of the date in the output
    return result

def format_date(date_output):
    year = date_output[0:4]
    month = date_output[4:6]
    day = date_output[6:8]
    hour = date_output[8:10]
    minute = date_output[10:12]
    second = date_output[12:14]
    
    formatted_date =f"{year}-{month}-{day} at {hour}h{minute}:{second}"
    
    return formatted_date

def get_creation_date(process_name):
    try:
        result = wmic_command(process_name)
        if result == "":
            raise ProcessNotFoundError(f"Process '{process_name}' not found.")
            
        formatted_date = format_date(result)
        print(f"Creation date of the process: {formatted_date}")
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
    except ProcessNotFoundError as e:
        print(e)
    
if __name__ == "__main__":
    while True:
        os.system('cls')
                
        process_name = input("Enter the process name: ")
        if process_name == "": # Verificar se o nome do processo está vazio
            print("Process name cannot be empty.")
            os.system('timeout /t -1')
            continue
        elif process_name.isdigit(): # Verificar se o nome do processo contém caracteres especiais
            print("Process name cannot contain only numbers.")
            os.system('timeout /t -1')
            continue
        
        process_name = process_name.lower()
        
        get_creation_date(process_name)
        
        response = input("Do you want to continue? (y/n): ")

        if response.lower() != 'y':
            break