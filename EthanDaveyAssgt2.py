#
# Author: c3374491 (Ethan Davey)
# Date: 20/04/21
# Functionality: Finding the most suitable position for an aspiring politician using .csv and .txt files.
# To Do: Task 11.
#

import csv # Allows the access to the csv library.
from csv import reader # Imports a specific piece from the csv librabry that isn't imported in the above line.

# This function opens the csv file. If the file is "preprocessed" the file is translated into a list of sublists. 
# If the csv file is "raw" any empty cells are modified to '0'.
def analyse_csv(filename, filetype): # TASK 1
    file_lines = []
    with open(filename,'r') as file:
        csv_reader = reader(file)
        if(filetype == "preprocessed"):
            file_lines = list(csv_reader)
        else: # TASK 12
            for row in csv_reader:
                for i, x in enumerate(row):
                    if len(x)< 1: # Checks if the item has a length greater then 0, ie. it exists.
                        row[i] = "0" # If true change the element to 0.
                file_lines.append(row) # Add row (which is a list) to a list of sublists.
    candidate = len(file_lines) / 8 # This calculation gives a value based on the number of candidates within the csv file.
    process_candidate(candidate, file_lines, filetype)
        ###########################################################################################################
        #Reference C6: Externally sourced code.
        #Purpose: To create a list of sublists.
        #Date: 09/05/2021
        #Source: geeksforgeeks.org
        #Author: 'pawan_asipu'
        #url: https://www.geeksforgeeks.org/append-extend-python/
        #Adaptation required: Adjusted to work with lists instead of items.
        ###########################################################################################################
        
        #my_list = ['geeks', 'for']
        #my_list.append('geeks')
        #print my_list
        
        #output: ['geeks', 'for', 'geeks']
        
        ###########################################################################################################
        #End reference C6
        ###########################################################################################################
        
###################################################################################################################
#Reference C1: Externally sourced code.
#Purpose: To create a list of lists from a CSV file.
#Date: 03/05/2021
#Source: thispointer.com
#Author: 'Varun'
#url: https://thispointer.com/python-read-csv-into-a-list-of-lists-or-tuples-or-dictionaries-import-csv-to-list/
#Adaptation required: Modified very slightly to work with code from analyse_csv.
###################################################################################################################

#def main():
    #print('**** Read csv into a list of lists ****')
    # read csv file as a list of lists
    #with open('students.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        #csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        #list_of_rows = list(csv_reader)
        #print(list_of_rows)

###################################################################################################################
#End reference C1
###################################################################################################################    
  
    
# This function runs while candidate is greater then 0. 
# After all of the functions are completed once 1 is subtracted from "candidates" as n-1 candidates remain. 
# The first element of the first list is recorded as the candidates name. 
# The first list is then removed from the main list. 
# Answer list is recorded as elements 1-9 of each sublist. Element 0 is the question number.
# Other fucnctions are then called before we removed the first 8 elements from the list "file_lines".
def process_candidate(candidate, file_lines, filetype): # TASK 2 
    while candidate > 0:
        candidate_name = file_lines[0][0]
        file_lines.pop(0)
        answer_list = [i[1:9] for i in file_lines[ :7]]
        echo_answers(candidate_name, answer_list, filetype)
        column_totals = analyse(answer_list)
        sort_decending(column_totals)
        display(column_totals)
        candidate -= 1
        for i in range(7):
            file_lines.pop(0)
###################################################################################################################
#Reference C2: Externally sourced code.
#Purpose: To create a list of lists from a CSV file.
#Date: 04/05/2021
#Source: geeksforgeeks.org
#Author: 'manjeet_04'
#url: https://www.geeksforgeeks.org/python-getting-sublist-element-till-n/
#Adaptation required: Modified to work with varible names already assigned & added a range to collect only the 
#                     answers and to disregard the question number.
###################################################################################################################

# Python3 code to demonstrate
# getting sublist element till N
# using list comprehension + list slicing 
# initializing list 
#test_list = [['Geeks', 1, 15], ['for', 3, 5], ['Geeks', 3, 7]]
# printing original list 
#print("The original list : " + str(test_list))
# initializing N
#N = 2
# using list comprehension + list slicing
# getting sublist element till N
#res = [i[0] for i in test_list[ : N]] 
# print result
#print("The first element of sublist till N : " + str(res))

###################################################################################################################
#End reference C2
###################################################################################################################


# This fucntion simply displays the answers for the candidate using the "candidate_name", "filetype" and "answer_list".
def echo_answers(candidate_name, answer_list, filetype): # TASK 3
    print("Questionaire answers (" + filetype + ") for " + candidate_name)
    answers1 = [i[0:7] for i in answer_list[0]]
    print("Q1", answers1[0], answers1[1], answers1[2], answers1[3], answers1[4], answers1[5], answers1[6], answers1[7])
    answers2 = [i[0:7] for i in answer_list[1]]
    print("Q2", answers2[0], answers2[1], answers2[2], answers2[3], answers2[4], answers2[5], answers2[6], answers2[7])
    answers3 = [i[0:7] for i in answer_list[2]]
    print("Q3", answers3[0], answers3[1], answers3[2], answers3[3], answers3[4], answers3[5], answers3[6], answers3[7])
    answers4 = [i[0:7] for i in answer_list[3]]
    print("Q4", answers4[0], answers4[1], answers4[2], answers4[3], answers4[4], answers4[5], answers4[6], answers4[7])
    answers5 = [i[0:7] for i in answer_list[4]]
    print("Q5", answers5[0], answers5[1], answers5[2], answers5[3], answers5[4], answers5[5], answers5[6], answers5[7])
    answers6 = [i[0:7] for i in answer_list[5]]
    print("Q6", answers6[0], answers6[1], answers6[2], answers6[3], answers6[4], answers6[5], answers6[6], answers6[7])
    answers7 = [i[0:7] for i in answer_list[6]]
    print("Q7", answers7[0], answers7[1], answers7[2], answers7[3], answers7[4], answers7[5], answers7[6], answers7[7])

# This function produces a list of sublists of the totals for each question and their appropriate abbreviation.
def analyse(answer_list): # Task 4
    answers1 = [i[0:7] for i in answer_list[0]]
    answers2 = [i[0:7] for i in answer_list[1]]
    answers3 = [i[0:7] for i in answer_list[2]]
    answers4 = [i[0:7] for i in answer_list[3]]
    answers5 = [i[0:7] for i in answer_list[4]]
    answers6 = [i[0:7] for i in answer_list[5]]
    answers7 = [i[0:7] for i in answer_list[6]]
    rlTotal = ['rl', eval(answers1[0]) + eval(answers2[0]) + eval(answers3[0]) + eval(answers4[0]) + eval(answers5[0]) + eval(answers6[0]) + eval(answers7[0])]
    rmTotal = ['rm', eval(answers1[1]) + eval(answers2[1]) + eval(answers3[1]) + eval(answers4[1]) + eval(answers5[1]) + eval(answers6[1]) + eval(answers7[1])]
    rbTotal = ['rb', eval(answers1[2]) + eval(answers2[2]) + eval(answers3[2]) + eval(answers4[2]) + eval(answers5[2]) + eval(answers6[2]) + eval(answers7[2])]
    llTotal = ['ll', eval(answers1[3]) + eval(answers2[3]) + eval(answers3[3]) + eval(answers4[3]) + eval(answers5[3]) + eval(answers6[3]) + eval(answers7[3])]
    lmTotal = ['lm', eval(answers1[4]) + eval(answers2[4]) + eval(answers3[4]) + eval(answers4[4]) + eval(answers5[4]) + eval(answers6[4]) + eval(answers7[4])]
    lbTotal = ['lb', eval(answers1[5]) + eval(answers2[5]) + eval(answers3[5]) + eval(answers4[5]) + eval(answers5[5]) + eval(answers6[5]) + eval(answers7[5])]
    crTotal = ['cr', eval(answers1[6]) + eval(answers2[6]) + eval(answers3[6]) + eval(answers4[6]) + eval(answers5[6]) + eval(answers6[6]) + eval(answers7[6])]
    clTotal = ['cl', eval(answers1[7]) + eval(answers2[7]) + eval(answers3[7]) + eval(answers4[7]) + eval(answers5[7]) + eval(answers6[7]) + eval(answers7[7])]
    column_totals = [rlTotal, rmTotal, rbTotal, llTotal, lmTotal, lbTotal, crTotal, clTotal]
    return(column_totals)
    
# This function prints the totals of each position.
def display(column_totals): # TASK 5
    dictionary = {
    "rl": "Leader of a major right-wing party",
    "rm": "Minister or shadow minister in a major right-wing party",
    "rb": "Backbencher in a major right-wing party",
    "ll": "Leader of a major left-wing party",
    "lm": "Minister or shadow minister in a major left-wing party",
    "lb": "Backbencher in a major left-wing party",
    "cr": "Crossbench member inclined to support the right wing",
    "cl": "Crossbench member inclined to support the left wing",
    "cn": "Genuinely non-partisan crossbench member",
    }
    print("\nPossible roles in order of suitability, with indicative scores:")
    print()
    if(column_totals[0][1] < 12): # TASK 7
        print("Top: Genuinely non-partisan crossbench member")
        print(describe_role("cn") + "\n")
    print(str(column_totals[0][1]) + ": " + dictionary[column_totals[0][0]])
    print(describe_role(column_totals[0][0]) + "\n")
    print(str(column_totals[1][1]) + ": " + dictionary[column_totals[1][0]])
    print(describe_role(column_totals[1][0]) + "\n")
    print(str(column_totals[2][1]) + ": " + dictionary[column_totals[2][0]])
    if(column_totals[2][1] == column_totals[1][1]): # TASK 9
        print(describe_role(column_totals[2][0]) + "\n")
    print(str(column_totals[3][1]) + ": " + dictionary[column_totals[3][0]])
    if(column_totals[3][1] == column_totals[1][1]):
        print(describe_role(column_totals[3][0]) + "\n")
    print(str(column_totals[4][1]) + ": " + dictionary[column_totals[4][0]])
    if(column_totals[4][1] == column_totals[1][1]):
        print(describe_role(column_totals[4][0]) + "\n")
    print(str(column_totals[5][1]) + ": " + dictionary[column_totals[5][0]])
    if(column_totals[5][1] == column_totals[1][1]):
        print(describe_role(column_totals[5][0]) + "\n")
    print(str(column_totals[6][1]) + ": " + dictionary[column_totals[6][0]])
    if(column_totals[6][1] == column_totals[1][1]):
        print(describe_role(column_totals[6][0]) + "\n")
    print(str(column_totals[7][1]) + ": " + dictionary[column_totals[7][0]])
    print()
    
###################################################################################################################
#Reference C4: Externally sourced code.
#Purpose: To create a dictionary and print a specific item from the dictionary.
#Date: 04/05/2021
#Source: w3schools.com
#Author: N/A
#url: https://www.w3schools.com/python/python_dictionaries.asp
#Adaptation required: modified the dictionary with my own items and changed the dictionary name. 
###################################################################################################################

#thisdict = {
  #"brand": "Ford",
  #"model": "Mustang",
  #"year": 1964
#}
#print(thisdict["brand"])

###################################################################################################################
#End reference C3
###################################################################################################################  


# This function sorts the totals from highest to lowest.
def sort_decending(column_totals): # TASK 6
    return(column_totals.sort(reverse=True, key = lambda x: x[1]))
    
###################################################################################################################
#Reference C4: Externally sourced code.
#Purpose: To sort the list 'column_totals' in decending order based on the second element of each sublist.
#Date: 04/05/2021
#Source: geeksforgeeks.org
#Author: Chinmoy Lenka
#url: https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
#Adaptation required: modified the list name and added 'reverse=True' to sort the list in descending order
#                     instead of ascending order.
###################################################################################################################

# Python code to sort the tuples using second element 
# of sublist Function to sort using sorted()
#def Sort(sub_li):
  
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    #return(sorted(sub_li, key = lambda x: x[1]))    
  
# Driver Code
#sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
#print(Sort(sub_li))

###################################################################################################################
#End reference C4
###################################################################################################################


# This function calls the fuction "read_roles" and returns a string based on the "abreviation" argument.
def describe_role(abreviation): # TASK 8
    dictionary_desc = read_roles()
    return(dictionary_desc[abreviation])

# This function reads "RoleDescriptions.txt".
# Then creates a dictionary with the abreviations as the keys and the following paragraph as the description. 
def read_roles():
    content_list = []
    with open("RoleDescriptions.txt") as f:
        txt_reader = f.readlines()
        txt_reader = [line.rstrip('\n') for line in open("RoleDescriptions.txt")] # Creates a string with each line being a new element.
        n = 0
        dictionary_descriptions = {}
        while n < 80: # Repeats until the last line of the file is met. 
            if(len([i for i in txt_reader[n]]) == 2): # Checks if the element has a length of 2.
                temp_abreviation = txt_reader[n].lower() # If true it is assigned to a temporary value to be used as the key in the dictionary.
                temp_description = "" # Clears the temporary description variable to be added to for a new description.
                n += 1
            else:
                while(len([i for i in txt_reader[n]]) > 2 and n < 80): # Checks if the end of the file has been met and that the length of the element is greater then 2.
                    temp_description += (" " + txt_reader[n]) # Adds the line to the temporary description variable.
                    n += 1
                dictionary_descriptions[temp_abreviation] = temp_description # Adds the temporary key and description to the dictionary.
        return(dictionary_descriptions)
        
###################################################################################################################
#Reference C5: Externally sourced code.
#Purpose: To remove '\n' from the item when adding it to the list.
#Date: 06/05/2021
#Source: qiita.com
#Author: 'visualskyrim'
#url: https://qiita.com/visualskyrim/items/1922429a07ca5f974467
#Adaptation required: modified the list and file name.
###################################################################################################################

#lineList = [line.rstrip('\n') for line in open(fileName)]

###################################################################################################################
#End reference C5
###################################################################################################################