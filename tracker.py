# TODO:
# 1. write to csv file to store bugnumber, bug(short)(len=40), state(fixed, in progress, not fixed), information, and dev-information
# 2. nav-edit function to go to different lines/bugs and edit their state or branch of to new bug
# 3. track multiple projects

from tempfile import NamedTemporaryFile
import csv
import shutil

tracker_file = 'lol_bugs.csv'

def new_project():
    # create a new project. 
    pass

def nav_edit(file_name):
    # for now only the manipulation of state and further information will be allowed. 
    keep_running = False
    valid_id = False
    valid_field = False

    while not valid_id:
        # print('Please input a valid bug-id.')
        try:
            edit_bug_id = int(input('Which bug (bug-id) do you want to edit? '))
            valid_id = True
        except:
            # TODO: create an actual methode
            pass
    
    while not valid_field:
        # print('Please choose a valid field you want to edit.')
        edit_bug_field = input('Which bug-field (bug-state, bug-dev-information) do you want to edit? (state/dev): ')
        if edit_bug_field.lower() == 'state':
            edit_bug_field = 2
            valid_field = True
            bug_field_name = 'bug-state'
        elif edit_bug_field.lower() == 'dev':
            edit_bug_field = 4
            valid_field = True
            bug_field_name = 'bug-dev-information'
    """
    old_csv = []
    
    with open(file_name, newline='') as bug_csv, tempfile:
        reader = csv.reader(bug_csv, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quotechar='"')
        for row in reader:
            row[1] = row[1].title()
            writer.writerow(row)
        print(writer)
        #writer[edit_bug_id][edit_bug_field] = input('Input new %s: ' % bug_field_name)
    shutil.move(tempfile, file_name)"""
    old_csv = []
    with open(file_name, newline = '') as bug_csv:
        bugs = csv.reader(bug_csv)
        for bug in bugs:
            old_csv.append(bug)
    print(old_csv[edit_bug_id])
    old_csv[edit_bug_id][edit_bug_field] = input('Input new %s: ' % bug_field_name)

    tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
    with open(tempfile.name, 'r+') as temp:
        writer = csv.writer(temp)
        for row in old_csv:
            writer.writerow(row)
    shutil.move(tempfile.name, file_name)
    return(keep_running)

def main(file_name):
    # uses terminal input to navigate bugnumber, bugs, state, and addition info
    # working_dir = os.getcwd()
    with open(file_name, newline = '') as bug_csv:
        bugs = csv.reader(bug_csv)
        for bug in bugs:
            # make sure the bug[2] is aligned --> bug[1] is always 32 chars long and followed by a tab
            if len(bug[1]) > 32:
                bug[1] = bug[1][:32]
            else:
                filler = ' '
                filler_count = 32 - len(bug[1])
                filler = filler * filler_count
                bug[1] += filler
            # the same thing should be done for bugs[3] once more states (bug[2]) are added

            print("\t".join(bug))
    
    run_tracker = True
    while run_tracker:
        user_operation = input('Do you want to edit any of the tracked bugs? (y/n/exit): ')
        if user_operation.lower() == 'exit':
            run_tracker = False
        elif user_operation.lower() == 'y':
            run_tracker = nav_edit(file_name)
        elif user_operation.lower() == 'n':
            # create_new_project = input('Do you want to track bugs of a new_project? (y/n/exit): ')
            # create new project bug tracker
            # if user_operation.lower() == 'y':
            #   new_project()
            # elif user_operation.lower() == 'n':
            # 
            pass
        else:
            print('Please enter a valid response or use "ctrl + c" to end the program')

main(tracker_file)