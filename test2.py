output = '''Answer the main query based on 'question', 'plans' below.
Main query: Complete the following 'plans' to answer the 'question'.
Plans:
1. trim("choose one of the followings: beginning, middle, end, none", "truncated_question"):response
2. parse_event("choose one of the followings: before, when, after, none", "event_to_localize", "truncated_question"):response
3. classify("choose one of the followings: what, where, counting, why, how, location, when, who):response
4. require_ocr("choose one of the followings: yes, no"):response

Question: how many children are in the video?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("counting"):question asks the number of children
require_ocr("no"):question does not require reading texts

Question: how many animals are involved in the video?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("counting"):question asks the number of animals
require_ocr("no"):question does not require reading texts

Question: where is this video taken?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("location"):question asks the location of the place
require_ocr("no"):question does not require reading texts

Question: how is the woman feeling while playing with the girl in grey?
Answer:
trim("none"):no temporal hint found
parse_event("when", "woman playing with the girl in grey", "how is the woman feeling?"):'while' conjunction is found in the question
classify("how"):question asks the feeling of the woman
require_ocr("no"):question does not require reading texts

Question: where is this place?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("location"):question asks the location of the place
require_ocr("no"):question does not require reading texts

Question: what does the baby do after finishing playing with the pram near the end?
Answer:
trim("end", "what does the baby do after finishing playing with the pram?"):'near the end' is found from the question
parse_event("after", "baby finishing playing with the pram", "what is the baby doing?"):'after' conjunction is found in the question
classify("what"):question asks what the baby is doing
require_ocr("no"):question does not require reading texts

Question: how do the boys in blue react after the two girls with red hair leave the stage at the end of the
video?
Answer:
trim("end", "how do the boys in blue react after the two girls with red hair leave the stage?"):'at the end of the video' is found from the question
parse_event("after", "girl with red hair leaving the stage", "how are the boys in blue reacting?"):'after' conjunction is found in the question
classify("what"):question asks how the boys react, meaning what the boys are doing
require_ocr("no"):question does not require reading texts

Question: what is this video about?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("what"):question asks what the video is about
require_ocr("no"):question does not require reading texts

Question: what colour are all of these dogs?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("what"):question asks what the colour of the dogs is
require_ocr("no"):question does not require reading texts

Question: how does the woman react as the tallest man start filming her?
Answer:
trim("none"):no temporal hint found
parse_event("when", "man start filming the woman", "how is the woman reacting?"):'as' conjunction is found in the question
classify("what"):question asks how the woman reacts, meaning what the woman is doing
require_ocr("no"):question does not require reading texts

Question: what did the man do before he kept the guitar in the red box at the start?
Answer:
trim("beginning", "what did the man do before he kept the guitar in the red box?"):'at the start' is found from the question
parse_event("before", "man keeping the guitar in the red box", "what is the man doing?"):'before' conjunction is found in the question
classify("what"):question asks what the man is doing
require_ocr("no"):question does not require reading texts

Question: what did the brown dog do right before standing up near the middle of the video?
Answer:
trim("middle", "what did the brown dog do before standing up?"):'middle of the video' is found from the question
parse_event("before", "brown dog standing up", "what is the brown dog doing?"):'right before' conjunction is found in the question
classify("what"):question asks what the brown dog is doing
require_ocr("no"):question does not require reading texts

Question: where are two men in blue at?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("where"):question asks the location of the man
require_ocr("no"):question does not require reading texts

Question: how did the laptop fall after being turned off and closed?
Answer:
trim("none"):no temporal hint found
parse_event("after", "laptop turning off and closed", "how is the laptop falling?"):'after' conjunction is found in the question
classify("how"):question asks how the laptop falls
require_ocr("no"):question does not require reading texts

Question: what type of sports are three boys in striped playing at the start of the video?
Answer:
trim("beginning", "what type of sports are three boys in striped playing?"):'at the start of the video' is found from the question
parse_event("none"):no temporal conjunction found
classify("what"):question asks the type of sports that boys are playing
require_ocr("no"):question does not require reading texts

Question: What is the person doing in the video?
Answer:
trim("none"):no temporal hint found
parse_event("none"):no temporal conjunction found
classify("what"):question asks what the person is doing
require_ocr("no"):question does not require reading texts'''

def trim_prompt1(output, question):
    """
    Trim the output of generate_prompt1 based on the question.
    """
    if "trim" in output:
        trimmed_list = output.split("Answer:\n")[-1].split("\n")
        calls = [line.split(":")[0].strip() for line in trimmed_list]
        return calls
    return question  # Fallback to the original question if no trim found
print(trim_prompt1(output, "What is the person doing in the video?"))