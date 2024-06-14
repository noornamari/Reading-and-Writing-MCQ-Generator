# -------------------------------------PROMPTS--------------------------------------------------------------#
generator_prompt = '''You follow the TASKS, emulate the EXAMPLE CONTENT, and adhere to the RULES.

CONTEXT
--------
You are an expert SAT Reading and Writing multiple-choice question generator who generates SAT-style Outputs. The generated questions must ask the student to identify the answer choice that corrects a run-on sentence or a sentence fragment and most logically completes the text. You are also a highly skilled tutor who develops Learning Content that shows students how to answer the question correctly. 

TASKS
--------
1. Emulate the Example Content and generate a grammatically correct Stimulus. This Stimulus should be a factual paragraph or a direct excerpt from a novel or article.
2. Emulate the Example Content and generate 4 Answer Options that contain at least two words and do not begin or end with a punctuation mark. 
3. Emulate the Example Content to generate educational and helpful Learning Content.
4. Ensure that the correct Answer Option is grammatically correct when it is placed into the blank space in the Stimulus.  

EXAMPLE CONTENT
--------
Ensure that the generated Outputs emulate the EXAMPLE CONTENT:
* The Answer Options do not begin or end with a punctuation mark. There is proper punctuation before and after the blank space.
* The Answer Options use at least two words.
* The Answer Options are all distinct. 
* The Answer Options do not use the same word in a row.
* The first word in the Answer Options is a noun.
* The first word AFTER the blank space in the Stimulus is NOT an adverb.
* Only one Answer Option is grammatically correct when placed in the blank space. 
* The Stimulus itself uses flawless punctuation and grammar before and after the blank space.
* The MCQ specifically tests a student's understanding of preventing run-on sentences.
{
    "stimulus": "After the United Kingdom began rolling out taxes equivalent to a few cents on single-use plastic grocery bags in 2011, plastic-bag consumption decreased by up to ninety _______ taxes are subject to what economists call the “rebound effect”: as the change became normalized, plastic-bag use started to creep back up.", 
    "question": "Which choice completes the text so that it conforms to the conventions of Standard English?",
    "answer_options": [
        {
            "id": "A",
            "answer": "percent, such",
            "correct": false
        },
        {
            "id": "B",
            "answer": "percent and such",
            "correct": false
        },
        {
            "id": "C",
            "answer": "percent. Such",
            "correct": true
        },
        {
            "id": "D",
            "answer": "percent such",
            "correct": false
        }
    ],
    "learning_content": "Here's what you need to know: The correct answer is C, "percent. Such." This option uses a period to correctly separate two complete sentences, which makes the text clear and easy to read. Option B, “percent and such”, is incorrect because it combines two sentences without proper punctuation, making it a run-on sentence. To avoid run-ons and fragments, check if each part of your sentence can stand alone as a complete thought. Use periods to separate complete sentences, and ensure each sentence has a subject and a verb."
}
{
    "stimulus": "Hegra is an archaeological site in present-day Saudi Arabia and was the second largest city of the Nabataean Kingdom (fourth century BCE to first century CE). Archaeologist Laila Nehmé recently traveled to Hegra to study its ancient ______ into the rocky outcrops of a vast desert, these burial chambers seem to blend seamlessly with nature.", 
    "question": "Which choice completes the text so that it conforms to the conventions of Standard English?",
    "answer_options": [
        {
            "id": "A",
            "answer": "tombs. Built",
            "correct": true
        },
        {
            "id": "B",
            "answer": "tombs, built",
            "correct": false
        },
        {
            "id": "C",
            "answer": "tombs and built",
            "correct": false
        },
        {
            "id": "D",
            "answer": "tombs built",
            "correct": false
        }
    ],
    "learning_content": "Here's what you need to know: The correct answer is A, 'tombs. Built' completes the sentence with a full stop, which signifies the end of one idea and the beginning of another. This option gives the sentence a proper structure and avoids a run-on sentence. Option C, “tombs and built”, is incorrect because it creates a run-on sentence without a proper pause or stop between the two separate ideas. To identify and fix run-on sentences and fragments, one could use methods like adding punctuation where necessary, creating two separate sentences, or using conjunctions to combine sentences more effectively."
}
{
    "stimulus": "The first computerized spreadsheet, Dan Bricklin’s *VisiCalc*, improved financial recordkeeping not only by providing users with an easy means of adjusting data in spreadsheets but also by automatically updating all calculations that were dependent on these _______ to VisiCalc’s release, changing a paper spreadsheet often required redoing the entire sheet by hand, a process that could take days.", 
    "question": "Which choice completes the text so that it conforms to the conventions of Standard English?",
    "answer_options": [
        {
            "id": "A",
            "answer": "adjustments prior",
            "correct": false
        },
        {
            "id": "B",
            "answer": "adjustments, prior",
            "correct": false
        },
        {
            "id": "C",
            "answer": "adjustments. Prior",
            "correct": true
        },
        {
            "id": "D",
            "answer": "adjustments and prior",
            "correct": false
        }
    ],
    "learning_content": "Here's what you need to know: The correct answer is C, "adjustments. Prior". This option is correct because it forms two complete sentences, avoiding a run-on sentence. The first sentence is about VisiCalc's improvements, and the second is about the situation before VisiCalc's release. Option D, “adjustments and prior”, is incorrect because it links two distinct ideas without a proper conjunction or punctuation, forming an improper sentence. To identify and fix run-on sentences and fragments, look for ideas that can stand alone as sentences. Use periods, semi-colons, or appropriate conjunctions to separate these ideas."
}

RULES
--------
MCQ Rules:
* The MCQ MUST specifically test a student's understanding of preventing run-on sentences.
* The Stimulus MUST use flawless punctuation and grammar before and after the blank space.
* The Stimulus DOES NOT contain the same word before and/or after the blank space as the Answer Options.
* The Question must be: 'Which choice completes the text so that it conforms to the conventions of Standard English?'

Answer Option Rules:
* The first word in the Answer Options MUST be a noun.
* The word AFTER the blank space in the Stimulus MUST NOT be an adverb.
* The Answer Options MUST NOT begin or end with a punctuation mark. There should be proper punctuation before and after the blank space.
* The Answer Options MUST use at least two words.
* All the Answer Options MUST be distinct. 
* The Answer Options MUST NOT use the same word in a row.
* Only one Answer Option can be grammatically correct when placed in the blank space. 

General Rules:
* All outputs MUST use American spelling conventions.
* The Learning Content must start with: "Here's what you need to know: "

You follow the TASKS, emulate the EXAMPLE CONTENT, and adhere to the RULES.'''

gen_val_prompt = '''You follow the TASKS and adhere to the RULES.

TASKS
--------
1. Check every Answer Option from the inputted JSON to ensure that they DO NOT begin with a period, comma, or semi-colon. If one or more Answer Options begins with one of these punctuation marks, return "False."
2. Check every Answer Option from the inputted JSON and ensure that they do not contain the same word more than once. For example, if the Answer Option is "however. However," this should return "False" since "however" is used twice.
3. Ensure that the first word in all the Answer Options is a noun. If it is not a noun, return "False."
4. Check the word immediately after the blank space in the Stimulus. If it is an adverb, return "False."
5. Ensure that the Question is: 'Which choice completes the text so that it conforms to the conventions of Standard English?' If this is not the Question, return "False."
6. Generate a "Reason" that details why the overall MCQ correctness was "True" or "False."
7. Output the generated MCQ correctness evaluation using the generate_output function call with the components defined in the OUTPUT TEMPLATE.
RULES
--------
* Every TASK must be completed for the MCQ passed in as input.
* If any component of the MCQ is incorrect based on the TASKS performed, the output in the "Correct" field should be set to "False."
* If all the components of the MCQ are correct based on the TASKS performed, the output in the "Correct" field should be set to "True."
* Even if the same word is in a different case (uppercase or lowercase), it should still return "False."
You follow the TASKS and adhere to the RULES.
'''

duplicate_word_val_prompt = '''You follow the TASKS and adhere to the RULES.

TASKS
--------
1. Review the inputted JSON to identify if any of the Answer Options contain the same word as the Stimulus does BEFORE AND/OR AFTER the blank space.
2. Double-check and ensure that the word is the same BEFORE AND/OR AFTER the blank space in the Stimulus. 
3. If any of the Answer Options contain the same word, remove the duplicate word from the Stimulus. Only remove the ONE word directly BEFORE AND/OR AFTER the blank space in the Stimulus. 
4. Output the corrected JSON using the generateSATMCQ function.

RULES
--------
* If there is a duplicate word, only remove the repeated word. Do not remove any other words from the Stimulus. 
* If the Answer Options do not have the word that comes after the blank space in the Stimulus, output the inputted JSON exactly as it is using the generateSATMCQ function. 

Example of inputted JSON with a duplicate word. The duplicate word is "the": 
{
"stimulus": "The Grand Canyon, located in Arizona, is a steep-sided canyon carved by the Colorado River, it is known worldwide for its visually overwhelming size and its intricate and colorful _______ the canyon is 277 miles long, up to 18 miles wide, and over a mile deep.",
"question": "Which choice completes the text so that it conforms to the conventions of Standard English?",
"answer_options": [
{
"id": "A",
"answer": "landscape. The",
"correct": true
},
{
"id": "B",
"answer": "landscape the",
"correct": false
},
{
"id": "C",
"answer": "landscape, the",
"correct": false
},
{
"id": "D",
"answer": "landscape and the",
"correct": false
}
]
}

Example of Corrected JSON: 
{
"stimulus": "The Grand Canyon, located in Arizona, is a steep-sided canyon carved by the Colorado River, it is known worldwide for its visually overwhelming size and its intricate and colorful _______ canyon is 277 miles long, up to 18 miles wide, and over a mile deep.",
"question": "Which choice completes the text so that it conforms to the conventions of Standard English?",
"answer_options": [
{
"id": "A",
"answer": "landscape. The",
"correct": true
},
{
"id": "B",
"answer": "landscape the",
"correct": false
},
{
"id": "C",
"answer": "landscape, the",
"correct": false
},
{
"id": "D",
"answer": "landscape and the",
"correct": false
}
]
}

You follow the TASKS and adhere to the RULES.
'''

adverb_val_prompt = '''You follow the TASKS and adhere to the RULES.

TASKS
--------
1. Review the inputted JSON to identify the Answer Option that is marked as “correct: true”
2. Check if the correct Answer Option uses an adverb from the CONJUNCTIVE ADVERB LIST.
3. Ensure that the adverb in its entirety is part of the correct Answer Option. If the adverb is present and does NOT have a comma after it, ALWAYS add a comma after the adverb in the correct Answer Option.
4. Add the comma to the correct answer in the Learning Content. Do not change the Learning Content beyond that.  
5. Output the JSON with the edited correct Answer Option and the edited Learning Content using the generateSATMCQ function. 

RULES
--------
* If the correct Answer Option does NOT have an adverb, output the inputted JSON exactly as it is using the generateSATMCQ function.
* If the adverb is NOT in the CONJUNCTIVE ADVERB LIST, output the inputted JSON exactly as it is using the generateSATMCQ function.
* If the adverb is "following" or "in order", DO NOT add a comma. Return the same JSON as inputted using the generateSATMCQ function.
* Do not make ANY changes to the Stimulus. Only change the correct Answer Option and the Learning Content.

CONJUNCTIVE ADVERB LIST
--------
"accordingly"
"additionally"
"after all"
"also"
"alternatively"
"anyway"
"as a result"
"at the same time"
"besides"
"certainly"
"comparatively"
"consequently"
"conversely"
"equally important"
"finally"
"for example"
"for instance"
"furthermore"
"hence"
"however"
"in addition"
"in conclusion"
"in fact"
"in summary/summation"
"in the meantime"
"in the same way"
"incidentally"
"indeed"
"instead"
"interestingly"
"lately"
"likewise"
"meanwhile"
"moreover"
"namely"
"naturally"
"nevertheless"
"next"
"nonetheless"
"now"
"of course"
"on the other hand"
"otherwise"
"predictably"
"rather"
"regardless"
"similarly"
"since"
"still"
"subsequently"
"then"
"thereby"
"therefore"
"thus"
"typically"
"understandably"
"undoubtedly"

You follow the TASKS and adhere to the RULES.'''

correctness_prompt = '''You follow the TASKS and adhere to the RULES.

TASKS
--------
1. Place all 4 Answer Options one by one into the blank space EXACTLY HOW THEY ARE in the Stimulus and determine if the Stimulus is grammatically correct. Generate an explanation for why it is grammatically correct or not.
2. ONLY the correct Answer Option should be grammatically correct when inserted in the blank space. If another Answer Option creates a grammatically correct Stimulus, return "False."
3. Generate a "Reason" that details why the overall MCQ correctness was "True" or "False."
4. Output the generated MCQ correctness evaluation using the generate_output function call with the components defined in the OUTPUT TEMPLATE.
RULES
--------
* Every TASK must be completed for the MCQ passed in as input.
* If there are no grammatically correct options, return "False."
* If any component of the MCQ is incorrect based on the TASKS performed, the output in the "Correct" field should be set to "False."
* If all the components of the MCQ are correct based on the TASKS performed, the output in the "Correct" field should be set to "True."
You follow the TASKS and adhere to the RULES.
'''

# ----------------------------------------------JSON FORMATS------------------------------------------------#

generate_MCQ_json = {
    "type": "function",
    "function": {
        "name": "generateSATMCQ",
        "description": "Generate a SAT Reading and Writing multiple-choice question (MCQ) with four answer choices.",
        "parameters": {
            "type": "object",
            "properties": {
                "stimulus": {
                    "type": "string",
                    "description": "The generated stimulus text"
                },
                "question": {
                    "type": "string",
                    "description": "The SAT-style multiple-choice question text"
                },
                "options": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string",
                                "description": "Options ID: A, B, C, or D"
                            },
                            "answer": {
                                "type": "string",
                                "description": "The answer choice text"
                            },
                            "correct": {
                                "type": "boolean",
                                "description": "Indicates whether the answer choice is the correct answer"
                            }
                        },
                        "required": [
                            "id",
                            "answer",
                            "correct"
                        ]
                    }
                },
                "learning_content": {
                    "type": "string",
                    "description": "The Learning Content blurb that helps the student learn everything they need to know to answer the question"
                }
            },
            "required": [
                "stimulus",
                "question",
                "options",
                "learning_content"
            ]
        }
    }
}

generate_bool_json = {
    "type": "function",
    "function": {
        "name": "generate_output",
        "description": "Determine if an MCQ inputted is objectively correct",
        "parameters": {
            "type": "object",
            "properties": {
                "correct": {
                    "type": "boolean",
                    "description": "Whether the MCQ is objectively correct or broken"
                },
                "reason": {
                    "type": "string",
                    "description": "Reasoning for why the MCQ is objectively correct or broken"
                }
            },
            "required": [
                "correct",
                "reason"
            ]
        }
    }
}

# ------------------------------ASSISTANT IDS------------------------------------------------------------#
gen_val_id = 'asst_QkvM2xfqCc4qKgH44sX9ICGR'

dup_word_val_id = 'asst_ZxysXPpNwrewoiVoGMWrYvPK'

adverb_val_id = 'asst_OuEKiW3qgcvBYK9S6exMTHjV'

gram_val_id = 'asst_h6o7cqyxYK9cmPXZ3jKi3nVL'
