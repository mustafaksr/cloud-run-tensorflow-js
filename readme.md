# Cloud Run  Tensorflow js Simple Regression App
This demo's purpose is to deploy tensorflow js simple regression app to google cloud run from  [boilerplate version on glitch.me.](https://tensorflowjs-multiple-neuron-linear-regression-to-learn.glitch.me/)

## Files in repo:
* docker_app_deploy.sh: Automated bash file, to deploy the app into cloud run with docker image 
* no_docker_app_deploy.sh : Automated bash file, to deploy the app into cloud run without docker image
* traffic_test.sh : Automated traffic test bash file, it deploys new revision and split traffic between revision. And perform a traffic test.
## Steps:
In cloud shell:
1. clone repo: 
```
git clone https://github.com/mustafaksr/cloud-run-tensorflow-js.git
```
2. Deploy app into cloud run:
```
bash docker_app_deploy.sh
```
or
2. Deploy app into cloud run without docker image:
```
bash no_docker_app_deploy.sh
```

3. Deploy the app's new revision and perform traffic test:
Note: if the app deployed without docker, in the traffic_test.sh file(line 10) ,  you need to change  [--image "$TAG"] with [--source .] to run this file properly.
 
```
bash traffic_test.sh
```
4. Check results...

You can find html/css/js [files in here.](https://github.com/mustafaksr/Machine-Learning/tree/main/tensorflow.js/linear-regression) 
