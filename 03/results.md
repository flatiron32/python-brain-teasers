I was *correct*...but the book says I was wrong. I created an errata https://forum.devtalk.com/t/python-brain-teasers-teaser-3-wrong-answer/1279

# Why
The book says that ó will be counded as 2 bytes. This is true if you convert it to a byte array it will take up two bytes, but python correctly handles that chars. 

# What else learned 
I wrote a little script to check all the released version of python3.
```bash
for minor in `seq 2 8`
do 
    echo "Python 3.$minor"
    docker run -it python:3.$minor python -c "print(len('Kraków'))"
done
```