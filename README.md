### This code attempts to solve the classic Riddler from the week of Aug. 10, 2018.

[rugMachine.py](../rugMachine.py) is run to generate rugs.csv. rugMachine.py contains code that randomly generates 100x100 rugs of random colors (Green, white, silver) and then tries to find 4x4 grids where the same color is used in all tiles. [rugMachine.py](../rugMachine.py) tries to find 4 tiles of the same color in a row. Then, afterwards checking to see if those lines of 4 line up with 3 other lines of 4 of the same color.
> Optimization not included in [rugMachine.py](../rugMachine.py)...maybe one day 

> [rugMachine.py](../rugMachine.py) takes about 48 minutes to run on my machine. Could obviously try less rugs to reduce run time. 

[rugs.csv](../rugs.csv) stores data produced by rugMachine.py. The columns correspond to 
1. How many rugs have been checked so far 
2. How many 1x4 blocks of the same color have been found 
3. How many 2x4 blocks of the same color have been found 
4. How many 3x4 blocks of the same color have been found. 4. How many 4x4 blocks of the same color have been found




[inspectCSV.py](../inspectCSV.py) reads in rugs.csv into a pandas dataframe. Here we can try to visualize the data recorded. However, we are most interested in trying to see how many rugs will be rejected (have a 4x4 grid of the same color).
> According to the current version of [rugs.csv](../rugs.csv) , the following regression line is found. 
>> slope: 0.0007330219239534675

>> intercept: 1.131

>> rugs Per 4x4 Grid: 1364.215

![alt text](https://github.com/StewSchrieff/riddlerRugs/blob/master/rugs4x4.png "4x4 blocks as a function of number of rugs generated")
As you can see above, the rate of 4x4 blocks appears fairly linear. Not nearly as linear as the number of 3x4 blocks, as shown below. This would become more linear as we increase the number of rugs generated. `something something GPU programming?` 
![alt text](https://github.com/StewSchrieff/riddlerRugs/blob/master/rugs3x4.png "3x4 blocks as a function of number of rugs generated")

In order to improve this study, we could try to do some optimization to [rugMachine.py](../rugMachine.py) that would allow us to continue to measure 4x4 blocks by increasing the number of rugs generated.

# Conclusion

After running 80000 simulated rugs, we found 58 rugs that had 4x4 grids. This is a pretty low rate of bad rugs. By using linear regression, we find that we could expect a bad rug about once every 1364 rugs.



This code uses the following technologies
* python
* seaborn
* numpy
* seaborn
* scipy
* pandas











 