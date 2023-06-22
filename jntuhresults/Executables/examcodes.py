import requests
from bs4 import BeautifulSoup

def extract_exam_code(result_link):
    # Find the index of "examCode" in the result link
    exam_code_index = result_link.find("examCode")
    # Extract the exam code from the result link
    exam_code = result_link[exam_code_index + 9:exam_code_index + 13]
    try:
        if(exam_code[3]=='&'):
            return exam_code[:3]
    except:
        return exam_code
    return exam_code


def categorize_exam_code(result_text, exam_code):
    # Categorize the exam code based on the result text
    if " I Year I " in result_text:
        return "1-1"
    elif " I Year II " in result_text:
        return "1-2"
    elif " II Year I " in result_text:
        return "2-1"
    elif " II Year II " in result_text:
        return "2-2"
    elif " III Year I " in result_text:
        return "3-1"
    elif " III Year II " in result_text:
        return "3-2"
    elif " IV Year I " in result_text:
        return "4-1"
    elif " IV Year II " in result_text:
        return "4-2"
    else:
        return None


def categorize_masters_exam_code(result_text,exam_code):
    # Categorize the masters exam code based on the result text
    if " I Semester" in result_text:
        return "1-1"
    elif " II Semester" in result_text:
        return "1-2"
    elif " III Semester" in result_text:
        return "2-1"
    elif " IV Semester" in result_text:
        return "2-2"
    else:
        return None
    
def get_exam_codes():
    url = "http://results.jntuh.ac.in/jsp/home.jsp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    btech_results = soup.find_all("table")[0].find_all("tr")

    exam_codes = {
        "btech": {
            "R18": {},
            "R22": {}
        },
        "bpharmacy": {
            "R17": {}
        },
        "mtech":{
            "R19":{},
            "R22":{}
        },
        "mpharmacy":{
                "R19":{},
                "R22":{}
        },
        "mba":{
            "R19":{},
            "R22":{}
        }
    }
    degree=list(exam_codes.keys())
    for table in range(0,5):
        results = soup.find_all("table")[table].find_all("tr")
        regulations=exam_codes[degree[table]].keys()

         # Iterate through each result in the B.Tech results table
        for result in results:
            result_link =result.find_all("td")[0].find_all("a")[0]["href"]
            result_text=result.get_text()

            # Check if the result text contains any of the regulations
            for regulation in regulations:
                if regulation in result_text:
                    exam_code = extract_exam_code(result_link)
                    if(table<2):
                        category = categorize_exam_code(result_text, exam_code)
                    else:
                        category = categorize_masters_exam_code(result_text,exam_code)

                    if category is not None:
                        exam_codes[degree[table]][regulation].setdefault(category, [])
                        if exam_code not in exam_codes[degree[table]][regulation][category]:
                            exam_codes[degree[table]][regulation][category].append(exam_code)

        # Sort the exam codes within each category and sort the categories
        for regulation in regulations:
            for category, codes in exam_codes[degree[table]][regulation].items():
                exam_codes[degree[table]][regulation][category] = sorted(codes)
            exam_codes[degree[table]][regulation] = dict(sorted(exam_codes[degree[table]][regulation].items(), key=lambda x: x[0]))
    return exam_codes

exam_codes=get_exam_codes()
# print(exam_codes)



# import requests
# from bs4 import BeautifulSoup


# def extract_exam_code(result_link):
#     exam_code_index = result_link.find("examCode")
#     exam_code = result_link[exam_code_index + 9:exam_code_index + 13]
#     return exam_code


# def categorize_exam_code(result_text, exam_code):
#     if " I Year I " in result_text:
#         return "1-1"
#     elif " I Year II " in result_text:
#         return "1-2"
#     elif " II Year I " in result_text:
#         return "2-1"
#     elif " II Year II " in result_text:
#         return "2-2"
#     elif " III Year I " in result_text:
#         return "3-1"
#     elif " III Year II " in result_text:
#         return "3-2"
#     elif " IV Year I " in result_text:
#         return "4-1"
#     elif " IV Year II " in result_text:
#         return "4-2"
#     else:
#         return None


# def get_exam_codes():
#     url = "http://results.jntuh.ac.in/jsp/home.jsp"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     btech_results = soup.find_all("table")[0].find_all("tr")

#     exam_codes = {
#         "1-1": set(),
#         "1-2": set(),
#         "2-1": set(),
#         "2-2": set(),
#         "3-1": set(),
#         "3-2": set(),
#         "4-1": set(),
#         "4-2": set(),
#     }

#     for result in btech_results:
#         result_link = result.find_all("td")[0].find_all("a")[0]["href"]
#         result_text = result.get_text()

#         # or "R22" in result_text
#         if "R18" in result_text or "R22" in result_text :
#             exam_code = extract_exam_code(result_link)
#             category = categorize_exam_code(result_text, exam_code)

#             if category is not None:
#                 exam_codes[category].add(exam_code)

#     for category, codes in exam_codes.items():
#         exam_codes[category] = sorted(codes)
#     return exam_codes


# print(get_exam_codes())


# import requests
# from bs4 import BeautifulSoup
# urll = "http://results.jntuh.ac.in/jsp/home.jsp"


# arr11,arr12,arr21,arr22,arr31,arr32,arr41,arr42=set(),set(),set(),set(),set(),set(),set(),set()
# def examcodes():
#     response = requests.request("GET", urll)
#     soup = BeautifulSoup(response.content, "html.parser")
#     tr= soup.find_all("table")[0].find_all("tr")
#     for i in tr:
#         td=i.find_all("td")[0]
#         href=td.find_all("a")[0]['href']
#         text=td.get_text()
#         code='R18'
#         if code in text:
#             examCode_Index=href.find("examCode")
#             examCode=href[examCode_Index+9:examCode_Index+13]
#             if(' I Year I ' in text):
#                 arr11.add(examCode)
#             elif(' I Year II ' in text):
#                 arr12.add(examCode)
#             elif(' II Year I ' in text):
#                 arr21.add(examCode)
#             elif(' II Year II ' in text):
#                 arr22.add(examCode)
#             elif(' III Year I ' in text):
#                 arr31.add(examCode)
#             elif(' III Year II ' in text):
#                 arr32.add(examCode)
#             elif(' IV Year I ' in text):
#                 arr41.add(examCode)
#             elif(' IV Year II ' in text):
#                 arr42.add(examCode)
            
#     arr11=sorted(arr11)
#     arr12=sorted(arr12)
#     arr21=sorted(arr21)
#     arr22=sorted(arr22)
#     arr31=sorted(arr31)
#     arr32=sorted(arr32)
#     arr41=sorted(arr41)
#     arr42=sorted(arr42)
#     print(type(arr11))


