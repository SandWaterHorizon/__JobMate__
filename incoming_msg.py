# incoming_msg.py #


import json
import api_files.ChatGPT as ChatGPT
import api_files.LinkedIn as LinkedIn
import api_files.Google_job as Google_job
import save_jobs
import os


def main_menu_footer():
    return (
        "📋 *JobMate Menu*\n\n"
        "🧭 Just type a job + city, like:\n"
        "• `frontend developer in Berlin`\n\n"
        "⚙️ Commands:\n"
        "• `save` — Back up your saved jobs\n"
        "• `show saved jobs` — (Coming soon)\n"
        "• `bye` or `thanks` — End the chat\n\n"
        "Let’s find your dream job! 💼✨"
    )


def handle_incoming_message(incoming_msg):
    incoming_msg = incoming_msg.lower().strip()

    try:
        # Predefined keyword help
        if incoming_msg in ["help", "start", "menu"]:
            return (
                "📋 *JobMate Menu*\n\n"
                "🧭 Just type a job + city, like:\n"
                "• `frontend developer in Berlin`\n\n"
                "⚙️ Commands:\n"
                "• `save` — Back up your saved jobs\n"
                "• `show saved jobs` — (Coming soon)\n"
                "• `bye` or `thanks` — End the chat\n\n"
                "Let’s find your dream job! 💼✨"
            )


        #predefined keywords to save
        elif incoming_msg.startswith("save"):
            old_filename = "user_saved_jobs.txt"
            new_filename = "user_saved_jobs_backup.txt"

            print ('hello ')
            with open(old_filename, "r") as f:
                contents = f.read()
                print("content ----- >> ",contents)
                # new_supa_conten = contents

            # Step 2: Rename the file
            # os.rename(old_filename, new_filename)

            with open(new_filename, "w") as f:
                f.write(contents)


        elif "show saved jobs" in incoming_msg:
            saved_jobs = save_jobs.get_saved_jobs()
            return "📂 Your saved jobs:\n" + "\n".join(saved_jobs) if saved_jobs else "❌ No jobs saved yet."



        elif any(kw in incoming_msg for kw in ["bye", "thanks"]):
            # return f"👋 Good luck on your job hunt! I'm here whenever you need me. 💼 { main_menu_footer()}"
            return "👋 Good luck on your job hunt! I'm here whenever you need me. 💼 "

        # Fallback: treat anything else as job input
        try:
            answer_chatGPT = ChatGPT.format_for_target_api(incoming_msg)
            job_data = json.loads(answer_chatGPT)
            job_title = job_data.get("job_title", incoming_msg)


        except Exception as e:
            print("[ERROR in ChatGPT]", e)
            job_title = incoming_msg  # fallback to raw input

        try:
            # job_title = job_data.get("job_title", incoming_msg)
            return Google_job.indeed_job_search(incoming_msg)

        except Exception as e:
            print("[ERROR in LinkedIn]", e)
            # return Google_job.indeed_job_search(incoming_msg)
            return Google_job.indeed_job_search(incoming_msg)


    except Exception as e:
        print("[ERROR]", e)
        return "⚠️ Something went wrong. Try again later."



# incoming_msg.py #