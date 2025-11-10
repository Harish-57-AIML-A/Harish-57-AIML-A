import os
import datetime
import subprocess

start_date = datetime.date(2025, 9, 26)
end_date = datetime.date(2025, 11, 2)
sequence = [4, 5, 3, 6]

repo_path = os.getcwd()

day_count = 0
while start_date <= end_date:
    num_commits = sequence[day_count % len(sequence)]
    for i in range(num_commits):
        with open(os.path.join(repo_path, "streak_fix.txt"), "a") as f:
            f.write(f"Commit {i+1} on {start_date}\n")
        subprocess.run(["git", "add", "streak_fix.txt"])
        date_str = start_date.strftime("%Y-%m-%d 12:%M:%S")
        subprocess.run(["git", "commit", "-m", f"Commit {i+1} on {start_date}", "--date", date_str])
    start_date += datetime.timedelta(days=1)
    day_count += 1
