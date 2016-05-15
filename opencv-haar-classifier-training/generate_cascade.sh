opencv_traincascade -data classifier -vec merged.vec -bg negatives.txt\
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000\
  -numNeg 600 -w 88 -h 40 -mode ALL -precalcValBufSize 1024\
  -precalcIdxBufSize 1024