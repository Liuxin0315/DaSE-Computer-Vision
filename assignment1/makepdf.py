import PyPDF2
import os

file_merger = PyPDF2.PdfFileMerger()  # 类的实例
pdflist = []  # 准备一个空列表用于放pdf绝对路径
filelist = os.listdir(r'./pdf')
for f in filelist:  # 查找路径中的pdf文档
    if f.endswith('.pdf'):
        f1 = os.path.join(r'./pdf', f)
        pdflist.append(f1)
print(pdflist)
for pdf in pdflist:
    file_merger.append(pdf)  # 合并pdf文件
file_merger.write(r'assignment.pdf')  # 写到合并后的文件中