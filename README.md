
# Dstat Plugins

Dstat is a versatile tool for generating system resource statistics.
It also supports plugins, which can be written to monitor whatever you want.


# List of Plugins

These are my own dstat plugins:

## CPU Temperature

Displays CPU temperature in Celsius as reported by lm_sensors.

Example:
	
	$ dstat --cputemp
	---------------------temperature---------------------
	total  cpu0  cpu1  cpu2  cpu3  cpu4  cpu5  cpu6  cpu7
	47.88 49.00 48.00 48.00 48.00 49.00 48.00 45.00 48.00
	47.75 49.00 49.00 48.00 47.00 48.00 48.00 45.00 48.00
	47.75 49.00 49.00 48.00 47.00 48.00 48.00 45.00 48.00
	47.75 49.00 49.00 48.00 47.00 48.00 48.00 45.00 48.00
	47.75 49.00 49.00 48.00 47.00 48.00 48.00 45.00 48.00
	47.75 49.00 49.00 48.00 47.00 48.00 48.00 45.00 48.00
	47.75 49.00 49.00 48.00 47.00 48.00 48.00 45.00 48.00


# Installing

Download and install the scripts:

	git clone git://github.com/mvneves/dstat-plugins
	cd dstat-plugins
	mkdir -p ~/.dstat
	cp -a *.py ~/.dstat

Use 'dstat --list' to see the available plugins.

# Dependencies

Install lm_sensors:

	sudo apt-get install lm-sensors

Detect hardware monitoring sensors:

	sudo sensors-detect


# References

- Dstat: versatile resource statistics tool: 
[http://dag.wieers.com/home-made/dstat/](http://dag.wieers.com/home-made/dstat/)



