import os
import time

while(len(os.listdir("result_img"))>=0):
    os.system("./demos/classifier.py infer ./generated-embeddings/classifier.pkl result_img")

