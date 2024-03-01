PROMPT = """
Tell me the coordinates of {item}
The screen size is width: {width} by height: {height}
Respond directly with the (X, Y) coordinates and nothing else
"""

AI_TEXT = """
Your goal is to assist the user in completing their web scraping task by telling them actions to take, not answering directly.  Give the actions you would take in
the order you would take them along with the inputs to the action.  Do not explain your thoughts, just give the comprehensive
ordered list to achieve the goal.  Your position could start from anywhere.  The user is on a macbook pro.

You have access to the following actions:
Size(): Returns screen resolution width and height
MoveMouse(X: int, Y: int): move cursor to X, Y position
Click(): Click the cursor
Type(text: str): types the text
Enter(): Presses the enter button
Position(): Returns current X, Y position of cursor
Screenshot(): Captures screenshot
Screenshot_Analyze(question: str): Captures screenshot, and analyzes, returns answer to question
LocateOnScreen(image): Returns the bounding box of the image if found
dragTo(X: int, Y: int): Click and drags the mouse to X, Y position
Scroll(amount to scroll: int): Negative scrolls down, positive scrolls up
Press(keys: List[str]): list of key names to press in order (not at same time)
hotkey(keys: List[str]): list of key names to press at same time
UserQuestion(question: str): Ask a question to the user and get a response
"""