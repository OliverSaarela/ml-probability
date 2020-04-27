import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
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
        <div class="court__cell court__nml--right">18 ft. &times; 27 ft.<br/>(486 sq. ft.)</div>
        <div class="court__cell court__alley--bottom-left">
          <button>"prepare to be amazed"</button>
        </div>
        <div class="court__cell court__alley--bottom-right">39 ft. &times; 4.5ft (175.5 sq. ft.)</div>
      </div>
    </div>

      <label>Choose your fighter : </label>
      <select id = "player1" onchange="change_player1(this.value)">
        <option value = "Lad1">Lad1</option>
        <option value = "Lad2">Lad2</option>
        <option value = "Lad3">Lad3</option>
      </select>
      <br />
      <label>Choose your opponent : </label>
      <select id = "player2" onchange="change_player2(this.value)">
        <option value = "Lad1">Lad1</option>
        <option value = "Lad2">Lad2</option>
        <option value = "Lad3">Lad3</option>
      </select>
      <br />
      <label>Choose your arena : </label>
      <select id = "surface" onchange="change_surface(this.value)">
        <option value = "soft">soft</option>
        <option value = "hard">hard</option>
        <option value = "clay">clay</option>
        <option value = "grass">grass</option>
      </select>
    </body>
  );

}

export default App;
