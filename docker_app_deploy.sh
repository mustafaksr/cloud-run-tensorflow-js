#!/bin/bash
export PROJ=$GOOGLE_CLOUD_PROJECT 
export APP=tensorjs 
export PORT=8080
export REGION="us-central1"
export TAG="gcr.io/$PROJ/$APP"
echo "Enabling apis"
gcloud services enable cloudbuild.googleapis.com         \
                       containerregistry.googleapis.com  \
                       run.googleapis.com  

pip3 install -r requirements.txt
echo "App check!!!  from Web Preview - preview on port 8080 | to continue, you can press ctrl + c "
python3 main.py




export result=$(gcloud container images list --filter=tensorjs)
if [ -z "$result" ];then
    echo ""
    echo "submitting container"
    gcloud builds submit --tag $TAG
fi

gcloud container images list

echo " "
echo "docker run app check!!! from Web Preview - preview on port 8080 |to continue, you can press ctrl + c "
docker run -p $PORT:$PORT -e PORT=$PORT $TAG

echo ""
echo "Deploying app into cloud run"
gcloud run deploy "$APP"   \
  --image "$TAG"           \
  --platform "managed"     \
  --region "$REGION"       \
  --allow-unauthenticated

echo "App deployed into cloud run | retrieving app url:"

export APP=tensorjs 
export REGION="us-central1"
gcloud run services describe "$APP"  \
  --platform managed                \
  --region $REGION                  \
  --format "value(status.url)"

