import re  #Importing regular expression for search task

def arithmetic_arranger(problems,solve=False):

  #Error if more than 5 problems
  if len(problems)>5:
    return "Error: Too many problems."

  #Defining variables for each line
  top_line=""
  bottom_line=""
  dash_line=""
  solution_line=""
  arranged_line="" #Result string variable

  #find the sums that need to be calculated and put them in a list
  for problem in problems:
    num_list=problem.split()
    num1=num_list[0]
    operator=num_list[1]
    num2=num_list[2]

    #Error defining for validation
    if operator=="*" or operator=="/":
      return "Error: Operator must be '+' or '-'."

    if re.search("[^\d]",num1) or re.search("[^\d\+\-]",num2):
      return "Error: Numbers must only contain digits."

    if len(num1)>4 or len(num2)>4:
      return "Error: Numbers cannot be more than four digits."

    #Define the answers
    answer=""
    if operator=="+":
      answer=str(int(num1)+ int(num2))
    elif operator == "-":
      answer=str(int(num1) - int(num2))
      
    #Find the max length of the line needed
    line_length=max(len(num1),len(num2))+2

     #Find the value of the num1 line
    num1_line=""
    num1_line = str(num1.rjust(line_length))

    #Find the value of the num2 line
    num2_line=""
    num2_line =str(operator) + str(num2.rjust(line_length - 1))

    #Find the value of the dash line
    dashes=""
    for i in range(line_length):
      dashes +="-"

    #Find the value of the answer line
    answer_line=""
    answer_line += answer.rjust(line_length)

    #Formatting the space alignment of each line
    if problem != problems[-1]:
      top_line += num1_line + "    "
      bottom_line += num2_line + "    "
      dash_line += dashes + "    "
      solution_line += answer_line + "    "
    else:
      top_line += num1_line 
      bottom_line += num2_line 
      dash_line += dashes 
      solution_line += answer_line

  #Alignment of the arithemtic sum
  if solve==True:
    arranged_line = top_line + "\n" + bottom_line + "\n" + dash_line + "\n" + solution_line
  else:
    arranged_line = top_line + "\n" + bottom_line + "\n" + dash_line
  
  return arranged_line