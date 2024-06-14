import json
import csv
import time
from openai import OpenAI
import configs

# Use your API key here
api_key = "YOUR-API-KEY"

client = OpenAI(api_key=api_key)


# Function to generate MCQ--this is a completions call, you can change out the model and temperature
def run_prompt(prompt, json_format, id):
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=.5,
        tools=[json_format],
        tool_choice={
            "type": "function",
            "function": {"name": json_format["function"]["name"]}
        },
        max_tokens=5000
    )
    message = response.choices[0].message.tool_calls[0].function.arguments

    # You don't need to keep the following lines of code, they are written to output the original
    # MCQs to a csv file called "original" to keep track of the original completions calls
    # before they are sent through the validators--you can change this file name as well
    with open("files/original.csv", "a", newline='') as original_file:
        writer = csv.writer(original_file)
        json_string = json.loads(message)
        writer.writerow([id, json_string])
    return message


# Function to run the validators: the input is the User Message, the val_id is the assistant ID,
# the prompt is the assistant's system instructions, the tool_name is the function that is
# called, the file is the csv file to write outputs to, and the id is the identifier for the MCQ
def run_val(input, val_id, prompt, tool_name, file, id):
    # Create Thread
    thread = client.beta.threads.create()
    thread_id = thread.id
    print(input)
    # Add message to the thread
    thread_message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=input,
    )

    # Execute Run
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=val_id,
        instructions=prompt
    )

    run_status = "queued"

    while run_status != "requires_action":
        time.sleep(3)
        run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        run_status = run.status

        if run_status == "requires_action" and run.required_action.type == "submit_tool_outputs":
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            tool_outputs = [{"tool_call_id": tool_call.id, "output": tool_call.function.arguments}
                            for tool_call in tool_calls]
            tools_used = [_.type for _ in run.tools]
            messages = client.beta.threads.messages.list(thread_id=thread_id)
            output = tool_outputs[-1]["output"]
            # print(output)
            with open(file, "a", newline='') as file:
                writer = csv.writer(file)
                json_string = json.loads(output)
                writer.writerow([id, json_string])
            return output


        elif run_status == "completed":
            _ = client.beta.threads.messages.create(
                thread_id=thread_id,
                role="user",
                content=input,
            )
            run = client.beta.threads.runs.create(
                thread_id=thread_id,
                assistant_id=val_id,
                instructions=prompt,
                extra_body={"tool_choice": {"type": "function", "function": {"name": tool_name}}}
            )

        elif run_status == "failed" or run_status == "incomplete" or run_status == "expired":
            run_error_msg = run.last_error.message
            print(f"\t\t\tRun Status: {run_status}, Reason: {run_error_msg}")
            break

        elif run_status == "in_progress":
            continue


# This for loop triggers the MCQ generation and validation process. The numbers in this range
# here determine how many questions get generated and what "id" number they have which is why it
# starts with 1; to increase the number of questions, change the second number; the second number
# is not inclusive, so this specific statement generates 11 questions, not 12
for num in range(1, 12):
    # The generator_response is the result of the completions call -- change out these variables
    # to include your configs
    generator_response = run_prompt(configs.generator_prompt,
                                    configs.generate_MCQ_json, num)

    # This is the response for my general validator which returns a boolean (True/False)
    gen_val_response = run_val(prompt=configs.gen_val_prompt, input=generator_response,
                               val_id=configs.gen_val_id, tool_name="generate_output",
                               file="files/gen_val.csv", id=num)
    gen_val_json = json.loads(gen_val_response)

    # If the general validator returns True (there aren't any glaring issues that the MCQ should
    # be thrown out for, the validation process continues; if False, the next question gets
    # generated
    if gen_val_json["correct"]:
        # This is the response of my duplicate word validator (checks if the output has the same
        # word in the Stimulus and Answer Options--if so, it removes the word from the Stimulus
        dup_word_response = run_val(prompt=configs.duplicate_word_val_prompt,
                                    input=generator_response, val_id=configs.dup_word_val_id,
                                    tool_name="generateSATMCQ", file="files/post_duplicate.csv", id=num)

        # This is the response of my adverb validator (checks if the Answer Option has an adverb,
        # and if so, it adds a comma if there is not already one present)
        adverb_response = run_val(prompt=configs.adverb_val_prompt, input=generator_response,
                                  val_id=configs.adverb_val_id, tool_name="generateSATMCQ",
                                  file="files/post_adverb.csv", id=num)

        # This is the response for my grammatical correctness validator, which returns a boolean
        # (True/False)
        gram_correctness_response = run_val(prompt=configs.correctness_prompt,
                                            input=adverb_response, val_id=configs.gram_val_id,
                                            tool_name="generate_output",
                                            file="files/post_correctness.csv", id=num)
        correctness_json = json.loads(gram_correctness_response)

        # If the output is grammatically correct, I want to add the MCQ to my "final_outputs.csv"
        if correctness_json["correct"]:
            with open("files/final_outputs.csv", "a", newline='') as final_outputs:
                writer = csv.writer(final_outputs)
                json_string = json.loads(adverb_response)
                writer.writerow([num, json_string])
