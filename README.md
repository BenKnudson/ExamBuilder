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
Feel free to contact me with questions Imasillypirate@gmail.com

=====================
Formatting for .txt:<br>

-Question (this is where your question goes)<br>
-v or h (put a v here if you want the choices listed vertically, and h if you want them horizontally)<br>
-this and the following 4 lines should contain the options, each starting with '\choice' except the correct choice, which should start with '\correctchoice' <br>
-option 2 <br>
-option 3 <br>
-option 4 <br>
-option 5 <br>
-This line should contain a short explanation as to why the right answer is the correct choice. (this will show up on the Key only) <br>
-there should be a line left blank between this question and the next <br>

example: The questions for a 3 question quiz might look like that written between the lines of astrisks:<br>
**********************************************
Who likes chicken? <br>
v <br>
\choice Only me <br>
\choice Only your mother <br>
\correctchoice Everybody <br>
\choice Nobody <br>
\choice Only cats <br>
Obviously, everybody likes chicken, what else needs to be said? <br>
<br>
Look at the acompanying image of a llama, how many teeth are visible?  \includegraphics[width = 2in]{llama.jpg} <br>
h <br>
\correctchoice 4 <br>
\choice 2 <br>
\choice 5 <br>
\choice 63 <br>
\choice 9 <br>
There were 4 visible, that other thing is a breathmint. <br> 
<br>
If I code at 3 lines a minute, how long will it take me to write 600 lines? <br>
v <br>
\correctchoice 200 min <br>
\choice 3 min <br>
\choice 63 days <br>
\choice until the end of time <br>
\choice 100 min <br>
To calculate the time we will use unit conversion\\ $600 lines \cdot \frac{1 min}{3 lines} = 200 min$ <br>
<br>
**********************************************


















