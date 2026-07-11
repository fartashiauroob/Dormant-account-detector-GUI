from datetime import datetime
import tkinter as tk

names = ["Ali Raza", "Sara Khan", "Bilal Ahmed", "Hina Malik", "Usman Tariq", "Ayesha Noor", "Danish Iqbal"]
roles = ["Employee", "Manager", "Intern", "HR Officer", "Developer", "Finance Lead", "Support Staff"]
last_logins = ["2026-07-05", "2026-05-01", "2026-06-20", "2026-03-15", "2026-07-09", "2026-02-10", "2026-06-01"]

dormant_days = 30


def run_scan():

    output_box.delete("1.0", tk.END)

    today = datetime.now()
    dormant_count = 0

    report_file = open("dormant_account_report.csv", "w")
    report_file.write("Name,Role,Last Login,Days Inactive,Status\n")

    output_box.insert(tk.END, "==== DORMANT ACCOUNT SECURITY REPORT ====\n\n")

    for i in range(len(names)):
        name = names[i]
        role = roles[i]
        last_login_text = last_logins[i]

        last_login_date = datetime.strptime(last_login_text, "%Y-%m-%d")

        days_inactive = (today - last_login_date).days

        if days_inactive >= dormant_days:
            status = "DORMANT"
            dormant_count = dormant_count + 1
        else:
            status = "ACTIVE"

        output_box.insert(tk.END, "Name          : " + name + "\n")
        output_box.insert(tk.END, "Role          : " + role + "\n")
        output_box.insert(tk.END, "Last Login    : " + last_login_text + "\n")
        output_box.insert(tk.END, "Days Inactive : " + str(days_inactive) + "\n")
        output_box.insert(tk.END, "Status        : " + status + "\n")

        if status == "DORMANT":
            output_box.insert(tk.END, "Recommendation: Disable this account immediately.\n")

        output_box.insert(tk.END, "----------------------------------------\n")

        report_file.write(name + "," + role + "," + last_login_text + "," + str(days_inactive) + "," + status + "\n")

    report_file.close()

    output_box.insert(tk.END, "\nTotal accounts checked : " + str(len(names)) + "\n")
    output_box.insert(tk.END, "Dormant accounts found : " + str(dormant_count) + "\n")
    output_box.insert(tk.END, "Report saved as 'dormant_account_report.csv'\n")

window = tk.Tk()
window.title("Dormant Account Detector")
window.geometry("600x500")

title_label = tk.Label(window, text="Dormant Account Detector", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

scan_button = tk.Button(window, text="Run Scan", font=("Arial", 12), command=run_scan)
scan_button.pack(pady=5)

output_box = tk.Text(window, width=70, height=25)
output_box.pack(padx=10, pady=10)

window.mainloop()
