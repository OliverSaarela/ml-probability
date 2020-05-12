import React, { Component, useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';

function App() {

  var respString = '';

  var player1 = 'Nadal R';
  var player2 = 'Federer R';
  var surface = 'Clay';

  function testprint() {
    console.log(respString);
  }




  const dopost = (e) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json", "Access-Control-Allow-Headers");

    var raw = JSON.stringify({
      'player1': player1,
      'player2': player2,
      'surface': surface,
    });

    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
    };

    fetch("http://localhost:8080", requestOptions)
      .then(response => response.text())
      .then(result => respString = respString.concat(result))
      .catch(error => console.log('error', error));
    };

    const doget = (e) => {
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json", "Access-Control-Allow-Headers");

      var requestOptions = {
        method: 'GET',
        headers: myHeaders,
      };

      fetch("http://localhost:8080", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

      };

    return (



      <form class="court">

      <div class="court">
        <div class="court__grid">
          <div class="court__cell court__alley--top-left">

            <Typography variant='p' color='inherit'>{"Open console to see whats going on"}</Typography>

          </div>
          <div class="court__cell court__alley--top-right">39 ft. &times; 4.5ft (175.5 sq. ft.)</div>
          <div class="court__cell court__nml--left">"No Man's Land"</div>
          <div class="court__cell court__ad--left">

            <Select>
              <MenuItem value="lad">lad</MenuItem>
              <MenuItem value="lass">lass</MenuItem>
            </Select>

          </div>
          <div class="court__cell court__ad--right">21 ft. &times; 13.5 ft.<br/>(283.5 sq. ft.)</div>
          <div class="court__cell court__dc--left"><TextField>Player2</TextField></div>
          <div class="court__cell court__dc--right"><Button onClick={testprint}>testprint</Button></div>
          <div class="court__cell court__nml--right">answer here<br/></div>
          <div class="court__cell court__alley--bottom-left">
            <Button onClick={dopost}>Prepare to be amazed</Button>
          </div>
          <div class="court__cell court__alley--bottom-right"><Button onClick={doget}>Prepare to be amazed</Button></div>
        </div>
      </div>

      </form>
    );

    };


export default App;
