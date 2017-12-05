## Speed Test and Save
Runs speedtest.net speed test on best server (as determined by speedtest.net) and saves to .txt file. The reason I made this was to record and save multiple speed tests conducted throughout the day on cron jobs.

This couldn't have been done without the work of [@sivel](https://github.com/sivel), whose speedtest-cli library can be found here https://github.com/sivel/speedtest-cli

### Instructions
1. `touch speedtests.txt` in the same directory as the `speed_test_and_save.py` file in order to create the required .txt ouput file.
2. Run `python speed_test_and_save.py` to run once. Or setup [cron jobs](https://stackoverflow.com/questions/30835547/how-to-execute-python-script-on-schedule) and schedule regular executions of the file.

### Contributing
Feel free to contribute to this repository through a pull request. 
