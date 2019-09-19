import React from 'react';
import LogForm from "./components/form";
import './App.css';

function App() {
    return (
        <div className="App">
            <h2>Basic Log Submission</h2>
            <LogForm labelName='Prototype logline' buttonName='Send proto-log'/>
            <h2>JSON Log Submission</h2>
            <LogForm labelName='Prototype JSON' buttonName='Submit proto-json'/>
        </div>
    );
}

export default App;
