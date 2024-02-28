import json
import pandas as pd


file_path = "/home/niaj/Desktop/sale_order_mail_message.xlsx"  # Replace with the actual path to your Excel file
sheet_name = "Sheet1"
header_row = 0
# df = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row,dtype=str).fillna(method='ffill', axis=1)
df = pd.read_excel(file_path,header=header_row, dtype=str).fillna('NULL')
# header_names = df.columns.tolist()
# df = df.fillna(False)

records = df.to_dict('records')
# print(json.dumps(df.to_dict('records'), indent=2,  ensure_ascii=False))
# print(json.dumps(df.to_dict(), ensure_ascii=False))

so_mail_msg_file = open("/home/niaj/Desktop/sale_order_mail_message.sql", "a")
table='mail_message'
for record in records:     
    vals = []
    for val in record.values():
        if val != "NULL":
            try:
                int(val) 
            except:
                val = "'"+str(val).replace('\n', '')+"'"
        # print(val)
        vals.append(val)
    columns_string= '('+','.join(record.keys())+')'    
    values_string = '('+','.join(vals)+')'    
    sql = """INSERT INTO %s %s VALUES %s;\n"""%(table, columns_string,values_string)
    # print(sql)        
    so_mail_msg_file.write(sql)
so_mail_msg_file.close()