CREATE DATABASE yolo_frames;
use yolo_frames;

CREATE TABLE frames (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    FrameNum INT,
    x INT,
    y INT,
    w INT,
    h INT,
    t TIMESTAMP,
    hr INT,
    min INT,
    sec INT
);