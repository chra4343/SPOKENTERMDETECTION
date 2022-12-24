# SPOKENTERMDETECTION
RETRIEVING THE SPOKEN WORD FROM THE SPEECH

IMPORTANT - PLEASE RUN THIS COMMAND AT THE START IN THE TERMINAL OR IPNYB CELL BEFORE RUNNING THE CODE FILES - 

!pip install -r requirements.txt
This command installs the required libraries for running the code files without any errors.


Regarding the code for First and Second Evaluation - FOLDER NAME IS 'Code for 1,2 Eval' 

a. The file name is srmodel.py - This file is required to be run in a python interpreter. 
b. The datasets are in the folder and their path is already specified in the code, so no need to import additionally.
c. There are other audio visualization to run to find out graphical representation.


Regarding the Web Application for First and Second Evaluations - FOLDER NAME IS 'Web App for 1,2 Eval'

a. The web application file name is webapp.py - Run in terminal with command, streamlit run webapp.py
b. After running the web application, import the test recording with the name testrec.wav in the same folder to test the audio-to-text conversion.
c. After testing, take a Youtube URL, paste in the sidebar input field and click 'GO' button. It saves the audio format of the youtube video. 
d. Import the new audio file to transcribe audio and see the audio-to-text analysis result.


Regarding the code for Third Evaluation - FOLDER NAME IS 'Code for third Eval'

a. The code file name is BTPThirdEval.ipnyb - This file should be run in either Google Colab or Jupyter Notebook.
b. The datasets are in the folder and their path is already specified in the code, so no need to import additionally.
c. If using Google Colab, please import the files to the runtime of Colab and run the cells.


Regarding the code for Fourth Evaluation - FOLDER NAME IS 'Code for fourth Eval'

a. The code file name ins BTPFourthEval.ipnyb - This file should be run in either Google Colab or Jupyter Notebook.
b. The datasets are in the folder and their path is already specified in the code, so no need to import additionally.
c. If using Google Colab, please import the files to the runtime of Colab and run the cells.

Regarding the Web Application for Third and Fourth Evaluation - FOLDER NAME IS 'Web App for 3,4 Eval'

a. The code files are present in the folder BTPWebApp. The folder consists of HTML, CSS, JS files.
b. The website can be seen directly by opening index.html or by opening this link - https://jnaneswar-ghub.github.io/finalEval-BTP/
c. The website can be run on localhost using the command http-server on the terminal.
d. Select the language and dialect from the dropdowns and click the microphone symbol and give access to the website.
e. Then start speaking and the web application does real-time speech-to-text conversion.
f. After stopping the recording all the text displayed will be selected to create a new dataset to train or predict the model.
