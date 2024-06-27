input_minuites=input("please type the number of minuties: ")
int_minuites=int(input_minuites)
total_hours= int_minuites// 60
total_minuites=int_minuites%60
total_secondes=int(total_minuites%60)
hours=str(total_hours)
minuites=str(total_minuites)
secondes=str(total_secondes)
print("this course is: "+hours+" hours,"+minuites+" minuites,and "+secondes+ " secondes")