import React from 'react';
import {
    BrowserRouter as Router,
    Route,
    Switch
} from 'react-router-dom';
import LogForm from "./components/form";
import JsonLogForm from "./components/jsonform";
import './App.css';

export default function App() {
    return (
        <Router>
            <Switch>
                <Route path="/scenario">
                    <Scenario/>
                </Route>
                <Route path="/">
                    <Home/>
                </Route>
            </Switch>
        </Router>
    )
}

function Home() {
    return (
        <div className="App">
            <img src="head.png" alt="Log Better" className="headImage"/>
            <h1>Plain Text Log Submission</h1>
            <LogForm labelName='Prototype logline' buttonName='Send proto-log' api='https://logbetter.nimbinatus.com/basic'/>
            <p>Want to send your data via curl instead? Just post your logs to the API. You can send a plain text
                message to https://logbetter.nimbinatus.com/basic like this:</p>
            <code>{`
            curl http://logbetter.nimbinatus.com/basic -X POST -H "Content-Type: text/plain" -A "curl-submit"
            -d "hello world"
            `}</code>
            <h1>JSON Log Submission</h1>
            <JsonLogForm labelName='Prototype JSON' buttonName='Submit proto-json' api='https://logbetter.nimbinatus.com/api'/>
            <p>If you want to send a structured log line as JSON, send it to https://logbetter.nimbinatus.com/api like
                this:</p>
            <code>{`
            curl http://logbetter.nimbinatus.com/api -X POST -H "Content-Type: application/json" -A "curl-submit" -d
            '{"key 1":"value 1", "key 2":"value 2"}'
            `}</code>
        </div>
    );
}

function Scenario() {
    return (
        <div className="App">
            <img src="head.png" alt="Log Better" className="headImage"/>
            <h1>A Scenario</h1>
            <p>
                You have a legacy application that has not been updated in 5 years. The system is running Python 2,
                which is sunsetting in January 2020. The system recently had its first incident in nearly 4 years, and
                your team was among the group that had to bring it back up. The logs that you received were not very
                helpful, and bringing the production instance back up ended up being a lot of trial and error.
            </p>
            <p>
                Management has decided all applications must be on Python 3 by the end of code freeze in January 2020.
                Your team has been tasked with updating the application to use Python 3. It's the ideal time to add
                proper logging. How would you go about planning and executing that logging update?
            </p>
        </div>
    )
}