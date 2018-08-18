__author__ = '''Nicat Shukurov
                email: nicatsukurov@gmail.com'''

##Importing important libraries
import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib import style
import matplotlib

from Tkinter import *
import ttk
import tkMessageBox
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
import tkFileDialog
import FileDialog


import xlrd
import xlwt


import math
import numpy as np



##====================================================================
##==============================cozmetic variables
LARGE_FONT=("Verdana",12)
NOMR_FONT=("Verdana",10)
SMALL_FONT=("Verdana",8)

DARK_COLOR="#183A54"
LIGHT_COLOR="#00A3E0"

style.use("ggplot")##style for matplot

path="C://"
filename="GRADES"

CURVE=0
##===================================================================POSITIONS
#Graph 1
graph_1_x=360
graph_1_y=10

#Graph 2
graph_2_x=790
graph_2_x=10

#Graph size
height_of_graph=4
width_of_graph=3

#Screen
x_of_root= 0
y_of_root= 0
height_of_root=600
width_of_root=1300
##==============================main variables
MAIN_DATA=[]
'''Data safe is an 2d array which consist of all datas of excel file,
and 1st dimension is types of arrays(mt1,mt2,names,finals and so.on) second dimension is
array objects of first dimension array(it can be grades , or all names , or all studing numbers so on.)
'''
##===============================Important functions
#======================================================Plotting graph for 1s place
def close_all():
    ##closing all open tabs
    plt.close('all')

def close_preexist():
    ##closing preexist open tabs
    plt.close()

def plot_graph_1(data_1):
       '''This function gets one dimension data from data_safe=[][] array
          and converts it to float then erases first data whihc is name of array for excample
          ['mt1','20','40','60']. After that it is easy to deal with float numbers.Then it shows the histogram
          at the left place of GUI of program.
       '''
       y=[]
       x=[]
       a=list(data_1)
       a.pop(0)

       '''in this part we will procses data if it consist of string number or just float integer numbers or [N.A, NA, n.a , na ] type strings
       '''
       boolean=True
       try:
           if len(a)>0:
               for m in range(len(a)):
                   if isinstance(a[m],float) is True or isinstance(a[m],int) is True:
                      y.append(int(a[m]))
                      x.append(m)
                      boolean=True
                   elif a[m]=='' or a[m]=='NA' or a[m]=='N.A' or a[m]=='na' or a[m]=='n.a' or a[m] is None or a[m]==' ':
                      y.append(0)
                      x.append(m)
                      boolean=True
                   elif a[m]=="erased":
                       boolean=True
                   else:
                      tkMessageBox.showwarning("DATA TYPE ERROR 1", "Can not open this data  \n(%s)  due to it consist of string variables"%data_1[0])
                      boolean=False
                      break
           else:
               tkMessageBox.showwarning("DATA TYPE ERROR 2", "data is zero")
               boolean=False
       except:
           tkMessageBox.showwarning("HISTOGRAM ERROR 2", "Can not open this data  \n(%s) , it is null"%data_1[0])

       ##creating canvas to clearing garbage
       canvas = Canvas(root, width =300, height = 250, bg="wheat")
       canvas.place(x=370,y=310)
       if boolean==True:
           try:
               f = Figure(figsize=(3,3), dpi=100)
               a = f.add_subplot(111)
               a.hist(y)
               dataPlot = FigureCanvasTkAgg(f, master=root)
               dataPlot.show()
               dataPlot.get_tk_widget().place(x=370, y=10)
               Label(root,text=str("Histogram 1:   "+data_1[0])).place(x=370,y=10)
           except:
               tkMessageBox.showwarning("HISTOGRAM ERROR 2", "Can not hist this data  \n(%s)"%data_1[0])
           ##Adding mean and std
           try:
               std=np.std(y)
               mean=np.mean(y)
           except:
               std=0
               mean=0

           Label(root,text=str("STD:   "+format(std,'.2f'))).place(x=370,y=320)
           Label(root,text=str("MEAN:    "+format(mean,'.2f'))).place(x=370,y=340)

       else:
           canvas_for_plot2=Canvas(root, width =300, height = 300, bg="wheat")
           canvas_for_plot2.place(x=370,y=10)
           canvas_for_plot2.create_text(150,10,fill="darkblue",font="Times 16 italic bold",text="(%s) is wrong type data"%data_1[0])
           canvas_for_plot2.update


##creating button fucntion for graph for different canvas
def show_graph_1(data_1):
    '''This function gets one dimension data from data_safe=[][] array
          and converts it to float then erases first data whihc is name of array for excample
          ['mt1','20','40','60']. After that it is easy to deal with float numbers.Then it shows the histogram
          at the left place of GUI of program.
       '''
    ##conveting to float
    y=[]
    x=[]
    a=list(data_1)
    a.pop(0)

    '''in this part we will procses data if it consist of string number or just float integer numbers or [N.A, NA, n.a , na ] type strings
       '''
    boolean=True
    if len(a)>0:
        for m in range(len(a)):
            if isinstance(a[m],float) is True or isinstance(a[m],int) is True:
                y.append(int(a[m]))
                x.append(m)
                boolean=True
            elif a[m]=='' or a[m]=='NA' or a[m]=='N.A' or [m]=='na' or [m]=='n.a' or a[m] is None or a[m]==' ':
                y.append(0)
                x.append(m)
                boolean=True
            elif a[m]=="erased":
                boolean=True
            else:
                tkMessageBox.showwarning("DATA TYPE ERROR", "Can not open this data  \n(%s)  due to it consist of string variables"%data_1[0])
                boolean=False
                break

    if boolean==True:
        try:
            fig_hist1=plt.figure()
            plt.hist(y)
            plt.title(str("Histogram:"+data_1[0]))
            plt.show(fig_hist1)
        except:
            tkMessageBox.showwarning("DATA TYPE ERROR 2", "can not hist data")
    else:
        pass

##=====================================================Plotting graph for 3th place
def plot_graph_2(data_2):
       '''This function gets one dimension data from data_safe=[][] array
          and converts it to float then erases first data whihc is name of array for excample
          ['mt1','20','40','60']. After that it is easy to deal with float numbers.Then it shows the histogram
          at the right place of GUI of program.
       '''
       ##conveting to float
       y=[]
       x=[]
       a=list(data_2)
       a.pop(0)
       boolean=True
       '''in this part we will procses data if it consist of string number or just float integer numbers or [N.A, NA, n.a , na ] type strings
       '''
       if len(a)>0:
           for m in range(len(a)):
               if isinstance(a[m],float) is True or isinstance(a[m],int) is True:
                  y.append(int(a[m]))
                  x.append(m)
                  boolean=True
               elif a[m]=='' or a[m]=='NA' or a[m]=='N.A' or [m]=='na' or [m]=='n.a' or a[m] is None or a[m]==' ':
                  y.append(0)
                  x.append(m)
                  boolean=True
               elif a[m]=="erased":
                       boolean=True
               else:
                  tkMessageBox.showwarning("DATA TYPE ERROR 1", "Can not open this data ' \n(%s) ' due to it consist of string variables"%data_2[0])
                  boolean=False
                  break
       else:
            tkMessageBox.showwarning("DATA TYPE ERROR 2", "data is zero")
            boolean=False

       canvas = Canvas(root, width =300, height = 250, bg="wheat")
       canvas.place(x=990,y=310)

       if boolean==True:

           canvas = Canvas(root, width =300, height = 250, bg="wheat")
           canvas.place(x=990,y=310)

           f = Figure(figsize=(3,3), dpi=100)
           a = f.add_subplot(111)
           a.hist(y)
           dataPlot = FigureCanvasTkAgg(f, master=root)
           dataPlot.show()
           dataPlot.get_tk_widget().place(x=990, y=10)
           Label(root,text=str("Histogram 2:   "+data_2[0])).place(x=990,y=10)
           ##adding std and mean
           try:
               std=np.std(y)
               mean=np.mean(y)
           except:
               std=0
               mean=0
           Label(root,text=str("STD:   "+format(std,'.2f'))).place(x=990,y=320)
           Label(root,text=str("MEAN:    "+format(mean,'.2f'))).place(x=990,y=340)
       else:
           canvas_for_plot1=Canvas(root, width =300, height = 300, bg="wheat")
           canvas_for_plot1.place(x=990,y=10)
           canvas_for_plot1.create_text(150,10,fill="darkblue",font="Times 16 italic bold",text="(%s) is wrong type data"%data_2[0])
           canvas_for_plot1.update


def show_graph_2(data_2):
    '''This function gets one dimension data from data_safe=[][] array
          and converts it to float then erases first data whihc is name of array for excample
          ['mt1','20','40','60']. After that it is easy to deal with float numbers.Then it shows the histogram
          at the left place of GUI of program.
       '''
    ##conveting to float
    y=[]
    x=[]
    a=list(data_2)
    a.pop(0)

    '''in this part we will procses data if it consist of string number or just float integer numbers or [N.A, NA, n.a , na ] type strings
       '''
    boolean=True
    if len(a)>0:
        for m in range(len(a)):
            if isinstance(a[m],float) is True or isinstance(a[m],int) is True:
                y.append(int(a[m]))
                x.append(m)
                boolean=True
            elif a[m]=='' or a[m]=='NA' or a[m]=='N.A' or [m]=='na' or [m]=='n.a' or a[m] is None or a[m]==' ':
                y.append(0)
                x.append(m)
                boolean=True
            elif a[m]=="erased":
                       boolean=True
            else:
                tkMessageBox.showwarning("DATA TYPE ERROR 1", "Can not open this data  \n(%s)  due to it consist of string variables"%data_2[0])
                boolean=False
                break
    else:
        tkMessageBox.showwarning("DATA TYPE ERROR 2", "Data is empy")
        boolean=False

    if boolean==True:
        try:
            fig_hist2=plt.figure()
            plt.hist(y)
            plt.title(str("Histogram:"+data_2[0]))
            plt.show(fig_hist2)
        except:
            tkMessageBox.showwarning("DATA TYPE ERROR 2", "can not hist data")

    else:
        pass

##=====================================================Plotting graph for 2nd  place
def plot_graph_3(data_1,data_2):
    '''This function gets 2 datas one dimension data from data_safe=[][] array
          and converts it to float then erases first data whihc is name of array for excample
          ['mt1','20','40','60']. After that it is easy to deal with float numbers. Then it plots the graph
          and place it in the middle of histograms..
    '''

    ##========================
    x=[]
    y=[]
    a=list(data_1)
    a.pop(0)
    b=list(data_2)
    b.pop(0)
    boolean_for_a=True
    if len(a)>0:
        for q in range(len(a)):
            if isinstance(a[q],float) is True or isinstance(a[q],int) is True :
                x.append(int(a[q]))
            elif a[q]=='' or a[q]=='NA' or a[q]=='N.A' or a[q]=='na' or a[q]=='n.a' or a[q] is None or a[q]==' ':
                x.append(0)
            elif a[q]=="erased":
                pass
            else:
                boolean_for_a=False
                break
    else:
        tkMessageBox.showwarning("DATA TYPE ERROR 2","One of datas is empy" )
        boolean_for_a=False

    boolean_for_b=True
    if len(b)>0:
        for q in range(len(b)):
            if isinstance(b[q],float) is True or isinstance(b[q],int) is True:
                y.append(int(b[q]))
            elif b[q]=='' or b[q]=='NA' or b[q]=='N.A' or b[q]=='na' or b[q]=='n.a' or b[q] is None or b[q]==' ':
                y.append(0)
            elif b[q]=="erased":
                pass
            else:
                boolean_for_b=False
                break
    else:
        tkMessageBox.showwarning("DATA TYPE ERROR 2", "One of datas is empy")
        boolean_for_b=False

    canvas = Canvas(root, width =300, height = 250, bg="wheat")
    canvas.place(x=680,y=310)
    canvas_for_scatter=Canvas(root, width =300, height = 300, bg="wheat")
    canvas_for_scatter.place(x=680,y=10)
    canvas_for_scatter.create_text(150,10,fill="darkblue",font="Times 16 italic bold",text=" can not show scatter graph")
    canvas_for_scatter.update
    if boolean_for_a==True and boolean_for_b==True:
        if all(v == 0 for v in x):
          canvas_for_scatter=Canvas(root, width =300, height = 300, bg="wheat")
          canvas_for_scatter.place(x=680,y=10)
          canvas_for_scatter.create_text(150,10,fill="darkblue",font="Times 16 italic bold",text=" can not show scatter graph")
          canvas_for_scatter.update
          tkMessageBox.showwarning("DATA TYPE ERROR 1 for scatter graph ", "Can not create scatter graph due to one of datas ")

        else:
            try:
                f = Figure(figsize=(3,3), dpi=100)
                plotting = f.add_subplot(111)
                plotting.scatter(x,y)
                m_n_data=np.polyfit(x,y,1)## m+n*x=y
                m=m_n_data[0]
                n=m_n_data[1]
                plotting.plot(x,np.poly1d(np.polyfit(x, y, 1))(x))
            except:
                canvas_for_scatter=Canvas(root, width =300, height = 300, bg="wheat")
                canvas_for_scatter.place(x=680,y=10)
                canvas_for_scatter.create_text(150,10,fill="darkblue",font="Times 16 italic bold",text=" can not show scatter graph")
                canvas_for_scatter.update

                tkMessageBox.showwarning("DATA SCATTER ERROR", "Cannot scatter datas due to dimension difference")


            try:
                alfa,betta ,Sxy,Sxx,Syy =Least_Square_Method(y,x)##LEAST SQUARE METHOD
            except:
                alfa=0
                betta=0
                Sxy=0
                Sxx=0
                Syy=0
            try:
                information,data=ANOVA_TEST(Sxx,Sxy,Syy,x)
            except:
                information=0
                data=test_anova=[["SOURCE","      DF","     SS","           MS","          F"],["Regression  ",str(format(0,'.2f')),str(format(0,'.2f')),str(format(0,'.2f')),str(format(0,'.2f'))],["Error            ",str(format(0,'.2f')),str(format(0,'.2f')),str(format(0,'.2f'))],["Total            ",str(format(0,'.2f')),str(format(0,'.2f'))]]
            ##formatting for text label
            alf=format(alfa,'.2f')
            bett=format(betta,'.2f')
            ## CREATING TABLE
            ##Title of table
            Label(root, text="ANOVA TABLE", fg="black",font=("Helvetica", 14)).place(x=760,y=310)
            ##Header
            header='   '.join(data[0])
            Label(root,text=header).place(x=680,y=340)
            first_row='   '.join(data[1])
            first_row_pack=Label(root,text=first_row)
            first_row_pack.place(x=680,y=360)

            second_row='   '.join(data[2])
            second_row_pack=Label(root,text=second_row)
            second_row_pack.place(x=680,y=380)

            third_row='   '.join(data[3])
            third_row_pack=Label(root,text=third_row)
            third_row_pack.place(x=680,y=400)

            ##PEARSON COFFICIENT
            Label(root,text="PEARSON CORRELATION COEFFICIENT:").place(x=680,y=420)

            try:
                pearson_number=pearson_def(x,y)
            except:
                pearson_number=0

            pearson=Label(root,text=str(format(pearson_number,'.2f')))
            pearson.place(x=900,y=420)

            ##R^2
            Label(root,text="R^2:").place(x=680,y=440)
            try:
                Label(root,text=str(format(math.sqrt(pearson_def(x,y)),'.2f'))).place(x=710,y=440)
            except:
                Label(root,text=str(format(0,'.2f'))).place(x=710,y=440)

            ##line fit a and be
            Label(root,text="BEST LINE DATA",fg="black").place(x=680,y=460)
            Label(root,text="a:").place(x=680,y=480)
            A=Label(root,text=str(alf))
            A.place(x=700,y=480)
            Label(root,text="b:").place(x=680,y=500)
            B=Label(root,text=str(bett))
            B.place(x=700,y=500)
            ##placing plotted graph
            dataPlot = FigureCanvasTkAgg(f, master=root)
            dataPlot.show()
            dataPlot.get_tk_widget().place(x=680, y=10)
            Label(root,text=str("Scatter graph:"+data_1[0]+" vs "+data_2[0])).place(x=680,y=10)

    else:
        canvas_for_scatter=Canvas(root, width =300, height = 300, bg="wheat")
        canvas_for_scatter.place(x=680,y=10)
        canvas_for_scatter.create_text(150,10,fill="darkblue",font="Times 16 italic bold",text=" can not show scatter graph")
        canvas_for_scatter.update
        tkMessageBox.showwarning("DATA TYPE ERROR 2 for scatter graph ", "Can not open datas")

def show_scatter(data_1,data_2):
    '''This function gets 2 datas one dimension data from data_safe=[][] array
          and converts it to float then erases first data whihc is name of array for excample
          ['mt1','20','40','60']. After that it is easy to deal with float numbers. Then it plots the graph
          and place it in the middle of histograms..
    '''

    ##========================
    x=[]
    y=[]
    a=list(data_1)
    a.pop(0)
    b=list(data_2)
    b.pop(0)
    boolean_for_a=True
    for q in range(len(a)):
           if isinstance(a[q],float) is True or isinstance(a[q],int) is True :
               x.append(int(a[q]))
           elif a[q]=='' or a[q]=='NA' or a[q]=='N.A' or a[q]=='na' or a[q]=='n.a' or a[q] is None or a[q]==' ':
               x.append(0)
           elif a[q]=="erased":
               pass
           else:
               boolean_for_a=False
               break

    boolean_for_b=True
    for q in range(len(b)):
          if isinstance(b[q],float) is True or isinstance(b[q],int) is True:
               y.append(int(b[q]))
          elif b[q]=='' or b[q]=='NA' or b[q]=='N.A' or b[q]=='na' or b[q]=='n.a' or b[q] is None or b[q]==' ':
               y.append(0)
          elif b[q]=="erased":
              pass
          else:
              boolean_for_b=False
              break

    if boolean_for_a==True and boolean_for_b==True:
        if all(v == 0 for v in x):
          tkMessageBox.showwarning("DATA TYPE ERROR 1 for scatter graph ", "Can not create scatter graph due to one of datas ")

        else:

            try:
                alfa,betta ,Sxy,Sxx,Syy =Least_Square_Method(y,x)##LEAST SQUARE METHOD
            except:
                alfa=0
                betta=0
                Sxy=0
                Sxx=0
                Syy=0
            try:
                information,data=ANOVA_TEST(Sxx,Sxy,Syy,x)
            except:
                information=0
                data=test_anova=[["SOURCE","      DF","     SS","           MS","          F"],["Regression  ",str(format(0,'.2f')),str(format(0,'.2f')),str(format(0,'.2f')),str(format(0,'.2f'))],["Error            ",str(format(0,'.2f')),str(format(0,'.2f')),str(format(0,'.2f'))],["Total            ",str(format(0,'.2f')),str(format(0,'.2f'))]]
            ##formatting for text label
            alf=format(alfa,'.2f')
            bett=format(betta,'.2f')
            fig_scatter=plt.figure()
            plt.plot(x,np.poly1d(np.polyfit(x, y, 1))(x))
            plt.scatter(x,y)
            plt.title(str("Scatter graph:"+data_1[0]+" vs "+data_2[0]))
            plt.xlabel(str(data_1[0]))
            plt.ylabel(str(data_2[0]))
            plt.show(fig_scatter)

    else:
        tkMessageBox.showwarning("DATA TYPE ERROR 2 for scatter graph ", "Can not open datas")

##========================================================Best fit function excample one
def best_fit(X, Y):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)
    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    b = float(numer) / float(denum)
    a = ybar - b * xbar
    return a, b

##========================================================Lest square method
def Least_Square_Method(y,x):##calculatin alfa and betta
    alfa=0;
    betta=0;
    x_=0
    y_=0
    xi=0
    yi=0
    xi_2=0
    yi_2=0
    xi_yi=0
    Sxx=0
    Syy=0
    Sxy=0
    for i in range(0,len(x)):
        xi+=x[i]
        xi_2+=(x[i]*x[i])
    for i in range(0,len(y)):
        yi+=y[i]
        yi_2+=(y[i]*y[i])
        xi_yi+=(x[i]*y[i])
    x_=float(xi)/float(len(x))
    y_=float(yi)/float(len(y))
    Sxx=float(xi_2-(float(xi)*float(xi))/len(x))
    Syy=float(yi_2-(float(yi)*float(yi))/len(y))
    Sxy=float(xi_yi-(float(xi)*float(yi))/len(x))
    betta=float(Sxy)/float(Sxx)
    alfa=y_-betta*x_
    ##plottong line and scatter together
    return alfa,betta ,Sxy,Sxx,Syy

##===================================================================Anova test
def ANOVA_TEST(Sxx,Sxy,Syy,x):##COMPUTES ANOVA TABLE AND GENERATES IT TO TXT FILE also finds the R2
    name="anovatest.txt"
    total_df=len(x)-1
    regression_df=1
    error_df=len(x)-2
    SSR=float((Sxy*Sxy)/Sxx)
    total_SS=Syy
    SSE=float(total_SS-SSR)
    #Mean squares
    MSR=float(SSR/1)
    MSE=float(SSE/(len(x)-2))
    F=float(MSR/MSE)
    R2=float(SSR/total_SS)
    R2_=float(1-SSE/total_SS)
    information="SSR/total_SS= ",R2," (1-SSE/total_SS)= ",R2_
    test_anova=[["SOURCE","      DF","     SS","           MS","          F"],["Regression  ",str(format(regression_df,'.2f')),str(format(SSR,'.2f')),str(format(MSR,'.2f')),str(format(F,'.2f'))],["Error            ",str(format(error_df,'.2f')),str(format(SSE,'.2f')),str(format(MSE,'.2f'))],["Total            ",str(format(total_df,'.2f')),str(format(total_SS,'.2f'))]]
    ##test_data_object=np.array(test_data,dtype=str)
    ##writing to text file an array data
    return information , test_anova


##===========================================================Chi square
def chi_square(x,y):
    p=np.polyfit(x,y,1)
    chi_squared = np.sum((np.polyval(p, x) - y) ** 2)
    return chi_squared

##===========================================================Creating array
def create_array(data_name,data):
    data_name=[]
    for i in range(len(data)):
        data_name.append(data[i].value)
    return data_name
##===========================================================Finding average
def average(x):
       assert len(x) > 0
       return float(sum(x)) / len(x)
##===========================================================Pearson function
def pearson_def(x, y):
       ##converting data to integer
       '''
       x=[]
       a=list(data1)
       a.pop(0)
       for m in range(len(a)):
           x.append(int(a[m]))
       ##converting data to integer
       y=[]
       b=list(data2)
       b.pop(0)
       for n in range(len(a)):
           y.append(int(b[n]))
       '''

       assert len(x) == len(y)
       n = len(x)
       assert n > 0
       avg_x = average(x)
       avg_y = average(y)
       diffprod = 0
       xdiff2 = 0
       ydiff2 = 0
       for idx in range(n):
           xdiff = x[idx] - avg_x
           ydiff = y[idx] - avg_y
           diffprod += xdiff * ydiff
           xdiff2 += xdiff * xdiff
           ydiff2 += ydiff * ydiff
       return diffprod / math.sqrt(xdiff2 * ydiff2)

##==============================File saving
def save_file():
    book = xlwt.Workbook()
    sheet_0 = book.add_sheet("GRADES")

    for num in range(len(MAIN_DATA[0])):
        row = sheet_0.row(num)
        for index in range(len(MAIN_DATA)):
            row.write(index,MAIN_DATA[index][num])

    book.save(path+"(1).xlsx")

def save_file_as():
    book = xlwt.Workbook()
    sheet_0 = book.add_sheet("GRADES")

    for num in range(len(MAIN_DATA[0])):
        row = sheet_0.row(num)
        for index in range(len(MAIN_DATA)):
            row.write(index,MAIN_DATA[index][num])

    save_filename = asksaveasfilename(defaultextension=".xlsx")
    book.save(save_filename)

##==============================testing filename
def open_file_test():
    '''This fucntions tests file before opening it this file extension should fit one of the array objects of
    excel_extension arrays then it opens the file. If it fails program shows warning screen dialoge
    '''
    excel_extensions=['xlsx','xlsm','xlsb','xltx','xltm','xlt','xls','xml','xlam','xla','xlw']
    try:
        filename = askopenfilename(parent=root)
        name_array=filename.split('.')
        global path
        path=name_array[0]
        global name
        name=name_array[1]
        for a in range(len(excel_extensions)):
            if name_array[1]==excel_extensions[a]:
                openfile(filename)
                break
            else:
                tkMessageBox.showwarning("FILE TYPE ERROR", "Can not open this file ' \n(%s) ' because of it is not excell type "%filename)
                break
    except:
         tkMessageBox.showwarning("FILE OPENING ERROR 1" , " Can not open file due to name or path ")


radiobutton_list_1=[]
radiobutton_list_2=[]
def openfile(filename):
   '''After open_file_test() function runs clears and not shows warning it will be run this function
      THIS FUCNTION IS IMPORTANT ONE WHICH IS ALL PROCSESESS WILL RUNE FROM THIS FUCNTION!!!
   '''

   book = xlrd.open_workbook(filename)
   first_sheet = book.sheet_by_index(0)
   ##===========================================================Creating array
   def data_to_array(data):
        temp_data=[]
        for i in range(len(data)):
            try:
                temp_data.append(int(data[i].value))
            except:
                if data[i].value=="" or data[i].value==" " or data[i].value=="  ":
                    temp_data.append(0)
                else:
                    temp_data.append(str(data[i].value))
        return temp_data

   global MAIN_DATA
   MAIN_DATA=[]
   for cell_number in range(len(first_sheet.row_values(0))):
       row_data=first_sheet.col(cell_number)
       add_data=data_to_array(row_data)
       MAIN_DATA.append(add_data)





   ##==========================================================Button fucntions
   def plot_graph_from_radio_button_1():
       plot_graph_1(MAIN_DATA[variable_for_all_radiobutton_1.get()])

   def plot_graph_from_radio_button_2():
       plot_graph_2(MAIN_DATA[variable_for_all_radiobutton_2.get()-len(radiobutton_list_1)])

   def plot_graph_from_all_buttos():
       try:
           plot_graph_3(MAIN_DATA[variable_for_all_radiobutton_1.get()],MAIN_DATA[variable_for_all_radiobutton_2.get()-len(radiobutton_list_1)])
       except:
            tkMessageBox.showwarning("SCATTER ERROR", "Error while scatter")



   def binded_plot_for_2():
       if variable_for_all_radiobutton_1.get()==0:
           plot_graph_from_radio_button_2()

       else:
           plot_graph_from_radio_button_2()
           plot_graph_from_all_buttos()


   def binded_plot_for_1():
       if variable_for_all_radiobutton_2.get()==0:
           plot_graph_from_radio_button_1()
       else:
           plot_graph_from_radio_button_1()
           plot_graph_from_all_buttos()

   def button_show_graph_1():
       show_graph_1(MAIN_DATA[variable_for_all_radiobutton_1.get()])

   def button_show_graph_2():
       show_graph_2(MAIN_DATA[variable_for_all_radiobutton_2.get()-len(radiobutton_list_1)])

   def button_show_scatter():
       show_scatter(MAIN_DATA[variable_for_all_radiobutton_1.get()],MAIN_DATA[variable_for_all_radiobutton_2.get()-len(radiobutton_list_1)])




   def recreate_buttons():
       canvas_for_radio=Canvas(root, width =260, height = 300, bg="wheat")
       canvas_for_radio.place(x=10,y=20)
       del radiobutton_list_1[ 0:len(radiobutton_list_1) ]
       radiobutton_1_x=10
       radiobutton_1_y=20
       frame_for_radiobutton_1=Frame(root,width=55,height=300)
       frame_for_radiobutton_1.place(x=radiobutton_1_x,y=radiobutton_1_y)
       canvas_for_radiobutton_1=Canvas(frame_for_radiobutton_1,bg='wheat',width=55,height=300,scrollregion=(0,0,0,1000))
       for button_n in range(len(MAIN_DATA)):
           button_name=MAIN_DATA[button_n][0]
           button_name=Radiobutton(canvas_for_radiobutton_1,text=button_name,indicatoron = 0,width = 10,padx = 10,variable=variable_for_all_radiobutton_1, value=button_n,command=binded_plot_for_1)
           radiobutton_list_1.append(button_name)
           ##button_name.place(x=radiobutton_1_x,y=radiobutton_1_y)
           radiobutton_window_1 = canvas_for_radiobutton_1.create_window(55, radiobutton_1_y, window=button_name)
           radiobutton_1_y+=25

       vbar=Scrollbar(frame_for_radiobutton_1,orient=VERTICAL)
       vbar.pack(side=RIGHT,fill=Y)
       vbar.config(command=canvas_for_radiobutton_1.yview)
       canvas_for_radiobutton_1.config(width=110,height=300)
       canvas_for_radiobutton_1.config(yscrollcommand=vbar.set)
       canvas_for_radiobutton_1.pack(side=LEFT,expand=True,fill=BOTH)

       ##================================================CREATING FRAME AND RADIOBUTTONS FOR RADIOBUTTON 2
       del radiobutton_list_2[ 0:len(radiobutton_list_2) ]
       radiobutton_2_x=140
       radiobutton_2_y=20
       frame_for_radiobutton_2=Frame(root,width=55,height=300)
       frame_for_radiobutton_2.place(x=radiobutton_2_x,y=radiobutton_2_y)
       canvas_for_radiobutton_2=Canvas(frame_for_radiobutton_2,bg='wheat',width=55,height=300,scrollregion=(0,0,0,1000))
       for button_n in range(len(MAIN_DATA)):
           button_name=MAIN_DATA[button_n][0]
           button_name_to_data=button_name+"2"
           button_name=Radiobutton(canvas_for_radiobutton_2,text=button_name,indicatoron = 0,width = 10,padx = 10,variable=variable_for_all_radiobutton_2, value=button_n+len(radiobutton_list_1),command=binded_plot_for_2)
           radiobutton_list_2.append(button_name_to_data)
           radiobutton_window_2 = canvas_for_radiobutton_2.create_window(55, radiobutton_2_y, window=button_name)
           radiobutton_2_y+=25

       vbar_for_radiobutton_2=Scrollbar(frame_for_radiobutton_2,orient=VERTICAL)
       vbar_for_radiobutton_2.pack(side=RIGHT,fill=Y)
       vbar_for_radiobutton_2.config(command=canvas_for_radiobutton_2.yview)
       canvas_for_radiobutton_2.config(width=110,height=300)
       canvas_for_radiobutton_2.config(yscrollcommand=vbar_for_radiobutton_2.set)
       canvas_for_radiobutton_2.pack(side=LEFT,expand=True,fill=BOTH)
##=================================================================================GRADING
##=========================================================CURVE GRADING
   def curve_calculating():
       master_for_cataloge = Tk()
       scrollbar = Scrollbar(master_for_cataloge)
       scrollbar.pack(side=RIGHT, fill=Y)
       listbox = Listbox(master_for_cataloge, yscrollcommand=scrollbar.set,selectmode=MULTIPLE)
         ##checking if there undimensional datas

       for i in range(len(MAIN_DATA)):
            list_name=str(MAIN_DATA[i][0])
            listbox.insert(END,list_name)

       listbox.pack(fill=BOTH)
       scrollbar.config(command=listbox.yview)


       def select():
           global CURVE
           CURVE=0
           reslist = list()
           seleccion = listbox.curselection()
           for i in seleccion:
                entrada = listbox.get(i)
                reslist.append(entrada)
           for listname in reslist:
               for i in range(len(MAIN_DATA)):
                   if listname==MAIN_DATA[i][0]:
                        print(listname)
                        ##calculating the curve of data
                        test_data=list(MAIN_DATA[i])
                        ##========================
                        test_data.pop(0)
                        work_data=[]

                        if len(test_data)>0:
                            for q in range(len(test_data)):
                                if isinstance(test_data[q],float) is True or isinstance(test_data[q],int) is True :
                                    work_data.append(int(test_data[q]))
                                elif test_data[q]=='' or test_data[q]=='NA' or test_data[q]=='N.A' or test_data[q]=='na' or test_data[q]=='n.a' or test_data[q] is None or test_data[q]==' ':
                                    work_data.append(0)
                                elif test_data[q]=="erased":
                                    pass
                                else:
                                    break
                        else:
                            tkMessageBox.showwarning("DATA TYPE ERROR 2","One of datas is empy" )

                        mean=np.mean(work_data)
                        CURVE+=mean
           label_string="Curve:"+str(CURVE)
           Label(master_for_cataloge,text=label_string).pack()
           print(format(CURVE,'.2f'))


       if CURVE==0:
           label_string="Curve: 0 "
       else:
           label_string="Prevoius Curve:"+str(CURVE)

       Label(master_for_cataloge,text=label_string).pack()
       Button(master_for_cataloge,text="Find Curve",command=select).pack()
       master_for_cataloge.mainloop()


   def curve_grading():
       grade_screen=Tk()
       grade_screen.geometry("300x100+400+100")
       grade_screen.resizable(height=False,width=False)
       grade_screen.title("Choose grading scale")
       def change():
           try:
               GRADING=int(grade_scale.get())
           except:
               tkMessageBox.showwarning("GRADING SCALE ERROR ", "Entry should be integer number")

           test_data=list(MAIN_DATA[variable_for_all_radiobutton_1.get()])
           test_data.pop(0)
           work_data=[]
           CURVE_GRADES=["CUR. GRADES"]
           H_CURVE_GRADES=["HIST. CUR. GRADES"]
           if len(test_data)>0:
                for q in range(len(test_data)):
                    if isinstance(test_data[q],float) is True or isinstance(test_data[q],int) is True :
                        work_data.append(int(test_data[q]))
                    elif test_data[q]=='' or test_data[q]=='NA' or test_data[q]=='N.A' or test_data[q]=='na' or test_data[q]=='n.a' or test_data[q] is None or test_data[q]==' ':
                        work_data.append(0)
                    elif test_data[q]=="erased":
                        pass
                    else:
                        break
           else:
                tkMessageBox.showwarning("DATA TYPE ERROR 2","One of datas is empy" )
           std=np.std(work_data)
           print(std,"--",CURVE)
           ems=CURVE/std
           nicat_number=GRADING/2-CURVE
           aa_grade=GRADING-nicat_number
           araliq=aa_grade/10

           for a in range(len(work_data)):
               if work_data[a]<aa_grade-7*araliq:
                   CURVE_GRADES.append('FF')
                   H_CURVE_GRADES.append(2)
               elif work_data[a]>=aa_grade-8*araliq and  work_data[a]<aa_grade-7*araliq:
                   CURVE_GRADES.append('FD')
                   H_CURVE_GRADES.append(3)
               elif work_data[a]>=aa_grade-7*araliq and  work_data[a]<aa_grade-6*araliq:
                   CURVE_GRADES.append('DD')
                   H_CURVE_GRADES.append(4)
               elif work_data[a]>=aa_grade-6*araliq and  work_data[a]<aa_grade-5*araliq:
                   CURVE_GRADES.append('DC')
                   H_CURVE_GRADES.append(5)
               elif work_data[a]>=aa_grade-5*araliq and  work_data[a]<aa_grade-4*araliq:
                   CURVE_GRADES.append('CC')
                   H_CURVE_GRADES.append(6)
               elif work_data[a]>=aa_grade-4*araliq and  work_data[a]<aa_grade-3*araliq:
                   CURVE_GRADES.append('CB')
                   H_CURVE_GRADES.append(7)
               elif work_data[a]>=aa_grade-3*araliq and  work_data[a]<aa_grade-2*araliq:
                   CURVE_GRADES.append('BB')
                   H_CURVE_GRADES.append(8)
               elif work_data[a]>=aa_grade-2*araliq and  work_data[a]<aa_grade-araliq:
                   CURVE_GRADES.append('BA')
                   H_CURVE_GRADES.append(9)
               elif work_data[a]>=aa_grade-araliq:
                   CURVE_GRADES.append('AA')
                   H_CURVE_GRADES.append(10)


           MAIN_DATA.append(CURVE_GRADES)
           MAIN_DATA.append(H_CURVE_GRADES)
           recreate_buttons()
       Label(grade_screen,text="Define grading scale").pack()
       grade_scale=Entry(grade_screen,width=10)
       grade_scale.pack()

       Button(grade_screen,text="Choose",command=change).pack()







##========================================================Catalogue grading
   def catalogue_grading():
        CATALOGUE_GRADES=['Cat. Grades']
        H_CATALOGUE_GRADES=['Hist. Cat. Grades']
        test_data=list(MAIN_DATA[variable_for_all_radiobutton_1.get()])
        ##========================
        test_data.pop(0)
        work_data=[]

        if len(test_data)>0:
            for q in range(len(test_data)):
                if isinstance(test_data[q],float) is True or isinstance(test_data[q],int) is True :
                    work_data.append(int(test_data[q]))
                elif test_data[q]=='' or test_data[q]=='NA' or test_data[q]=='N.A' or test_data[q]=='na' or test_data[q]=='n.a' or test_data[q] is None or test_data[q]==' ':
                    work_data.append(0)
                elif test_data[q]=="erased":
                    pass
                else:
                    break
        else:
            tkMessageBox.showwarning("DATA TYPE ERROR 2","One of datas is empy" )


        high = max(work_data)
        low = min(work_data)
        print(work_data)
        print(high)
        print(low)
        index_high=high/100
        print(index_high)
        for m in range(len(work_data)):
            grade_index=index_high*work_data[m]
            if grade_index>=90 and grade_index<=100:
                CATALOGUE_GRADES.append('AA')
                H_CATALOGUE_GRADES.append(10)
            elif grade_index>=85 and grade_index<=90:
                CATALOGUE_GRADES.append('BA')
                H_CATALOGUE_GRADES.append(9)
            elif grade_index>=80 and grade_index<=84:
                CATALOGUE_GRADES.append('BB')
                H_CATALOGUE_GRADES.append(8)
            elif grade_index>=75 and grade_index<=79:
                CATALOGUE_GRADES.append('CB')
                H_CATALOGUE_GRADES.append(7)
            elif grade_index>=65 and grade_index<=74:
                CATALOGUE_GRADES.append('CC')
                H_CATALOGUE_GRADES.append(6)
            elif grade_index>=60 and grade_index<=64:
                CATALOGUE_GRADES.append('DC')
                H_CATALOGUE_GRADES.append(5)
            elif grade_index>=55 and grade_index<=59:
                CATALOGUE_GRADES.append('DD')
                H_CATALOGUE_GRADES.append(4)
            elif grade_index>=50 and grade_index<=54:
                CATALOGUE_GRADES.append('FD')
                H_CATALOGUE_GRADES.append(3)
            else:
                CATALOGUE_GRADES.append('FF')
                H_CATALOGUE_GRADES.append(2)


        MAIN_DATA.append(CATALOGUE_GRADES)
        MAIN_DATA.append(H_CATALOGUE_GRADES)
        recreate_buttons()






##========================================================BINDING DATA
   def bind_datas():
       data=[]
       x=[]
       y=[]
       try:
           for i in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])):
               x.append(MAIN_DATA[variable_for_all_radiobutton_1.get()][i])
               y.append(MAIN_DATA[variable_for_all_radiobutton_2.get()-len(radiobutton_list_1)][i])
           name=str(x[0]+"/"+y[0])
           data.append(name)
           x.pop(0)
           y.pop(0)
           for a in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])-1):
               data.append(int(x[a])+int(y[a]))

           MAIN_DATA.append(data)
           recreate_buttons()
       except:
           tkMessageBox.showwarning("DATA BIND ERROR ", "Can not bind datas")
##===========================================================Change data
   def change_data():

        try:
            a=int(entry_for_data_change.get())
            if a>=0 and a<=100:
                carpim=a*(100**(-1))
        except:
            tkMessageBox.showwarning("MODIYF DATA ENTRY ERROR ", "Entry should be integer number and between 0 and 100")
        try:
            changed_data=[]
            used_data=[]
            for i in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])):
                  used_data.append(MAIN_DATA[variable_for_all_radiobutton_1.get()][i])

            data_name=used_data[0]
            used_data.pop(0)
            changed_data.append(str(data_name+"~"+str(a)+"%"))
            for m in range(len(used_data)):
                try:
                    changed_data.append(int(used_data[m])*carpim)
                except:
                    if used_data[m]=="erased":
                        changed_data.append("erased")
                    else:
                        changed_data.append("ERROR")


            MAIN_DATA.append(changed_data)
            recreate_buttons()
        except:
            tkMessageBox.showwarning("DATA MODIFY ERROR ", "Can not modify datas")

##=========================================================ERASE FROM DATA
   def erase_enrty():

        try:
            erase_entry=int(entry_for_erase.get())
        except:
            tkMessageBox.showwarning("ERASE FROM DATA ERROR ", "Entry should be integer number")
        try:
            changed_data=[]
            used_data=[]
            for i in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])):
                  used_data.append(MAIN_DATA[variable_for_all_radiobutton_1.get()][i])

            data_name=used_data[0]
            used_data.pop(0)
            changed_data.append(str(data_name+"-"+str(erase_entry)))
            for m in range(len(used_data)):
                if used_data[m]==erase_entry:
                   changed_data.append("erased")
                else:
                    changed_data.append(used_data[m])

            MAIN_DATA.append(changed_data)
            recreate_buttons()
        except:
            tkMessageBox.showwarning("ERASE FROM DATA ERROR ", "Can not erase data")

##===========================================================ERASE LOWER
   def erase_enrty_lower():
        try:
            erase_entry=int(entry_for_erase_lower.get())
        except:
            tkMessageBox.showwarning("ERASE FROM DATA ERROR ", "Entry should be integer number")
        try:
            changed_data=[]
            used_data=[]
            for i in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])):
                  used_data.append(MAIN_DATA[variable_for_all_radiobutton_1.get()][i])
            data_name=used_data[0]
            used_data.pop(0)
            changed_data.append(str(data_name+">"+str(erase_entry)))
            for m in range(len(used_data)):
                if int(used_data[m])<=erase_entry:
                   changed_data.append("erased")
                else:
                    changed_data.append(used_data[m])
            MAIN_DATA.append(changed_data)
            recreate_buttons()
        except:
            tkMessageBox.showwarning("ERASE FROM DATA ERROR ", "Can not erase data")

##===========================================================ERASE ENTRY HIGER
   def erase_enrty_higher():
        try:
            erase_entry=int(entry_for_erase_higher.get())
        except:
            tkMessageBox.showwarning("ERASE FROM DATA ERROR ", "Entry should be integer number")
        try:
            changed_data=[]
            used_data=[]
            for i in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])):
                  used_data.append(MAIN_DATA[variable_for_all_radiobutton_1.get()][i])
            data_name=used_data[0]
            used_data.pop(0)
            changed_data.append(str(data_name+"<"+str(erase_entry)))
            for m in range(len(used_data)):
                if int(used_data[m])>=erase_entry:
                   changed_data.append("erased")
                else:
                    changed_data.append(used_data[m])
            MAIN_DATA.append(changed_data)
            recreate_buttons()
        except:
            tkMessageBox.showwarning("ERASE FROM DATA ERROR ", "Can not erase data")

##=========================================================DELETING DATA
   def delete_data():
       try:
           array_to_delete=list(MAIN_DATA[variable_for_all_radiobutton_1.get()])
           MAIN_DATA.remove(array_to_delete)
           recreate_buttons()
       except:
           tkMessageBox.showwarning("Data remove error", "Can not remove data")
##============================================================SHOW ALL

   def show_all():
        master_for_show_all = Tk()
        master_for_show_all.title("All datas")

        scrollbar_y = Scrollbar(master_for_show_all)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x = Scrollbar(master_for_show_all,orient=HORIZONTAL)
        scrollbar_x.pack(side=BOTTOM, fill=X)

        listbox = Listbox(master_for_show_all, yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set)
        ##checking if there undimensional datas
        for i in range(len(MAIN_DATA[0])):
            string_insert=str(i)+"-"
            for m in range(len(MAIN_DATA)):
                string_insert+=str(MAIN_DATA[m][0])+":"+str(MAIN_DATA[m][i])+"    "
            listbox.insert(END,string_insert)

        listbox.pack(fill=BOTH,expand=1)
        scrollbar_y.config(command=listbox.yview)
        scrollbar_x.config(command=listbox.xview)

        def choosed():
               master_for_choosed = Tk()

               listbox_value=listbox.get(ACTIVE)
               listbox_value.split('-')

               number=int(listbox_value[0])

               master_for_choosed.Entries=[]
               master_for_choosed.Buttons=[]

               canvas_for_choosed=Canvas(master_for_choosed, width =400, height = 300)
               canvas_for_choosed.place(x=10,y=10)
               frame_for_choosed=Frame(master_for_choosed,width=55,height=300)
               frame_for_choosed.place(x=10,y=10)
               canvas_for_choosed_widget=Canvas(frame_for_choosed,width=55,height=300,scrollregion=(0,0,0,1000))


               for place in range(len(MAIN_DATA)):
                   Label(canvas_for_choosed_widget,text=str(str(MAIN_DATA[place][0])+"--"+str(MAIN_DATA[place][number]))).grid(row=place,column=1)

                   entry_name=Entry(canvas_for_choosed_widget,width=10)
                   entry_name.grid(row=place,column=2)
                   master_for_choosed.Entries.append(entry_name)

                   button_name=Button(canvas_for_choosed_widget,text="Change",command=lambda que=place: change_data(que)).grid(row=place,column=4)
                   master_for_choosed.Buttons.append(button_name)

               def change_data(pit):
                try:
                    MAIN_DATA[pit][number]=int(master_for_choosed.Entries[pit].get())
                except:
                    MAIN_DATA[pit][number]=str(master_for_choosed.Entries[pit].get())
                recreate_buttons()

               vbar=Scrollbar(frame_for_choosed,orient=VERTICAL)
               vbar.pack(side=RIGHT,fill=Y)
               vbar.config(command=canvas_for_choosed_widget.yview)
               canvas_for_choosed_widget.config(width=110,height=300)
               canvas_for_choosed_widget.config(yscrollcommand=vbar.set)
               canvas_for_choosed_widget.pack(side=LEFT,expand=True,fill=BOTH)

               master_for_choosed.mainloop()

        Button(master_for_show_all,text="Choose data",command=choosed).pack()
        master_for_show_all.mainloop()




   ##====================================================CREATING NEW SCREEN
   ##when this function runs it will create a new screen
   x = 0
   y = 0
   height_of_root=600
   ##screen_width = root.winfo_screenwidth()
   ##screen_height = root.winfo_screenheight()
   root.title(str("Excel file: "+filename))
   root.geometry('%dx%d+%d+%d' % (width_of_root,height_of_root, x, y))


   filemenu.add_command(label="Save", command=save_file)
   filemenu.add_command(label="Save as", command=save_file_as)
   filemenu.add_separator()

   data_control = Menu(menubar, tearoff=0)
   data_control.add_command(label="Show all", command=show_all)
   data_control.add_separator()
   menubar.add_cascade(label="Data ", menu=data_control)

   grading = Menu(menubar, tearoff=0)
   grading.add_command(label="CURVE calculating", command=curve_calculating)
   grading.add_separator()
   grading.add_command(label="CATALOGUE", command=catalogue_grading)
   menubar.add_cascade(label="Grading ", menu=grading)

   help = Menu(menubar, tearoff=0)
   help.add_command(label="Tutorial", command=curve_calculating)
   help.add_command(label="FAQ", command=curve_calculating)
   help.add_separator()
   help.add_command(label="About", command=catalogue_grading)
   help.add_command(label="Webpage", command=catalogue_grading)
   menubar.add_cascade(label="Help", menu=help)





   ##CREATING FIRST CANVAS
   '''
   canvas=Canvas(root,width=1200,height=600)
   canvas.pack(expand=False)
   canvas.create_rectangle(0,0,1200,600,fill='LightYellow2')
   canvas.create_line(775,10 ,775, 590)
   canvas.create_rectangle(360,10,760,310,fill='LightYellow3')
   canvas.create_rectangle(790,10,1190,310,fill='LightYellow3')
   '''
   main_frame=ttk.Frame(root)
   main_frame.pack(expand=True, fill='both')

   ##creating radiobutton===============================================================================================================
   ##variables
   variable_for_all_radiobutton_1 = IntVar()
   variable_for_all_radiobutton_2=IntVar()
   #=========================================
   variable_for_all_radiobutton_1_type_2=[]
   variable_for_all_radiobutton_2_type_2=[]
   radiobutton_1_x=10
   radiobutton_1_y=20
   ##===============================================CREATING FRAME AND RADIOBUTTON FOR RADIOBUTTON 1
   frame_for_radiobutton_1=ttk.Frame(root,width=55,height=300)
   frame_for_radiobutton_1.place(x=radiobutton_1_x,y=radiobutton_1_y)
   canvas_for_radiobutton_1=Canvas(frame_for_radiobutton_1,bg="wheat",width=55,height=300,scrollregion=(0,0,0,500))

   for button_n in range(len(MAIN_DATA)):
       button_name=MAIN_DATA[button_n][0]
       button_name=Radiobutton(canvas_for_radiobutton_1,text=button_name,indicatoron = 0,width = 10,padx = 10,variable=variable_for_all_radiobutton_1, value=button_n,command=binded_plot_for_1)
       radiobutton_list_1.append(button_name)
       canvas_for_radiobutton_1.create_window(55, radiobutton_1_y, window=button_name)
       radiobutton_1_y+=25

   vbar=Scrollbar(frame_for_radiobutton_1,orient=VERTICAL)
   vbar.pack(side=RIGHT,fill=Y)
   vbar.config(command=canvas_for_radiobutton_1.yview)
   canvas_for_radiobutton_1.config(width=110,height=300)
   canvas_for_radiobutton_1.config(yscrollcommand=vbar.set)
   canvas_for_radiobutton_1.pack(side=LEFT,expand=True,fill=BOTH)
   ##================================================CREATING FRAME AND RADIOBUTTONS FOR RADIOBUTTON 2

   radiobutton_2_x=140
   radiobutton_2_y=20
   frame_for_radiobutton_2=Frame(root,width=55,height=300)
   frame_for_radiobutton_2.place(x=radiobutton_2_x,y=radiobutton_2_y)
   canvas_for_radiobutton_2=Canvas(frame_for_radiobutton_2,bg="wheat",width=55,height=300,scrollregion=(0,0,0,500))



   for button_n in range(len(MAIN_DATA)):

       button_name=MAIN_DATA[button_n][0]
       button_name_to_data=button_name+"2"
       button_name=Radiobutton(canvas_for_radiobutton_2,text=button_name,indicatoron = 0,width = 10,padx = 10,variable=variable_for_all_radiobutton_2, value=button_n+len(radiobutton_list_1),command=binded_plot_for_2)
       radiobutton_list_2.append(button_name_to_data)
       radiobutton_window_2 = canvas_for_radiobutton_2.create_window(55, radiobutton_2_y, window=button_name)
       radiobutton_2_y+=25

   vbar_for_radiobutton_2=Scrollbar(frame_for_radiobutton_2,orient=VERTICAL)
   vbar_for_radiobutton_2.pack(side=RIGHT,fill=Y)
   vbar_for_radiobutton_2.config(command=canvas_for_radiobutton_2.yview)
   canvas_for_radiobutton_2.config(width=110,height=300)
   canvas_for_radiobutton_2.config(yscrollcommand=vbar_for_radiobutton_2.set)
   canvas_for_radiobutton_2.pack(side=LEFT,expand=True,fill=BOTH)


   def scroll_data():
        master = Tk()
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(master, yscrollcommand=scrollbar.set)
        master.title(str(MAIN_DATA[variable_for_all_radiobutton_1.get()][0]))
        for i in range(len(MAIN_DATA[variable_for_all_radiobutton_1.get()])):
            listbox.insert(END,str(MAIN_DATA[variable_for_all_radiobutton_1.get()][i]))
        listbox.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.config(command=listbox.yview)
        mainloop()

   ttk.Button(main_frame,text="Bind datas" ,command=bind_datas).place(x=280,y=220)

   ttk.Button(main_frame,text="Show data" ,command=scroll_data).place(x=280,y=260)

   ttk.Button(main_frame,text="show hist 1",command=button_show_graph_1).place(x=280,y=20)
   ttk.Button(main_frame,text="show scatter",command=button_show_scatter).place(x=280,y=60)
   ttk.Button(main_frame,text="show hist2",command=button_show_graph_2).place(x=280,y=100)

   ttk.Button(main_frame,text="close all",command=close_all).place(x=280,y=180)
   ttk.Button(main_frame,text="close pre-exist",command=close_preexist).place(x=280,y=140)

   ttk.Button(main_frame,text="DELETE" ,command=delete_data).place(x=280,y=300)


   ttk.Button(main_frame,text="Modify data by (%)",command=change_data).place(x=20,y=340)
   entry_for_data_change=ttk.Entry(main_frame,width=10)
   entry_for_data_change.place(x=140,y=340)

   ttk.Button(main_frame,text="Erase from data",command=erase_enrty).place(x=20,y=380)
   entry_for_erase=ttk.Entry(main_frame,width=10)
   entry_for_erase.place(x=140,y=380)

   ttk.Button(main_frame,text="Erase lower than",command=erase_enrty_lower).place(x=20,y=420)
   entry_for_erase_lower=ttk.Entry(main_frame,width=10)
   entry_for_erase_lower.place(x=140,y=420)

   ttk.Button(main_frame,text="Erase higher than",command=erase_enrty_higher).place(x=20,y=460)
   entry_for_erase_higher=ttk.Entry(main_frame,width=10)
   entry_for_erase_higher.place(x=140,y=460)

   ttk.Button(main_frame,text="CURVE grading",command=curve_grading).place(x=20,y=500)
   entry_for_erase_higher=ttk.Entry(main_frame,width=10)
   entry_for_erase_higher.place(x=140,y=460)

   ttk.Button(main_frame,text="CATALOGUE grading",command=catalogue_grading).place(x=20,y=540)
   entry_for_erase_higher=ttk.Entry(main_frame,width=10)
   entry_for_erase_higher.place(x=140,y=460)



##================================running main function
##=====================================================================================================GUI MAIN FUCNTION

root = Tk()## Creating root
root.wm_title("Usefull application")## creating root title

##GETTING SCREEN SIZE
##screen_width = root.winfo_screenwidth()
##screen_height = root.winfo_screenheight()
##                                                                    root.iconbitmap(default="fav.ico")
root.geometry("300x50+100+100")## creating root geometry
root.resizable(height=False,width=False)
##===================================
menubar = Menu(root)##creating menu bar on root
filemenu = Menu(menubar, tearoff=0)## creating filemenu variable
filemenu.add_command(label="Open", command=open_file_test)## adding Open button to File bar
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu) ##creating File(Open,Exit) bar
root.config(menu=menubar)## adding menu to root
root.mainloop()## running main loop
