# Log Better: Workshop Resources

[![Coverage Status](https://coveralls.io/repos/github/nimbinatus/log-better/badge.svg?branch=master)](https://coveralls.io/github/nimbinatus/log-better?branch=master)

This repo holds the source code and sample playground for the Log Better workshop. A list of where I've presented this workshop can be found further down in this README.

## Running locally

If you don't want to use the main playground at https://logbetter.nimbinatus.com (or if it's not up, which is always possible), you can run this system on your local machine. Right now, all you need is Python 3, Node, and a command line.

1. Clone or download the repo.
1. Set up and activate a Python virtual environment.
1. Go into the `api` directory.
1. Run `pip install -r requirements.txt`.
1. Go into the `web` directory.
1. Run your favorite package install command for Node. I use Yarn. I also set up a Node virtual environment because I like my systems clean (nvm, for the curious). It's up to you.
1. Go to the `api`.
1. Run `python -m api`.
1. In a new terminal, go into the `web` directory.
1. Run `npm start`
1. The start script will open your browser to the right page automatically. Open the developer tools and try entering in a line of logs.

You can also use the API standalone, if you would prefer. 

### Local testing

To run local tests, simply run `python tests/test_api.py` from the root of the repo on your local machine.

## Nitty Gritty: Conference Details

### Abstract

Sure, we’re told actionable, parsable logs are important. But what does that mean? How has that guidance changed? Experiment with different log formats, see how machines parse logs, and discuss best practices for logging. After all, a good log helps the next person, and that might even be you.

### Description

Logging is deceptively simple. You import a library, pass strings to it, and BAM you have logs. However, do you know how to write machine-parsable logs? Do you know all of the different log levels and why you need them? What does current logging best practices look like? Logging is an underutilized tool in the developer’s toolbox, and it is often misunderstood as just another unnecessary debugging tool. In reality, logging is a boon to the people who will be working on a system later down the line, and making fantastic logs really is a team sport.

For the hands-on portions of this workshop, we’ll learn and practice writing good logs, and we’ll view our practice logs. We’ll see how different logs appear in a parsing system, and we’ll experiment with different formats. Finally, we’ll see how to translate those best practices into code with a basic hello-world Python application. You just need a laptop, a terminal of some sort (anything from basic terminal to Powershell is fine), and the ability to connect to the conference wifi.

### Conference List

DeveloperWeek Austin 2019