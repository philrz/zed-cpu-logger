# `zed-cpu-logger.py`

This is a simple Python program to poll the local CPU utilization every second
and push a "% busy" metric to a [Zed lake](https://zed.brimdata.io/docs/commands/zed/)
presumed to be running on the local system.

# Installation

To install and run with needed dependencies in a [virtual environment](https://docs.python.org/3/tutorial/venv.html):

```
git clone https://github.com/philrz/zed-cpu-logger
cd zed-cpu-logger
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
./zed-cpu-logger.py
```

Assuming a Zed lake is listening on the local host, when running you'll see a
dot printed as each batch of CPU points is loaded to the pool.

```
$ ./zed-cpu-logger.py 
Loading data to newly-created pool "default"...................
```

# Why?

I created this as a continuous source of time-series data to be used with the
prototype [Grafana Zed data source plugin](https://github.com/philrz/zed-datasource)
I also recently developed.

If I were a better Go developer, surely a better approach would have been to
develop something like a general purpose Zed lake
[Telegraf output plugin](https://docs.influxdata.com/telegraf/v1.22/plugins/#output-plugins).
That would allow for gathering and ingest of _any_ metric that Telegraf
can poll, with CPU being but one example. Perhaps someone with more skills and
experience could be inspired to take that on.
