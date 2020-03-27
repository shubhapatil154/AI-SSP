import yagmail
import os

receiver = "shubhapatil154@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2020-03-27_14-35-40.csv"  # attach the file

# mail information
yag = yagmail.SMTP("shubhapatil154@gmail.com", "ssp191099")

# sent the mail
yag.send(
    to=receiver,
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
