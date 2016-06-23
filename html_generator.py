
stage_topics=[["www","How the web works?","html","Tags in HTML","HTML attributes","void tags","pages linked"," Why are Computers Stupid","difference between inline tags and block tags","whitespace tags","container tags"]
              ,["Why Start with HTML and CSS","How to think like a FRONT END WEB DEVELOPER","Imporatnce of DOM","BOXES,BOXES ,BOXES EVERYWHERE","Tree like structure of the page","Importance of boxes and indentation","Text Editors"]
              ,["Using CSS","Creating Reusable Code Using Various Selectors","Methods to implement CSS","The Box Model","All About the Borders","Very Important","Code Test Refine"],
              ["What is a Program?","What is Python","Need for invention of new languages for computer","Bakus-Naur form","difference between a compiler and an interpreter","variable","comments","Strings","Important Properties of Strings","Find Operation in Strings","Functions","Lists & Lists v/s Strings","Nested Lists","Mixed Up Lists","Mutation","Aliasing","List Operations"," Making Decisions","Proramming is cool","Loops","Break Statement","For Loops","How To Solve Problems","Debugging"]]


stages={1:"Some  basic  Concepts  of  the  Web  and HTML", 2:"Creating  A  Structured  Document  With  HTML",
        3: "Styling  using  CSS",4: "Structured  Data-Lists, Strings  and  Loops"}

def generate_stage(stage):
    html_stage= '''
<div class="stage">'''+stage
    return html_stage

def generate_stage_end():
    return """
</div>"""

def get_stage(stage,stages):  
    return stages[stage]

def generate_concept_HTML(concept_title, concept_description):
    html_text_title_opening = '''
<div class="concept">
    <div class="concept_title">
        ''' + concept_title
    html_text_description_opening = '''
    </div>
    <div class="concept_description">
        ''' + concept_description
    html_text_tag_close = '''
    </div>
</div>'''   
    full_html_text = html_text_title_opening + html_text_description_opening + html_text_tag_close
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(stage,text, concept_number,stages):
    counter = 0    
    next_concept_stage_start=text.find(stages[stage])    
    next_stage=text.find("STAGE",next_concept_stage_start+1)
    text=text[next_concept_stage_start+1:next_stage-1]
    
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        if next_concept_end >= 0:
            concept = text[next_concept_start:next_concept_end]
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:]
        text = text[next_concept_end:]
    return concept

TEST_TEXT = """
STAGE 1: Some  basic  Concepts  of  the  Web  and HTML

TITLE: What is the World Wide Web(WWW)?		
DESCRIPTION: The WWW is basically a bunch of computers connected together
These computers can communicate that is share information,pictures,videos etc with each other through internet.
It is simply called Web.
It came up in early 1990's and contains about 30 billion pages.
The Web is a collection of many WEB PAGES which are actually HTML documents.It glues everything on the web-
IMAGES,TEXTS,VIDEO,MEDIA etc.
HTML stands for HYPER TEXT MARKUP LANGUAGE	
Hyperlinks are used to communicate between different web pages.

TITLE: How the web works?
DESCRIPTION: When the user (with a computer and a browser) opens a website,the browser makes request to the internet.
The internet further requests the server using the HTTP .
The server finds the appropriate HTML document and sends it back to the 
user's computer where a web browser interprets the page and displays it on the user's screen

TITLE: What is HTML?
DESCRIPTION: HTML stands for HYPER TEXT MARKUP LANGUAGE
Its text content describes all that we see
Markup decides what everything looks like
HTML document contains refrences/links to other documents like images,video,other web pages etc.
HTML is made up of elements

TITLE: What are the Tags in HTML?
DESCRIPTION: HTML documents are made up of elements.
(start of tag using triangular brackets )tag content (end of tag using triangular brackets and / ) = HTML element 
HTML tags tell the browser the type of elements 
Except for void tag,Once a tag is started,it has to be closed otherwise its effect will be seen on all the following elements
FOR EXAMPLE:
bold,em,img,br,p tags cater to making the text bold,emphasized,add image,line break,paragraph tag respectively

TITLE: What are HTML attributes ?
DESCRIPTION: Attributes provide additional information about an element
Attributes are always specified in the start tag.
Attributes come in name/value pairs like: name="value"
for example:		
The href=" "  attribute in anchor (a) tag provides the hyperlink 
The src(source) ="url" attribute in image tag provides the file path of the image
The alt="text" attribute in image tag provides an alternate text if the image is not displayed 	

TITLE: What are void tags?
DESCRIPTION: Tags which don't need to be closed are void tags.For Example br tag is a void tag

TITLE: How are pages linked?
DESCRIPTION: Pages are linked using Hyperlinks with the help of a (anchor) tag.The href attribute is used to give the url.
for example <a href="www.google.com">Link to google </a>

TITLE: Why are Computers Stupid?
DESCRIPTION: Computers are stupid because they blankly follow the instructions given to them.They <b class="bold"> Do Not Rectify </b> the mistakes made by 
the programmer themselves.Computers interpret the instructions as such	

TITLE: What is the difference between inline tags and block tags? 
DESCRIPTION: Inline tags are written along with the text.They don't create any separate block.They are just texts For Example,br tag is written 
at the end of line Br tag means end of linr.When written between text,the following text after the tag wraps up in the next line
b,em ,img are inline tags
Block tags create a separate invisible block of text .These boxes can have hheight and width also
for example: p tag

............
. text     .
. text     .
. text     .
. text     .
............	

TITLE: What are the whitespace tags? 
DESCRIPTION: Whitespace tags are used to marks end of line or separate out a segment of text.
When an HTML page is created,no matter how many whitespaces are given all of them are created into a single white space		
for example:
br tag and p tag

TITLE: What are container tags?
DESCRIPTION: Span & Div are container tags
Span is inline while Div is block type tag.		
Div tag behaves like paragraph tag.
various arrtributes can be given to Span and Div
They contain text.



STAGE 2: Creating  A  Structured  Document  With  HTML

TITLE: Why Start with HTML and CSS?
DESCRIPTION: Any Code that is written,Changes made are visible automatically .
When websites are created,they give a medium to share knowledge	

TITLE: How to think like a FRONT END WEB DEVELOPER
DESCRIPTION: Think of the website as a home 			
HTML-HTML files are like the structure 
for Example:
Where are the walls,kitchen,doors etc
HTML is the Language,Syntax rules of the web
CSS-CSS files are the style of your house,What colour are the walls etc
CSS is the use of specific syntax and rules to change how elements look on the page eg: colour,font etc
Javascript-javascript files are the interactive components like door opener,TV remote etc
DOM-Standard convention for representing and interacting with HTML elements

TITLE: Imporatnce of DOM
DESCRIPTION: Basic word in a HTML document is a tag.browser turns html tags into elements that form a TREE like structure .It knows how to do that 
because of DOCUMENT OBJECT MODEL that is DOM
each element creates an element in the dom 

TITLE: BOXES,BOXES ,BOXES EVERYWHERE
DESCRIPTION: On a web page anything may seem to be circular,triangular or irregular in shape but it is actually all in a box

TITLE: Tree like structure of the page
DESCRIPTION: The "tree-like structure" comes from the fact that HTML elements can have other elements inside of them. You can draw this 
relationship like a family tree.Parent class has multiple children.
In a browser, this structure shows up as a series of nested boxes. There are boxes inside of boxes inside of boxes, and so on...

TITLE: Importance of boxes and indentation
DESCRIPTION: By thinking in terms of boxes we can easily rearrange things if we decide to give user's a different experience.
we define boxes using div tag.Each box and sub box corresponds to div tag
each div tag should be marked to style later 
In HTML document we see a wave of changing indentations going up and down the left side of the document. The more indented an 
element is, the more deeply nested it's corresponding "box" is.

TITLE: Text Editors
DESCRIPTION: Coders use text editors which can make programming easier.Some of these automatically generate the tag/code the author is typing thus 
reducing time and effort
sublim text is such example

STAGE 3:Styling  using  CSS 

TITLE:	Using CSS
DESCRIPTION: CSS stands for cascading style sheets
CSS is a powerful languages to add style to web pages
the most important fact is that reusable code can be created using classes ids etc
CSS provides numerous properties to modify the web page making it more attractive				
some examples:
background-color
font-family
background-img
and MANY MANY MORE

TITLE: Creating Reusable Code Using Various Selectors
DESCRIPTION: Various types of classes and ids can be given to different elements which need similar type of styling
Reusable code is important because it provides a standard design pattern,framework.It also saves time and effort
some of the selectors are:

if a class is given

.classname{ 

properties;
}			

if an id is given


#idame{ 

properties;
}


if tag is used directly


tagname{ 
properties;
}   		


TITLE: Methods to implement CSS
DESCRIPTION: CSS can be added in 3 ways:
Inline method :style is added along with the tags
Internal method:Style is written is the head
External method:Styles are written in a separate file stored with the extension .css and linked to the html

TITLE: The Box Model
DESCRIPTION: Margins,borders,padding and content make the box model 
Content:is present at the center.other layers protect it so that other items on the page do not overlap
padding: It clears around the content.It is affected by the background colour around the box
Border: It surrounds padding and content.it inherits colour properties of the box
margins:It is the outermost layer.It has no background color and is transparent,It is the space between boxes	

TITLE: All About the Borders
DESCRIPTION: By default the size of element = border+padding+Content space		
*{		
box-sizing:border-box;		
}		
can be used to find the element size
By just setting the size of the box,no matter what the border and padding is the box size will remain the same.
Browser Specific Prefixes have to be added to make sure that all browsers are able to display this					
BROWSER SPECIFIX PREFIXES:				
webkit 
moz
ms

TITLE: Very Important
DESCRIPTION: If the size is set in percentage,the size will change depending on how big the screen is.If the box size is in pixels
it will take exactly that size and will not change according to the screen	

TITLE: Positioning of the Elements
DESCRIPTION: FLEX BOX LAYOUTz
flex Box layout provides an efficient way layout line and distributor space among items in a container
if several items are to be placed next to each other,the display attribute of parent container should be set to value FLEX	

TITLE: Cool web sites to get more HTML and CSS hacks
DESCRIPTION: http://www.dtelepathy.com/ for colour palette
http://tympanus.net/codrops/
w3schools
https://css-tricks.com	

TITLE: Code Test Refine
DESCRIPTION: Look for natural boxes
look for repeated styles and semantics
write your html
apply styles biggest to smallest
fix things
repeat 3,4,5


STAGE 4:Structured  Data-Lists, Strings  and  Loops

TITLE: What is a Program?
DESCRIPTION: A program is a set of instructions which tell the computer what to do.A computer can execute many steps in just fraction of seconds.We can execute billions of instructions in one second using a computer program.A program needs to be precise sequence of steps

TITLE: What is Python?
DESCRIPTION: PYthon is a high level language.Instead of writing the program directly on the computer,the program will be an input to the python program which runs on the computer.
PYTHON IS CALLED AN INTERPRETER.It runs our programs,interprets them and executes the programs that we write in Python language by returning a program in a language that the computer and the user can understand quickly.

TITLE: Why we need to invent new languages to program computers rather than using natural languages like English?
DESCRIPTION: 1) AMBIGUITY: Different people interpret same language differently,but in a computer we want it to interpret the same program the exact same way that the programmers intended.			
2) VERBOSITY:To write a program, we need to describe exactly what the computer should do in a very precise sequence of steps.Using a natural language for such large description will require a huge amount of text.WITH PYTHON,WE CAN DESCRIBE IN A VERY PRECISE STEP BY STEP WAY	

TITLE: What is Bakus-Naur form? 
DESCRIPTION: BACKUS-NAUR FORM is the Python grammar for Arithematic expressions
expression operator expression is called recursive definition.Expression can be numbers and terminals.

TITLE: What is the difference between a compiler and an interpreter?
DESCRIPTION: A compiler does all the worl once and then runs the program whereas an iterpreter reads,executes,runs etc all simultaneously	

TITLE: What is a variable?
DESCRIPTION: A variable is a name given to a memory location to store some data.Variable name can be any sequence of alphabets,numbers etc as long as it starts with a letter.Their values can be varied at any time.	

TITLE: What are comments ?
DESCRIPTION: Comments are statements written after "#" sign.They are ignored by the Python interpreter but are useful for a programmer to understand.If someone other than the progrmmer is reading the code,he can understand the code better with help of comments.

TITLE: What are Strings?
DESCRIPTION: A string is traditionally a sequence of characters,either as constants or some kind of variable.In Python,strings are immutable.A String is a data type and is implemented as array of bytes

TITLE: Important Properties of Strings
DESCRIPTION: 1) If string starts with single quote it ends with same..if double quotes same end
2)
Print hello will give error
but if hello is a variable and not a string it will print the value of the variable 
also " 'string data" is a valid string or vice a versa with the quotes

3) Strings can be concatenated that is two or more strings can be joint using '+ 'sign and form a new string,It dosen't ad spaces or anything automatically

4) Concatinating a string and a number will give error

5) We can multiply numbers and strings,
for eg:
print '!'*4
will print: !!!!

6) String indexing:
used to extract sub parts of a string
"string name"[expression]
eg:
name='udacity'
print name[0]
will print u

or:
'udacity'[0] will give 'u'
indexing starts from 0s
'udacity'[1+1] gives 'a'
index -1 gives last character 
-2 gives next to last character and so on

7) Selecting a substring:
<string>[<expression(start)>:<expression(end)>]
this gives a substring of characters from the string starting from position start and ending with position end-1
also strring[3:3]
prints nothing
if we leave one of the sides of colon empty:
string[4:] will print all characters from inex 4 onwards uptill end

string[:6] will produce all characters upto index 5 starting from begining

if we leave both sides of colon empty it will give the string from beginng to end i.e. the complete string itself
eg: string[:]	

TITLE: Find Operation in Strings
DESCRIPTION: 1) method to find a sub string in a big string:
find is a method which means it is a built in procedure
syntax: 
string.find(string to be fouund)
the result will be the position of the first occurrence of the string.a string may be present multiple times
if the sub string is not found anywhere it will return -1

2) There might be other occurrences of the same sub string.if  we pass an extra parameter i.e. number it will give the position of the sub string immediately after the 
occurrences of the sub string first time after the position given by the parameter number
syntax: 
string.find(string to be fouund,number)
if we pass 0 it will return the position of first string only
-1 will be returned if no string is found after the given parameter number

3) Triple quotes can be used to make a string of multiple lines
index method:
list.index(element to be found) returns the index of the list whose value is the same as required element

TITLE: All About Methods/Procedures/Functions
DESCRIPTION: 1) How to use functions/procedures?
procedure name(list of inputs called arguments or operands separated by a ,) 
syntax:
procedure name(input1,input2....)

2) return means jumping back to the procedure

3) making or defining a procedure:
Functions are made by starting a line of code with the keyword def and then giving a function name followed by the function parameters in parentheses. These parameters will eventually be replaced by actual values when the function is used (called).
syntax:
def procedure_name(parameter1/input1,parameter2/input2.....)
we are actually making a procedure using this.we are defining set of statements which will perform certain task on the inputs

4) How do functions help programmers avoid repetition?
Functions are tools that programmers can create and reuse forever! Once you've defined a function once, you never have to define it again.By defining a function and passing inputs we can avoid repition of same code for different set of values.All we need to do is call the function and pass the values as arguments.

5) What happens if a function doesn't have a return statement?
if a function does not have a return statement it will do nothing.When the function is called it will give no value.The return keyword tells Python exactly what the function should produce as output.

TITLE: Lists & Lists v/s Strings
DESCRIPTION: LISTS:are collection of variables and constants of same of different data types

List v/s Strings

1) In a list elements can be of any data type but in strings they are always character type
2) string="characters in single or double quotes"
list=['element 1','element 2'....]

3) Indexing:
string[0]=c
list[0]=element 1

4) example: st='abcdefg'
l=['a','b','c','d','e','f','g']
st[2:4]='cd' that is a string
but
l[2:4]=['c','d'] which is a list
5) lists are mutable,strings are not
example:
l=[1,2,3,4,5]
l[2]=9
therefore l=[1,2,9,4,5]

TITLE: Nested Lists
DESCRIPTION: Lists can be nested i.e. a list can contain multiple lists
We can access elements of the main list using indexing.Since sub lists are also lists,we can access their elements also

TITLE: Mixed Up Lists
DESCRIPTION: Lists can contain different data type elements:
for example :
mixed=[1,2,["apple","banana,23,34"]]
we can access the member of sub list as:
mixed[2][2] This will give 23

TITLE: Mutation
DESCRIPTION: we can change the values of a list after we have created it
in strings,we have to create a new string to replace the old one or concatenate two strings but in Lists we can simply replace the element to be changed using indexing.
In lists,if one list is assigned to another then both of them refer the same object Therefore,any change made in the second list(copied) will also be visible in the first list(ORIGINALS)
IMPORTANT:
a) Once an object is mutable,we have to worry about the variables refering to the same objects.
b)strings are immutable,we can not change any element of the string even using indexing	

TITLE: Aliasing
DESCRIPTION: When two or more variables refer to the same object,then any change made in the object ,then the change will come in all the variables
example:
p=[1,2,3,4],
q=p,
here both p and q refer to same list
if we change a cee like q[2]=7
then the object changes 
p and q both =[1,2,7,4],
BUT:
if we do an assignment like p=["a","b","c"]
This will create a new object to which p refers.q will not be affected	

TITLE: List Operations 
DESCRIPTION: 1)Append:
list.append(element to be added)
append is a function or method of lists.Append is not creating a new list,it is mutating an old list by adding an element at its end
2) + operation:
+ operator works like concatination 
example:
[1,2]+[3,4]=[1,2,3,4]

3) len operator:
len is short form for length. len(<list>) will give the length of the list
for example:
len([0,1])=2
IMPORTANT EXAMPLE:
p=[1,2],
q=[3,4]
len(p+q)=4,
p+q=[1,2,3,4],
BUT
p.append(q)=[1,2,[3,4]]
therefore len(p.append(q))=3

TITLE: Making Decisions
DESCRIPTION: 1) Comparison operators can be used as:
operand 1 comparison operator operand 2
"<", "> ","<=","<=" etc are examples of comparison operators
The output is not a number but a boolean value True or False
2) The if statement:
syntax:
if test expression:
block
next statement
The block contains the statements/instructions to do when the test expression is True.
the next statement that is not indented will be evaluated no mater the test case is true or not

3) the "or" construct
evaluates an expression to check two conditions
returns:
true for true and true,
true for true and false,
false for false and false,
expression 1 or expression2
if expression1 is true expression2 is not evaluated and True is returned,
if expression2 is not true  expression2 is evaluated and True is returned if expression2 is true,
if expression2 is not true  expression2 is evaluated and False is returned if expression2 is False.	

TITLE: Proramming is cool
DESCRIPTION: Once you (or anyone else) has coded something once, you can use that thing again later as a tool!

TITLE: Loops	
DESCRIPTION: Its a way to do things do over and over again
While loop:
syntax:
while test expression:
<t>block</t>
with while loop ,block can execute any number of times.It  keeps going as long as the test case is true
the test expression is tested,if it is true,Python goes to the block.It tests the expression again,if it is true it wil go to the block again otherwise break out of the loop	

TITLE: Break Statement
DESCRIPTION: Break statement is used to stop the loop if a particular condition is met,even while test condition of the loop is true
syntax:
while test expression:
block
if break test:
break

TITLE: For Loop
DESCRIPTION: A for loop is used to perform iterative operatios that is to repaeat a task multiple times.
Structure of for loop:
for name in list:
block 
for each element in a list,we are going to assign it to the name and evaluate the block
example:
def printall(p):
for e in p:
print e

This function assigns the value of each element in p to e at a time and is printed

TITLE: How To Solve Problems
DESCRIPTION: PYTHONIA'S GUIDE TO SOLVE ALL PROBLEMS IN THE KNOWN COMPUTATION GALAXY:
STEP 0) Don't Panic
STEP 1) Think/Ask about the inputs
STEP 2) Think about the output
STEP 3) Work throug some examples by hand
STEP 4) Simple mechanical solution 
TIP:
DON'T OPTIMIZE PREMATURELY.THE KEY IS SIMPLICITY		
Make sure you understand the problem.
The problem with start writing code first is that we may end up code that dosn't work properly which can be frustrating or the code that dosn't actually work.

FOR EXAMPLE: In a program we have to calculate the present age in number of days,we will proceed as:
STEP 1) Inputs: 2 dates
What is set of valid inputs?
As a good defensive programmer we must check that the second date is always greater tham the first date
it is a good practice to check that the dates are in the Georgian Calender 
STEP 2) Output: return the number of days between the two dates

STEP 3) Solving Problem:
aUnderstand the relationships using examples
STEP 4) Starting to form the solution:
1)We will write the function nextDay(yr,month,date) to get next day for simple case or isLeapYear(year) to check if the year is leap or not
2)The next step is to define daysBetweenDates(y1, m1, d1, y2, m2, d2) to give approximate answers using nextDay procedure
3)Write pseudocode
4)Write helper function
STEP 5) Adding assertions for invalid inputs




TITLE: Debugging
DESCRIPTION: Errors in programs are called bugs.Sometimes the error is obvious as it makes the program crash and when it crashes it usually gives some kind of error message.
When a Python code crashes it gives back a message "Traceback".
TRACEBACK:
Traceback tells you what line it crashed on and what file was running and how it got there.The information it gives you especially the line number and the function name.Even if the root of the problem is not in that line,it is somewhere upstream that line.We can look up the error message to see how to rectify it.
ONE APPROACH TO DEBUGGING IS:
1) Comment out the original code
2) Copy and paste the sample code and make changes in it according to the output required
3) When the desired output is achieved,make ammendments in the original code and uncomment it
IMPORTANT:
Always remove the debugging print statement.
To comment out a statement just put a hash mark(#) before the statement or make it into a large string by using triple quotes.Software programmers use version control systems like GIT,which are super powerful undo systems that let you navigate to any version of the code that have multiple modified version and share them and so on

DEBUGGING STRATEGY RECAP:
1) Examine error messages when programs crash:
The last line of Python Tracebacks will tell you what went wrong. Reading backwards from there will tell you more about where the problem occurred.

2)Work from example code:
If your modified code doesn't work, comment it out and do step-by-step modifications to the example code until it does what you want.

3)Make sure examples work:
Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect.

4)Check (print) intermediate results:
When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly.

5)Keep and compare old versions:
When you have a working version of your code, save it before you add to the code. This will give you something to go back to if you introduce too many new bugs

DEBUGGING IS ACTUALLY A SCIENTIFIC APPROACH OF EXAMINING THE CODE TO DISCOVER UNEXPECTED RESULTS
"""

def generate_all_html(text):
    iteration=1
    
    complete_html=''
    while iteration<=4:
        
        stage_text=get_stage(iteration,stages)      
        
        get_stage_title=generate_stage(stage_text)        
        complete_html=complete_html+get_stage_title
        
        current_concept_number = 1
        
        concept = get_concept_by_number(iteration,text, current_concept_number,stages)
        
        all_html = ' '                
        
        while current_concept_number <=(len(stage_topics[iteration-1])) :           

            title = get_title(concept)
            
            description = get_description(concept)
            
            concept_html = generate_concept_HTML(title, description)
            
            all_html = all_html + concept_html
            
            current_concept_number = current_concept_number + 1

            concept = get_concept_by_number(iteration,text, current_concept_number,stages)
           
        
        iteration=iteration+1
        stage_end=generate_stage_end()
        complete_html=complete_html+all_html
        complete_html=complete_html+stage_end+str("""
----------------------------------------------------------------------""")
    return complete_html
        
print generate_all_html(TEST_TEXT)

        

        
        
