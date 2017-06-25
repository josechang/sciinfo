# README #

This is a file for calculating scores base on git log. It uses git with version higher than 1.9.5.
It consists of three parts: generate_stat.py, fake_commits.txt, and the contents in html folder.

### Usage

* To call the function please use 

		python generate_stat.py $(path to .git)
		
    it will generate an index.html in html folder which can be load into the webserver directly.
    
* To run the code automatically, use crontab to setup a schedule using

        crontab -e
        0 * * * * python path_to_generate_stat path_to_git >| path_to_log 2>&1
        
### Settings

* In fake_commits.txt, we can manually input the commits which will be mark as fake.
* In generate_stat.py, there are several variables can be customize:
    * additional -- Additional options for git log. To exclude file extensions, use -- . ':(exclude)*.xxx' ':(exclude)*.yyy'
    * threshold -- The threshold of words for deciding if a commit is invalid.
    * highest_score -- The index of the score to be set as 100.
    * wt -- The weighting of [commits, lines_inserted, lines_deleted, words_inserted, words_deleted]

		
