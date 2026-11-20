This app uses MurmurHash library in order to run the app you need python runtime and and you have to install mmh3 library with "pip install mmh3" command
To run app on Mac/Linux use "python3 hash_app.py n s" on windows use "python hash_app.py n s" insead of n represents bucket count and s represent bucket sizes
App will create buckets under buckets folder lets say we have 1.txt, 1_1.txt and 1_2.txt 1 represends 1 bucket file 1_1.txt and 1_2.txt represends overflow bucket files
In order to run the program again you have to delete bucket files or the folder itself manually (i didn't implement automatically deleting bucket files for security reasons also keeping it a bit more simple)

"pip instal mmh3"
"python3 hash_app.py n s"
