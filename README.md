# DNS-STRESS

DNS-STRESS is a performance testing tool designed to stress test DNS servers by simulating high traffic. It allows network administrators and security professionals to evaluate how DNS servers perform under heavy load conditions, helping identify potential vulnerabilities, bottlenecks, and misconfigurations. This tool supports both UDP and TCP protocols, enabling you to test a variety of real-world scenarios and gain insight into how a DNS server behaves under stress.

## Features
- High Traffic Simulation: Simulate and stress test DNS servers by sending a large volume of queries to assess their performance under high traffic.
- Multiple Protocol Support: Support for both UDP and TCP protocols, allowing testing of DNS servers under different types of communication.
- Customizable Query Types: Choose from a variety of DNS query types such as A, AAAA, MX, TXT, and more to simulate realistic DNS queries.
- Distributed Load Simulation: Simulate traffic originating from multiple source IP addresses, replicating real-world attack patterns like DDoS.
- Performance Metrics: Collect and analyze detailed performance metrics during the test to evaluate DNS server efficiency and capacity.
- Configuration Flexibility: Modify the tool’s configuration to fit specific testing needs such as rate limiting, query timeouts, and retry attempts.

## Table of Contents
- Features
- Installation
- Usage
- Configuration
- Contributing
- License

## Installation

To begin using DNS-STRESS, you need to install the necessary dependencies and set up the environment. Follow these instructions for easy installation.

### Prerequisites
- Python 3.x or higher is required.
- pip (Python package installer) to install dependencies.

### Steps
1. **Clone the Repository:**
   First, clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/lothbrok9/DNS-STRESS.git
   ```

2. **Navigate to the Project Directory:**
   Change to the directory where the project is located:
   ```bash
   cd DNS-STRESS
   ```

3. **Install Required Dependencies:**
   Install the required Python libraries and dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   This will install all the necessary libraries to run the script.

4. **Verify the Installation:**
   Once installation is complete, verify that everything is set up correctly by running the help command:
   ```bash
   python dns_stress.py --help
   ```
   This should output the available commands and options, confirming that the tool is ready to use.

## Usage

After installation, you can start using DNS-STRESS to stress test DNS servers. Below are the available command-line arguments and examples of how to use them.

### Command-Line Arguments
- `--target <DNS_SERVER_IP>`: The IP address of the DNS server you want to test.
- `--queries <NUMBER_OF_QUERIES>`: The number of DNS queries you want to send during the stress test.
- `--protocol <UDP|TCP>`: The protocol to use for the test. Options are UDP or TCP. Default is UDP.
- `--query-type <QUERY_TYPE>`: The type of DNS query to use, such as A, AAAA, MX, TXT, etc. Default is A.
- `--rate <RATE>`: The rate at which queries are sent, measured in queries per second. Default is 1.
- `--timeout <TIMEOUT>`: The timeout period in seconds for each query. Default is 5 seconds.

#### Advanced Stress Test
Send 10,000 DNS queries to the target DNS server (8.8.8.8) with MX record queries using TCP protocol, at a rate of 100 queries per second:
```bash
python dns_stress.py --target 8.8.8.8 --queries 10000 --protocol TCP --query-type MX --rate 100 --timeout 10
```
### Performance Metrics

During the test, DNS-STRESS will output the following performance metrics:
- Queries Sent: The total number of queries sent during the test.
- Success Rate: The percentage of successfully received DNS responses.
- Error Rate: The percentage of DNS queries that failed (timeout, server errors, etc.).
- Average Response Time: The average response time for DNS queries.
- Max Response Time: The maximum response time for any single query.

## Configuration

You can customize the behavior of DNS-STRESS by modifying the `config.json` configuration file. Here, you can set default values for query types, protocols, timeout settings, and more.

### Example `config.json`
```json
{
  "default_query_type": "A",
  "default_protocol": "UDP",
  "timeout": 5,
  "retry_attempts": 3,
  "default_rate": 1
}
```
- `default_query_type`: Default DNS query type to use (e.g., A, AAAA, MX).
- `default_protocol`: Default protocol to use for queries (UDP or TCP).
- `timeout`: Default timeout for each query in seconds.
- `retry_attempts`: The number of retry attempts for failed queries.
- `default_rate`: Default number of queries per second.

Modify this file to match your testing needs.

## Contributing

We welcome contributions to improve DNS-STRESS. If you find any issues or have suggestions for new features, feel free to fork the repository and submit a pull request.

### How to Contribute
1. **Fork the Repository:** Click the “Fork” button at the top right of this repository.
2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/<your-username>/DNS-STRESS.git
   cd DNS-STRESS
   ```

3. **Create a New Branch:**
   ```bash
   git checkout -b feature-name
   ```

4. **Make Changes:** Implement your feature or bug fix.
5. **Commit Changes:**
   ```bash
   git commit -am "Add feature"
   ```

6. **Push Changes:**
   ```bash
   git push origin feature-name
   ```

7. **Open a Pull Request:** Submit a pull request to the main branch for review.

Please ensure your code adheres to the existing style and that you write tests for any new features or changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.