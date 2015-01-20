# cs50-downloader

Note: Windows coming soon!

You can do this in any number of ways, but in the spirit of CS50, I'm going to do it solely from the command line.

**Debian/Ubuntu**

1. Type `wget https://github.com/b4ux1t3/cs50-downloader/archive/master.zip` into the command line.

2. Type `unzip *.zip`

3. Type `cd cs50-downloader-master/debian`

4. Now figure out if you want the lecture videos in 240p, 360p, 720p, or 1080p. Note, the 1080p videos are upwards of 4 GB in size.

5. Once you know which size you want, type `python cs50dl_<your resolution here>.py`.  Example:  

    `python cs50dl_1080p.py`

6. Once thy are downloaded, you should be able to watch the videos and view the HTML files for each of the problem sets!


**Appliance/Fedora**

1. Type `curl -o master.zip https://github.com/b4ux1t3/cs50-downloader/archive/master.zip` into the command line.

2. Type `unzip *.zip`

3. Type `cd cs50-downloader-master/debian`

4. Now figure out if you want the lecture videos in 240p, 360p, 720p, or 1080p. Note, the 1080p videos are upwards of 4 GB in size.

5. Once you know which size you want, type `python cs50dl_<your resolution here>.py`. Example: 

    `python cs50dl_1080p.py`

6. Once thy are downloaded, you should be able to watch the videos and view the HTML files for each of the problem sets!
