from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "just-camera-432415-h9"

    template_path = "gs://newpipeline001/templates_csvbq/dataflow_template"

    template_body = {
    "jobName": "bq-load-csv",  # Provide a unique name for the job
    "parameters": {
        
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
