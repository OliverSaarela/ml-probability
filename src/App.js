import React, { Component, useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';


function App() {


  const [stringy, setValues] = useState( {
  responseString: '',
});

  const dopost = (e) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json", "Access-Control-Allow-Headers");

    var raw = JSON.stringify({
      'player1': 'Nadal R',
      'player2': 'Federer R',
      'surface': 'Clay',
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
    };

    fetch("http://localhost:8080", requestOptions)
      .then(response => response.json())
      .then(result => console.log(result))


      .then(response => stringy.setValues({responseString: response}))

      .catch(error => console.log('error', error));




    };

    return (

      <body>
      <div class="court">
        <div class="court__grid">
          <div class="court__cell court__alley--top-left">Doubles Alley</div>
          <div class="court__cell court__alley--top-right">39 ft. &times; 4.5ft (175.5 sq. ft.)</div>
          <div class="court__cell court__nml--left">"No Man's Land"</div>
          <div class="court__cell court__ad--left">Ad Court<br />Left Service Box</div>
          <div class="court__cell court__ad--right">21 ft. &times; 13.5 ft.<br/>(283.5 sq. ft.)</div>
          <div class="court__cell court__dc--left">Deuce Court<br />Left Service Box </div>
          <div class="court__cell court__dc--right">21 ft. &times; 13.5 ft.<br/>(283.5 sq. ft.)</div>
          <div class="court__cell court__nml--right">answer here<br/>{stringy.responseString}</div>
          <div class="court__cell court__alley--bottom-left">
            <button onClick={dopost}>"prepare to be amazed"</button>



          </div>
          <div class="court__cell court__alley--bottom-right">39 ft. &times; 4.5ft (175.5 sq. ft.)</div>
        </div>
      </div>
      </body>
    );

    };



export default App;
