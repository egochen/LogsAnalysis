# Project: Logs Analysis
This is a reporting tool that prints out reports (in plain text) based on the
data in the database. This reporting tool is a Python program using the
psycopg2 module to connect to the database. The  tool answers the following three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Setup
You will need to install the following softwares:
- [Vagrant](https://www.vagrantup.com)
- [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
- [VM Configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)

[The data to use can be downloaded here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip this file after downloading it. The file inside is called `newsdata.sql`. To use load data, use the command `psql -d news -f newsdata.sql`.
## Usage
Run `project1.py` in your terminal. You should see outputs on the terminal
which are the same as those shown in `output_example.txt`
