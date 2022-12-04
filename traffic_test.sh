#!/bin/bash
export PROJ=$GOOGLE_CLOUD_PROJECT 
export APP=tensorjs 
export PORT=8080
export REGION="us-central1"
export TAG="gcr.io/$PROJ/$APP"
echo "to test trafic-split, revision 2 deploying into cloud run with same docker image"
#note: if app deployed without docker, you need to change  --image "$TAG" with --source . to run this file properly.
gcloud run deploy "$APP"   \
  --image "$TAG"           \
  --platform "managed"     \
  --region "$REGION"       \
  --allow-unauthenticated

gcloud run revisions list --region us-central1

echo "please enter revision ids "
read -p "enter revision 1 id : " rev1
read -p "enter revision 2 id : " rev2
echo "please enter revision split rates "
read -p "enter split traffic rate for revision 1 : " rev1split
read -p "enter split traffic rate for revision 2 : " rev2split

gcloud run services update-traffic $APP \
    --to-revisions=$rev1=$rev1split,$rev2=$rev2split \
    --region us-central1

export URL=$(gcloud run services describe "$APP"  \
  --platform managed                \
  --region $REGION                  \
  --format "value(status.url)")

echo "test starting"
hey -q 1000 -c 200 -z 30s $URL

echo "test finished."
echo "you can check test results from cloud run > service name > metrics"
