Problem Statement : Detecting people for statistical analalytic. Want to provide a platform where the Data Scientist can generate a statistic e.g. we can generate a histogram where we see the number of people that we see at a certain time of the day 

Why does this matter : In COVID times, we can track the traffic in the retail store and plan foot traffic so as to align with social distancing guidelines. 

Acceptance criteria : System is able to detect the people and store it in a database with a dockerized container so that the design is scalable

Techincal implementation : Picking up videos from the directory, running object detection with a model trained on COCO dataset, then storing the bounding boxes and timestamp in txt format and storing the files on a data base. This data base can be used to generate statistics. 

Data Flow : Video Files --> Inference Model --> Txt Files --> Store into Database --> Analyst pulls data --> Display stats on dashboard


