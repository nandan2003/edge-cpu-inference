from models_config import MODEL_REGISTRY

# 10 coding, 10 reasoning, 10 chat = 30 tasks
TEST_SUITE = [

# ---------------- CODING (10 tests) ----------------

{"cat": "Coding", "prompt": "Write a Python function to check if a number is even. Return code only.",
 "check": lambda x: "def" in x and "return" in x and "%" in x},

{"cat": "Coding", "prompt": "Write valid JSON with key 'ok' = true. Return JSON only.",
 "check": lambda x: "{" in x and "ok" in x.lower()},

{"cat": "Coding", "prompt": "Write a bash command to create a directory named test_dir.",
 "check": lambda x: "mkdir" in x},

{"cat": "Coding", "prompt": "Fix this: for i in range(5) print(i). Return fixed code.",
 "check": lambda x: "print" in x and ":" in x},

{"cat": "Coding", "prompt": "Write a SQL query to select all rows from a table called users.",
 "check": lambda x: "select" in x.lower() and "users" in x.lower()},

{"cat": "Coding", "prompt": "Write a Python list comprehension producing squares from 1 to 5.",
 "check": lambda x: "[" in x and "**2" in x},

{"cat": "Coding", "prompt": "Write a one-line JavaScript arrow function adding two numbers.",
 "check": lambda x: "=>" in x},

{"cat": "Coding", "prompt": "Write HTML containing only a <p>Hello</p> element.",
 "check": lambda x: "<p>" in x.lower()},

{"cat": "Coding", "prompt": "Write a C function to return 1. Return only code.",
 "check": lambda x: "int" in x and "return 1" in x.lower()},

{"cat": "Coding", "prompt": "Write a Dockerfile line to set environment variable MODE=prod.",
 "check": lambda x: "ENV" in x.upper() and "MODE" in x},

# ---------------- REASONING (10 tests) ----------------

{"cat": "Reasoning", "prompt": "Compute 13 * 7. Return only number.",
 "check": lambda x: "91" in x},

{"cat": "Reasoning", "prompt": "Compute (12 + 8) / 5. Return only number.",
 "check": lambda x: "4" in x},

{"cat": "Reasoning", "prompt": "If A > B and B > C, which is smallest? Return letter.",
 "check": lambda x: x.strip().upper() == "C"},

{"cat": "Reasoning", "prompt": "Which is odd: 2, 6, 9, 10? Return only number.",
 "check": lambda x: "9" in x},

{"cat": "Reasoning", "prompt": "If a train travels 60km in 1h, what is speed? Return number + ' km/h'.",
 "check": lambda x: "60" in x and "km" in x.lower()},

{"cat": "Reasoning", "prompt": "What is the next number: 2, 4, 8, 16? Return only number.",
 "check": lambda x: "32" in x},

{"cat": "Reasoning", "prompt": "If x=10, y=3, compute x%y. Return only number.",
 "check": lambda x: "1" in x.strip()},

{"cat": "Reasoning", "prompt": "Select the largest: 89, 23, 95, 74. Return number.",
 "check": lambda x: "95" in x},

{"cat": "Reasoning", "prompt": "Two people, one always lies. You ask 'Is the sky blue?'. Expected answer?",
 "check": lambda x: "yes" in x.lower() or "blue" in x.lower()},

{"cat": "Reasoning", "prompt": "Sort numbers: 5,1,8,2 into ascending order. Return exact sequence.",
 "check": lambda x: "1" in x and "2" in x and "5" in x and "8" in x},

# ---------------- CHAT (10 tests) ----------------

{"cat": "Chat", "prompt": "What is the capital of Japan? One word only.",
 "check": lambda x: "tokyo" in x.lower()},

{"cat": "Chat", "prompt": "What gas do plants release at night? One word.",
 "check": lambda x: "co2" in x.lower() or "carbon" in x.lower()},

{"cat": "Chat", "prompt": "Convert 'world' to uppercase.",
 "check": lambda x: "WORLD" in x},

{"cat": "Chat", "prompt": "What is 1+1?",
 "check": lambda x: "2" in x},

{"cat": "Chat", "prompt": "Is water a liquid? Respond yes or no.",
 "check": lambda x: "yes" in x.lower()},

{"cat": "Chat", "prompt": "What is the opposite of hot?",
 "check": lambda x: "cold" in x.lower()},

{"cat": "Chat", "prompt": "What planet do humans live on?",
 "check": lambda x: "earth" in x.lower()},

{"cat": "Chat", "prompt": "What is H2O?",
 "check": lambda x: "water" in x.lower()},

{"cat": "Chat", "prompt": "Translate 'bonjour' to English.",
 "check": lambda x: "hello" in x.lower()},

{"cat": "Chat", "prompt": "What shape has 3 sides?",
 "check": lambda x: "triangle" in x.lower()},
]


def evaluate_accuracy(llm, model_key: str):
    meta = MODEL_REGISTRY[model_key]
    template = meta["prompt_template"]

    scores = {"Coding": 0, "Reasoning": 0, "Chat": 0, "Total": 0}
    counts = {"Coding": 0, "Reasoning": 0, "Chat": 0, "Total": 0}

    print("   Profiling intelligence (Coding, Reasoning, Chat)...", end="", flush=True)

    for test in TEST_SUITE:
        cat = test["cat"]
        counts[cat] += 1
        counts["Total"] += 1

        full_prompt = template.format(prompt=test["prompt"])

        out = llm(
            full_prompt,
            max_tokens=128,
            stop=["<|end|>", "\n\n", "User:", "```"],
            echo=False,
            temperature=0.0,
        )
        response = out["choices"][0]["text"].strip()

        if test["check"](response):
            scores[cat] += 1
            scores["Total"] += 1
            print(".", end="", flush=True)
        else:
            print("x", end="", flush=True)

    print(" Done.")

    results = {}
    for k in scores:
        results[k] = round((scores[k] / counts[k]) * 100.0, 1) if counts[k] > 0 else 0.0

    return results
