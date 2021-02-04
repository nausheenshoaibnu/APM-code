import os

videos = os.listdir("data/Dataset_size_10/")
videos.sort()
for v in videos:
    os.system("./darknet detector demo cfg/obj.data cfg/yolo-obj.cfg backup/yolo-obj_20900.weights "+os.path.join("data/Dataset_size_10/"+v))

