ExamBuilder
===========

Code to take a .txt file containing specially formatted multiple choice questions and build 3 seperate versions of an exam in the form of LaTeX documents.

===========
ExamBuilder.py should be placed into a folder with a .txt file containing the specially formatted questions. (said .txt is set in this version to 'Mt1Questions.txt', to use another file change line 26 to reflect the desired file name)
Each question needs 5 options
You will need to ensure that the the variable np on line 20 is set to the number of questions found in the .txt
You can change the headers and whatnot by changing other variables in that area. (exam # and class name)
The format of the questions in the .txt file should be as described below.
After running, 3 .tex files will appear after running.
To generate a key, uncomment line 9 in the .tex file (remove the % from '%\printanswers ') and run. 
The 3 test versions will contain the same questions in randomly shuffled orders, with the choices shuffled within each question.
<br>
feel free to contact me with questions Imasillypirate@gmail.com

=====================
Formatting for .txt:

-Question (this is where your question goes)
-v or h (put a v here if you want the choices listed vertically, and h if you want them horizontally)
-this and the following 4 lines should contain the options, each starting with '\choice' except the correct choice, which should start with '\correctchoice' 
-option 2
-option 2
-option 2
-option 2
-This line should contain a short explanation as to why the right answer is the correct choice. (this will show up on the Key only)
-there should be a line left blank between this question and the next

example: The questions for a 3 question quiz might look like that written between the lines of astrisks:
**********************************************
Who likes chicken?
v
\choice Only me
\choice Only your mother
\correctchoice Everybody
\choice Nobody
\choice Only cats
Obviously, everybody likes chicken, what else needs to be said?

Look at the acompanying image of a llama, how many teeth are visible?  \includegraphics[width = 2in]{llama.jpg} 
h
\correctchoice 4 
\choice 2
\choice 5
\choice 63
\choice 9
There were 4 visible, that other thing is a breathmint. 

If I code at 3 lines a minute, how long will it take me to write 600 lines?
v
\correctchoice 200 min
\choice 3 min
\choice 63 days
\choice until the end of time
\choice 100 min
To calculate the time we will use unit conversion\\ $600 lines \cdot \frac{1 min}{3 lines} = 200 min$

**********************************************


















