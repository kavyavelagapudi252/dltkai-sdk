from dltkai.nlp import pos_tagger

#print(pos_tagger('Hello my name is vishnu'))
#print(ner_tagger('Hello my name is vishnu'))
#print(parser('Hello my name is vishnu'))
#print(clean_text('Hello my name is vishnu'))
#print(toxic_comment_detect('Hello my name is vishnu'))

from dltkai.cv import face_detection_image
from dltkai.cv import licence_plate_image,image_classification
import cv2
from dltkai.cv import object_detection_image

#img  = face_detection_image('group.jpg')
#cv2.imwrite('test.jpg',img)
#data = face_detection_image('group.jpg')
#print(data)
#print(image_classification('group.jpg'))
print(object_detection_image('group.jpg'))
