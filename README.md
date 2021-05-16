# untsrproject
Senior Project 2020


How to send video to S3:
aws s3 cp vid.mp4 s3://blacktheory/testVid.mp4

How to start face search:
aws rekognition start-face-search \
    --video "S3Object={Bucket=blacktheory,Name=testVid.mp4}" \
    --collection-id my-faces

How to get face search results:
aws rekognition get-face-search \
    --job-id 4f5f48956110967fd0e7ca3083ed626721598b4008f93229a4e4ae781d27d875


How to convert h264 format to mp4:
MP4Box -add vid.h264 vid.mp4
rm video.h264		//remove to save space
rm vid.mp4
