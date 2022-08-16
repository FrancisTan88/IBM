import array
import logging
from datetime import datetime
import xlsxwriter



def toMilliseconds(time):
    t = time.split(".")
    d = datetime.strptime(t[0], '%Y-%m-%d %H:%M:%S').timestamp() * 1000 +float("0."+t[1])*1000
    return d

dt=datetime.today().strftime('%Y%m%d%H%M')

logging.basicConfig(level=logging.DEBUG, format='%(lineno)d  - %(message)s')


fileName = "log.txt"
outputfileName = dt+".csv"

workbook = xlsxwriter.Workbook(dt+'.xlsx')
worksheet = workbook.add_worksheet()

f = open(fileName, "r")

lines = f.readlines()

logging.info(f"reading {len(lines)} lines from {fileName}")

req_str = ' Sending HTTP request '
rsp_str =' Received HTTP response ' 
exe_db_str = 'Executed DbCommand'


worksheet.write('A'+str(1),'time')
worksheet.write('C'+str(1),'interval')
worksheet.write('D'+str(1),'action')
worksheet.write('E'+str(1),'time took')
worksheet.write('F'+str(1),'command')

i =2
pt =0

for l in lines:
    includeSnapshot = False
    if exe_db_str in l:
        ws = l.split(" ");
        
    if exe_db_str in l:
        a = l.split("|");
        worksheet.write('A'+str(i),a[0])
        mt = toMilliseconds(a[0])
        dt = mt-pt if pt>0 else 0
        exet = int(a[6][a[6].index("(")+1:a[6].index(")")-2])
        worksheet.write('B'+str(i),int(dt))
        worksheet.write('C'+str(i),int(dt)-float(a[6][a[6].index("(")+1:a[6].index(")")-2]))
        worksheet.write('D'+str(i),'DB')
        worksheet.write('E'+str(i),exet)
        worksheet.write('F'+str(i),a[6].replace( "Executed DbCommand ("+str(exet)+"ms)","" ))
        print(a[6])
        print("Executed DbCommand ("+str(exet)+"ms)")
        print(a[6].replace( "Executed DbCommand ("+str(exet)+"ms)","" ))




        pt =mt
        i += 1


    if req_str in l:
        req = l.split("|")[6].replace(req_str,"")
         
    if rsp_str in l:
        a = l.split("|");
        t = l.split("|")[6].replace(rsp_str,"").replace("headers after ","").replace("ms - 200","").replace("ms - 201","").replace("ms - 400","")
        worksheet.write('A'+str(i),a[0])
        mt = toMilliseconds(a[0])
        dt = mt-pt if pt>0 else 0
        worksheet.write('B'+str(i),int(dt))
        worksheet.write('C'+str(i),int(dt)-float(t))
        worksheet.write('D'+str(i),'API')
        worksheet.write('E'+str(i),float(t))
        worksheet.write('F'+str(i),req)
        pt =mt
        i += 1

workbook.close()


