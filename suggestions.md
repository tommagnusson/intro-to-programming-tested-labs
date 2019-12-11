 # General Lab Improvement Suggestions
 
 - **Keep a short length:** Labs should be no more than a page long, with short, concise descriptions of the problem without much instruction (less is more)

    - **Factor out implementation details:** Specific directions should be a separate handout or covered in class

    - Provide links to helpful resources instead of explaining inline

      - This encourages students to engage with materials outside of the instructor’s own and gets them used to looking at documentation and stackoverflow posts, a very  - helpful point to hammer home.

      - Factoring out common operations (like git) into separate cheat sheets decouples the information from the specific lab, which makes it easier for indexing and future reference (as well as declutters the lab sheet).

 - **Avoid “copy-paste” instructions;** either explain in words or provide a starter repository for all the labs

    - There are problems in PDFs with the quotation character that might trip people up

 - **Use helpful tools:** I would encourage at least something like VSCode or even the free edition of PyCharm instead of IDLE. Getting students used to working in code editors and IDEs that are actually used by professionals allows them to leverage features that are useful for them, like the integrated terminal in VSCode (PyCharm has one, too). Showing students how to use useful tools is important for helping them establish a workflow.

 - **Minimize `print`:** To help with good practices and testing, wean students off of print statements as much as possible (even though it’s impossible to do so with command line 
 applications). At the very least, encourage students to separate out rendering (print) from generating the string that will be printed. This allows students to test their string generation function without the complexity of capturing standard out.

 - **Minimize `input`:** Along the same lines, minimize the input function, even though (like printing) it is necessary in command line applications. Encourage students to separate 
 out the input gathering function from the “business logic” part of the application.

 - **Keep Github issues**: Keep encouraging the use of Github issues and project management! This is excellent for establishing a workflow for students (but keep that kind of information in a handout separate from the lab handouts!)

 - **Integrate Markdown:** Write labs in markdown (I might have just received a PDF as an intermediate format, but that’s what I had). It gets students used to seeing markdown-like
 documents. Maybe have them write a README.md for each of their labs describing to others how to run and test their lab.

 - **Use realistic labs:** Tend toward real life examples with appropriate context to show how problem definition can have lots of extra information. Part of the skills students need to program well is being able to translate a problem into pseudocode (and then code). Real life examples help motivate students to demonstrate programming’s applicability in “real life” rather than simply practicing obscure math problems.

 - **Introduce testing with functions:** After careful analysis, I recommend testing be introduced as soon as functions are introduced. Testing immediately motivates refactoring long procedural code into more modular function, with well-defined pre and post conditions. Students (and everyone, in my opinion) will find that it is easier to test code when it is broken into small functions (or small methods in small classes).

 - **Avoid verbatim commands:** Avoid repeating verbatim “commands” (like git commit messages) when the concept has already been introduced. Instead, simply link to the git cheat sheet and mention in a short note that students are still expected to have commits with messages.

 - **Describe the problem rather than the solution:** Avoid explicitly telling students what kinds of programming structures (control statements, variables, variable names, function parameters, etc.) they should have in their code. Leave implementation details out of lab problem definitions. Instead link to extra resources that hint at what might be the most useful for them to use.

