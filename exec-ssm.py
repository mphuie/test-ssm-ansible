import boto3
import json

session = boto3.session.Session(profile_name="212027156525")
ssm_client = session.client("ssm")


response = ssm_client.send_command(
    InstanceIds=["i-0477794a77179ce00"],
    DocumentName="AWS-ApplyAnsiblePlaybooks",
    DocumentVersion="$LATEST",
    Parameters={
        "SourceType": ["GitHub"],
        "SourceInfo": [json.dumps({"owner": "mphuie", "repository": "test-ssm-ansible"})],
        "InstallDependencies": ["True"],
        "PlaybookFile": ["hello-world-playbook.yml"]
    },
)

print(response)
