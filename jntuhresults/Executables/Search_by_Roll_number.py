from bs4 import BeautifulSoup
import asyncio
import aiohttp
from jntuhresults.Executables.constants import *
import time


class Results:
    def __init__(self):
        self.deta={}
        self.deta.clear()
        self.deta["Results"]={}
        self.tasks=[]

    #Running all the links asynchronously
    def get_tasks(self,session,arr,roll):
        for payload in payloads:
            for i in arr:
                payloaddata="degree=btech&examCode="+str(i)+payload+roll
                self.tasks.append(session.post(url[1], data=payloaddata,headers=headers,ssl=False))
        return self.tasks  

    #SGPA Calculator
    def total_grade_Calculator(self,code,value):
        grades = ['A','A+',"B+","B","O","C"]
        orgGrades =[]
        try:
            total,credits=0,0
            for data in value:
                if('DETAILS' in data):
                    pass
                else:
                    total=total+int(grades_to_gpa[value[data]['subject_grade']])*float(value[data]['subject_credits'])
                    credits=credits+float(value[data]['subject_credits'])
                    orgGrades.append(value[data]['subject_grade'])
            if("F" in orgGrades or "Ab" in orgGrades or credits == 0):
                self.deta["Results"][code]["status"]="FAILED"
            else:
                self.deta["Results"][code]["status"]="PASSED"
            self.deta["Results"][code]["total"]=total
            self.deta["Results"][code]["credits"]=credits
            self.deta["Results"][code]["SGPA"]="{0:.2f}".format(round(total/credits,2)) 
        except:
            pass

            
     #Scraping the grades from the html page
    def scraping_the_grades(self,code,soup):
        try:
            table = soup.find_all("table")
            table1 = table[0].find_all("tr")
            Roll_NO = table1[0].find_all("td")[1].find_all("b")[0].contents[0]
            NAME = table1[0].find_all("td")[3].find_all("b")[0].contents[0]
            FATHER_NAME = table1[1].find_all("td")[1].find_all("b")[0].contents[0]
            COLLEGE_CODE = table1[1].find_all("td")[3].find_all("b")[0].contents[0]
            table2 = table[1].find_all("tr")
            table2_column_names = [content.text for content in table2[0].findAll('b')]

            subject_internal_index = table2_column_names.index("INTERNAL") #added
            subject_total_index = table2_column_names.index("TOTAL") #added
            grade_index = table2_column_names.index("GRADE")
            subject_name_index = table2_column_names.index("SUBJECT NAME")
            subject_code_index = table2_column_names.index("SUBJECT CODE")
            subject_credits_index = table2_column_names.index("CREDITS(C)")
            subject_external_index = table2_column_names.index("EXTERNAL") #added
            table2 = table2[1:]
            self.deta["DETAILS"] = {"NAME": NAME, "ROLL_NO": Roll_NO, "COLLEGE_CODE": COLLEGE_CODE, "FATHER_NAME":FATHER_NAME}
            
            for row in table2:
                try:
                    subject_name = row.find_all("td")[subject_name_index].find("b").contents[0]
                except:
                    subject_name=""
                subject_code = row.find_all("td")[subject_code_index].find("b").contents[0]
                try:
                    subject_internal = row.find_all("td")[subject_internal_index].find("b").contents[0]
                except:
                    subject_internal = ""#added
                try:
                    subject_total = row.find_all("td")[subject_total_index].find("b").contents[0]
                except:
                    subject_total = ""#added
                subject_grade = row.find_all("td")[grade_index].find("b").contents[0]
                subject_credits = row.find_all("td")[subject_credits_index].find("b").contents[0]
                try:
                    subject_external = row.find_all("td")[subject_external_index].find("b").contents[0]
                except:
                    subject_external = ""#added

                try:
                    if(self.deta["Results"][code][subject_code]["subject_grade"]!="F" and self.deta["Results"][code][subject_code]["subject_grade"]!="Ab" and self.deta["Results"][code][subject_code]["subject_grade"]!="-"): #added
                        continue    
                except:
                    pass
                self.deta["Results"][code][subject_code]={}
                self.deta["Results"][code][subject_code]["subject_name"]=subject_name
                self.deta["Results"][code][subject_code]["subject_code"]=subject_code
                self.deta["Results"][code][subject_code]["subject_internal"]=subject_internal#added
                self.deta["Results"][code][subject_code]["subject_total"]=subject_total#added
                self.deta["Results"][code][subject_code]["subject_grade"]=subject_grade
                self.deta["Results"][code][subject_code]["subject_credits"]=subject_credits
                self.deta["Results"][code][subject_code]["subject_external"]=subject_external#added
        except:
            pass
    
    
    async def getting_the_grades(self,code,roll):
        exam_Codes=exam_codes(code,roll)
        
        async with aiohttp.ClientSession() as session:
            tasks=self.get_tasks(session,exam_Codes,roll)
            
            ###########################################################
            responses =await asyncio.gather(*tasks)
            ###########################################################

            self.deta["Results"][code]={}
            for response in responses:
                r=await response.text()
                soup = BeautifulSoup(r, "html.parser")
                self.scraping_the_grades(code,soup)
        await session.close()
        self.total_grade_Calculator(code,self.deta["Results"][code])
        return self.deta

    
    #Function to call from views
    async def getting_faster_Grades(self,roll,code):
        Result=Results()
        result=asyncio.run(self.getting_the_grades(code,roll))
        del Result
        return result