import smtplib
import time

uvRange = {'low': [1,2], 'medium': list(range(3,6)), 'high' :  [6,7], 'veryHigh' : [8,9,10], 'extremelyHigh' : list(range(11,15)) }

#print(uvRange)


emailSubjLine = ''
emailBody = ''

def sendEmail(sensorType, sensorValue):

    print("sensorType" + sensorType + " " + "sensorValue" + str(sensorValue))

    if (sensorType == 'UV'):
        if (sensorValue in uvRange['low']):
                emailSubjLine = 'UV is low'
                emailBody = 'Plesant weather, Enjoy the match'
        elif (sensorValue in uvRange['high'] or sensorValue in uvRange['medium']):
                emailSubjLine = 'UV is Medium/High'
                emailBody = 'UV is little high, please use protective gears'
        elif (sensorValue in uvRange['veryHigh']):
                emailSubjLine = 'UV is Medium/High'
                emailBody = 'UV is very high, please use extra protective gears'
        elif (sensorValue in uvRange['extremelyHigh']):
                emailSubjLine = 'URGENT: UV is Extremely High'
                emailBody = 'UV is extremely high, match should be abandoned'
    elif (sensorType == 'rain'):
        email = type
    else:
        email = 'errorSentToAdmins'

    



    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('iotproj6045@gmail.com','--------')

        print("emailSubjLine " + emailSubjLine + "emailBody " + emailBody + "\n\n")

        emailMsg = f'Subject: {emailSubjLine}\n\n{emailBody}'

        print (emailMsg + "\n\n")
            
        smtp.sendmail('iotproj6045@gmail.com','iotproj6045@gmail.com',emailMsg)

if __name__ == '__main__':
    for i in range(1,16):
        sendEmail('UV',i)
        print("i " + str(i))
        time.sleep(5)
