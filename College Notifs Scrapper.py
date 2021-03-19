import bs4, requests, smtplib, keyboard
from email.mime.text import MIMEText
from datetime import date

# Download page.
getPage = requests.get('http://old.etfbl.net/?c=prikazi&objekat=oglas')
getPage.raise_for_status()

# Parse HTML text.
HTMLOfThePage = bs4.BeautifulSoup(getPage.text, 'html.parser')

# Enter subject in lowercase, optimally cyrilic and latin.
mySubjects = ['дискретна математика', 'основи електронике и дигиталне технике', 'структуре података и алгоритми',
              'основи софтверског инжењерства', 'програмски језици', 'рачунарске мреже', 'енглески језик',
              'diskretna matematika', 'osnovi elektronike i digitalne tehnike', 'strukture podataka i algoritmi',
              'osnovi softverskog inzenjerstva', 'programski jezici', 'računarske mreže', 'engleski jezik']

notifications = []

for text in HTMLOfThePage.select('.tdlight'): # Looping through the objects of a class that contains one notification post.
    for subject in mySubjects: 
        if subject in text.find('a').get_text().lower(): # Comparing my list of subjects with the current notification post.
            if date.today().strftime('%d.%m.%Y') in text.get_text()[:11]: # Is the date of the post today's date.
                notifications.append(text.get_text()[13:23] + ' ' + subject.capitalize() + ': http://old.etfbl.net/' + text.find('a')['href'])

message = 'Notifications for ' + date.today().strftime('%d.%m.%Y') + ':\n\n'

for link in notifications:
    message = message + link + '\n'
            
if message == 'Notifications for ' + date.today().strftime('%d.%m.%Y') + ':\n\n':
    message = message + 'No new notifications.'

message = message.rstrip()

recepientAddresses = ['njegos.dukic.998@gmail.com']

# Sending an e-mail

# for recepient in recepientAddresses:
#     to = recepient + ';'

# conn = smtplib.SMTP('smtp.gmail.com', 587) # SMTP Address and Port.
# conn.ehlo() # Starting connection.
# conn.starttls() # Statring TLS encryption, encrpyted when password sent.
# conn.login('njegos.dukic.998@gmail.com', 'xzmbzobvgbklvcpy')

# msg = MIMEText(message)
# msg['Subject'] = 'New notifications!'
# msg['From'] = 'njegos.dukic.998@gmail.com'
# msg['To'] = to
# conn.send_message(msg)

# conn.quit()

print(message)

# print('\n\nInformed and sent email for the following recepients:')
# for email in recepientAddresses:
#         print(email)

print('\n\nPress enter to close the program!')
while True:
    if keyboard.is_pressed('enter'):
        break