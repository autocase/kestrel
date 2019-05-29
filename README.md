# Kestrel
A falcon boilerplate

# Requirements
Docker

# Installation
1. Clone this repo
2. Open up your terminal/powershell and navigate to the project folder.
3. Run Docker Compose to start the VM
`docker-compose up -d`
4. Go to `http://localhost`!


# Testing
Some sample tests have been written in PyTest, running them is as simple as typing `pytest` in the
directory.

## Coverage
You can get a test coverage report by running
`pytest --cov=app`
