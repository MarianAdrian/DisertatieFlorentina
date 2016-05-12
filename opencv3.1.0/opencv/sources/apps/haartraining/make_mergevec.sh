/c/MinGW/bin/g++.exe `pkg-config --libs --cflags opencv` -I. -o mergevec mergevec.cpp\
  cvboost.cpp cvcommon.cpp cvsamples.cpp cvhaarclassifier.cpp\
  cvhaartraining.cpp\
  -lopencv_core -lopencv_calib3d -lopencv_imgproc -lopencv_highgui -lopencv_objdetect