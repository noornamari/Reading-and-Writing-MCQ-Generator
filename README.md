# Reading and Writing MCQ Generator

#### This process uses a Chat Completions API call to generate an MCQ, proceeded by 4 sequential validators. 
![image](https://github.com/noornamari/Reading-and-Writing-MCQ-Generator/assets/168593615/e3ca4117-5be5-41c8-92d9-f5f4f9c9391a)
1) General Validator: Checks to see the generated MCQ is SAT-aligned. If not, it returns "False" and the MCQ generation process begins again. If it returns "True," the MCQ goes to the next validator.
2) Duplicate Word Validator: Checks to see if the Answer Options have the same word as the word before and/or after the blank space in the Stimulus. The output is the generated MCQ in JSON with any edits.
3) Adverb Validator: Checks to see if there is a conjunctive adverb in the Answer Options. If so, it edits the output to ensure there is a comma after the adverb (if not one already). The output of this validator is the generated MCQ with any edits.
4) Grammatical Correctness Validator: Checks to see if the correct Answer Option is grammatically correct when placed in the Stimulus; and if it is the only Answer Option that is grammatically correct. If "True," the final output will be the MCQ post the adverb validator.

<br> <br>
To use this repo, first change the configs.py file to include the prompts for your generator and validators, the JSON schemas for any function calling, and the validator assistant IDs.
<br> <br>
Then, add any .csv files you want to the "files" folder to store your outputs as they go through the generation process. 
<br> <br>
Change the variable names in the main.py file to reflect the changes you made to the configs and the files folder. Then, run the main.py file.

<br> <br> 
If your validation process is different from the above, then you can take out or add the run_val function to accomodate your process. 
