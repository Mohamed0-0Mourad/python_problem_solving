# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def contains_unwanted_characters(s:str):
    unwanted = re.findall(r"[^\d-]", s)

    return len(unwanted)

def check_hyphened(s:str):
    pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
    # Findall will just ignore if there are more integers which is not valid
    return re.fullmatch(pattern, s) and len(s)==19
        
def contains_consecutive(s:str):
    last = s[0]
    cnt=1
    for i in range(1, len(s)):
        if s[i]==last:
            cnt+=1
            if cnt >= 4:
                return True
        else:
            cnt=1
            last = s[i]    
    return False

def validate_credit_card(s:str)->str:
    if contains_unwanted_characters(s):
        return "Invalid"
    
    elif s[0] not in ['4', '5', '6']:
        return "Invalid"
    
    elif s.find('-')!=-1:
        if not check_hyphened(s):
            return "Invalid"
    else:
        if len(s) != 16:
            return "Invalid"

    num_only = ''.join( re.findall(r"\d", s))
    if contains_consecutive(num_only):
        return "Invalid"
    return "Valid"

n = int(input())

for i in range(n):
    card = input()
    print( validate_credit_card(card) )
