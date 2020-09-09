import face_recognition
from matplotlib import pyplot

image = face_recognition.load_image_file("AIrang/images/ariel.jpg")
face_locations = face_recognition.face_locations(image)

pyplot.rcParams["figure.figsize"] = (16, 16)
pyplot.imshow(image)
pyplot.show()
