import cv2
import libs.pybgs.pybgs as bgs

print("OpenCV Version: {}".format(cv2.__version__))

## bgslibrary algorithms
algorithms = []
algorithms.append(bgs.FrameDifference)
algorithms.append(bgs.StaticFrameDifference)
algorithms.append(bgs.WeightedMovingMean)
algorithms.append(bgs.WeightedMovingVariance)
algorithms.append(bgs.AdaptiveBackgroundLearning)
algorithms.append(bgs.AdaptiveSelectiveBackgroundLearning)
algorithms.append(bgs.MixtureOfGaussianV2)
algorithms.append(bgs.KNN) # if opencv 3.x
algorithms.append(bgs.DPAdaptiveMedian)
algorithms.append(bgs.DPGrimsonGMM)
algorithms.append(bgs.DPZivkovicAGMM)
algorithms.append(bgs.DPMean)
algorithms.append(bgs.DPWrenGA)
algorithms.append(bgs.DPPratiMediod)
algorithms.append(bgs.DPEigenbackground)
algorithms.append(bgs.DPTexture)
algorithms.append(bgs.T2FGMM_UM)
algorithms.append(bgs.T2FGMM_UV)
algorithms.append(bgs.T2FMRF_UM)
algorithms.append(bgs.T2FMRF_UV)
algorithms.append(bgs.FuzzySugenoIntegral)
algorithms.append(bgs.FuzzyChoquetIntegral)
algorithms.append(bgs.LBP_MRF)
algorithms.append(bgs.PixelBasedAdaptiveSegmenter)
algorithms.append(bgs.KDE)
algorithms.append(bgs.IndependentMultimodal)
algorithms.append(bgs.SigmaDelta)
algorithms.append(bgs.SuBSENSE)
algorithms.append(bgs.LOBSTER)
algorithms.append(bgs.PAWCS)
algorithms.append(bgs.TwoPoints)
algorithms.append(bgs.ViBe)
algorithms.append(bgs.CodeBook)

algorithms.append(cv2.createBackgroundSubtractorMOG2)
algorithms.append(cv2.bgsegm.createBackgroundSubtractorMOG)
algorithms.append(cv2.bgsegm.createBackgroundSubtractorGMG)
algorithms.append(cv2.bgsegm.createBackgroundSubtractorCNT)
algorithms.append(cv2.bgsegm.createBackgroundSubtractorGSOC)
algorithms.append(cv2.createBackgroundSubtractorKNN)
algorithms.append(cv2.bgsegm.createBackgroundSubtractorLSBP)

video_file = "dataset/video01.mp4"

with open("demos/bgs/times.txt", "a+") as f:
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
				img_output = _algorithm.apply(frame)
			except:
				print(_algorithm.__class__.__name__ + " cant run")
				print(f.write(_algorithm.__class__.__name__ + ";error\n"))
				break
			# cv2.imshow('i', img_output)
			diff = (datetime.datetime.now() - start)
			if diff.total_seconds() > 300:
				f.write(_algorithm.__class__.__name__ + ";timeout\n")
				break
			if i == 200:
				diff = (datetime.datetime.now() - start)
				f.write(_algorithm.__class__.__name__ + ";" + str(diff.total_seconds()) + "\n")
				print('Write:', str(
					cv2.imwrite(
						'./demos/bgs/' + _algorithm.__class__.__name__ + '_' + str(diff.total_seconds()) + '.jpg',
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
