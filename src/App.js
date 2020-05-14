import React, { useState, useEffect } from 'react';
import './App.css';
import Button from '@material-ui/core/Button';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import Input from '@material-ui/core/Input';


function App() {


    var [statelist, setStatelist] = useState([]);

    var [player1, setPlayer1] = useState("Player1");
    var [player2, setPlayer2] = useState("player2");
    var [surface, setSurface] = useState("Hard");

    var respString;
    var [answer, setAnswer] = useState();


    //function for sending player and surface info to the server and receiving the matchwinner data
    function dopost() {

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

            .then(console.log("Fetching Winner..."))
            .then(setAnswer("Fetching Winner..."))

            .then(response => response.json().then(data => {
                respString = data.result
            }))

            .then(console.log(respString))
            .catch(error => console.log('error', error))

            .then(display)

    }

    //Function for getting the list of players from the server
    function doget() {
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json", "Access-Control-Allow-Headers");

        var requestOptions = {
            method: 'GET',
            headers: myHeaders,
        };

        fetch("http://localhost:8080", requestOptions)
            .then(response => response.json()
            .then(data => setStatelist(data)))
            .then(result => console.log(result))
            .catch(error => console.log('error', error))

    }

    //eventhandlers for updating the variables for calculating the winner
    const updateplayer1 = (event) => {
        setPlayer1(event.target.value);
    };

    const updateplayer2 = (event) => {
        setPlayer2(event.target.value);
    };

    const updateSurface = (event) => {
        setSurface(event.target.value);
    };



    function display() {
        setAnswer(respString)
    }
    function calculate() {
        dopost()
        display()
    }

    useEffect(() => {
        doget()
    },[]);


    return (

        <form class="court">

            <div class="court">
                <div class="court__grid">
                    <div class="court__cell court__alley--top-left">Tennismatch calcunator 3000</div>
                    <div class="court__cell court__alley--top-right">"Patent not pending"</div>
                    <div class="court__cell court__nml--left">Choose your players and fieldtype</div>
                    <div class="court__cell court__ad--left">


                        <Select input={<Input />} value={player1} onChange={updateplayer1}>
                            {statelist.map((name) => (
                                <MenuItem id="player1select" key={name} value={name}>{name}</MenuItem>
                            ))}
                        </Select>

                    </div>
                    <div class="court__cell court__ad--right">


                        <Select input={<Input />} value={surface} onChange={updateSurface}>
                            <MenuItem value="Clay">Clay</MenuItem>
                            <MenuItem value="Hard">Hard</MenuItem>
                            <MenuItem value="Grass">Grass</MenuItem>
                            <MenuItem value="Carpet">Carpet</MenuItem>
                        </Select>

                    </div>
                    <div class="court__cell court__dc--left">


                        <Select input={<Input />} value={player2} onChange={updateplayer2}>
                            {statelist.map((name) => (
                                <MenuItem id="player2select" key={name} value={name}>{name}</MenuItem>
                            ))}
                        </Select>

                    </div>
                    <div class="court__cell court__dc--right"><Button onClick={() => calculate()}>calculate Winner</Button></div>
                    <div class="court__cell court__nml--right">Carefully calculated answer:<br />{answer}</div>
                    <div class="court__cell court__alley--bottom-left"></div>
                    <div class="court__cell court__alley--bottom-right"></div>
                </div>
            </div>

        </form>
    );

};


export default App;
