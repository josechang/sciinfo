All code related to calculation of the submission statistics of the GIT repository can be found in this folder and the setup instructions in this file.

GENERATE THE HTML FILE
1. git clone the Nordron-SciInfo repository to your local computer
2. execute the stat_scinfo.py with the parameter of location of the git repository+"/.git",
	e.g. python stat_sciinfo.py /home/yslin/nordron-sciinfo/.git
3. if succeed, you will get an index.html file. You can browse it in your own computer

MAKE THE PYTHON CODE EXECUTE AUTOMATICALLY
1. In Linux operating system, use crontab to do it. Type "crontab -e" in command line to edit the context of your crontab.
2. The form for setting crontab looks like this: "min hr date month week instruction". For example, for setting our python code, you should type "0 */4 * * * python stat_sciinfo.py /home/yslin/nordron-sciinfo/.git", where * stands for accept anyway.
3. If you set all above that and your crontab doesn't work, it might be the problem of recognizing the path of python for the system. Type "which python" to find where your python is. Then replace the first line of stat_sciinfo.py by your python path. Then add "PATH=your python path" in the forst line of crontab.
4.See http://linux.vbird.org/linux_basic/0430cron.php for more information about crontab.
