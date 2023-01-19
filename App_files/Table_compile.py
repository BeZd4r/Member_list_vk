#  def Create_table(self,url,new):

#         wb = load_workbook(url)

#         if new == True:
#             wb.remove(wb[wb.sheetnames[-1]])
#             ws = wb.create_sheet("Members_Data")
#         elif new == False:
#             ws = wb[wb.sheetnames[-1]]

#         ws.column_dimensions['A'].width = 24
#         ws.column_dimensions['B'].width = 15
#         ws.column_dimensions['C'].width = 30
#         for i in range(1,len(names)+1):
#             ws[f"A{i}"] = names[i-1]
#             ws[f"B{i}"] = page_ids[i-1]
#             ws[f"C{i}"] = page_url[i-1]

#         wb.save(url)
#         wb.close()
