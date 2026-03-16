# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Bug 1. The hints showed the opposite of what I should of done.
Bug 2. The "hard" difficulty supposedly had a less range than normal difficulty so it is easier.
Bug 3 Trying to start a new game gives the error:

AttributeError: module 'streamlit' has no attribute 'rerun'
Traceback:
File "C:\Programs\x__\ActiveState\ActivePython\v3.7.4\lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 552, in _run_script
    exec(code, module.__dict__)
File "C:\Users\n1exp\OneDrive\Documents\ai110-module1show-gameglitchinvestigator-starter\app.py", line 138, in <module>
    st.rerun()
    AttributeError: module 'streamlit' has no attribute 'rerun'
Traceback:
File "C:\Programs\x__\ActiveState\ActivePython\v3.7.4\lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 552, in _run_script
    exec(code, module.__dict__)
File "C:\Users\n1exp\OneDrive\Documents\ai110-module1show-gameglitchinvestigator-starter\app.py", line 138, in <module>
    st.rerun()

AI Assisted explanation of the third bug:
The reason for this traceback is due to the fact that the function that added st.rerun() in streamlit was added in version 1.27 but the installed package is . To fix it, the ways would be to either upgrade streamlit to 1.27.0 or above, or to replace that function with "st.experimental_rerun()" instead.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- One example of an AI Suggestion was where it suggested for changing the number of attempts for the different difficulty levels. It suggested to switch around the attempts so that the easy difficulty had the highest number of attempts wihle hardest had the lowest and I checked that this made common sense with how it should work and so I accepted this.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One example was in the ranges for the guesses for the difficulty settings. It made the decision to move the 1-50 guessing range to medium and switch with the hard difficulty range, but it broke the correct syntax. I used the inline editor feature to fix this and set it to the correct syntax and then I redid the program and saw that the ranges were accurate.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided if a bug was fixed by attempting to replicate the conditions that started the bug and seeing if it happened again. One example of this was a manual test I did about the restart of the game where I tested if the "New Game" button, which normally started an error, would properly create a new game. In this instance, it did end up properly starting a new game.
The AI did help design new tests for inputs such as if a blank input was given, or if a decimal instead of an integer was given. It helped me understnad them by explaining the logic behind how each of these tests would work.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I unddertand streamlit reruns better now. I would explain them by saying that the rerun function would rerun the entire script from the top whenever the state of the game is changed; in the case of this game, when the session state of the game is changed then the code would have called st.rerun() to force the reexecution of the game. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - I will take care to use prompting strategies that are clearer and incorporate specific references to the files that I want to change rather than just saying what I wanted to change in general without a specific reference.
- What is one thing you would do differently next time you work with AI on a coding task?
- I will make sure to be more careful about the ways that I use AI to help me in learning, rather than just using the code that I am given directly.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- Before I used to treat AI as this thing that used to just be better than me at coding and that i would trust it and fix small errors, but now I see that it is indeed much closer to a partnership than me letting AI do what it wants.
