# This script will read in the questions 
# from a .txt file (currently set to Mt1Questions.txt below)
# the format of the .txt should be as follows:
# -1st line is the question,
# -2nd line is either an h or a v, to determine 
#  if the choices are vertically or horizontally listed
# -the next five lines should be the potential choices
#  they should be formatted as \choice Answer
#  All except the correct choice, noted by \correctchoice Answer
# -The next line should be an explaination of why the above was the correct solution.
# -There should then be one empty line.
# -Repeat the above for each question.
#(change variable nq to the correct number of questions)
#
# Run this .py, then run the 3 .tex files in the same folder
# If you uncomment line 9 in a .tex file, it will produce a key.

from random import shuffle
exNum = 1 #exam number
exNam = 'Optics'
nq = 3 #number of questions
cls = 'Phys195 - Spring 2014' #Name of the class to appear in the header
ex = 'Test ' + str(exNum) + '- ' + exNam

version = ['A','B','C'] # 3 versions of the exam
Qlist = range(1,nq+1) #question numbers

file1 = open('Mt1Questions.txt','r') #read in questions, solutions and choices
Questions = {}
Solutions = {}
Answers = {}
Stacks = {}
for q in Qlist:
	question = file1.readline()#question
	stack = file1.readline()#choice stack option
	Answer1 = file1.readline()#A1
	Answer2 = file1.readline()#A2
	Answer3 = file1.readline()#A3
	Answer4 = file1.readline()#A4
	Answer5 = file1.readline()#A5
	Solution =  file1.readline()#solution
	ES =  file1.readline()#Empty Space
	Questions[q] = question
	Solutions[q] = Solution
	Answers[q] = [Answer1, Answer2, Answer3, Answer4, Answer5]
	Stacks[q] = stack


for i in version:
	shuffle(Qlist) #determine question order
	
	FileName = 'Mt'+ex+'V'+i+'.tex'
	with open(FileName, 'w') as texfile:
		texfile.write('\\documentclass[12pt,addpoints]{exam} \n')
		texfile.write('\\usepackage{graphicx} \n')
		texfile.write('\\pagestyle{headandfoot} \n')
		texfile.write('\\runningheadrule \n')
		texfile.write('\\firstpageheader{'+cls+'}{Exam'+ex+' Version '+i+'}{ } \n')
		texfile.write('\\runningheader{'+cls+'}{Exam'+ex+' Version '+i+'} {Page \\thepage of \\numpages} \n')
		texfile.write('\\firstpagefooter{}{}{} \n')
		texfile.write('\\runningfooter{}{}{} \n')
		texfile.write('%\\printanswers \n')
		texfile.write('\n')
		texfile.write('\\begin{document} \n')
		texfile.write('\\ifprintanswers \\begin{center} \\huge KEY \\end{center} \\fi \n')
		texfile.write('\n')
		
		texfile.write('\\begin{center} \n')
		texfile.write('\\fbox{\\fbox{\\parbox{5.5in}{\\centering This exam contains 3 questions. You will have 15 minutes to complete the exam. Record the answer that you would like graded on your scantron. Make sure to put your name and RedId on the scantron.}}} \n')
		texfile.write('\\end{center} \n')
		texfile.write('\\vspace{0.3in} \n')
		texfile.write('\\makebox[\\textwidth]{Name:\\enspace\\hrulefill} \n')
	
		texfile.write('\\begin{questions} \n')
		
		for k in Qlist: #write questions
			Ans = Answers[k]
			shuffle(Ans) #Determine Choice order
			texfile.write('\\begin{minipage}{\\textwidth} \n')
			texfile.write('\\question \n')
			texfile.write(Questions[k]) #the question
#			texfile.write('\\answerline[\\ref{Ans'+str(k)+'}] \n')
			
			if Stacks[k] in 'h\n': #determine layout of choices
				choiceStyle = 'oneparchoices'
				ln = '\\'
			else:
				choiceStyle = 'choices'
				ln =  ' ' 
			texfile.write('\\begin{'+choiceStyle+'}'+ln+' \n')
			
			for j in Ans: #write choices
				texfile.write(j)
			
			texfile.write('\\end{'+choiceStyle+'} \n')
			
			texfile.write('\\begin{solution} \n')
			texfile.write(Solutions[k])
			texfile.write('\\end{solution} \n')
			texfile.write('\\vspace{0.2in} \n')
			texfile.write('\\end{minipage} \n')
			texfile.write('\n')
			
		texfile.write('\\end{questions} \n')
		texfile.write('\\end{document}')    
