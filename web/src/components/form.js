import React from 'react';

// import Button from './button';

class LogForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('This button was clicked!');
        event.preventDefault();
    }

    render() {
        return (
            <form>
                <label>
                    {this.props.labelName}
                    <input type="text" value={this.state.value} onChange={this.handleChange}/>
                </label>
                <button className="button-basic" type="submit" onClick={() => this.handleSubmit}>
                    {this.props.buttonName}
                </button>
            </form>
        );
    }
}

export default LogForm;