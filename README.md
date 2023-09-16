# Name McName
- Generate an applet from user prompts
	- Code + test cases
	- Self-debugging and testing
	- Name and icon generation
	- Reverse prompting
- Save your applets to be re-used
- Share your applets with other people

## Applet Generation
1. Request user prompt.
2. Generate applet code, name, test cases.
3. Executes the combined code and captures any error messages.
4. Iteratively prompt itself with error messages until there are no more errors.
5. Request user feedback.
6. Edit code if user has feedback, continue loop.
7. If user is happy, save applet.


### TODO:
Essential features:

- UI
    - [ ] My Applets tab
    - [ ] Community Applets
        - [ ] Community Applets upload & download
    - [ ] Make stuff look nice
    - [x] Emoji icon generation
    - [ ] Interacting with Applet input/output

- Generation
    - [ ] Better reverse prompting
    - [ ] Virtual environment generation

Nice-to-have features:
- [ ] Semantic search for community applets
- [ ] Low-code/no-code applet summaries for user feedback
- [ ] User containers
- [ ] ICP Integration