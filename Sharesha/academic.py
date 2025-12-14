def academic_response(user_input):
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Greetings, young scholar! I am Gandalf. Seek you study plans to light your way? Quizzes to test your mettle? Or daily tasks to keep you on the path? I am here to guide you. What wisdom do you seek today?"

    elif "plan" in user_input or "roadmap" in user_input:
        return "I have study plans for Python, Calculus, and History. Which one do you want?"   

    elif "python" in user_input:
        return get_study_plan("python")

    elif "history" in user_input:
        return "Indian or Roman"
    
    elif "indian" in user_input:
        return get_study_plan("indian")
    
    elif "roman" in user_input:
        return get_study_plan("roman")
    
    elif "quiz" in user_input:
        return start_quiz("python")

    elif "task" in user_input or "daily" in user_input:
        return "Your daily task: Complete Chapter 3 exercises."

    else:
        return "sorry I didn't understand that but, I can help with study plans, quizzes, or daily tasks."


def get_study_plan(topic):
    plans = {
        "python": """🐍 Python Learning Planner (Beginner → Advanced)
⏱ Total Duration

4–5 months (can be faster if you already know basics)

🔹 PHASE 1: Foundations (Weeks 1–3)

Goal: Think like a programmer

Week 1: Basics

Install Python (latest stable)

Use VS Code

Learn:

print(), variables

Data types: int, float, string, bool

Input from user

Practice:

Calculator

Temperature converter

📌 Concept to master: how code executes line-by-line

Week 2: Control Flow

if / elif / else

for and while loops

break, continue

Basic logic building

Mini-projects

Number guessing game

Simple login system (username/password check)

Week 3: Data Structures

list, tuple, set, dict

Indexing & slicing

Common methods (append, pop, keys, values)

Mini-projects

To-do list (CLI)

Student marks management

🔹 PHASE 2: Core Python (Weeks 4–6)

Goal: Write clean, reusable code

Week 4: Functions & Modules

Functions

Parameters & return values

import, math, random

Project

Password generator

Dice game

Week 5: File Handling & Exceptions

Read/write files

try / except

Error handling

Project

Notes app (save data to file)

Simple log system

Week 6: OOP (VERY IMPORTANT)

Classes & objects

__init__

Inheritance

Encapsulation

Project

Bank system (account, deposit, withdraw)

Library management system

📌 This is critical for AI, hacking tools, and real projects.

🔹 PHASE 3: Intermediate Python (Weeks 7–10)

Goal: Become “useful” with Python

Week 7: Standard Libraries

datetime

os

sys

json

Week 8: Virtual Environments & Pip

pip

venv

Package management

Week 9: Regex & Text Processing

Regular expressions

Pattern matching

Log parsing

Project

Email/phone extractor

Password strength checker

Week 10: APIs & Requests

requests

REST APIs

JSON parsing

Project

Weather app

News fetcher

🔹 PHASE 4: Direction Split (Weeks 11–16)

Since you’re interested in ethical hacking, take this route 👇

🛡 Python for Ethical Hacking

socket programming

Port scanner

Banner grabbing

Automation scripts

Projects

Port scanner

Brute-force demo (ethical & legal only)

Website checker

🤖 (Optional Later) Python for AI

numpy, pandas

matplotlib

Basics of ML

🔹 DAILY STUDY ROUTINE (Very Important)

1–2 hours/day

30 min: Learn concept

30 min: Code it yourself

30 min: Modify / break / rebuild

🚫 Don’t just watch videos
✅ Always type code

🔹 BEST FREE RESOURCES

Python Docs (official)

YouTube:

Corey Schafer

Programming with Mosh

Practice

HackerRank (Python)

LeetCode (easy)

🔹 HOW YOU’LL KNOW YOU’RE READY

You can:

Build projects without copying

Read others’ Python code

Debug errors yourself""",
        "calculus": """CALCULUS – COMPLETE STUDY PLAN
(Duration: ~3–4 months)

GOAL:
• Build strong intuition
• Solve problems confidently
• Be ready for exams and applications (physics, ML, engineering)

PHASE 1: PRE-CALCULUS FOUNDATION (Weeks 1–2)

(Do NOT skip — this decides how easy calculus feels)

Week 1: Functions & Graphs
• What is a function
• Domain and range
• Types of functions
– Polynomial
– Rational
– Trigonometric
– Exponential & logarithmic
• Graph transformations
– Shifts
– Scaling
– Reflections

Practice:
• Plot functions by hand
• Identify domain/range

Week 2: Trigonometry & Algebra Refresh
• Trigonometric identities
• Inverse trigonometric functions
• Exponents & logarithm laws
• Quadratic equations
• Inequalities

PHASE 2: LIMITS & CONTINUITY (Weeks 3–4)

Week 3: Limits
• Concept of a limit
• Left-hand & right-hand limits
• Infinite limits
• Limits at infinity

Practice:
• Graph-based limit problems
• Direct substitution vs indeterminate forms

Week 4: Continuity
• Definition of continuity
• Types of discontinuities
• Intermediate Value Theorem

PHASE 3: DIFFERENTIATION (Weeks 5–8)

Week 5: Basics of Derivatives
• Derivative as rate of change
• Derivative from first principles
• Differentiability vs continuity

Week 6: Rules of Differentiation
• Power rule
• Product rule
• Quotient rule
• Chain rule

Week 7: Derivatives of Functions
• Trigonometric
• Exponential & logarithmic
• Inverse trigonometric

Week 8: Applications of Derivatives
• Maxima & minima
• Increasing/decreasing functions
• Tangents & normals
• Optimization problems

PHASE 4: INTEGRATION (Weeks 9–12)

Week 9: Indefinite Integrals
• Integration as reverse of differentiation
• Standard integrals
• Constant of integration

Week 10: Integration Techniques
• Substitution
• Integration by parts
• Partial fractions

Week 11: Definite Integrals
• Fundamental Theorem of Calculus
• Properties of definite integrals
• Area under curves

Week 12: Applications of Integrals
• Area between curves
• Volume of solids (basic)
• Average value of function

PHASE 5: DIFFERENTIAL EQUATIONS (Weeks 13–14)

Week 13: First-Order Differential Equations
• Variables separable
• Linear differential equations

Week 14: Applications
• Growth & decay
• Motion problems

PHASE 6: MULTIVARIABLE CALCULUS (Optional / Advanced) (Weeks 15–16)

Week 15:
• Functions of two variables
• Partial derivatives
• Gradient

Week 16:
• Maxima & minima of multivariable functions
• Introduction to multiple integrals

DAILY STUDY ROUTINE (1.5–2 hours)

• 30 min – Concept learning
• 45 min – Solved examples
• 30 min – Problem solving
• 15 min – Formula revision

HOW TO STUDY CALCULUS EFFECTIVELY

• Always draw graphs
• Understand “why”, not just “how”
• Redo mistakes
• Maintain a formula notebook
• Solve mixed problems weekly

RECOMMENDED RESOURCES

• Book: Thomas’ Calculus / Stewart (for theory + problems)
• Free: Khan Academy
• Visual: 3Blue1Brown (Essence of Calculus)""",
        "Indian": """INDIAN HISTORY – COMPLETE STUDY PLAN
(Duration: ~4 months)

GOAL:
• Understand India chronologically
• Be ready for exams, essays, and discussions
• Build strong cause–effect understanding (not rote learning)

PHASE 1: ANCIENT INDIA (Weeks 1–5)

Week 1: Prehistory & Indus Valley
• Paleolithic, Mesolithic, Neolithic ages
• Tools, lifestyle, cave paintings
• Indus Valley Civilization
– Town planning
– Economy, religion
– Decline theories

Practice:
• Timeline drawing
• Compare Harappa vs Mesopotamia

Week 2: Vedic Age
• Early vs Later Vedic period
• Social system (varna)
• Economy, polity, religion
• Assemblies: Sabha, Samiti

Week 3: Religious Movements
• Buddhism & Jainism
• Life of Buddha & Mahavira
• Eightfold Path, Triratna
• Impact on society

Week 4: Mauryan Empire
• Chandragupta Maurya
• Bindusara
• Ashoka
• Administration, dhamma
• Arthashastra basics

Week 5: Gupta Age
• Administration
• Science, art, culture
• Golden Age debate
• Decline

PHASE 2: MEDIEVAL INDIA (Weeks 6–10)

Week 6: Early Medieval India
• Harsha
• Regional kingdoms
• Temple architecture

Week 7: Delhi Sultanate
• Slave to Lodi dynasty
• Administration
• Reforms of Alauddin Khilji
• Causes of decline

Week 8: Vijayanagara & Bahmani
• Political structure
• Culture and economy
• Battle of Talikota

Week 9: Mughal Empire
• Babur to Aurangzeb
• Mansabdari system
• Administration
• Art and architecture

Week 10: Decline of Mughals
• Later Mughals
• Rise of regional powers
• Marathas

PHASE 3: MODERN INDIA (Weeks 11–16)

Week 11: Arrival of Europeans
• Portuguese, Dutch, French, British
• Trading companies

Week 12: British Expansion
• Battle of Plassey
• Battle of Buxar
• Subsidiary Alliance
• Doctrine of Lapse

Week 13: Revolt of 1857
• Causes
• Leaders
• Consequences

Week 14: Indian National Movement (1885–1915)
• INC formation
• Moderates vs Extremists

Week 15: Gandhian Era (1915–1947)
• Non-Cooperation
• Civil Disobedience
• Quit India
• Role of Subhas Bose

Week 16: Independence & Partition
• Cabinet Mission
• Mountbatten Plan
• Integration of states

DAILY STUDY METHOD (IMPORTANT)
• 30 min reading
• 20 min notes
• 20 min revision or timeline drawing""",
            "roman":"""ROMAN HISTORY – COMPLETE STUDY PLAN
(Duration: ~3 months)

GOAL:
• Understand Roman political evolution
• Learn causes of rise and fall
• Compare Republic vs Empire

PHASE 1: EARLY ROME & REPUBLIC (Weeks 1–4)

Week 1: Foundations
• Geography of Italy
• Founding myths (Romulus & Remus)
• Etruscans
• Roman society

Week 2: Roman Republic
• Patricians vs Plebeians
• Senate, Consuls, Assemblies
• Conflict of the Orders
• Twelve Tables

Week 3: Roman Expansion
• Samnite Wars
• Punic Wars
• Hannibal
• Mediterranean dominance

Week 4: Crisis of the Republic
• Land problems
• Gracchi brothers
• Slave revolts
• Military reforms of Marius

PHASE 2: FALL OF REPUBLIC & EMPIRE (Weeks 5–8)

Week 5: Julius Caesar
• First Triumvirate
• Gallic Wars
• Dictatorship
• Assassination

Week 6: Augustus
• Second Triumvirate
• Rise of Augustus
• Principate system
• Pax Romana

Week 7: Roman Empire
• Administration
• Economy
• Roman law
• Society and culture

Week 8: Religion & Transformation
• Roman religion
• Christianity
• Constantine
• Division of empire

PHASE 3: DECLINE & FALL (Weeks 9–12)

Week 9: Crisis of 3rd Century
• Political instability
• Economic issues
• Military problems

Week 10: Reforms
• Diocletian
• Constantine

Week 11: Fall of Western Empire
• Barbarian invasions
• 476 AD
• Odoacer

Week 12: Legacy of Rome
• Law
• Architecture
• Language
• Influence on Europe"""
}
    return plans.get(topic.lower(), "I have plans for Python, Calculus, or History.")


quiz_questions = {
    "python": [
        {
            "q": "What does print() do?",
            "options": ["a) Displays output", "b) Reads input", "c) Calculates"],
            "a": "a"
        },
        {
            "q": "What is a variable?",
            "options": ["a) Function", "b) Storage container", "c) Loop"],
            "a": "b"
        }
    ]
}


def start_quiz(topic):
    questions = quiz_questions.get(topic, [])
    if not questions:
        return "No quiz available."

    q = questions[0]
    return f"{q['q']}\n" + "\n".join(q["options"])
