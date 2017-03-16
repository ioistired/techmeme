# technical-meme-helper
Helps you make dank "X but every time Y happens it gets Z% faster" may-mays.

## Instructions for use

1. Get a source video.
2. Make a list of timestamps where some event happens.
You can use audacity to make a bunch of markers,
then export them to a text file.
Use audacity_scrubber.py to clean them up.
3. Put them in a text file, where the first line is a speed multiplier.
At every timestamp, the video speed
will be multiplied by this floating-point amount.

### Example config

Have a video, such as WeAreNumberOne.mp4
Have a config file called WeAreNumberOne.mp4.techmeme
that looks like this:

```
1.69
39.21739
56.91304
...
420
``` 

Run `techmeme WeAreNumberOne.mp4 
'We Are Number One but every "one" speeds up the video by 69%.webm'`
and at the timestamps given, the video will be sped up by 69%.

**NB** You can use any float.
So feel free to use values x s.t. 0 < x < 1
or sqrt(2) or whatever.

## License

Copyright © 2017 Benjamin Mintz

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.