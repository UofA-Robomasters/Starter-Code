# pid_tutorial
Tutorials for new members of EE team in Robomasters. Wish all of you can master PID controllers!
This is more like a simulator for you to tune the parameters rather than a detailed tutorial.

### Requirements
numpy, [matplotlib](https://matplotlib.org/users/installing.html)

### Usage
`source robo` for windows or `source activate robo` for mac/linux if you are using the environment package(Starter-kit).

1. Change kp, ki, kd in `hover_plot.py`
2. Run `python hover_plot.py`
3. There should be two images popped up. Have a look at the plot and repeat the process.

### Error when import plt for mac users
This is caused by different rendering back end of matplotlib.
Follow the instructions [here](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python)