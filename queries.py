import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable
import settings

def display_table(list_of_dicts):
    table = PrettyTable(list(list_of_dicts[0].keys()))
    for entry in list_of_dicts:
        table.add_row(list(entry.values()))
    print(table)

def execute_and_display_query(query):
    settings.cur.execute(query)
    rows = settings.cur.fetchall()

    if settings.cur.rowcount != 0:
        display_table(rows)
    # for i in rows:
    #     print(i)
    print("\033[94m" + str(settings.cur.rowcount) + " rows retrieved" + "\033[0m")

def get_participants_in_team(team_id):
    query = 'SELECT * FROM participants WHERE Team_Id = {tid}'.format(tid= team_id) 
    execute_and_display_query(query)

def get_problems_of_author(author_id):
    query = 'SELECT * FROM problem WHERE Author_id = {aid}'.format(aid= author_id)
    execute_and_display_query(query)

def get_participants_in_university(uni_id):
    query = 'SELECT * FROM participants WHERE University_ID = {uid}'.format(uid= uni_id)
    execute_and_display_query(query) 

def get_teams_who_solved_problem(prob_id):
    query = 'SELECT DISTINCT(Team_id) FROM submission WHERE Problem_id = {pid}'.format(pid= prob_id)
    execute_and_display_query(query) 

def get_submissions_in_language(lang):
    query = "SELECT * FROM submission WHERE Programming_Language = '{lg}'".format(lg= lang)
    execute_and_display_query(query) 

def get_teams_with_max_ac():
    query = '''
    SELECT Team_id, SUM(Acceptance) AS AC 
    FROM submission 
    GROUP BY Team_id 
    HAVING SUM(Acceptance) = (
        SELECT MAX(total_acceptance) 
        FROM (
            SELECT Team_id, SUM(Acceptance) AS total_acceptance 
            FROM submission 
            GROUP BY Team_id
        ) AS max_acceptance
    );
    '''
    execute_and_display_query(query) 

def get_avg_problems_solved_by_region(region_id):
    query = '''
    SELECT AVG(total_problems_solved) AS avg_problems_solved
    FROM (
        SELECT t.Team_Id, COUNT(DISTINCT s.Problem_id) AS total_problems_solved
        FROM team t
        LEFT JOIN submission s ON t.Team_Id = s.Team_id
        WHERE t.Region_Id = {}
        GROUP BY t.Team_Id
    ) AS team_problems;
    '''.format(region_id)
    execute_and_display_query(query) 

def get_most_solved_problem():
    query = '''
    SELECT Problem_id, COUNT(*) AS total_solutions
    FROM submission
    WHERE Acceptance = 1
    GROUP BY Problem_id
    ORDER BY total_solutions DESC
    LIMIT 1;
    '''
    execute_and_display_query(query) 

def get_count_of_ac_in_language(lang):
    query = '''
    SELECT COUNT(*) AS total_ac
    FROM submission
    WHERE Programming_Language = '{}' AND Acceptance = 1;
    '''.format(lang)
    execute_and_display_query(query) 

def get_teams_with_char(search_string):
    query = '''
    SELECT * 
    FROM team
    WHERE Name LIKE '%{}%';
    '''.format(search_string)
    execute_and_display_query(query) 

def get_teams_of_uni_starting_with(starts_with):
    query = '''
    SELECT * 
    FROM team
    WHERE University_Id IN (
        SELECT University_Id
        FROM university
        WHERE name LIKE '{}%'
    );
    '''.format(starts_with)
    execute_and_display_query(query) 

def get_mentors_starting_with(fname):
    query = '''
    SELECT DISTINCT Fname,Lname
    FROM mentor
    WHERE Fname LIKE '{}%';
    '''.format(fname)
    execute_and_display_query(query) 

def get_avg_penalty_of_problem(problem_id):
    query = '''
    SELECT COALESCE(AVG(total_tries), 0) AS avg_penalty
    FROM (
        SELECT Team_id, COUNT(*)-1 AS total_tries
        FROM submission
        WHERE Problem_id = {}
        GROUP BY Team_id
        HAVING SUM(Acceptance) > 0
    ) AS team_tries;
    '''.format(problem_id)
    execute_and_display_query(query)

def get_ranklist_of_region(region_id):
    query = '''
    SELECT 
        ROW_NUMBER() OVER (ORDER BY COALESCE(SUM(s.Acceptance), 0) DESC) AS team_rank,
        t.Team_Id, 
        t.Name, 
        COALESCE(SUM(s.Acceptance), 0) AS total_acceptance
    FROM team t
    LEFT JOIN submission s ON t.Team_Id = s.Team_id
    WHERE t.Region_Id = {}
    GROUP BY t.Team_Id, t.Name
    ORDER BY total_acceptance DESC;
    '''.format(region_id)
    execute_and_display_query(query)

def get_ac_rate_of_problems_by_author(author_id):
    query = '''
    SELECT p.Problem_id, 
           COUNT(s.Acceptance) AS total_submissions,
           SUM(s.Acceptance) AS total_acceptances,
           SUM(s.Acceptance)/COUNT(s.Acceptance) AS acceptance_rate
    FROM submission s
    RIGHT JOIN problem p ON s.Problem_id = p.Problem_id
    WHERE p.Author_Id = {}
    GROUP BY p.Problem_id
    ORDER BY acceptance_rate DESC;
    '''.format(author_id)
    execute_and_display_query(query) 

def add_submission(time_stamp, team_id, problem_id, lang, acceptance):
    query = f"INSERT INTO submission (time_stamp, Team_id, Problem_id, Programming_Language, Acceptance) VALUES ('{time_stamp}', {team_id}, {problem_id}, '{lang}', {acceptance});"
    settings.cur.execute(query)
    print("\033[94m" + "Rows affected: "+str(settings.cur.rowcount) + "\033[0m")
    settings.con.commit()

def add_testcase(problem_id, testcase_id, testcase):
    query = f"INSERT INTO test_case (problem_id, testcase_id, testcase) VALUES ({problem_id}, {testcase_id}, '{testcase}');"
    settings.cur.execute(query)
    print("\033[94m" + "Rows affected: "+str(settings.cur.rowcount) + "\033[0m")
    query = f"UPDATE problem SET Number_of_testcases = Number_of_testcases + 1"
    settings.cur.execute(query)
    settings.con.commit()

def update_score(team_id):
    query = f"UPDATE team SET Score = (SELECT COUNT(DISTINCT Problem_id) FROM submission WHERE Team_id = {team_id} AND Acceptance = 1) WHERE Team_Id = {team_id};"
    settings.cur.execute(query)
    print("\033[94m" + "Rows affected: "+str(settings.cur.rowcount) + "\033[0m")
    settings.con.commit()

def update_testcase(problem_id, testcase_id, updated_testcase):
    query = f"UPDATE test_case SET testcase = '{updated_testcase}' WHERE problem_id = {problem_id} AND testcase_id = {testcase_id};"
    settings.cur.execute(query)
    print("\033[94m" + "Rows affected: "+str(settings.cur.rowcount) + "\033[0m")
    settings.con.commit()

def remove_team(team_id):
    query = f"DELETE FROM team WHERE Team_Id = {team_id};"
    settings.cur.execute(query)
    print("\033[94m" + "Rows affected: "+str(settings.cur.rowcount) + "\033[0m")
    settings.con.commit()

def remove_team_based_on_avg_rating(avg_rating):
    query = f"DELETE FROM team WHERE Avg_Rating < {avg_rating};"
    settings.cur.execute(query)
    print("\033[94m" + "Rows affected: "+str(settings.cur.rowcount) + "\033[0m")
    settings.con.commit()