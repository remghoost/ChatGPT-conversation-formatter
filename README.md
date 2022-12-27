# ChatGPT conversation reformatter for use with Pastebin

**This tool is for reformatting an entire ChatGPT conversation into something that is actually readable in Pastebin (or anywhere else you'd want to use it). It removes your email address and inserts lines between each message.**

This was made entirely with ChatGPT. 

[Here is the entire conversation used to make it, which is also a good example of what this script does.](https://pastebin.com/r6K8UvE5) 

*Warning, this conversation is a hot mess. I did it late at night with very little sleep. I look like an idiot with most of my questions.*

The output is still kinda ugly, but it's readable. Might fix it later but seeing how well that's worked so far in my life, I doubt it.

## Usage

Copy from your "icon" down to the end of the conversation.

Paste entire contents into text box.

**Your email address _must_ be the first line.**

Press reformat button.

The output is saved as a text document in the same directory as the script.

## Requirements
A working install of [python](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads).

## Installation
Open a cmd or terminal in the directory of your choosing.

```
git pull https://github.com/remghoost/ChatGPT-conversation-formatter
cd ChatGPT-conversation-formatter
pip install -r requirements.txt
```
then use 
```
python reformat_conversation.py
```

## BUT ARE YOU STEALING MY EMAIL ADDRESS?!
Just wanted to hedge this one off at the pass because I know how the internet works.

I want nothing to do with your email address. Due to how the conversations are formatted in the HTML of the chat window, your email address is present on every response. The script takes the first line (which needs to be your email address) and uses that to remove all subsequent traces of it from the document (which also works well for putting in the lines separating responses).

I can understand why they might want this, but I'm not a fan of blasting my email address all over a pastebin.

This script is 63 lines of code. Go read through it if you're scared of me somehow skimming info off of your computer.

## License

[MIT](https://choosealicense.com/licenses/mit/)