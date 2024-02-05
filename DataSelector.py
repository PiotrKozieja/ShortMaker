import csv
def select_data(file_path):
    actual_data=[]
    with open(file_path, mode='r',encoding='utf-8',newline='') as csv_file:
        reader = csv.reader(csv_file,delimiter=';')
        for row in reader:
            actual_data.append(row)
    for i in actual_data:
        if i[2]=='u':
            i[2]='ux'
            Title = i[0]
            Content1 =i[1]
            break

    with open(file_path,mode='w',encoding='utf-8',newline='') as csv_file1:
        writer = csv.writer(csv_file1,delimiter=';')
        writer.writerows(actual_data)
    return(Title,Content1)