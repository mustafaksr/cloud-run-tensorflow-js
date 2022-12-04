# cloud run  tensorflow js simple regression app
This demo's purpose is deploying tensorflow js simple regression app to google cloud run from  [boilerplate version on glitch.me.](https://tensorflowjs-multiple-neuron-linear-regression-to-learn.glitch.me/)

## Files in repo:
* docker_app_deploy.sh: Automated bash file, to deploy app into cloud run with docker image 
* no_docker_app_deploy.sh : Automated bash file, to deploy app into cloud run without docker image
* traffic_test.sh : Automated traffic test bash file, it deploys new revision and split trafics between revision. And perfom traffic test.
## Steps:
in cloud shell:
1. clone repo: 
```
git clone
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

3. Deploy app's new revision and perfom traffic test:
Note: if app deployed without docker, in traffic_test.sh file(line 10) ,  you need to change  [--image "$TAG"] with [--source .] to run this file properly.
 
```
bash traffic_test.sh
```
4. Check results...

You can find html/css/js [files in here.](https://github.com/mustafaksr/Machine-Learning/tree/main/tensorflow.js/linear-regression) 