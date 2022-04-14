*I had completed all tasks except for task 11. While I had a somewhat working solution rodeo would not run as it was too long for the program to handle. (Assignment had to run in Rodeo for marking)*

# INFT1004-Assing2
INFT1004 - Assignment 2 [Python]

## YOUR ASSESSMENT TASK
For this assignment you are to write a Python program that analyses results from the Simon Questionnaire for Understanding Aspiring Politicians (SQUAP). This is a questionnaire designed to assess potential politicians and suggest what positions they might be best suited for. It has just seven questions, each of which has eight possible answers. Here are three example questions. (You might find it fun to devise your own questions, but we don’t need all seven.)

When a question makes me feel uncomfortable, I tend to respond by:<br>
(a) explaining that it makes me feel uncomfortable, then answering to the best of my ability<br>
(b) staring blankly at the questioner as if they were stupid<br>
(c) answering the question that I would have preferred them to ask me<br>
(d) saying that I will respond after seeking advice from the relevant department<br>
(e) attacking the questioner, for example by saying that their question is stupid<br>
(f) responding that the question should be answered by a member of the opposing party<br>
(g) saying the first remotely relevant thing that comes to my mind<br>
(h) looking at my watch, excusing myself, and leaving

When a politician in my party is accused of profiting from questionable land deals:<br>
(a) I decline to comment because that should be the role of the party leader<br>
(b) I express empathy with any victims of the alleged behaviour<br>
(c) I decline to comment because the accusation should be investigated by the police<br>
(d) I suggest that it is in keeping with the politician’s past behaviour<br>
(e) I express my dismay at the accusation, and hope that it will prove to be unfounded<br>
(f) I remind the public and the press of similar accusations against members of other parties<br>
(g) I call on the media to say nothing about the accusation until it is established as fact<br>
(h) I call on my party to bring in measures to avert such behaviour in the future

My perspective on taxation is that:<br>
(a) it should be entirely abolished<br>
(b) I have thought of a far better way to administer it<br>
(c) it is a way of helping to distribute a country’s wealth<br>
(d) it is a necessary contribution to the cost of running the country<br>
(e) it is probably unfair, but is a reasonable way of raising funds<br>
(f) it is easily avoided with the right accounting techniques<br>
(g) it is a blight on the wealthy, forcing them to support those who won’t support themselves<br>
(h) politicians should be exempt because they already contribute in other ways<br>

Now this is not a standard multiple-choice questionnaire. Rather than choosing just one option for your answer, you are given ten points for each answer, and you divide them as you wish among the eight options. So for example, for the first question you might simply give all ten points to option b; whereas for the third question you might give five points to g, three points to h, and two points to a.<br>
Your task is to write a Python program to process people’s answers to this questionnaire and let them know which political roles they seem best suited for.<br>
For the purposes of the program, the answer to a single question will be a set of eight integers, the points allocated to each of the options a to h. If somebody gives all ten points to option b, their answer to that question will be 0 10 0 0 0 0 0 0; if somebody gives five points to g, three points to h, and two points to a, their answer to that question will be 2 0 0 0 0 0 5 3.<br>
Once the program has the answers to all seven questions for a person, it puts them into the following grid. Notice that the cells of this grid are not in the order a to h: rather, each cell explicitly indicates which value goes into it. For example, in the first cell of question 6 the program will put the value for question 6 option e; in the second cell of question 6, the value for option d; in the third cell, the value for option f; and so on.

| Question | RL | RM | RB | LL | LM | LB | CR | CL |
| -------- | -- | -- | -- | -- | -- | -- | -- | -- |
| 1 | b: | c: | e: | f: | d: | h: | g: | a: |
| 2 | c: | f: | a: | b: | g: | e: | d: | h: |
| 3 | f: | g: | h: | c: | b: | d: | a: | e: |
| 4 | h: | a: | c: | d: | e: | b: | f: | g: |
| 5 | a: | e: | d: | f: | a: | c: | b: | c: |
| 6 | e: | d: | f: | a: | c: | g: | h: | b: |
| 7 | g: | h: | b: | e: | f: | a: | c: | d: |


Here is a full example. If somebody gives the following answers to the seven questions (let’s call them the raw answers) . . .<br>
Question 1: 3 0 0 0 0 3 0 4<br>
Question 2: 0 0 0 0 3 0 0 7<br>
Question 3: 0 0 0 5 4 0 0 1<br>
Question 4: 0 1 0 1 3 0 5 0<br>
Question 5: 1 2 5 1 1 0 0 0<br>
Question 6: 1 3 1 0 0 0 5 0<br>
Question 7: 0 0 0 2 5 3 0 0<br>
. . . the grid will be filled as follows . . .

| Question | RL | RM | RB | LL | LM | LB | CR | CL |
| -------- | -- | -- | -- | -- | -- | -- | -- | -- |
| 1 | b: 0 | c: 0 | e: 0 | f: 3 | d: 0 | h: 0 | g: 0 | a: 3 |
| 2 | c: 0 | f: 0 | a: 0 | b: 0 | g: 0 | e: 0 | d: 0 | h: 7 |
| 3 | f: 0 | g: 0 | h: 1 | c: 0 | b: 0 | d: 0 | a: 0 | e: 4 |
| 4 | h: 0 | a: 0 | c: 0 | d: 1 | e: 3 | b: 3 | f: 0 | g: 5 |
| 5 | a: 1 | e: 1 | d: 1 | f: 0 | a: 0 | c: 0 | b: 2 | c: 5 |
| 6 | e: 0 | d: 0 | f: 0 | a: 1 | c: 1 | g: 5 | h: 0 | b: 3 |
| 7 | g: 0 | h: 0 | b: 0 | e: 5 | f: 3 | a: 0 | c: 0 | d: 2 |
| Total | 1 | 1 | 2 | 10 | 7 | 18 | 2 | 29 |

The program then sums the values in each column, and looks for the two biggest values. In this case they are the CL column, with 29, and the LB column, with 18. These columns are then used to indicate what political roles the person seems best suited to.<br>
While the assignment will undoubtedly seem daunting at first, we have broken it into a number of tasks, each of which is described in the sections below. If you tackle just one task at a time, and don’t move on until you have completed that task, you might be surprised at the program that you will eventually produce.

## ASSIGNMENT TASK

### Task 1: analyse_csv(filename, filetype): read a preprocessed csv file – 5 marks
We’ll start somewhere moderately simple. Rather than the raw answers shown above, we will have a csv file containing preprocessed answers: answers that have already been translated into the grid. For the example shown above, this csv file will contain the following eight rows:

| Lee Ping Hai |   |   |   |   |   |   |   |   |
| ------------ | - | - | - | - | - | - | - | - |
| Q1 | 0 | 0 | 0 | 3 | 0 | 4 | 0 | 3 |
| Q2 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 7 |
| Q3 | 0 | 0 | 1 | 3 | 0 | 5 | 0 | 4 |
| Q4 | 0 | 0 | 0 | 1 | 3 | 1 | 0 | 5 |
| Q5 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 5 |
| Q6 | 0 | 0 | 0 | 1 | 1 | 5 | 0 | 3 |
| Q7 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 2 |

This file has been made available to you, as CandidateAnswers1Preprocessed.csv.<br>
The first task for your program is to write a function called analyse_csv() that will read this csv file into a list of strings which will then be sent off for further processing. The first argument of the function will be the file name; the second is irrelevant for now, but call it filetype, and when calling the function, make the second argument "preprocessed".

### Task 2: process_candidate(candidate, file_lines, filetype): form a list of lists of numbers – 7 marks
The second task is to transform the data from a list of comma-separated strings into a list of sublists for other parts of the program to work on.<br>
The list that is returned should be a list of lists of the numbers, one sublist for each row, like this:<br>
`[[0, 0, 0, 3, 0, 4, 0, 3], [0, 0, 0, 0, 0, 3, 0, 7], [0, 0, 1, 0, 0, 5, 0, 4], [0, 0, 0, 1, 3, 1, 0, 5], [1, 1, 1, 0, 0, 0, 2, 5], [0, 0, 0, 1, 1, 5, 0, 3], [0, 0, 0, 5, 3, 0, 0, 2]]`

This is not a trivial task. You will need to consider what each line of the input file actually looks like as text; you will need to separate its components; you might need to be wary of the end-of-line character; you will need to work out how to form a list of the eight numbers in each row; and you will need to work out how to form a list of those lists.<br>
While it might seem that the best way to discover these things is by desperately searching the web, it’s actually the case that the answers are all in the material we have covered so far in the course, including the exercises; you just have to think about how to apply that material to this new problem.<br>
You can ignore the candidate parameter for now, but when calling the function, use 0 as the corresponding argument. The argument corresponding to file_lines will be the list of strings produced in `analyse_csv()`, and filetype will be the same value that was passed in to `analyse_csv()`. So at the end of `analyse_csv()`, add a command such as `process_candidate(0, file_lines, filetype)`.

### Task 3: echo_answers(candidate_name, answer_list, filetype): display the input – 4 marks
Write the function echo_answers(), which takes three arguments: the name of the candidate, the list of lists of numbers produced by process_candidate(), and the file type (which is currently ‘preprocessed’). The data should now be displayed like this:<br>
```
Questionnaire answers (preprocessed) for Lee Ping Hai
Q1 0 0 0 3 0 4 0 3
Q2 0 0 0 0 0 3 0 7
Q3 0 0 1 0 0 5 0 4
Q4 0 0 0 1 3 1 0 5
Q5 1 1 1 0 0 0 2 5
Q6 0 0 0 1 1 5 0 3
Q7 0 0 0 5 3 0 0 2
```
The first line of the output includes both the candidate’s name and the file type; each subsequent line starts with ‘Q’ and the question number, then displays the eight numbers that make up the preprocessed answers for this candidate.<br>
Add a command near the end of `process_candidate()` to call `echo_answers()`.

### Task 4: analyse(answer_list): work out the totals for the eight columns – 10 marks
Write the function `analyse()`, which takes one argument: the list of lists of numbers produced by `process_candidate()`. This function will work out the column totals, and will return a list of two-element sublists in which the first element is the two-letter abbreviation of a political role and the second element is the total score in the column associated with that role.<br>
For the example that we have been using, the function will return the list `[['rl', 1], ['rm', 1], ['rb', 2], ['ll', 10], ['lm', 7], ['lb', 18], ['cr', 2], ['cl', 29]]` – the same abbreviations and totals that we saw in the grid at the start of this specification.<br>
You will need to give some thought to how to add the numbers in each ‘column’, as the numbers are in different sublists of a list, not in an actual grid.<br>
Add a command near the end of `process_candidate()` to call `analyse()`. As `analyse()` returns a list, the command will need to assign the returned list to a variable.

### Task 5: display(column_totals): display the column totals and the corresponding roles – 7 marks
Each of the nine possible roles has a two-letter abbreviation and a full name, as follows:<br>
rl: Leader of a major right-wing party<br>
rm: Minister or shadow minister in a major right-wing party<br>
rb: Backbencher in a major right-wing party<br>
ll: Leader of a major left-wing party<br>
lm: Minister or shadow minister in a major left-wing party<br>
lb: Backbencher in a major left-wing party<br>
cr: Crossbench member inclined to support the right wing<br>
cl: Crossbench member inclined to support the left wing<br>
cn: Genuinely non-partisan crossbench member<br>

Write a function called `display()`, which takes the list of column totals as its argument, and begins by creating a dictionary of the two-letter abbreviations and the corresponding names.
Once the dictionary has been created, `display()` will use the list of column totals to display the totals and the corresponding role names. For our example, it will print this:
```
Possible roles, with indicative scores:

1: Leader of a major right-wing party
1: Minister or shadow minister in a major right-wing party
2: Backbencher in a major right-wing party
10: Leader of a major left-wing party
7: Minister or shadow minister in a major left-wing party
18: Backbencher in a major left-wing party
2: Crossbench member inclined to support the right wing
29: Crossbench member inclined to support the left wing
```
Remember, the ninth role doesn’t have a corresponding column, so it doesn’t have a score. We’ll deal with that later.<br>
Add a command near the end of `process_candidate()` to call `display()`.

### Task 6: sort_descending(column_totals): sort column totals by total, descending – 4 marks
Write a function called `sort_descending()`, which takes the list of role abbreviations and column totals as its argument and returns a similar list in which the roles are in descending order of total. For example, given the list `[['rl', 1], ['rm', 1], ['rb', 2], ['ll', 10], ['lm', 7], ['lb', 18], ['cr', 2], ['cl', 29]], it will return the list [['cl', 29], ['lb', 18], ['ll', 10], ['lm', 7], ['rb', 2], ['cr', 2], ['rm', 1], ['rl', 1]]`.
Add a command near the end of process_candidate() to call sort_descending(), then ensure that the call to `display()` acts on the newly sorted list<br>
The `display()` function should then print this:
```
Possible roles in order of suitability, with indicative scores:

29: Crossbench member inclined to support the left wing
18: Backbencher in a major left-wing party
10: Leader of a major left-wing party
7: Minister or shadow minister in a major left-wing party
2: Backbencher in a major right-wing party
2: Crossbench member inclined to support the right wing
1: Minister or shadow minister in a major right-wing party
1: Leader of a major right-wing party
```
Students who are not yet good at problem solving might immediately turn to the web to find out how to sort a list of sublists by the second element of each sublist in descending order. They might well find something, and it might well be somewhat involved. On the other hand, students who have started to apply the techniques of problem solving might think along the following lines. Exercise 8 in the week 5 notes explicitly talks about how one might sort a list of two-element sublists by the second element. If the elements in each sublist are swapped, the standard `sort()` method might then take care of it. As for sorting in the opposite order: if you don’t like the order resulting from the `sort()` method, you could then apply the `reverse()` method.

### Task 7: the genuinely non-partisan crossbench member – 4 marks
A genuinely non-partisan crossbencher is indicated not a by a score in a particular column, but by having every column total less than 12. If that is the case, the genuinely non-partisan crossbench member role will be ranked top, with the other roles still in their existing order. Because there is no column total, the program will instead use the word ‘Top’. Here is an example, from a different candidate.
```
Questionnaire answers (preprocessed) for Isabella Sounder
Q1 0 1 4 1 1 1 0 2
Q2 1 3 0 2 0 2 2 0
Q3 1 1 2 0 1 1 3 1
Q4 3 1 1 1 1 1 1 1
Q5 2 0 2 1 0 2 1 2
Q6 0 2 1 2 1 1 2 1
Q7 3 1 1 1 1 1 1 1

Possible roles in order of suitability, with indicative scores:

Top: Genuinely non-partisan crossbench member
11: Backbencher in a major right-wing party
10: Leader of a major right-wing party
10: Crossbench member inclined to support the right wing
9: Minister or shadow minister in a major right-wing party
9: Backbencher in a major left-wing party
8: Leader of a major left-wing party
8: Crossbench member inclined to support the left wing
5: Minister or shadow minister in a major left-wing party
```
In `display()`, after setting up the dictionary and printing the heading for the candidate, find the maximum column score. If it’s less than 12, print the genuine non-partisan crossbencher line. The function will then proceed to display the ranked column totals and roles as before.

### Task 8: the role descriptions – 7 marks
The file called RoleDescriptions.txt contains the nine two-letter role abbreviations and a multiline description of each role. The system should now be adjusted to display these descriptions for the top two column scores. Here is an example, with the descriptions shortened to save space.
```
Questionnaire answers (preprocessed) for Lee Ping Hai
Q1 0 0 0 3 0 4 0 3
Q2 0 0 0 0 0 3 0 7
Q3 0 0 1 0 0 5 0 4
Q4 0 0 0 1 3 1 0 5
Q5 1 1 1 0 0 0 2 5
Q6 0 0 0 1 1 5 0 3
Q7 0 0 0 5 3 0 0 2

Best suited roles in order of suitability, with indicative scores and role descriptions:

29: Crossbench member inclined to support the left wing
A crossbencher is a politician who is either independent or associated
with a party that is highly unlikely to attain government in its own
right.
More description of crossbenchers here.

18: Backbencher in a major left-wing party
A major party is likely to be either in government or the main
opposition party.
A main purpose of backbenchers is to contribute to the number of seats
required for the party to attain majority and govern the country.
More description of backbenchers here.

Remaining roles in order of suitability, with indicative scores:
10: Leader of a major left-wing party
7: Minister or shadow minister in a major left-wing party
2: Backbencher in a major right-wing party
2: Crossbench member inclined to support the right wing
1: Minister or shadow minister in a major right-wing party
1: Leader of a major right-wing party
```
Write a function called `read_roles()`, which has no parameters. This function will read the file *RoleDescriptions.txt* and set up the two-letter abbreviations and their multiline descriptions in a suitable structure: this might be a list of sublists, where each sublist has two elements, the abbreviation and the description; or it might be a dictionary. Whatever structure the function creates, it should then return it. It might be helpful to know that the only lines in the file that consists of just two letters (and an end-of-line character) are the abbreviations; so when you find such a line, you know that the preceding description has finished.<br>
Write a function called `describe_role()`, which takes a single argument, the two-letter abbreviation of a role. This function will call `read_roles()` to set up the structure of abbreviations and descriptions, and will then print the description corresponding to the abbreviation that was provided as its argument.<br>
You might notice that the role abbreviations in the grid and in *RoleDescriptions.txt* are in upper case, while in much of this specification we have used lower-case versions. When comparing the abbreviation from the list with the one from the file, it might be wise to allow for differences in case.<br>
Adjust `display()` so that for the top two roles it prints the role description after the column score and role name; then it displays the remaining roles as before. It should first call `describe_role()` for the genuine crossbencher role if that one is selected; but it will still go on to describe the top two of the remaining roles.

### Task 9: the role descriptions continued – 4 marks
As described, the system prints descriptions of a candidate’s top two column scores. But what if the third-ranked column has the same score as the second? What if the fourth-ranked column has the same score as the second? While it’s unlikely, a candidate might contrive to get seven scores of 8 and one of 4. That candidate would clearly be a genuinely independent crossbencher, but would then have seven equal highest column scores – all of which should therefore come with descriptions.<br>
Adjust your code for task 8 to determine whether any subsequent columns have the same column score as the second-ranked one, and, if so, to display their descriptions as well.

### Task 10: multiple candidates’ answers in the same file – 6 marks
So far we have been working with csv files that contain the name and answers of a single candidate. However, for the sake of human efficiency we would like to combine the names and answers of several candidates into a single file.<br>
Back in `analyse_csv()` we told you to use 0 as the candidate number when calling `process_candidate()`. Now is the time to expand on that. Once you have read all the lines from the csv file, you can trivially work out how many candidates are represented in the file. You can then set up a loop to process each candidate in turn, using the loop index as the candidate number in the call to `process_candidate()`.
Each time `process_candidate()` is called, it will need to know which lines of the file apply to the candidate it is processing. That’s also trivial: you know the candidate number, and you know that each candidate takes eight lines, so you can work out which lines to process for candidate n.<br>
You might first try this on *CandidateAnswers123Preprocessed.csv*; then, once you have it working, on *CandidateAnswersAllPreprocessed.csv*.

### Task 11: raw data – 14 marks and Task 12: empty cells – 3 marks
All this time we’ve been working with preprocessed data: the candidates’ actual answers have already been shifted into columns corresponding to the specified roles. But that’s not the way the questionnaire was set up: otherwise candidates would quickly learn that if they gave all their answers to, say, options d, f, and h, they would be observing some form of consistency. Instead, the answers for each question are jumbled, and we need the grid (remember the grid?) to work out which answer for each question goes into which column.<br>
It’s now time for you to implement the grid. Write a function called `translate()`, that takes the list of answer lists produced in `process_candidate()` and returns a list of the same form, but translated onto the grid. When we showed you the grid, we also showed you the raw answers that we have since been using in their preprocessed form. With that example, which is in the file *CandidateAnswers1Raw.csv*, `process_candidate()` would produce and echo the list `[[3, 0, 0, 0, 0, 3, 0, 4], [0, 0, 0, 0, 3, 0, 0, 7], [0, 0, 0, 5, 4, 0, 0, 1], [0, 1, 0, 1, 3, 0, 5, 0], [1, 2, 5, 1, 1, 0, 0, 0], [1, 3, 1, 0, 0, 0, 5, 0], [0, 0, 0, 2, 5, 3, 0, 0]] (the candidate’s actual answers to the questionnaire), but would then call translate(), which would produce the list [[0, 0, 0, 3, 0, 4, 0, 3], [0, 0, 0, 0, 0, 3, 0, 7], [0, 0, 1, 0, 0, 5, 0, 4], [0, 0, 0, 1, 3, 1, 0, 5], [1, 1, 1, 0, 0, 0, 2, 5], [0, 0, 0, 1, 1, 5, 0, 3], [0, 0, 0, 5, 3, 0, 0, 2]]`.<br>
This translation need not involve a great deal of code – perhaps a dozen lines of Python – but it will involve a great deal of thought, of problem solving. As one of the steps, you might find it useful to create yet another list of lists, this one representing in some way the order of the answer letters for each question: for example, for question 1, a list that represents the order b c e f d h g a, as found in the first row of the grid.<br>
You should be able to work this out, but the list returned by `translate()` should be assigned to a variable, and it is that list that should now be analysed, sorted, and displayed.<br>
You should also have worked out that when you call `analyse_csv()` with a raw file, the file type should be ‘raw’; remember that the file type is passed to `process_candidate()`, which will use the file type to decide whether the answers need translating to the grid.<br>
But there’s a catch: as you’ll see if you open them, the raw csv files include blank cells. These are likely to cause problems when you try to form a list of numbers; so while producing the list of numbers from the list of strings in `process_candidate()`, your program will need to replace any blank entries with zeros.<br>

Once you have completed these tasks, your program should work just as well on all the raw files as on the preprocessed files.

### Assumptions: well-behaved data
A ‘real’ program of the sort described here would need to include checks for many things that could go wrong with the data that it is given. A csv file might have the wrong number of lines; it might have the wrong number of entries in each line; the first entry on an answer line might not be of the form Q and a digit (would that matter?); the answer elements might not all be numbers; the numbers in a row might not add up to 10; the candidate’s name might be missing; and so on.<br>
For this assignment you may assume that the data files are all well behaved: that they have none of these problems, and that your program does not need to check for them.

### Note regarding global variables
The Inft1004 text book explains how to use global variables, but we have advised that it is best to use them only when really necessary. This assignment, as specified, does not require any global variables; you are therefore advised not to use any.

## ASSESSMENT CRITERIA
Your work will be assessed out of 100 marks. In addition to the 75 marks listed above with the task descriptions, there will be marks for
- your journal, as specified above, clearly showing the design and development process (12)
- program style, including well-named variables and appropriate and useful comments in the code (13)<br>
Once these marks have been allocated, marks will be deducted for the following:
- failure to follow instructions/requirements, eg with file names
- syntax errors or runtime errors in your program
- failure to fully and clearly reference any material from external sources, such as code written by other people or code with which other people have assisted you
- late submission – see below<br>
If you get code from other people or sources, or if other people help you with your own code, you must add comments making this clear, and explain it in your journal. If the marker uncovers evidence that you have cheated in any way, for example, by sharing your code with others in the class, or by getting help from anyone other than your partner and not referencing it, the matter will be reported to the Student Academic Conduct Officer as a potential case of academic misconduct. (See Academic integrity below.)
