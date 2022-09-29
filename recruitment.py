# Anfal Alali
#This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from

def get_skills():
    skills= [
        "c++",
        "paython",
        "java"
     ]
    return skills

# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    for i, item in enumerate(skills,start=1):
       # print (skills.index(skill)+1)
        #print("",skill)
     print(i,item)


# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    choose_skills=[]
    skill1 = int(input("please enter a number of first skill:"))
    skill2 = int(input("please enter a number of second skill:"))
    
    for skill in skills:
        choose_skills.append(skills[skill1 -1])
        choose_skills.append(skills[skill2 -1])
        return choose_skills


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    cv = {}
    cv["age"]= int(input("How old are you?"))
    cv["name"]= input("whats your name")
    cv["experience"]= int(input("how many years of experience?"))
    cv["skills"]= get_user_skills(skills)
    
    return cv

# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if (20<=cv["age"]<=30)and (cv["experience"]>3) and (desired_skill in cv["skills"]):
            return True
    else:
        return False


def main():
    print("Welcome to the special recruitment program, please answer the following questions:")

    
    skills = get_skills()
    show_skills(skills)
    cv = get_user_cv(skills)
    print(get_user_skills(skills))
    desired_skill = skills[2]
    if check_acceptance(cv, desired_skill):
        print(f"you've been accepted,{cv['name']}")
    else:
        print(f"sorry,{cv['name']} you've been rejected." )

    

    


if __name__ == "__main__":
    main()
 