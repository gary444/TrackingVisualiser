
import csv
import cv2 as cv
import numpy as np

# TODO provide cmd line arguments for the following variables
dyad=1
partner=1
trial=2
tracked_object="HandLeftModel"

room_bbox_min = np.array((-2, 0, -2))
room_bbox_max = np.array(( 2, 3,  2))
room_bbox_size = room_bbox_max - room_bbox_min

class Recording(object):
	def __init__(self):
		super(Recording, self).__init__()
		self.left_hand_positions = []
		self.right_hand_positions = []
		self.head_positions = []



# read csv file(s)

recording = Recording()

filename="data/dyad_" + str(dyad) + "_partner" + str(partner) + "_trial" + str(trial) + "_" + "HandLeftModel" + "_track.csv"
print("Will load positional data from file: " + filename)
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
    	pos_x = float(row[0])
    	pos_y = float(row[1])
    	pos_z = float(row[2])
    	recording.left_hand_positions.append((pos_x, pos_y, pos_z))
print("Found " + str(len(recording.left_hand_positions)) + " positions")


filename="data/dyad_" + str(dyad) + "_partner" + str(partner) + "_trial" + str(trial) + "_" + "HandRightModel" + "_track.csv"
print("Will load positional data from file: " + filename)
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
    	pos_x = float(row[0])
    	pos_y = float(row[1])
    	pos_z = float(row[2])
    	recording.right_hand_positions.append((pos_x, pos_y, pos_z))
print("Found " + str(len(recording.left_hand_positions)) + " positions")


filename="data/dyad_" + str(dyad) + "_partner" + str(partner) + "_trial" + str(trial) + "_" + "Head" + "_track.csv"
print("Will load positional data from file: " + filename)
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
    	pos_x = float(row[0])
    	pos_y = float(row[1])
    	pos_z = float(row[2])
    	recording.head_positions.append((pos_x, pos_y, pos_z))
print("Found " + str(len(recording.left_hand_positions)) + " positions")


# visualise positions on an image. render paths as lines
# convert positions to normalised 2D coordinates (effectively orthogonal projection matrix, looking along one of the axes)

img_w=300.0
img_h=300.0
canvas   = np.zeros((int(img_w), int(img_h), 3), dtype="uint8")
l_draw_col = (255, 0, 0)
r_draw_col = (0, 255, 0)
h_draw_col = (0, 0, 255)

for p_idx in range(1,len(recording.left_hand_positions)):
# for p in recording.left_hand_positions:

	p = recording.left_hand_positions[p_idx]
	last_p = recording.left_hand_positions[p_idx-1]

	line_start = (np.asarray(p) - room_bbox_min) / room_bbox_size
	line_end = (np.asarray(last_p) - room_bbox_min) / room_bbox_size

	cv.line(canvas, (int(line_start[0]*img_w), int(img_h) - int(line_start[1]*img_h)), (int(line_end[0]*img_w),  int(img_h) - int(line_end[1]*img_h)), l_draw_col)

	p = recording.right_hand_positions[p_idx]
	last_p = recording.right_hand_positions[p_idx-1]

	line_start = (np.asarray(p) - room_bbox_min) / room_bbox_size
	line_end = (np.asarray(last_p) - room_bbox_min) / room_bbox_size

	cv.line(canvas, (int(line_start[0]*img_w), int(img_h) - int(line_start[1]*img_h)), (int(line_end[0]*img_w),  int(img_h) - int(line_end[1]*img_h)), r_draw_col)


	p = recording.head_positions[p_idx]
	last_p = recording.head_positions[p_idx-1]

	line_start = (np.asarray(p) - room_bbox_min) / room_bbox_size
	line_end = (np.asarray(last_p) - room_bbox_min) / room_bbox_size

	cv.line(canvas, (int(line_start[0]*img_w), int(img_h) - int(line_start[1]*img_h)), (int(line_end[0]*img_w),  int(img_h) - int(line_end[1]*img_h)), h_draw_col)


cv.imshow("Canvas", canvas)
cv.waitKey(0)