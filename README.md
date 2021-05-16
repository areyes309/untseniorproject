# untsrproject
Senior Project 2020


gst-launch-1.0 -v v4l2src do-timestamp=TRUE device=/dev/video0 ! videoconvert ! video/x-raw,format=I420,width=640,height=480,framerate=30/1 ! omxh264enc periodicty-idr=45 inline-header=FALSE ! h264parse ! video/x-h264,stream-format=avc,alignment=au ! kvssink stream-name=test access-key="AKIASCQU5NZRFHAD2G6A" secret-key="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"
export AWS_ACCESS_KEY_ID=AKIASCQU5NZRFHAD2G6A
export AWS_SECRET_ACCESS_KEY=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
export PATH=/home/pi/amazon-kinesis-video-streams-producer-sdk-cpp/kinesis-video-native-build/downloads/local/bin:$PATH
export PATH=~/.local/bin:$PATH
export GST_PLUGIN_PATH=/home/pi/amazon-kinesis-video-streams-producer-sdk-cpp/kinesis-video-native-build/downloads/local/lib:$GST_PLUGIN_PATH
export LD_LIBRARY_PATH=/home/pi/amazon-kinesis-video-streams-producer-sdk-cpp/kinesis-video-native-build/downloads/local/lib:$LD_LIBRARY_PATH
AWS_ACCESS_KEY_ID=AKIASCQU5NZRFHAD2G6A AWS_SECRET_ACCESS_KEY=mtZuLotRFRewJzemfSys3X/3H+gWT+m5rM+lQP2m sudo ./kinesis_video_gstreamer_sample_app blackTheoryVideo -w 1280 -h 720 -f 30 -b 2500


gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=I420,width=640,height=480 ! omxh264enc periodicty-idr=45 target-bitrate=512000 control-rate=2 inline-header=FALSE ! h264parse ! video/x-h264,streamformat=avc,alignment=au,profile=baseline ! kvssink stream-name="blackTheoryVideo" access-key="AKIASCQU5NZRFHAD2G6A" secret-key="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" aws-region="us-west-2"

aws rekognition index-faces --collection-id my-faces --image '{"S3Object":{"Bucket":"blacktheory","Name":"fadi.jpg"}}' --external-image-id Fadi

aws rekognition cre=ate-stream-processor --input '{"KinesisVideoStream":{"Arn":"arn:aws:kinesisvideo:us-west-2:142851534434:stream/blackTheoryVideo/1575237859818"}}' --name store-processor --role-arn arn:aws:iam::142851534434:role/AmazonRekognitionServiceRole --stream-processor-output '{"KinesisDataStream":{"Arn":"arn:aws:kinesis:us-west-2:142851534434:stream/blackTheoryData"}}' --settings '{"FaceSearch":{"CollectionId":"my-faces", "FaceMatchThreshold": 85.5}}'

aws rekognition start-stream-processor --name store-processor

"StreamProcessorArn": "arn:aws:rekognition:us-west-2:142851534434:streamprocessor/store-processor"

aws rekognition list-faces \
    --collection-id my-faces


Refer to SQL Queries with source as: SOURCE_SQL_STREAM_001

arn:aws:kinesisvideo:us-west-2:142851534434:stream/blackTheoryVideo/1581277690755

arn:aws:kinesis:us-west-2:142851534434:stream/blackTheory 

 arn:aws:firehose:us-west-2:142851534434:deliverystream/blackTheoryFirehose

arn:aws:iam::142851534434:role/analysisRole


aws rekognition start-label-detection --video "S3Object={Bucket=bucketname,Name=videofile}" \
--notification-channel "SNSTopicArn=TopicARN,RoleArn=RoleARN" \
--region us-west-2


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
