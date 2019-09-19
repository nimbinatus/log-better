import React from 'react';

class Button extends React.Component {
    // constructor(props) {
    //     super(props);
        // this.handleSubmit = this.handleSubmit().bind(this);
    // }

    handleSubmit(event) {
        alert('This button was clicked!');
        event.preventDefault();
    }

    render(props) {
        return (
            <button className="button-basic" type="submit" onClick={() => this.handleSubmit}>
                {this.props.value}
            </button>
        );
    }
}

export default Button;