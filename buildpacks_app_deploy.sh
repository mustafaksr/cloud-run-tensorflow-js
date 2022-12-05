#!/bin/bash
export PROJ=$GOOGLE_CLOUD_PROJECT 
export APP=tensorjs 
export PORT=8080
export REGION="us-central1"

#This tells the buildback system how to run your app in the auto-generated container. 
cat > Procfile <<EOF
web: python3 main.py
EOF


echo "Enabling apis"
gcloud services enable cloudbuild.googleapis.com         \
                       containerregistry.googleapis.com  \
                       run.googleapis.com  

pip3 install -r requirements.txt
echo "App check!!!  from Web Preview - preview on port 8080 | to continue, you can press ctrl + c "
python3 main.py

echo "Deploying app into cloud run"
gcloud run deploy "$APP"-nodocker   \
  --source .           \
  --platform "managed"     \
  --region "$REGION"       \
  --allow-unauthenticated

export APP=tensorjs 
export REGION="us-central1"
echo "App deployed into cloud run | retrieving app url:"
gcloud run services describe "$APP"-nodocker  \
  --platform managed                \
  --region $REGION                  \
  --format "value(status.url)"
