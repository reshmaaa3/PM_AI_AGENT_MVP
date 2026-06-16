# PM AI AGENT MVP

## Overview

PM AI AGENT MVP is an AI-powered Process Mining application built with Python and Streamlit. The system automatically validates event logs, analyzes process data, identifies bottlenecks, and provides actionable insights for business process improvement.

This project demonstrates the integration of Process Mining concepts with AI Agent architecture to support data-driven process analysis and decision-making.

## Features

### Current Features (Version 1)
* Event Log Validation
* CSV File Upload
* Process Summary Dashboard
* Case Count Analysis
* Event Count Analysis
* Activity Analysis
* Missing Value Detection
* Interactive Streamlit Interface

### Planned Features
* Bottleneck Analysis Agent
* Process Discovery using PM4Py
* Conformance Checking
* AI-Powered Process Recommendations
* Predictive Process Analytics
* Multi-Agent Process Mining Architecture

## Technology Stack
* Python
* Streamlit
* Pandas
* Process Mining Concepts
* AI Agent Architecture
## Project Structure


PM_AI_AGENT_MVP
│
├── data/
│   └── sample_event_log.csv
│
├── outputs/
│
├── tools/
│   └── data_validation_tool.py
│
├── app.py
├── requirements.txt
└── .env


## Installation

Clone the repository:

```bash
git clone https://github.com/reshmaaa3/PM_AI_AGENT_MVP.git
cd PM_AI_AGENT_MVP
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

Or:

```bash
py -3.13 -m streamlit run app.py
```

---

## Sample Dataset

A sample event log is included for testing and demonstration purposes.

Example activities:

* Register Request
* Initial Assessment
* Inspect Device
* Repair Device
* Quality Check
* Close Case

## Future Roadmap

### Version 2

* Bottleneck Detection Agent
* Process Performance Analytics

### Version 3

* PM4Py Process Discovery
* Process Visualization

### Version 4

* AI Recommendation Agent
* LLM-Based Process Insights

### Version 5

* Multi-Agent Process Mining Platform

## Author

Uma Venkata Sathya Reshma Bodapati

MSc Information Technology (Business)
Heriot-Watt University Dubai

## License

This project is licensed under the MIT License.
