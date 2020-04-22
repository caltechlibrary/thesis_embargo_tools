import sys
import os
from datetime import datetime
from tet import CommitteeForm, process_email

def usage(msg = "", exit_code = 0):
    app_name = os.path.basename(sys.argv[0])
    if msg:
        print(msg)
    print(f'''
USAGE: {app_name} STACKS_EMAIL EXCEL_FILENAME

This program takes an template excel filename,
an email from stacks form that has been saved as a
plain text file and renders a new Excel workbook
using for use by the embargo committee.

''')
    sys.exit(exit_code)

def generate_committee_excel(stacks_email, xlsx_filename):
    name, obj = process_email(stacks_email)
    #Add today's date
    today = datetime.today().date().isoformat()
    obj['date_routing_initiated'] = today
    form = CommitteeForm()
    form.render(xlsx_filename, name, obj)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage("", 1)
    generate_committee_excel(sys.argv[1], sys.argv[2])
