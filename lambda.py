import json
import base64
import boto3




def lambda_handler(event, context):
    regions = ['us-east-1','us-east-2','us-west-1','us-west-2','af-south-1','ap-east-1','ap-south-1','ap-northeast-3','ap-northeast-2','ap-southeast-1','ap-southeast-2','ap-northeast-1','ca-central-1','eu-central-1','eu-west-1','eu-west-2','eu-south-1','eu-west-3','eu-north-1','me-south-1','sa-east-1']
    #regions = ['ap-south-1','ap-northeast-1']
    for i in regions:
        try:
            client = boto3.client('guardduty', region_name=i)
            a = client.list_detectors(
            )
            detector= a['DetectorIds'][0]
           
            #Create new threat lists
            response = client.create_threat_intel_set(
            DetectorId=detector,
            Name='*',
            Format='TXT',
            Location='*',
            Activate=True,
            Tags={
                'Threatlist': '*'
            }
            )
            print('doing it')
        except Exception as e:
            print('Error on region',i,e)
            
        '''#list threat lists id
		listok = client.list_threat_intel_sets(
        DetectorId=detector
        )
        list_id = listok['ThreatIntelSetIds'][0]
            
        #Update threatlists
        response = client.update_threat_intel_set(
        DetectorId=detector,
        ThreatIntelSetId=list_id,
        Name='*',
        Location='*',
        Activate=True|False
        )'''
            
            
        #deletes all threatintel lists
        '''for j in list_id:    
            response = client.delete_threat_intel_set(
            DetectorId=detector,
            ThreatIntelSetId=j
            )'''

    key = {'Work':'Done'}
    return key    
