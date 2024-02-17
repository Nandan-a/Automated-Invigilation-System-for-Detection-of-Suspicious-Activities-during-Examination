import serial
import math
import cv2
import os
from math import sqrt, acos, degrees
import numpy as np
import face_recognition
from math import sqrt, acos, degrees

serial_data=serial.Serial("COM5",9600)
start_camera = cv2.VideoCapture(0)
thres = 0.45
# start_camera.set(3,1280)
# start_camera.set(4,720)
# start_camera.set(10,70)
def image_mail_sender1():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    from email.mime.base import MIMEBase
    from email import encoders

    strFrom = 'anjaliproject1234@gmail.com'
    strTo = 'anjaliproject1234@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Malpractise detected'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')

    msgRoot.attach(msgAlternative)

    mail_message_Text = MIMEText('Anjali in malpractise')

    msgAlternative.attach(mail_message_Text)

    sending_image = open('anjali_malpractise.jpg', 'rb')

    msgImage = MIMEImage(sending_image.read())

    sending_image.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')

    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('anjaliproject1234@gmail.com', 'upbzscqeqotnlzlu')

    print("mail id and password correct")

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())

    print("mail send")

    smtp.quit()

def image_mail_sender2():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    from email.mime.base import MIMEBase
    from email import encoders

    strFrom = 'anjaliproject1234@gmail.com'
    strTo = 'nandana39790@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Malpractise detected'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')

    msgRoot.attach(msgAlternative)

    mail_message_Text = MIMEText('Nandan in malpractise')

    msgAlternative.attach(mail_message_Text)

    sending_image = open('nandan_malpractise.jpg', 'rb')

    msgImage = MIMEImage(sending_image.read())

    sending_image.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')

    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('anjaliproject1234@gmail.com', 'upbzscqeqotnlzlu')

    print("mail id and password correct")

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())

    print("mail send")

    smtp.quit()

def image_mail_sender3():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    from email.mime.base import MIMEBase
    from email import encoders

    strFrom = 'anjaliproject1234@gmail.com'
    strTo = 'anjaliproject1234@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Malpractise detected'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')

    msgRoot.attach(msgAlternative)

    mail_message_Text = MIMEText('Navya in malpractise')

    msgAlternative.attach(mail_message_Text)

    sending_image = open('navya_malpractise.jpg', 'rb')

    msgImage = MIMEImage(sending_image.read())

    sending_image.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')

    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('anjaliproject1234@gmail.com', 'upbzscqeqotnlzlu')

    print("mail id and password correct")

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())

    print("mail send")

    smtp.quit()

def image_mail_sender4():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    from email.mime.base import MIMEBase
    from email import encoders

    strFrom = 'anjaliproject1234@gmail.com'
    strTo = 'anjaliproject1234@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Malpractise detected'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')

    msgRoot.attach(msgAlternative)

    mail_message_Text = MIMEText('Priya in malpractise')

    msgAlternative.attach(mail_message_Text)

    sending_image = open('priya_malpractise.jpg', 'rb')

    msgImage = MIMEImage(sending_image.read())

    sending_image.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')

    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('anjaliproject1234@gmail.com', 'upbzscqeqotnlzlu')

    print("mail id and password correct")

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())

    print("mail send")

    smtp.quit()

def image_mail_sender5():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.image import MIMEImage
    import smtplib
    from email.mime.base import MIMEBase
    from email import encoders

    strFrom = 'anjaliproject1234@gmail.com'
    strTo = 'anjaliproject1234@gmail.com'

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'Mobile detected'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    msgAlternative = MIMEMultipart('alternative')

    msgRoot.attach(msgAlternative)

    mail_message_Text = MIMEText('mobile detected')

    msgAlternative.attach(mail_message_Text)

    sending_image = open('mobile.jpg', 'rb')

    msgImage = MIMEImage(sending_image.read())

    sending_image.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')

    msgRoot.attach(msgImage)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.starttls()

    smtp.login('anjaliproject1234@gmail.com', 'upbzscqeqotnlzlu')

    print("mail id and password correct")

    smtp.sendmail(strFrom, strTo, msgRoot.as_string())

    print("mail send")

    smtp.quit()

def face_angle_coordinate():
    import math

    import cv2
    import numpy as np
    import face_recognition
    import os
    from math import sqrt, acos, degrees
    import time

    path = 'office_employ_data_base_folder'
    images = []
    classNames = []
    myList = os.listdir(path)

    # print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)

    while True:
        record, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        radius = 300
        center = (360, 240)
        angle = 0
        vec = (radius, 0)

        # ---------circle---------#
        for x in (0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330):
            cv2.circle(img, (320, 240), 240, (255, 255, 255), 8)
            x_coordinate = center[0] + radius * math.cos(x * 3.14 / 180)
            y_coordinate = center[1] + radius * math.sin(x * 3.14 / 180)

        # -------------line-----------#
        cv2.line(img, (320, 0), (320, 480), (0, 0, 255), 3)
        cv2.line(img, (0, 240), (640, 240), (0, 0, 255), 3)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(matches)
            matchIndex = np.argmin(faceDis)
            # print(matchIndex)

            if matches[matchIndex]:
                name = classNames[matchIndex]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                midx = int((x1 + x2) / 2)
                midy = int((y1 + y2) / 2)

                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.circle(img, (midx, midy), 4, (250, 0, 0), 4)
                cv2.line(img, (590, 230), (590, 260), (0, 0, 0), 4)
                cv2.putText(img, ("0"), (580, 270), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
                cv2.line(img, (10, 230), (10, 260), (0, 0, 0), 4)
                cv2.putText(img, ("180"), (11, 280), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
                cv2.line(img, (300, 10), (350, 10), (0, 0, 0), 4)
                cv2.putText(img, ("90"), (250, 20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
                cv2.line(img, (300, 400), (350, 400), (0, 0, 0), 4)
                cv2.putText(img, ("270"), (350, 390), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
                cv2.putText(img, ("1"), (500, 200), cv2.FONT_HERSHEY_PLAIN, 2, (20, 0, 255), 3)
                cv2.putText(img, ("2"), (200, 200), cv2.FONT_HERSHEY_PLAIN, 2, (20, 0, 255), 3)
                cv2.putText(img, ("3"), (200, 300), cv2.FONT_HERSHEY_PLAIN, 2, (20, 0, 255), 3)
                cv2.putText(img, ("4"), (400, 300), cv2.FONT_HERSHEY_PLAIN, 2, (20, 0, 255), 3)

                cv2.circle(img, (midx, midy), 4, (250, 0, 0), 4)
                cv2.line(img, (midx, midy), (320, 240), (255, 255, 0), 4)
                cv2.circle(img, (320, 240), 4, (250, 0, 0), 4)

                a1x1 = midx
                b1y1 = 240
                a2x2 = 320
                b2y2 = midy
                dist = math.sqrt((a2x2 - a1x1) ** 2 + (b2y2 - b1y1) ** 2)
                cv2.putText(record, "{}".format(dist), (midx, midy), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)
                # print("distance between", (a1x1, b1y1), "and", (a2x2, b2y2), "is :  ", (dist))

                # ----------angle-------------#

                dy = b1y1 - b2y2
                dx = a1x1 - a2x2
                rads = math.atan2(dy, dx)
                degs = degrees(rads)

                if degs < 0:
                    degs += 360

                # print("person =", name)

                if name == "anjali":
                    if degs > 0 and degs < 90:
                        print("anjali in first coordinate")
                    else:
                        print("anjali in malpractice")
                        cv2.imwrite("anjali_malpractise.jpg",img)
                        serial_data.write(b'A')
                        print(b'A')
                        image_mail_sender1()

                elif name == "nandan":
                    # print("angle find")
                    if degs > 90 and degs < 180:
                        print("nandan in 2nd coordinate")
                    else:
                        print(" nandan in malpractice")
                        cv2.imwrite("nandan_malpractise.jpg", img)
                        serial_data.write(b'A')
                        image_mail_sender2()

                elif name == "navya":
                    # print("angle find")
                    if degs > 180 and degs < 270:
                        print("navya in 3nd coordinate")
                    else:
                        print("navya in malpractice")
                        cv2.imwrite("navya_malpractise.jpg", img)
                        serial_data.write(b'A')
                        image_mail_sender3()

                elif name == "priya":
                    if degs > 270 and degs < 360:
                        print("priya in 4th coordinate")
                    else:
                        print("priya in malpractice")
                        cv2.imwrite("priya_malpractise.jpg", img)
                        serial_data.write(b'A')
                        image_mail_sender4()

        cv2.imshow('CAMERA', img)
        cv2.waitKey(1)
        window_close = cv2.waitKey(1)
        if window_close == 27:
            break


def main_function():

    classNames1= []
    classFile = 'coco.data'
    with open(classFile,'rt') as f:
        classNames1 = f.read().rstrip('\n').split('\n')

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt.txt'
    weightsPath = 'frozen_inference_graph.pb'
    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)



    while 1:

        frame, record = start_camera.read()
        classIds, confs, bbox = net.detect(record,confThreshold=0.45)


        if len(classIds) != 0:
                for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):

                    object_name=(classNames1[classId-1])
                    object_id=[classId-1]
                    # print(object_id)



                    if object_id ==[76]:

                        print(" phone detected  ")
                        # ser1.write(b'A')
                        cv2.rectangle(record, box, color=(0, 255, 0), thickness=2)
                        cv2.putText(record, classNames1[classId - 1], (box[0] + 10, box[1] + 30),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(record, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imwrite("mobile.jpg",record)
                        serial_data.write(b'A')
                        image_mail_sender5()

        serial_data.write(b'x')
        cv2.imshow("output", record)
        window_close = cv2.waitKey(1)



        if window_close == 27:
            break

a = input("Enter the mode of invigilation =")

if a=='mobile_mode':
    main_function()
elif a=='malpractice_mode':
    face_angle_coordinate()
else:
    print("Enter the correct mode of invigilation")

