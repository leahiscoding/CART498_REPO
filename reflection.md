Reflection

Leah Song 
40321005

Jungian Dream Interpreter – Project Report  

I found this project challenging and interesting because it required me to combine something conceptual with something technical. At the beginning, I did not know how to translate psychological theory into something a model could follow. It felt abstract. However, once I began experimenting with prompt structure, the process became more concrete.

I started by testing simple prompts like “interpret this dream through Jungian psychology.” The results were often vague and overly poetic. They sounded thoughtful but did not consistently reflect specific Jungian concepts. Because of this, I decided to introduce structure. I explicitly required the output to be divided into four sections: Key Symbols, Archetypal Dynamics, Psychological Meaning, and Individuation Insight. Using AI for prompting was helpful as it added more details from the idea I was thinking. Once I added this constraint, the responses became more stable and conceptually clearer. The model began referencing archetypes more consistently. Through this process, I realized that the model’s “psychological depth” depends heavily on constraint rather than intelligence.

For the image generation stage, I initially used the raw dream text as the prompt. The images were visually interesting but not always aligned with the interpretation. I then expanded the image prompt to include symbolic motifs, layered depth, restrained color palettes, and cinematic composition. Once again, I created a detailed prompt to create a prompt for an AI. The idea of using AI as a prompt engineer to tame the AI was quite interesting.

Technically, the web app is built using Flask. The user enters a dream in a text area and clicks submit. The server sends the prompt to the OpenAI model, retrieves the interpretation, then generates a 1024x1024 image in JPEG format. The results are rendered on the same page. I also depolyed the project using Render, which helped me understand how a local Flask application can be made accessible online. I began to see python as a flexible tool to build an interactive website.

One insight I gained is that AI systems respond more reliably to structure than to intention. The clearer the format and constraints, the more coherent the output. The model does not truly “understand” Jungian archetype—it produces pattern shaped by instructions, which is something I also noticed in assignment 3. If I continue developing this project, I would connect the image prompt directly to the generated interpretation instead of the original dream input to strengthen conceptual continuity. I would also experiment with storing previous entries to observe recurring symbolic themes over time.

Overall, this project helped me think differently about prompt design and try experimenting prompt design with AI. It feels less like asking a question and more like designing a system of constraints.
