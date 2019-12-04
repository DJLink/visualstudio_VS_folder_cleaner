# Visual studio ".vs" folder cleaner

## What it does

Visual Studio generates a ".vs" folder with all projects, this range be a couple megabytes to GBs depending on project size. These are recreated each time VS opens but it's generally a good practice to keep them around on active projects, but if you have a lot of old projects you can remove them to free some space. This Python script will search every ".vs" folder within a directory and will prompt to delete. This will make all folders to be send to Recicle Bin if possible, I prefer this method to destroying the files right away. The safest way is just let the script list and delete manually if you don't want to risk any potential bugs, I'm not responsible for any data lost.  

## How to use
This script depends on [send2trash](https://github.com/hsoft/send2trash) python module
```console
$ pip install send2trash
````

Run the script
```console
$ py vs_cleaner.py D:/Projects
````

Optionally can use -i arg, script will prompt [Y/N] deletion for each folder instead of all or nothing.
```console
$ py vs_cleaner.py -i D:/Projects
````

It will list the folder if any, and ask to delete, at this point it's up to you to either automate the deletion or delete manually.

![alt text](https://github.com/DJLink/visualstudio_VS_folder_cleaner/raw/master/sample.png "Testing")

"human_bytes" function by [whereisalext](https://stackoverflow.com/a/31631711)

## License
MIT License

Copyright (c) 2019 David Amador

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
