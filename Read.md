first build script and run it with directrunner locally
then it got success and run with DATAFLOWRUNNER

then uncomment templete_location 

and run it again so it built templete in provided path
_________________________________________________________________________________________
event when file with employee.csv into 001project

create cloud function with cloud storage and event type (creating/finilizing)

---------------------------------------
gcloud functions deploy trigger_dataflow \
  --runtime python39 \
  --trigger-topic file-upload-topic \
  --entry-point trigger_dataflow \
  --region us-central1 \
  --project just-camera-432415-h9

---------------------------------------------------

upload file

gsutil cp example.csv gs://001project/

check

gcloud functions logs read trigger_dataflow --region us-central1
 
 
