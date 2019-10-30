import React from 'react';
import LogForm from "./components/form";
import JsonLogForm from "./components/jsonform";
import './App.css';

function App() {
    return (
        <div className="App">
            <h2>Plain Text Log Submission</h2>
            <p>Want to send your data via curl instead? Just post a plain-text message to the API at DATA/api.</p>
            <LogForm labelName='Prototype logline' buttonName='Send proto-log' api='https://logbetter.nimbinatus.com/basic'/>
            <h2>JSON Log Submission</h2>
            <JsonLogForm labelName='Prototype JSON' buttonName='Submit proto-json' api='https://logbetter.nimbinatus.com/api'/>

        </div>
    );
}

export default App;
