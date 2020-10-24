# **1. Application Overview**
The implementation of this Application is in Python 3 , using Tinkter for GUI. Application takes 2 files as input that needs to be ASCII text file. Input file contains text to be analysed and keyword file contains set of keywords. After taking input by the respective buttons on th GUI, the Statistical information will be displayed on GUI itself which is as follows - 
* Number of lines 
* Number of blank lines
* Number of Sentences
* Number of Words
* Number of StopWords
* Number of words after removing StopWords
* Word with highest Frequency
* Word with least Frequency

we can also plot Histogram corresponding to frequency of words by hitting the "plot histogram" button. Now, if something in input file has been changed or modified by the user then there will be a **Refresh** button which can be hit to update Statistical information & histogram. There will be button "open keyword file", After hitting this, All the sentences/lines having the keywords will be displayed on GUI itself.

***

# **2. Application Overview with Testfiles**
* <h3> <b>Intially GUI looks like this - </b> </h3> <br>
![GUI image](https://github.com/khyati18/LAP-Lab-3-Text-Stats/blob/main/testfiles/GUI_images/GUI.png?raw=true)
* <h3> <b> After Adding input file by hitting the button , the stats of input file will be displayed.</b></h3> <br>
![stats image](https://github.com/khyati18/LAP-Lab-3-Text-Stats/blob/main/testfiles/GUI_images/stats.png?raw=true)
<ol>
- <b>stats overview </b>
<ol>
<li> Load each line from input file </li>
<li> First remove the punctuation mark from each line </li>
<li> Count the No. of lines </li>
<li> Split the line into words </li> 
<li> Count the words </li>
<li> for <b>StopWords</b> , import <b>nltk</b> library and then from nltk.corpus import stopwords </li> 
</ol>
</ol>

* <h3> <b> Histogram </b> </h3> <br>
![Histogram image](https://github.com/khyati18/LAP-Lab-3-Text-Stats/blob/main/testfiles/GUI_images/HIstogram.png?raw=true)
<ol>
 <p> -> After hitting "Plot Histogram" button , Histogram plot will seperately displayed as png file and Necessary libraries to be imported to plot histogram are <b> Numpy , Matplotlib , counter .</b> <br>
 NOTE : stopwords are excluded in histogram. <br>
</ol> <br>

* <h3> <b> Dynamic Editing of text file </b> </h3> 
<ol>
<p> If something has been changed in input file then hit the Refresh button to update the stats and histogram plot information.</p>
</ol>

* <h3> <b> Keywords Line </b> </h3> <br>
![lines with keywords image](https://github.com/khyati18/LAP-Lab-3-Text-Stats/blob/main/testfiles/GUI_images/lines%20with%20keywords.png?raw=true)
<ol> 
  <p> -> Browse the keyword file then the lines (which contains the keywords) will display on GUI itself. </p> 
</ol>  

* <h3> <b> NOTE :  </b> </h3> 
 <ol>
 -> <strong> <em> Images shown in the Design.md file are output according to the TestFiles present at </strong> </em>( https://github.com/khyati18/LAP-Lab-3-Text-Stats/tree/main/testfiles ) . 
 </ol>
 
 ***
 # **3. Files Overview**
 This Application have Several files which are - 
 * **_gui.py_** - This files gives proper interface for our application which has various buttons which help to achieve our desired task.
 * **_stats.py_** - This file will return all the statistical information about the input file.
 * **_hist.py_** - This file will return the histogram plot corresponding to frequency of words.
 * **_keywords.py_** - This file will return the lines in input file having at least one keyword.
 * **_requirements.txt_** - This file contains name of all libraries which has to be install to run the Application. Run `pip3 install -r requirements.txt` to install all libraries. 

  
