import  sys
import  subprocess
import  pdfkit
inputfile = sys.argv[1].replace(" ","\ ")
temp_html = inputfile[0:inputfile.rfind('.')] + '.html'
command = 'ipython nbconvert --to html' + inputfile
subprocess.call(command,shell=True)
print("*"*10)
outputfile = inputfile[0:inputfile.rfind('.')]+ '.pdf'
pdfkit.from_file(temp_html,outputfile)
subprocess.call('rm'+temp_html,shell=True)