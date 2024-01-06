import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable
from queries import *

# def connect_to_sever():
#     return pymysql.connect(host='localhost',
#                         port=3306,
#                         user="root",
#                         password="rootroot",
#                         db='icpc',
#                         cursorclass=pymysql.cursors.DictCursor)

def show_catgories():
    print("1. Retrieval\n2. Modification\n3. Analysis\n4. Exit")

def show_options(choice):
    tmp = sp.call('clear', shell=True)
    if choice == 1:
        print("1. Retrieve participants in a team")
        print("2. Retrieve problems set by an author")
        print("3. Retrieve list of participants based on their university")
        print("4. Retrieve list of teams who have solved a particular problem")
        print("5. Retrieve all submissions in a coding language")
        print("6. Find teams with the most accepted submissions")
        print("7. Find average number of problems solved in each region")
        print("8. Find most solved problems")
        print("9. Count number of accepted submissions in a language")
        print("10. Search for team names containing a string")
        print("11. Search for teams belonging to universities starting with string")
        print("12. Search for mentors with their first name")
        print("13. Back")
    
    elif choice == 2:
        print("1. Add Submission")
        print("2. Add Test Case")
        print("3. Update Test Case")
        print("4. Update score of a team")
        print("5. Disqualify Team")
        print("6. Remove Low-Rated Team")
        print("7. Back")

    elif choice == 3:
        print("1. Display the average penalty for every problem based on their non-accepted submissions.")
        print("2. Generate a rank list of teams participating based on their scores (after penalty) for a region.")
        print("3. Retrieve the acceptance rate of problems created by an author.")
        print("4. Back")

def dispatch(choice, sub_choice):        
    tmp = sp.call('clear', shell=True)
    if choice == 1:
        if sub_choice == 1:
            team_id = input("Team ID: ")
            get_participants_in_team(team_id)
        elif sub_choice == 2:
            author_id = input("Author ID: ")
            get_problems_of_author(author_id)
        elif sub_choice == 3:
            uni_id = input("University ID: ")
            get_participants_in_university(uni_id)
        elif sub_choice == 4:
            prob_id = input("Problem ID: ")
            get_teams_who_solved_problem(prob_id)
        elif sub_choice == 5:
            lang = input("Language: ")
            get_submissions_in_language(lang)
        elif sub_choice == 6:
            get_teams_with_max_ac()
        elif sub_choice == 7:
            region = input("region ID: ")
            get_avg_problems_solved_by_region(region)
        elif sub_choice == 8:
            get_most_solved_problem()
        elif sub_choice == 9:
            lang = input("Language: ")
            get_count_of_ac_in_language(lang)
        elif sub_choice == 10:
            search_string= input("search string: ")
            get_teams_with_char(search_string)
        elif sub_choice == 11:
            starts_with = input("Enter university beginning: ")
            get_teams_of_uni_starting_with(starts_with)
        elif sub_choice == 12:
            fname = input("Mentor fname: ")
            get_mentors_starting_with(fname)
        else:
            return None
    
    elif choice == 2:
        
        if sub_choice == 1:
            time_stamp = input("time stamp: ")
            team_id = input("Team ID: ")
            problem_id = input("Problem_ID: ")
            lang = input("Language: ")
            acceptance = input("Acceptance: ")
            add_submission(time_stamp, team_id, problem_id, lang, acceptance)

        elif sub_choice == 2:
            problem_id = input("Problem ID: ")
            testcase_id = input("testcase ID: ")
            testcase = input("testcase: ")
            add_testcase(problem_id, testcase_id, testcase)

        elif sub_choice == 3:
            problem_id = input("Problem ID: ")
            testcase_id = input("Testcase ID: ")
            updated_testcase = input("Updated testcase: ")
            update_testcase(problem_id, testcase_id, updated_testcase)
        
        elif sub_choice == 4:
            team_id = input("Team ID: ")
            update_score(team_id)

        elif sub_choice == 5:
            team_id = input("Team ID: ")
            remove_team(team_id)

        elif sub_choice == 6:
            avg_rating = input("Avg rating: ")
            remove_team_based_on_avg_rating(avg_rating)

        else:
            return None 

    elif choice == 3:
        if sub_choice == 1:
            problem_id = input("Problem ID: ")
            get_avg_penalty_of_problem(problem_id)
        elif sub_choice == 2:
            region_id = input("Region ID: ")
            get_ranklist_of_region(region_id)
        elif sub_choice == 3:
            author_id = input("Author ID: ")
            get_ac_rate_of_problems_by_author(author_id)
        else:
            return None 