import openai


def complete_batch(prompts, stop_words, top_p=0.95, temperature=0.6, n=1, **kwargs):
    if stop_words == []:
        stop_words = None
    else:
        stop_words = stop_words[:4]
    return openai.ChatCompletion.create(
        model="gpt-4",
        messages=prompts,
        stop=stop_words,
        max_tokens=3000,
        top_p=top_p,
        temperature=temperature,
        n=n,
        **kwargs
    )


api_keys = open("/nobackup/yuhao_data/my_api.txt").read().splitlines()
openai.api_key = api_keys[0]
try:
    print(
        complete_batch([{"role": "system",
                         "content": "You are an expert of model checking. You have more than ten years of experience on verifying models using CTL and LTL."},
                        {"role": "user",
                         "content": "why LTL is preferred over CTL? And why CTL is preferred over LTL?"},
                        {"role": "assistant",
                         "content": "Both Linear Temporal Logic (LTL) and Computation Tree Logic (CTL) are valuable tools for model checking, but each has its own advantages and scenarios where it might be preferred over the other.\n\nLTL is often preferred over CTL for the following reasons:\n\n1. Expressiveness: LTL is more expressive in specifying sequences of states that a system must follow. It can express properties about paths without referring to a global state of the system.\n\n2. Simplicity: LTL is simpler than CTL as it doesn't require distinguishing between path quantifiers and state quantifiers. \n\n3. Wide Usage: LTL is widely used in software verification where the focus is more on sequence of actions or events.\n\nOn the other hand, CTL might be preferred over LTL due to:\n\n1. Richness: CTL is richer than LTL in expressiveness when it comes to branching time properties. It allows expressing properties that can have different outcomes based on different choices at a state.\n\n2. Flexibility: CTL allows for quantification over paths which gives it more flexibility. \n\n3. Specific Usage: CTL is particularly useful in hardware verification where at each state there could be multiple possible next states.\n\n4. Efficient Model Checking: The model checking algorithm for CTL is usually more efficient than that for LTL, due to its tree-based structure.\n\nIn conclusion, the preference for LTL or CTL depends on the specific needs of the model checking task at hand."},
                        {"role": "user",
                         "content": "what's the extension of LTL with finite automata called?"}],
                       [])
    )
except Exception as e:
    print(e)
