Problem Statement : Detecting people for vision based statistical analalytic. Want to provide a platform where the Data Scientist can generate a statistic e.g. we can generate a histogram where we see the number of people that we see at a certain time of the day.

Why does this matter : In COVID times, we can track the traffic in the retail store and plan foot traffic so as to help the business owners understand the number of people in the retail store . 

Acceptance criteria : System is able to detect the people and store the locale of the person and the timestamp it in a database using a dockerized container so that the design is scalable.

Techincal implementation : Picking up videos from the directory, running object detection with a YOLO model trained on COCO dataset, then storing the bounding boxes and timestamp in text format in .txt files and storing the files on a data base then showing the stats on a frontend dashbaord. This data base can be used to generate other statistics. 

Data Flow : Video Files --> Inference Model --> Txt Files with bounding boxes and timestamp --> Store into Database --> Analyst pulls data --> Display stats on dashboard


