from codecs import encode
import os, json, datetime

def setup_db(chapters_length):
    chapters = json.load(open("chapters.json"))['chapters']

    default_scores = {}
    default_scores_dates = {}
    if os.path.exists('db.json'):
        with open('db.json', 'r') as file:
            user_data = json.load(file)
        with open('db_dates.json', 'r') as dates_file:
            user_data_dates = json.load(dates_file)
        return user_data, user_data_dates
    else: # then it's a new user, and I need to take in some preferences and stuff
        print("It appears this is your first time using the system, O mortal memorizer!!")
        parts_size = input("Enter your preferred chunk size for testing (in pages) [0 for full suras]: ") # this is the 10 you're seeing in the code. To be replaced later.

        for chapter in chapters_length:
            if chapters_length[chapter] >= 15:
                length = chapters_length[chapter]
                full_length = chapters_length[chapter]
                while length > 5:
                    default_scores[f"{chapter}-{(full_length - length) // 10 + 1}"] = 0
                    # default_scores_dates[f"{chapter}-{(full_length - length) // 10 + 1}"] = datetime.date.today().strftime("%d/%m/%Y")
                    length -= min(length, 10)
            else:
                default_scores[chapter] = 0
                # default_scores_dates[chapter] = datetime.date.today().strftime("%d/%m/%Y")

        # we'll take the user's current range here
        user_start_part = input("Enter your start range (the range which you'll be graded on) [2-1 for Baqarah start and 114 for An-Nas start]: ")
        user_end_part = input("Enter your end range (the last part you know you know) [sura_number]-[part_number]. Example: Al-Ma'idah 2nd 10 pages will be 5-2: ")
        user_range = {}
        if int(user_start_part.split('-')[0]) > int(user_end_part.split('-')[0]):
            a = user_start_part
            user_start_part = user_end_part
            user_end_part = a

        start_sura_number = int(user_start_part.split('-')[0])
        end_sura_number = int(user_end_part.split('-')[0])
        start_sura_name = [chapter for chapter in chapters if chapter['id'] == start_sura_number][0]['name_simple']
        end_sura_name = [chapter for chapter in chapters if chapter['id'] == end_sura_number][0]['name_simple']
        user_start_part_name = f"{start_sura_name}-{int(user_start_part.split('-')[1])}"
        end_user_part_name = f"{end_sura_name}-{int(user_end_part.split('-')[1])}"


        for i in range((list(default_scores.items()).index((user_start_part_name, 0))), (list(default_scores.items()).index((end_user_part_name, 0))) + 1):
            print(list(default_scores.items())[i])
            user_range[list(default_scores.items())[i][0]] = 0
            default_scores_dates[list(default_scores.items())[i][0]] = datetime.date.today().strftime("%d/%m/%Y")
        # return

        with open('db.json', 'w') as file:
            json.dump(user_range, file)

        with open('db_dates.json', 'w') as dates_file:
            json.dump(default_scores_dates, dates_file)
        return default_scores, default_scores_dates
