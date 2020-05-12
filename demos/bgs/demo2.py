import cv2

print("OpenCV Version: {}".format(cv2.__version__))

## bgslibrary algorithms
algorithms = []
algorithms.append(cv2.bgsegm.createBackgroundSubtractorMOG)

video_file = "dataset/video01.mp4"

for algorithm in algorithms:
	capture = cv2.VideoCapture(video_file)
	_algorithm = None
	try:
		_algorithm = algorithm(noiseSigma=12, history=500, nmixtures=5)
	except:
		import warnings

		_algorithm = algorithm()
	i = 0
	# pos_frame = capture.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
	# pos_frame = capture.get(cv2.CV_CAP_PROP_POS_FRAMES)
	import datetime

	start = datetime.datetime.now()
	while True:
		flag, frame = capture.read()

		i = i + 1

		try:
			x = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
			print(x.shape)
			img_output = _algorithm.apply(x)
			cv2.imshow('bgs demo2', img_output)
		except:
			print(_algorithm.__class__.__name__ + " cant run")
			break

		if i == 200:
			diff = (datetime.datetime.now() - start)
			print(_algorithm.__class__.__name__ + ";" + str(diff.total_seconds()) + "\n")
			print('Write:', str(
				cv2.imwrite(
					'./demos/bgs/a' + _algorithm.__class__.__name__ + '_' + str(diff.total_seconds()) + '.jpg',
					img_output)))
			break
		if 0xFF & cv2.waitKey(10) == 27:
			break

# if capture.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == capture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
# if capture.get(cv2.CV_CAP_PROP_POS_FRAMES) == capture.get(cv2.CV_CAP_PROP_FRAME_COUNT):
# if capture.get(1) == capture.get(cv2.CV_CAP_PROP_FRAME_COUNT):
# break

print("Finished")
cv2.destroyAllWindows()
