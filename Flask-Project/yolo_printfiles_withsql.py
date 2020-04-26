#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import ntpath
import cv2
import os
import numpy as np
import time
import pymysql
pymysql.install_as_MySQLdb()
con = pymysql.connect('localhost', 'testuser', 'test623', 'testdb')

# In[ ]:
def getListOfFiles(dirName):
    # create a list of files and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    listOfFile.sort()
    # iterate over all the entries
    for entry in listOfFile:
        # create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def startdetection(file_list, dbname, label='person'):
    first_start_time = time.time()

    # Load yolo
    net = cv2.dnn.readNet("/media/mynewdrive/data/Retail_AI/3DPeS/yolov3.weights.1",
                          "/media/mynewdrive/data/Retail_AI/3DPeS/darknet/cfg/yolov3.cfg")
    classes = []
    with open("/media/mynewdrive/data/Retail_AI/3DPeS/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # Start detecting
    #open connection to mysql
    with con:
        cur = con.cursor()
        drop_table_query = "DROP TABLE IF EXISTS {}".format(dbname)
        cur.execute(drop_table_query)
        create_table_query = "CREATE TABLE {}(Id INT PRIMARY KEY AUTO_INCREMENT, FrameNum INT, x INT, y INT, w INT, h INT, t TIMESTAMP)".format(dbname)
        cur.execute(create_table_query)
        for file_name in file_list:
            cap = cv2.VideoCapture(file_name)
            frame_count = 0
            img_array = []
            metadata_file = file_name.split('.')[0] + '.txt'
            video_output = file_name.split('.')[0] + '_yolo.avi'
            label_index = classes.index(label)
            outF = open(metadata_file, "w")
            while True:
                _, frame = cap.read()
                frame_count += 1
                if _!=True:
                    break

                height, width, channels = frame.shape
                blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
                net.setInput(blob)
                outs = net.forward(output_layers)

                class_ids = []
                confidences = []
                boxes = []

                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5 and class_id == label_index:
                            # Object detected
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)

                            # draw circle
                            cv2.circle(frame, (center_x, center_y), radius=5, color=(0, 255, 0), thickness=1)
                            w = int(detection[2] * width)
                            h = int(detection[3] * width)

                            # Rectangle coordinates
                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)

                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.6)
                font = cv2.FONT_HERSHEY_PLAIN

                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        color = colors[i]
                        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                        cv2.putText(frame, label, (x, y + 30), font, 1, color, 2)

                        # create a text file to output bounding boxes
                        # write frame number and coordinates
                        t = time.localtime()
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', t)
                        # time_timestamp = time.strftime('%H:%M:%S', t)
                        outF.write("FrameNum=%s, x=%f, y=%f, w=%f, h=%f, t=%s\n" % (frame_count, x, y, w, h, timestamp))
                        insert_row_query = "INSERT INTO {}(FrameNum,x,y,w,h,t) VALUES({},{},{},{},{},{}) ".format(dbname, frame_count , x,y,w,h,'CURRENT_TIMESTAMP')
                        cur.execute(insert_row_query)
                        # outF.write("FrameNum=%s, x=%f, y=%f, w=%f, h=%f\n" % (frame_count, x, y, w, h))


                img_array.append(frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
            cap.release()
            cv2.destroyAllWindows()
            outF.close()

            # Create the output video file
            size = (width, height)
            out = cv2.VideoWriter(video_output, cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

            for i in range(len(img_array)-1):
                out.write(img_array[i])
            out.release()
        return "--- %s seconds ---" % (time.time() - first_start_time)

# dirName='/media/mynewdrive/data/Retail_AI/3DPeS/small_video_set_1'
# file_list = getListOfFiles(dirName)
# print("Calling startdetection")
# time = startdetection(file_list,ntpath.basename(dirName))
#
# print(time)