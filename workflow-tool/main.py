import os
import subprocess
import inquirer

# def open_folder_or_create_template():
#     main_question = [
#         inquirer.List('action',
#                       message="What would you like to do?",
#                       choices=['Open a folder in VSCode', 'Create a template'],
#                      ),
#     ]
#     main_answer = inquirer.prompt(main_question)
#     action = main_answer['action']
    
#     if action == 'Open a folder in VSCode':
#         questions = [
#             inquirer.List('folder',
#                           message="Select a folder to open in VSCode",
#                           choices=['folder1', 'folder2', 'folder3'],
#                          ),
#         ]
#         answers = inquirer.prompt(questions)
#         folder = answers['folder']
        
#         folder_paths = {
#             'folder1': 'one/',
#             'folder2': 'two/',
#             'folder3': 'three/'
#         }
        
#         path = folder_paths.get(folder)
#         if path and os.path.exists(path):
#             subprocess.run(['code', path])
#         else:
#             print(f"Path {path} does not exist.")
    
#     elif action == 'Create a template':
#         template_questions = [
#             inquirer.Text('template_name', message="Enter the template name"),
#             inquirer.Text('template_content', message="Enter the template content"),
#         ]
#         template_answers = inquirer.prompt(template_questions)
#         template_name = template_answers['template_name']
#         template_content = template_answers['template_content']
        
#         with open(f"{template_name}.txt", 'w') as file:
#             file.write(template_content)
#         print(f"Template {template_name}.txt created successfully.")

# if __name__ == '__main__':
def open_folder_or_create_template():
    while True:
        main_question = [
            inquirer.List('action',
                            message="What would you like to do?",
                            choices=['Open a folder in VSCode', 'Create a template', 'Exit'],
                            ),
        ]
        main_answer = inquirer.prompt(main_question)
        action = main_answer['action']
        
        if action == 'Open a folder in VSCode':
            while True:
                questions = [
                    inquirer.List('folder',
                                    message="Select a folder to open in VSCode",
                                    choices=['PNP', 'Snowfalke Scripts', 'Streamlit', 'Go Back'],
                                    ),
                ]
                answers = inquirer.prompt(questions)
                folder = answers['folder']
                
                if folder == 'Go Back':
                    break
                
                folder_paths = {
                    'PNP': 'source/one/',
                    'Snowfalke Scripts': 'source/two/',
                    'Streamlit': 'source/three/'
                }
                
                path = folder_paths.get(folder)
                if path and os.path.exists(path):
                    subprocess.run(['code', path])
                else:
                    print(f"Path {path} does not exist.")
        
        elif action == 'Create a template':
            while True:
                template_type_question = [
                    inquirer.List('template_type',
                        message="Select a template type",
                        choices=['AWS Glue', 'AWS EMR', 'Snowflake', 'Go Back'],
                        ),
                ]
                template_type_answer = inquirer.prompt(template_type_question)
                template_type = template_type_answer['template_type']
                
                if template_type == 'Go Back':
                    break
                
                template_questions = [
                    inquirer.Text('folder_name', message="Enter the folder name"),
                    inquirer.List('confirm', message="Do you want to create this folder?", choices=['Yes', 'No', 'Go Back']),
                ]
                template_answers = inquirer.prompt(template_questions)
                if template_answers['confirm'] == 'Go Back':
                    break
                elif template_answers['confirm'] == 'No':
                    continue
                
                folder_name = template_answers['folder_name']
                # path to templates
                template_source_paths = {
                    'AWS Glue': 'source/one/',
                    'AWS EMR': 'source/two/',
                    'Snowflake': 'source/three/'
                }

                source_path = template_source_paths.get(template_type)

                template_destination_path = {
                    'AWS Glue': 'destination/dest_one/',
                    'AWS EMR': 'destination/dest_two/',
                    'Snowflake': 'destination/dest_three/'
                }
                
                destination_path = os.path.join(template_destination_path.get(template_type), folder_name)
                
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)
                
                if source_path and os.path.exists(source_path):
                    for file_name in os.listdir(source_path):
                        full_file_name = os.path.join(source_path, file_name)
                        if os.path.isfile(full_file_name):
                            subprocess.run(['cp', full_file_name, destination_path])
                        print(f"Folder {folder_name} created successfully with {template_type} templates.")
                else:
                    print(f"Source path {source_path} does not exist.")
                break

        elif action == 'Exit':
            break

if __name__ == '__main__':
    open_folder_or_create_template()