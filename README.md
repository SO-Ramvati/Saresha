# Sharesha - Rule-Based Chatbot with Dual Avatar System

## Overview

Sharesha is a web-based rule-based chatbot that demonstrates the fundamental principles of conversational AI through pattern matching and structured response generation. Unlike modern machine learning chatbots, Sharesha operates on explicitly programmed rules, making it transparent, predictable, and ideal for understanding the foundational concepts of AI agents.

Developed as part of the Introduction to AI and Applications course at PES College of Engineering, Mandya, this project showcases how effective conversational systems can be built using classical AI approaches without neural networks or deep learning.

## The Core Concept

The chatbot operates on a simple but powerful principle: every user input is matched against predefined patterns, and when a match is found, a corresponding response is returned. This deterministic approach ensures that the system is fully understandable, debuggable, and controllable.

Think of it as a sophisticated decision tree where each branch represents a different conversation path. The system preprocesses user input by converting it to lowercase and removing extra spaces, then tests it against various keyword patterns in a specific priority order until a match is found.

## Dual Avatar System

Sharesha features two distinct conversational personalities, each designed for different user needs:

### Academic Mode - Gandalf

Named after the wise wizard from literature, this mode serves as a virtual study companion. It embodies the characteristics of a patient teacher who guides students through their learning journey with knowledge and encouragement.

The Academic Mode specializes in educational assistance, providing structured learning resources and progress tracking. When users interact with Gandalf, they experience a scholarly yet approachable personality that focuses on helping them achieve their academic goals.

### Personal Mode - Samwise

Inspired by the loyal and caring companion from Tolkien's works, this mode focuses on emotional support and creative interaction. Samwise represents warmth, empathy, and genuine care for the user's wellbeing.

The Personal Mode is designed for casual conversation, emotional support, and creative expression. It creates a safe space where users can share their feelings, create stories, or simply have a friendly chat without judgment or pressure.

## How It Works

### Pattern Matching Engine

At the heart of Sharesha is a pattern matching engine that analyzes user input through multiple layers of detection. The system looks for specific keywords and phrases, testing them in order of priority from most specific to most general.

For example, when a user types a greeting like "hello" or "hi," the system recognizes this as a conversation starter and responds with an appropriate welcome message. If the user mentions "quiz" or "test," the system understands they want to practice their knowledge and initiates the quiz feature.

This waterfall approach ensures that more specific patterns are checked first, with broader fallback patterns catching anything that doesn't match the primary rules. Every query receives a response, even if it's just a gentle redirect to available features.

### Mode Routing

When a message arrives at the backend, the system first identifies which mode is currently active. This mode information travels with every request, allowing the server to route the query to the appropriate rule set.

Academic queries are handled by one set of rules that understand educational contexts and know how to retrieve study plans or quiz questions. Personal queries go to a different rule set that specializes in emotional recognition and creative interaction.

This separation of concerns keeps the code organized and makes it easy to expand either mode independently without affecting the other.

### Response Generation

Responses come from two main sources: pre-written content stored in dictionaries and dynamically generated text using templates.

For study plans and informational content, the system retrieves complete, pre-written text that has been carefully crafted to provide comprehensive and accurate information. These responses are stored efficiently and can be quickly accessed when needed.

For conversational responses, especially in Personal Mode, the system uses templates that incorporate parts of the user's own message. This creates a more dynamic and personalized feel to the conversation, making users feel heard and understood.

## Academic Mode Features

### Comprehensive Study Plans

The Academic Mode contains detailed learning roadmaps for several subjects, each structured as a multi-week journey from beginner to advanced levels. These plans break down complex topics into manageable weekly goals with clear objectives and practice recommendations.

The Python programming roadmap, for instance, guides learners through four to five months of progressive skill-building, starting with basic syntax and culminating in specialized tracks like ethical hacking or AI development. Each phase includes specific topics to master, projects to complete, and resources to consult.

Similarly, the Calculus study plan takes students from pre-calculus foundations through differentiation, integration, and into multivariable calculus over three to four months. The plan emphasizes understanding over memorization and includes practice problems at each stage.

History study plans cover both Indian and Roman civilizations, presenting historical events in chronological order with emphasis on cause-and-effect relationships and cultural context.

### Interactive Quiz System

The quiz feature demonstrates how rule-based systems can conduct structured assessments. When triggered, the system presents multiple-choice questions, accepts user answers, and can validate responses against correct answers.

While the current implementation includes a limited set of questions as a proof of concept, the architecture is designed to easily accommodate expanded question banks across multiple subjects and difficulty levels.

### Task Management

The system can assign daily tasks to help users maintain consistent study habits. These tasks are drawn from a predefined list appropriate to the subject matter and learning phase.

This feature demonstrates how chatbots can serve not just as information sources but as accountability partners in the learning process.

## Personal Mode Features

### Interactive Story Generation

One of the most engaging features of Personal Mode is the collaborative story generator. Using a mad-libs style approach, the system guides users through creating a custom story by collecting specific inputs.

The process begins when the user expresses interest in creating a story. The chatbot then asks a series of questions, collecting a character name, location, action, and emotion. Once all inputs are gathered, the system weaves them into a complete narrative using a predefined template.

What makes this interesting is the state management. The system must remember where it is in the story creation process and what information has already been collected, demonstrating how conversational agents can maintain context across multiple turns.

### Emotional Support System

Personal Mode includes sophisticated emotional keyword detection that recognizes when users express feelings like sadness, stress, anxiety, or frustration. When these emotional indicators are detected, the system shifts into a more empathetic mode, acknowledging the feeling and offering to listen.

This feature shows how rule-based systems can demonstrate care and support through appropriate response selection, creating meaningful interactions even without true emotional understanding.

### ELIZA-Style Reflection

The chatbot implements patterns inspired by ELIZA, one of the earliest chatbot programs from the 1960s. ELIZA created the illusion of understanding by reflecting user statements back as questions.

For example, if a user says "I feel overwhelmed," the system might respond "Why do you feel overwhelmed?" This reflection technique, while simple, creates surprisingly effective conversational flow and helps users explore their own thoughts.

The system uses pattern matching to identify specific sentence structures and extract key phrases, then reformulates these phrases into thoughtful questions. This demonstrates how sophisticated conversational behavior can emerge from relatively simple rules.

### Casual Conversation

Beyond specific features, Personal Mode simply provides friendly companionship. It maintains a warm, approachable tone and offers generic but supportive responses when specific patterns aren't matched, keeping the conversation flowing naturally.

## Technical Architecture

### Three-Tier Structure

Sharesha follows a classic web application architecture with three distinct layers working together seamlessly.

The presentation layer handles everything the user sees and interacts with. This includes the visual design, the chat interface, avatar displays, and all interactive elements. It runs entirely in the user's web browser using standard web technologies.

The application layer acts as the middle coordinator. It receives requests from the browser, processes them, and sends back responses. This layer handles the technical details of web communication and routes requests to the appropriate logic handlers.

The business logic layer contains all the intelligence of the chatbot. This is where pattern matching happens, where responses are generated, and where the rules live. By separating this logic from the web layer, the system remains organized and maintainable.

### Communication Flow

When a user types a message and hits send, that message travels from their browser to the server as a structured data package. The package includes both the message text and information about which mode is currently active.

The server receives this package, extracts the information, and passes the message to the rule engine. The rule engine processes the message through its pattern matching logic and generates an appropriate response.

This response then travels back to the browser, again as a structured data package, where it's displayed in the chat interface as a message from the bot. The entire round trip typically takes less than a second, creating a smooth conversational experience.

### State Management Philosophy

An important design decision in Sharesha is the stateless server approach. The server doesn't remember previous conversations or maintain any user-specific information between requests. All context is managed on the client side.

This design choice offers several advantages. It makes the server simpler and more scalable since it doesn't need to track sessions or store conversation history. It also makes the system more predictable and easier to test since each request is handled independently.

For features that do require memory, like the story generation that needs to remember previously collected inputs, this state is managed in the client's browser and sent with each request rather than stored on the server.

## User Interface Design

### Visual Theme

The interface uses a nature-inspired color palette called the Solstice theme, featuring deep teals, muted greens, and earth tones. This creates a calming atmosphere appropriate for both focused study and relaxed conversation.

The design incorporates gradient overlays and transparency effects to add visual depth while maintaining readability. Text appears in off-white against darker backgrounds, ensuring comfortable reading for extended use.

### Layout Philosophy

The interface uses a split-screen approach. The left sidebar displays the current avatar, provides mode selection buttons, and shows which personality is currently active. This keeps important controls visible and easily accessible.

The right side contains the chat area itself, with messages flowing chronologically from top to bottom. User messages appear aligned to the right in one color scheme, while bot messages appear on the left in a different style, making it easy to follow the conversation thread.

### Interactive Elements

The interface provides multiple forms of feedback to keep users informed about what's happening. When a message is being processed, animated dots indicate the bot is "typing." When modes are switched, the avatar image smoothly transitions and the interface confirms the change.

Buttons highlight when hovered over, providing clear visual feedback that they're interactive. The active mode is always clearly indicated through different styling, so users never lose track of which personality they're talking to.

### Responsive Behavior

The design adapts to different screen sizes automatically. On desktop computers, the split-screen layout provides ample space for both controls and conversation. On tablets, elements resize and adjust spacing to fit the narrower screen.

On mobile phones, the layout restructures completely. The sidebar moves to the top, and mode selection buttons rearrange horizontally. This ensures the chatbot remains fully functional regardless of how users access it.

## Development Approach

### AI-Assisted Creation

The development of Sharesha leveraged multiple AI tools strategically throughout the process, demonstrating modern approaches to software development while maintaining full human understanding and control.

DeepSeek helped create the initial prototype, generating basic structure and foundational code. This provided a starting point that was then iteratively refined through human insight and additional AI assistance.

ChatGPT served as the primary tool for code modifications, debugging, and styling work. It helped resolve specific technical issues, refine the visual design, and optimize the JavaScript functionality. The interaction with ChatGPT was iterative, with multiple rounds of refinement for each feature.

Claude provided architectural guidance and code organization suggestions. It helped structure the codebase in a more maintainable way and ensured best practices were followed throughout the implementation.

Image generation tools created the custom avatars and visual assets, allowing for unique branding without requiring graphic design skills or stock image licenses.

Gemini generated educational content including the comprehensive study plans, ensuring the chatbot had valuable, well-structured information to share with users.

### Human Contribution

Despite extensive AI assistance, significant human work was essential. All AI-generated code was tested and validated. Design decisions were made by humans evaluating what worked best for users. Integration of different components required manual coordination and problem-solving.

Testing was entirely manual, with systematic verification of each feature across different scenarios. The final user experience was shaped by human judgment about what felt natural and helpful in conversation.

## Educational Value

### Learning Outcomes

Building Sharesha provided hands-on experience with several fundamental computer science and AI concepts.

The project demonstrated how rule-based systems work and how they differ from learning-based systems. It showed that effective AI doesn't always require complex machine learning, and that simpler approaches have their own advantages in transparency and controllability.

The three-tier architecture illustrated standard web application design patterns that apply broadly across software development. Understanding how presentation, application, and business logic layers interact is foundational knowledge for any web developer.

Working with pattern matching and regular expressions provided practical experience with text processing, a fundamental skill in many programming domains from data analysis to system administration.

### Conceptual Understanding

The project reinforced several important conceptual lessons about AI and software development.

First, that transparency has value. Because every response in Sharesha comes from an explicit rule, it's possible to fully understand and explain why the system behaves as it does. This contrasts with neural networks where decisions emerge from millions of parameters and are difficult to interpret.

Second, that constraints can be beneficial. The limitations of rule-based approaches forced creative problem-solving and careful design decisions. Working within these constraints produced a focused, purposeful system rather than an overly complex one.

Third, that user experience matters more than technical complexity. A simple system that works smoothly and predictably can be more valuable than a sophisticated one that behaves unpredictably or confuses users.

## Limitations and Constraints

### Understanding Boundaries

Sharesha has clear limitations that are important to acknowledge. The system cannot understand natural language in any deep sense. It recognizes keywords and patterns but doesn't grasp meaning, context, or nuance.

Complex sentences, ambiguous queries, or topics outside the predefined domains will confuse the system. It cannot handle typos gracefully or understand implied meaning. Everything must match explicit patterns or fall through to generic responses.

The chatbot has no memory of previous conversations. Each message is processed independently, preventing the system from building on earlier exchanges or maintaining long-term context about a user's interests or progress.

### Content Limitations

The knowledge base is entirely static. Study plans, quiz questions, and response templates are fixed at development time and don't update based on usage. The system cannot learn from interactions or improve its responses over time.

The quiz system is intentionally limited as a proof of concept, with only a few questions implemented. Expanding this would require manually writing and coding additional questions rather than the system generating them.

The story generation follows a single rigid template. While users provide custom inputs, the narrative structure never varies, limiting creative possibilities.

### Technical Constraints

The implementation uses simple keyword matching rather than sophisticated natural language processing. This means the system can be fooled by unexpected phrasing or miss valid queries that don't use exact keywords.

There's no spell-checking or error correction. Users must type clearly enough for the pattern matching to work. Real chatbots would typically include more robust text processing to handle variations and mistakes.

The state management approach, while architecturally clean, means the browser must be kept open to maintain conversation context. Closing the browser loses all state, including partially completed stories or quiz progress.

## Future Directions

### Near-Term Enhancements

The most obvious expansion would be growing the content base. Adding more study plans, more quiz questions, and more conversation patterns would immediately increase the system's usefulness without requiring architectural changes.

Implementing fuzzy matching would make the system more forgiving of typos and variations in phrasing. This could use string similarity algorithms to match close-enough keywords even when they're not exactly right.

Adding basic context memory on the client side would enable features like remembering a user's preferred subjects or tracking which study plan they're following. This wouldn't require server-side changes but would enhance personalization.

### Medium-Term Development

Integrating a database would enable persistent storage of user progress, quiz scores, and learning history. This would transform the chatbot from a stateless tool into a more personalized learning companion.

Expanding the quiz system with scoring, feedback, and adaptive difficulty would make it more educationally valuable. The system could track which topics users struggle with and adjust question difficulty accordingly.

Adding more modes beyond Academic and Personal could expand the chatbot's versatility. A "Professional" mode for career advice or a "Creative" mode for writing prompts could serve different user needs.

### Long-Term Vision

The ultimate enhancement would be a hybrid approach combining rule-based logic with natural language understanding. Rules would handle structured interactions while NLU would interpret user intent for better pattern matching.

Voice integration would make the chatbot accessible through speech, using speech-to-text for input and text-to-speech for responses. This would particularly benefit users who prefer auditory learning or have visual impairments.

A mobile application could provide a more tailored experience for phones and tablets, potentially with offline capability for basic features when internet isn't available.

Multi-user features like shared study groups or collaborative storytelling could add social dimensions to the learning experience, leveraging the chatbot as a facilitator rather than just an individual tool.

## Project Significance

### Demonstrating Fundamentals

Sharesha succeeds in its primary goal of demonstrating rule-based AI principles in an accessible, practical way. It shows that effective conversational agents don't require cutting-edge AI research or enormous computational resources.

The project proves that transparency and predictability can be features rather than limitations. In educational contexts especially, knowing exactly how a system works and why it gives certain responses has inherent value.

### Educational Impact

For students using Sharesha, the chatbot provides genuine utility through its study plans and quiz features while teaching about AI through direct interaction. Users experience firsthand what rule-based systems can and cannot do.

For developers studying the code, the project offers a clean example of web application architecture, pattern matching implementation, and thoughtful code organization. It's simple enough to understand completely yet sophisticated enough to be interesting.

### Modern Development Practices

The transparent use of AI assistance in development demonstrates how contemporary programmers work. Rather than coding everything from scratch, modern development involves strategically leveraging AI tools while maintaining human oversight and understanding.

This approach to development will become increasingly standard, making it valuable to document and demonstrate how AI assistance and human expertise combine effectively.

## Conclusion

Sharesha represents a successful implementation of rule-based conversational AI that achieves its goals of demonstrating knowledge-based agent behavior and effective query handling. While intentionally limited compared to modern machine learning chatbots, these limitations serve an educational purpose.

The dual-mode system shows how different rule sets can create distinct personalities and serve different user needs. The comprehensive study plans provide genuine value to students, while the personal mode features demonstrate how even simple rules can create engaging interactions.

Most importantly, the project achieves clarity and transparency. Every behavior can be traced to specific code, every response to specific rules. This makes it an ideal teaching tool for understanding how conversational AI works at its most fundamental level.

As AI continues to advance with increasingly complex neural networks and large language models, there remains value in understanding these simpler foundations. Rule-based systems still have their place in applications requiring predictability, explainability, and precise control.

Sharesha stands as a demonstration that effective AI doesn't always mean the most advanced AI, and that sometimes the best solution is the one you can fully understand and explain.
