from flask import Flask
import os
import random

app = Flask(__name__)  # Create a Flask object.
PORT = os.environ.get('PORT')  # Get PORT setting from the environment.

# The app.route decorator routes any GET requests sent to the root path
# to this function, which responds with a 'Hello world!' HTML document.   
@app.route('/', methods=['GET'])
def tensorjs_app():
    html = """
    <!DOCTYPE html><html lang="en">  <head>    <title>Hello World - TensorFlow.js</title>    <style type="text/css">		    body {		  font-family: helvetica, arial, sans-serif;		  margin: 2em;		}		h2 {		  font-style: italic;		  color: #ff6f00;		}    </style>        <meta charset="utf-8" />    <meta http-equiv="X-UA-Compatible" content="IE=edge" />    <meta name="viewport" content="width=device-width, initial-scale=1" />     </head>  <body>    <h2 id="h12">      TensorFlow.js Multiple Neuron Non Linear Regression to learn y = 2*x+4    </h2>    <div>      wanna enter inputs?: <input type="checkbox" id="check" />      <p>separate inputs with "," comma like: 1,2,3... etc</p>    </div>    <div class="slidecontainer">      X: <input type="text" id="input" />      <p id="intext"></p>    </div>    <p id="outputtest"></p>    <div class="slidecontainer">      y: <input type="text" id="output" />      <p id="outtext"></p>    </div>    <p id="test">epoch: 50</p>    <div class="slidecontainer">      <input        type="range"        min="10"        max="500"        value="50"        class="slider"        id="epoch"      />    </div>    <p id="batch-size">batch size: 32</p>    <div class="slidecontainer">      <input        type="range"        min="2"        max="128"        value="32"        class="slider"        id="slider2"      />    </div>    <div id="div2">      <p id="text-output">click run for outputs.</p>      <button type="button" id="run">Run</button>      <p>MAKE PREDICTION</p>      <p>before training(run) enter X_test values for prediction</p>      <p id="info"></p>    </div>    <div id="myCanvas" width="500" height="400"></div>    <p id="in1"></p>    <p id="out1"></p>    <div class="slidecontainer">      X test:      <input type="text" id="predict" value="enter value for prediction" />    </div>    <p id="inTest"></p>    <div>      <p id="predictText">predictions: ...</p>    </div>    <div>      <p id="expectedText">expected results: ...</p>    </div>    <script      src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@3.11.0/dist/tf.min.js"      type="text/javascript"    ></script>    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-vis"></script>    <script >     const LEARNING_RATE = 0.001;const OPTIMIZER = tf.train.sgd(LEARNING_RATE);var slider = document.getElementById("epoch");var output = document.getElementById("test");slider.oninput = function () {  output.innerHTML = `epoch: ${this.value}`;};var slider2 = document.getElementById("slider2");var output2 = document.getElementById("batch-size");slider2.oninput = function () {  output2.innerHTML = `batch size: ${this.value}`;};var elmOutput = document.getElementById("output");var elmInput = document.getElementById("input");var inputhtml = document.getElementById("intext");var outputhtml = document.getElementById("outtext");elmInput.oninput = function () {  inputhtml.innerHTML = this.value;};var head = document.getElementById("h12");elmOutput.oninput = function () {  outputhtml.innerHTML = this.value;};var predInput = document.getElementById("predict");var predhtml = document.getElementById("inTest");predInput.oninput = function () {  predhtml.innerHTML = this.value;};function trainall() {  var INPUTS2 = [];  for (let tt in inputhtml.innerText.split(",")) {    INPUTS2.push(parseFloat(inputhtml.innerText.split(",")[tt]));  }  var OUTPUTS2 = [];  for (let tt in outputhtml.innerText.split(",")) {    OUTPUTS2.push(parseFloat(outputhtml.innerText.split(",")[tt]));  }  var TestINPUTS = [];  for (let yy in predhtml.innerText.split(",")) {    TestINPUTS.push(parseFloat(predhtml.innerText.split(",")[yy]));  }  var isCheck = document.getElementById("check");  if (isCheck.checked != true) {    var INPUTS = [];    var OUTPUTS = [];    for (let n = -20; n <= 20; n++) {      INPUTS.push(n);      OUTPUTS.push(2 * n + 4);    }  } else {    [INPUTS, OUTPUTS] = [INPUTS2, OUTPUTS2];  }  const INPUTS_TENSOR = tf.tensor1d(INPUTS);  const OUTPUTS_TENSOR = tf.tensor1d(OUTPUTS);    var model = tf.sequential();  model.add(    tf.layers.dense({ inputShape: [1], units: 25, activation: "relu" })  );  model.add(tf.layers.dense({ units: 15, activation: "relu" }));  model.add(tf.layers.dense({ units: 1, activation: "linear" }));  model.summary();  const LEARNING_RATE = 0.0001;  const OPTIMIZER = tf.train.sgd(LEARNING_RATE);  train();  async function train() {    model.compile({      optimizer: OPTIMIZER,      loss: "meanSquaredError",      metrics: ["mse","mae"],    });
    //
    // Finally do the training itself
    let results = await model.fit(INPUTS_TENSOR, OUTPUTS_TENSOR, {
      shuffle: false, // Ensure data is shuffled again before using each epoch.
      batchSize: parseInt(document.getElementById("slider2").value),
      epochs: parseInt(document.getElementById("epoch").value), // Go over the data 80 times!
      callbacks: { onEpochEnd: logProgress },
    });
    // Go over the data 80 times!

    // Update the current slider value (each time you drag the slider handle)

    OUTPUTS_TENSOR.dispose();
    // FEATURE_RESULTS.NORMALIZED_VALUES.dispose();

    console.log(
      "Final Average error loss: " +
        Math.sqrt(results.history.loss[results.history.loss.length - 1])
    );

    // Once trained we can evaluate the model.
    evaluate();

    var expected_result = [];
    var x_y_list = [];
    var mae = [];
    var mse = [];
    for (let i = 0; results.history.loss.length > i; i++) {
      var d = parseFloat(results.history.loss[i].toFixed(2));
      expected_result[i] = d;
      x_y_list[i] = i;

      var mse2 = parseFloat(results.history.mse[i].toFixed(2));
      mse[i] = mse2;
      var mae2 = parseFloat(results.history.mae[i].toFixed(2));
      mae[i] = mae2;
    }

    // // var result = {};
    // // x_y_list.forEach((key, i) => result[key] = expected_result[i]);
    // // console.log(result);

    const x_history = Array(results.history.loss.length).fill("x");
    const y_history = Array(results.history.loss.length).fill("y");

    var result = [];
    x_y_list.forEach(
      (key, i) =>
        (result[key] = JSON.parse(`{"${x_history[i]}":${x_y_list[i]},"${y_history[i]}":${mse[i]}}`))
    );
    console.log(result);

    var result2 = [];
    x_y_list.forEach(
      (key, i) =>
        (result2[key] = JSON.parse(
          `{"${x_history[i]}":${x_y_list[i]},"${y_history[i]}":${mae[i]}}`
        ))
    );

    // #visualization

    const series1 = result;
    const series2 = result2;
    console.log(result2);
    const series = ["MSE", "MAE"];
    const data = { values: [series1, series2], series };
    const surface = document.getElementById("myCanvas");
    tfvis.render.linechart(surface, data);
    console.log(INPUTS);
    console.log(OUTPUTS);
    var printIn = document.getElementById("in1");
    var printOut = document.getElementById("out1");
    printIn.innerText = `inputs: ${INPUTS}`;
    printOut.innerText = `inputs: ${OUTPUTS}`;
    predict();
  }
 function evaluate() {    tf.tidy(function () {      let newInput =        tf.tensor1d([7]);      let output = model.predict(newInput);      output.print();    });  }  console.log(TestINPUTS);  function predict() {    tf.tidy(function () {      let output = model.predict(tf.tensor1d(TestINPUTS));      output.print();      var predtext = document.getElementById("predictText");      predtext.innerText = `predictions: ${output}`;      let AA = tf.add(        tf.scalar(4),        tf.mul(tf.scalar(2), tf.tensor1d(TestINPUTS))      );      AA.print();      var exptext = document.getElementById("expectedText");      exptext.innerText = `expected results: ${AA}`;    });    model.dispose();  }}function logProgress(epoch, logs) {  console.log("Data for epoch " + epoch, Math.sqrt(logs.loss));  const element = document.getElementById("text-output");  element.innerText = `epoch: ${epoch + 1}, loss(mse): ${logs.loss.toFixed(    2  )} `;  if (epoch == 70) {    OPTIMIZER.setLearningRate(LEARNING_RATE / 2);  }}let runb = document.getElementById("run");runb.addEventListener("click", myFun7);function myFun7() {  trainall();}      </script>  </body></html>
    """
    return html


# This code ensures that your Flask app is started and listens for
# incoming connections on the local interface and port 8080.
if __name__ == '__main__':
    print("PORT is "+str(PORT))
    app.run(host='0.0.0.0', port=PORT)
