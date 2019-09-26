import React from 'react';
import {createLogger,ConsoleFormattedStream} from 'browser-bunyan';

const logger = createLogger({
    name: 'jsonform-log',
    streams: [
        {
            level: 'info',
            stream: new ConsoleFormattedStream(),
            type: 'raw'
        }
    ]
});

class JsonLogForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            field1: '',
            field2: '',
            res: '',
            status: ''
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({
            ...this.state,
            [event.target.name]: event.target.value
        });
        logger.debug(`The values are ${this.state.field1} and ${this.state.field2}`);
    }

    handleSubmit(event) {
        event.preventDefault();
        let generalData = {
            key1: `${this.state.field1}`,
            key2: `${this.state.field2}`
        };
        this.postLog(generalData).then(() => {
            if (this.state.status === 200) {
                logger.info(this.state.status);
            } else {
                logger.warn(this.state.status);
            }
        });
    }

    async postLog(bodyData) {
        const response = await fetch(this.props.api, {
            method: 'POST',
            mode: 'cors',
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify(bodyData)
        }).then((res) => {
            this.setState({
                status: res.status
            });
            return res.json()
        }).then((data) => {
            this.setState({
                res: data,
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
                    Key 1
                    <input type="text" name="field1" value={this.state.field1} onChange={this.handleChange}/>
                </label>
                <label>
                    Key 2
                    <input type="text" name="field2" value={this.state.field2} onChange={this.handleChange}/>
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

export default JsonLogForm;