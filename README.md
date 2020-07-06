# Eye Can Code
### A link to our youtube demo - https://www.youtube.com/watch?v=CpUsaPoQAtE&t=1s
## Inspiration
With the recent COVID-19 pandemic, students worldwide have transitioned to online schooling. For some students, however, the transition has been harder than for others. Near where Veer lives is the oldest school for blind students: Perkins School for the Blind. Veer had always wanted to help them, and, during these times, he decided to help them when they needed it more than ever. Together, Veer and Saber worked on an online platform dedicated for the blind and targeted for Veer and Saber's favourite lesson: programming.<br>
According to the National Federation of the Blind, COVID-19 has had a disproportionate impact on the blind, with many facing additional challenges during the pandemic. From an education standpoint, blind students and blind parents face uncertainty about the types of electronic materials they will be expected to use for the remainder of the academic year, making it hard for them to keep up with classes. Lastly, it is difficult for the visually impaired to learn how to code on their computer, a challenge which has been exacerbated by the pandemic.

## What it does
We built a text editor which can listen to speech, translate it to Python code, and then run the code in a console. The platform is complete with an academy to teach blind students how to code, with lessons in variable types, for loops, if loops, functions, etc.<br>
We used natural language processing to:
<ol>
<li>Allow the visually impaired to code in python by simply speaking</li>
<li>Provide a handful of python tutorials with voice and speech recognition features to effectively teach coding to people with visual impairments</li>
<li>Create an online platform for the visually impaired to learn</li>
</ol>

## How we built it
We used:
<ul>
<li>Flask</li>
<li>HTML, CSS, and JS</li>
<li>Python</li>
<li>Natural Language Processing</li>
<li>Google Cloud Speech API</li>
</ul>

## Challenges we ran into
We at first parsed the code in Python. However, when connecting it to the JS, it was incredibly laggy and didn't update in real time. Therefore, we had to translate all the Python code into JS which was tedious. In addition, SpeechRecognition only worked on one teammate's computer and not the other, which caused a lot of debugging to occur.

## Accomplishments that we're proud of
We're really proud that our product is actually working for others to use. Not only did we complete a text editor, but we also got the academy working, which was great.

## What we learned
We learnt how to use speech recognition and execute the code in string form. One of our teammates learned how to deploy code to Heroku and link it to a domain. We also learned more about linking JS with Python, especially for real-time work.

## What's next for Eye Can Code
We want to make more aspects of our website audio to further help make it accessible for the blind. Afterwards, we hope to have the platform available for all to use.
