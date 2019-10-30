import React from 'react';
import {createLogger,ConsoleFormattedStream} from 'browser-bunyan';

const logger = createLogger({
    name: 'textform-log',
    streams: [
        {
            level: 'info',
            stream: new ConsoleFormattedStream(),
            type: 'raw'
        }
    ]
});

class LogForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            res: '',
            status: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
        logger.debug(`State set to ${this.state.value}.`)
    }

    handleSubmit(event) {
        event.preventDefault();
        this.postLog(this.state.value).then(() => {
            if (this.state.status === 200) {
                logger.info(this.state.status)
            } else {
                logger.warn(this.state.status)
            }
        });
    }

    async postLog(body) {
        const response = await fetch(this.props.api, {
            method: 'POST',
            mode: 'cors',
            body: `${body}`,
            headers: {
                "Content-Type": "text/plain",
                // "Origin": "logbetter-web.nimbinatus.com"
            }
        }).then((res) => {
            this.setState({
                status: res.status,
            });
            return res.json()
        }).then((data) => {
            this.setState({
                res: data.body,
            });
        }).catch((e) => {
            logger.error(`I encountered an error: ${e}`)
        });
        return response;
    }

    render() {
        return (
            <div>
            <form>
                <label>
                    {this.props.labelName}
                    <input type="text" value={this.state.value} onChange={this.handleChange}/>
                </label>
                <button className="button-basic" type="submit" onClick={this.handleSubmit}>
                    {this.props.buttonName}
                </button>
            </form>
                <p>{this.state.res}</p>
            </div>
        );
    }
}

export default LogForm;