import whoisUI as wui
import csv, os, sys



def cmd_runner(website):

    cmd = f'whois {website}'

    obj = os.popen(cmd)

    obj_text = obj.read()

    return obj_text




def readCSV():

    header = []    
    address = []


    with open(wui.csvReadName_ent.get() , 'r') as csv_file:
        
        csv_reader_obj = csv.reader(csv_file, delimiter=',')

        header = next(csv_reader_obj)
        
        for row in csv_reader_obj:
            
            if len(row[2]) >= 1:
            
                address.append(row[2])


    return address


#####################  GLOBAL

while(True):
    
    try:
    
        #fName = input('Enter the file name: ')
        open(wui.csvReadName_ent.get(), 'r')
        
        break
    
    except:
        print('Something is wrong!')




res = readCSV()




with open(wui.csvWriteName_ent.get() , 'w') as csv_file:
    
    csv_writer_obj = csv.writer(csv_file)


    headers = ['Registrar URL', 'Registrar', 'Name Server 1', 'Name Server 2', 'Name Server 3', 'Name Server 4']
    csv_writer_obj.writerow(headers)


    for item in res:

        cmdRes = cmd_runner(item)

        splited = cmdRes.splitlines()
        
        ns = []
        ru = 'Unknown'
        r = 'Unknown'


        for stringData in splited:

            if 'Registrar URL:' in stringData:
                ru = stringData

            elif 'Name Server:' in stringData:
                ns.append(stringData)

            elif 'Registrar:' in stringData:
                r = stringData


        nameServers = []

        for elemnt in ns:
            if not 'IP' in elemnt:
                y = elemnt.split(':')
                nameServers.append(y[1])


        if ru != 'Unknown':
            ru  = ru.split('URL:')
            ru = ru[-1]
        
        if r != 'Unknown':
            r = r.split(':')
            r = r[-1]
        


        final_row = [ru, r] + nameServers


        csv_writer_obj.writerow(final_row)



        # delete it
        #break